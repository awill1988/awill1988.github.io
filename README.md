# Adam Williams

I’m a staff software engineer in Bozeman, Montana. At Arro Finance, I build banking services and an AI assistant. As the founding backend engineer for onX Backcountry, I built the SNOTEL service that brings mountain snowpack histories to onX Hunt, Backcountry and Offroad.

[Read the résumé](index.md) · [LinkedIn](https://www.linkedin.com/in/adam1988/)

## Local preview

Install the Ruby version in `.ruby-version` and run `bundle install`. Run `bundle exec python3 scripts/build_resume.py` to generate the static HTML and its two-page PDF, then `bundle exec jekyll serve` to preview the site. The print script uses Chrome or Chromium. Set `CHROME_BIN` if the executable is outside the usual locations.

## Publishing

Pull requests build the site, check the PDF and run Trivy. After a merge to `main`, GitHub Actions repeats those checks on the merged commit and deploys the resulting static files to GitHub Pages. Both browser printing and the PDF download use the homepage résumé and its print stylesheet.
