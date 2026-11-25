"""Build the Pages site and print its HTML to the downloadable résumé."""

import functools
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
PDF = Path("assets/Adam-Williams-Resume.pdf")


def main():
    chrome = (
        os.environ.get("CHROME_BIN")
        or shutil.which("google-chrome")
        or shutil.which("chromium")
        or "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    )
    subprocess.run(["jekyll", "build"], cwd=ROOT, check=True)
    handler = functools.partial(SimpleHTTPRequestHandler, directory=SITE)
    with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            # Jekyll ignores this hidden browser profile during live previews.
            with tempfile.TemporaryDirectory(prefix=".resume-", dir=ROOT / "assets") as tmp:
                output = Path(tmp) / PDF.name
                subprocess.run([
                    chrome, "--headless", "--disable-background-networking",
                    "--user-data-dir=" + tmp + "/profile", "--no-pdf-header-footer",
                    "--print-to-pdf=" + str(output),
                    f"http://127.0.0.1:{server.server_port}/",
                ], check=True)
                output.replace(ROOT / PDF)
        finally:
            server.shutdown()
    shutil.copy2(ROOT / PDF, SITE / PDF)


if __name__ == "__main__":
    main()
