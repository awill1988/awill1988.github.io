"""Print the generated résumé and check its screen and paper layouts."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import shutil
from tempfile import TemporaryDirectory
from threading import Thread
import unicodedata

from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
RESULTS = ROOT / "visual-results"
BASELINES = ROOT / "visual-baselines"
DESIGNS = ("editorial", "engineering")
DOWNLOADS = {"styled": "Adam-Williams-Resume.pdf", "plain": "Adam-Williams-Resume-Plain.pdf"}
SIZES = {"phone": (390, 844), "tablet": (768, 1024), "desktop": (1440, 900)}


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def ready(page):
    page.evaluate("""async () => {
      const samples = ['h1','h2','h3','h4','.dates','li','strong','em'];
      for (const selector of samples) {
        const s = getComputedStyle(document.querySelector(selector));
        const family = s.fontFamily.split(',')[0];
        const faces = await document.fonts.load(s.fontStyle+' '+s.fontWeight+' 16px '+family);
        if (!faces.length || faces.some(f => f.status !== 'loaded')) throw Error('missing font: '+family);
      }
      await Promise.all([...document.images].map(i => i.decode()));
      await document.fonts.ready;
      await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    }""")


def normalized(text):
    # Line and word boundaries can move during PDF shaping, as can list markers.
    return re.sub(r"[\s•\u00ad\u200b]+", "", unicodedata.normalize("NFKC", text)).casefold()


def verify_pdf(path, content, links, design, edition, images):
    with pymupdf.open(path) as doc:
        assert len(doc) == 2, f"{path.name} has {len(doc)} pages"
        text, urls, fonts = [], set(), set()
        for number, page in enumerate(doc, start=1):
            assert tuple(page.rect) == (0, 0, 612, 792), f"page {number} is not US Letter"
            text.append(page.get_text())
            if number == 2:
                assert normalized(text[-1]).startswith("payoutsnetwork"), "Payouts must start page two"
            urls.update(link["uri"] for link in page.get_links() if "uri" in link)
            for block in page.get_text("dict", flags=pymupdf.TEXTFLAGS_TEXT)["blocks"]:
                if edition == "plain":
                    for line in block["lines"]:
                        assert all(s["color"] == 0 for s in line["spans"]), "plain PDF has colored text"
            for xref, _, _, name, *_ in page.get_fonts():
                assert doc.extract_font(xref)[3], f"{name} is not embedded"
                fonts.add(name.split("+")[-1].lower())
            if edition == "plain":
                assert not page.get_image_info(), "plain PDF contains artwork"
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5))
            pixels = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
            ink = ImageChops.difference(pixels, Image.new("RGB", pixels.size, "white")).getbbox()
            # 0.6 inch at 108 dpi, allowing one pixel for antialiasing.
            assert ink and min(ink[0], ink[1], pixels.width - ink[2], pixels.height - ink[3]) >= 63, (number, ink)
            pixels.save(images / f"{edition}-page-{number}.png")
        expected, actual = normalized(content), normalized("".join(text))
        if expected != actual:
            idx = next((i for i, (x, y) in enumerate(zip(expected, actual)) if x != y),
                       min(len(expected), len(actual)))
            raise ValueError(f"{path.name} text at {idx}: HTML {expected[idx:idx+80]!r}, PDF {actual[idx:idx+80]!r}")
        assert set(links) == urls, f"{path.name} link differences: {set(links) ^ urls}"
        expected_fonts = {"sourcesans3"}
        if edition == "styled":
            expected_fonts.add("ibmplexmono")
            if design == "editorial":
                expected_fonts.add("spectral")
        assert all(any(f.startswith(family) for f in fonts) for family in expected_fonts), fonts
        assert all(any(f.startswith(family) for family in expected_fonts) for f in fonts), fonts


def print_downloads(page, design, output, images):
    page.emulate_media(media="print", color_scheme="light", reduced_motion="reduce")
    for edition, name in DOWNLOADS.items():
        page.locator("main").evaluate("(m, plain) => m.classList.toggle('resume--plain', plain)", edition == "plain")
        ready(page)
        assert not page.locator(".work").is_visible(), "selected work must be screen-only"
        assert page.locator("article :is(h2,h3,h4):visible").first.get_attribute("id") == "arro-finance"
        links = page.locator("main a:visible").evaluate_all("els => els.map(a => a.href)")
        path = output / name
        page.pdf(path=path, tagged=True, print_background=True, prefer_css_page_size=True)
        verify_pdf(path, page.locator("main").inner_text(), links, design, edition, images)
    page.locator("main").evaluate("m => m.classList.remove('resume--plain')")
    page.emulate_media(media="screen", reduced_motion="no-preference")


def measure(page):
    problems = page.evaluate("""() => {
      const errors = [];
      if (document.documentElement.scrollWidth > innerWidth) errors.push('horizontal overflow');
      for (const title of document.querySelectorAll('h4')) {
        const range = new Range();
        range.selectNodeContents(title.firstChild);
        const d = title.querySelector('.dates').getBoundingClientRect();
        for (const t of range.getClientRects()) {
          if (t.x < d.right && t.right > d.x && t.y < d.bottom && t.bottom > d.y) errors.push(title.innerText);
        }
      }
      window.scrollTo(0, document.scrollingElement.scrollHeight);
      const last = document.querySelector('article > :last-child').getBoundingClientRect();
      const bottom = document.querySelector('main').getBoundingClientRect().bottom;
      if (last.top < 0 || last.bottom > bottom || innerHeight-bottom < 32) errors.push('bottom edge clipped');
      window.scrollTo(0, 0);
      return errors;
    }""")
    assert not problems, f"{page.viewport_size}: {problems}"


def screen_checks(page, images):
    for width in (320, 575, 576, 577):
        page.set_viewport_size({"width": width, "height": 844})
        ready(page)
        measure(page)
    for device, (width, height) in SIZES.items():
        page.set_viewport_size({"width": width, "height": height})
        for scheme in ("light", "dark"):
            page.emulate_media(color_scheme=scheme)
            ready(page)
            measure(page)
            last_highlight = page.locator(".work__row p").last.bounding_box()
            assert last_highlight["y"] + last_highlight["height"] <= height, f"{device}: final highlight below fold"
            for view, selector in (("top", "body"), ("onx", "#onxmaps"),
                                   ("payouts", "#payouts-network-formerly-wonder-technologies"),
                                   ("end", "article > :last-child")):
                page.locator(selector).evaluate("e => e.scrollIntoView({block:'start',behavior:'instant'})")
                page.evaluate("() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")
                page.screenshot(path=images / f"{device}-{scheme}-{view}.png", scale="css")
    page.evaluate("scrollTo(0,0)")
    for target in page.locator("a:visible").all():
        page.keyboard.press("Tab")
        assert target.evaluate("""a => a === document.activeElement && a.matches(':focus-visible')
          && getComputedStyle(a).outlineStyle !== 'none'"""), target.inner_text()
    page.goto(page.url)
    page.locator(".skip").focus()
    page.keyboard.press("Enter")
    assert page.locator("#experience").evaluate("e => e === document.activeElement")
    targets = ["#arro-finance", "#onx-backcountry", "#onx-identity"]
    for link, target in zip(page.locator(".work a").all(), targets, strict=True):
        assert link.get_attribute("href") == target
        link.focus()
        page.keyboard.press("Enter")
        assert page.locator(target).evaluate("e => e === document.activeElement && e.matches(':target')")


def verify_downloads(page):
    for anchor, name in zip(page.locator("nav [download]").all(), DOWNLOADS.values(), strict=True):
        with page.expect_download() as event:
            anchor.click()
        download = event.value
        assert download.suggested_filename == name and not download.failure()
        assert download.path().read_bytes().startswith(b"%PDF-"), name


def compare(images, update):
    files = sorted(images.glob("*.png"))
    if update:
        BASELINES.mkdir(exist_ok=True)
        for obsolete in {p.name for p in BASELINES.glob("*.png")} - {p.name for p in files}:
            (BASELINES / obsolete).unlink()
        for path in files:
            shutil.copyfile(path, BASELINES / path.name)
    expected_names = {p.name for p in BASELINES.glob("*.png")}
    actual_names = {p.name for p in files}
    failures = sorted(expected_names ^ actual_names)
    for name in failures:
        folder = RESULTS / "diffs" / Path(name).stem
        folder.mkdir(parents=True, exist_ok=True)
        if name in expected_names:
            shutil.copyfile(BASELINES / name, folder / "expected.png")
        if name in actual_names:
            shutil.copyfile(images / name, folder / "actual.png")
    for name in sorted(expected_names & actual_names):
        with Image.open(BASELINES / name) as ref, Image.open(images / name) as actual:
            expected = ref.convert("RGB")
            got = actual.convert("RGB")
            if expected.size != got.size:
                size = tuple(map(max, zip(expected.size, got.size)))
                expected = expected.crop((0, 0, *size))
                got = got.crop((0, 0, *size))
            delta = ImageChops.difference(expected, got)
            if delta.getbbox():
                failures.append(name)
                folder = RESULTS / "diffs" / Path(name).stem
                folder.mkdir(parents=True, exist_ok=True)
                expected.save(folder / "expected.png")
                got.save(folder / "actual.png")
                delta.point(lambda p: min(255, p * 4)).save(folder / "diff.png")
    assert not failures, f"visual differences: {', '.join(failures)}"
    print(f"{len(files)} visual baselines verified", flush=True)


def proof_index():
    folder = SITE / "proofs"
    template = (ROOT / "scripts/renderer/proofs.html").read_text()
    cards = []
    for design in DESIGNS:
        description = {"editorial": "Spectral name and employers · sans serif section labels",
                       "engineering": "Source Sans 3 name and employers · monospace dates"}[design]
        samples = "".join(
            f'<figure><figcaption>{label}</figcaption><a href="{design}/{sample}.png">'
            f'<img alt="Full-size {design} {label.lower()}" src="{design}/{sample}.png"></a></figure>'
            for sample, label in (("desktop-light-top", "Desktop"), ("phone-dark-top", "Phone"),
                                  ("desktop-light-payouts", "Desktop · Payouts"),
                                  ("styled-page-1", "Styled PDF · page one"), ("styled-page-2", "Styled PDF · page two"))
        )
        links = " · ".join(f'<a href="{design}/{name}">{edition.title()} PDF</a>' for edition, name in DOWNLOADS.items())
        cards.append(f'<section><h2>{design.title()}</h2><p>{description}</p><p><a href="{design}/">Website</a> · {links}</p>{samples}</section>')
    (folder / "index.html").write_text(template.replace("<!-- proofs -->", "".join(cards)))


def run(browser, base, args):
    html = (SITE / "index.html").read_text()
    selected = re.search(r'<main class="[^"]*\bresume--(editorial|engineering)\b', html).group(1)
    for design in (DESIGNS if args.proofs else [selected]):
        print(f"rendering {design}", flush=True)
        target = SITE / "proofs" / design
        url = base
        if args.proofs:
            target.mkdir(parents=True, exist_ok=True)
            proof = html.replace("resume--" + selected + '"', "resume--" + design + '"')
            for name in DOWNLOADS.values():
                proof = proof.replace('href="/assets/' + name + '"', 'href="' + name + '"')
            (target / "index.html").write_text(proof)
            url += f"proofs/{design}/"
        with TemporaryDirectory(dir=RESULTS) as tmp, browser.new_context(locale="en-US", timezone_id="UTC") as context:
            work = Path(tmp)
            images = work / "images"
            images.mkdir()
            page = context.new_page()
            page.goto(url)
            assert page.locator("main").evaluate("(e,d) => e.classList.contains('resume--'+d)", design)
            print_downloads(page, design, work, images)
            if args.check or args.update_baselines or args.proofs:
                screen_checks(page, images)
            if args.proofs:
                for path in images.glob("*.png"):
                    shutil.copyfile(path, target / path.name)
            if design == selected and (args.check or args.update_baselines):
                compare(images, args.update_baselines)
            for name in DOWNLOADS.values():
                if args.proofs:
                    shutil.copyfile(work / name, target / name)
                if design == selected:
                    for assets in (SITE / "assets", ROOT / "assets"):
                        shutil.copyfile(work / name, assets / name)
            verify_downloads(page)
            if args.proofs and design == selected:
                page.goto(base)
                verify_downloads(page)
    if args.proofs:
        proof_index()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--update-baselines", action="store_true")
    parser.add_argument("--proofs", action="store_true")
    args = parser.parse_args()
    RESULTS.mkdir(exist_ok=True)
    if args.check and (RESULTS / "diffs").exists():
        shutil.rmtree(RESULTS / "diffs")
    handler = partial(QuietHandler, directory=SITE)
    with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server, sync_playwright() as pw:
        Thread(target=server.serve_forever, daemon=True).start()
        try:
            with pw.chromium.launch() as browser:
                run(browser, f"http://127.0.0.1:{server.server_port}/", args)
        finally:
            server.shutdown()


if __name__ == "__main__":
    main()
