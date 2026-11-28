# Adam Williams

I’m a staff software engineer in Bozeman, Montana. At Arro Finance, I build banking services and run the monitoring platform engineers use to investigate payment failures. I led engineering’s work on Arro’s SOC 2 Type II audit. At onX Backcountry, I built the service that lets skiers check mountain snowpack history on the map.

[Read the résumé](index.md) · [LinkedIn](https://www.linkedin.com/in/adam1988/)

## Local preview

Install the Ruby version in `.ruby-version` and run `bundle install`. Run `bundle exec python3 scripts/build_resume.py` to generate the static HTML and its two-page PDF, then `bundle exec jekyll serve` to preview the site. The print script uses Chrome or Chromium. Set `CHROME_BIN` if the executable is outside the usual locations.

## Publishing

Pull requests build the site, check the PDF and run Trivy. After a merge to `main`, GitHub Actions repeats those checks on the merged commit and deploys the resulting static files to GitHub Pages. Both browser printing and the PDF download use the homepage résumé and its print stylesheet.
