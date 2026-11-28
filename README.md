# Adam Williams

I’m a staff software engineer in Bozeman, Montana. At Arro Finance, I build banking services and run the monitoring platform engineers use to investigate payment failures. I led engineering’s work on Arro’s SOC 2 Type II audit. At onX Backcountry, I built the service that lets skiers check mountain snowpack history on the map.

[Read the résumé](index.md) · [LinkedIn](https://www.linkedin.com/in/adam1988/)

## Local preview

Install the Ruby version in `.ruby-version`, run `bundle install` and start Docker. Build the site and both downloads from the homepage with `bundle exec python3 scripts/build_resume.py`. Serve the resulting directory with `python3 -m http.server 4000 --bind 127.0.0.1 --directory _site`.

Add `--proofs` to the build command to compare Editorial and Engineering at `/proofs/`. Each proof includes the full résumé, desktop and phone captures, and both PDFs. Set `resume_typography` in `_config.yml` to select the homepage design. Browser printing and **Download PDF** use that design. **Plain PDF** uses black text in a single font family. Fonts and their licenses are in `assets/fonts/`.

## Visual checks

Run `bundle exec python3 scripts/build_resume.py --check` to compare the selected design with the PNG files in `visual-baselines/`. The same pinned Linux ARM64 Chromium and PDF rasterizer run locally and in CI. A mismatch saves expected, actual and difference images in `visual-results/diffs/`. After reviewing an intentional layout or copy change, run `bundle exec python3 scripts/build_resume.py --update-baselines` and review the changed images before committing.

Screen checks capture the top, onX, Payouts and bottom at phone, tablet and desktop sizes in both color schemes. They also exercise keyboard focus, downloads, and wrapping around the mobile breakpoint. Print checks verify each page’s Letter dimensions and margins, embedded fonts, selectable text in homepage order, external links and page break.

## Publishing

Pull requests build the site, verify the screen and PDF layouts and run Trivy. A merge to `main` repeats those checks and deploys the verified site to GitHub Pages. Proofs and visual testing files stay local.
