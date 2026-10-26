# slopcoreglobe.com

Static site for Slopcore Globe: home, privacy policy, terms. No build tools, fonts, scripts or trackers.

- Edit page bodies in `src/`, then run `python3 build.py` to regenerate `public/`.
- `public/` is the site root (Cloudflare Pages output dir `public`, no build command; or GitHub Pages from `/public` via an Actions workflow / copy to repo root).
- `/privacy/` and `/terms/` are `privacy/index.html` and `terms/index.html`, so they work on both hosts (`/privacy` redirects to `/privacy/`).
- `_headers` / `_redirects` are Cloudflare Pages only (ignored by GitHub Pages).
- `preview/` holds review screenshots (not part of the site).

Local preview: `cd public && python3 -m http.server 8766`

## Hosting

GitHub Pages, served from the `gh-pages` branch. Source lives on `main`. To publish: edit `src/`, commit and push `main`, then run `./deploy.sh`, which runs `build.py` and force-pushes the built `public/` (without the Cloudflare-only `_headers` / `_redirects`, plus `.nojekyll`) to `gh-pages`. Static assets (CSS, icons, robots.txt, sitemap.xml) live in `public/` and are committed on `main`. No custom domain or CNAME yet.
