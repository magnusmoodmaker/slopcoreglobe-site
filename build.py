#!/usr/bin/env python3
"""Builds public/*.html from src/*.html with a shared header and footer. No dependencies."""
from pathlib import Path
ROOT = Path(__file__).parent
PAGES = [
  # src, out, path, title, description
  ("home.html", "index.html", "/", "Slopcore Globe – AI music videos from X on a globe",
   "Slopcore Globe is a music player that plays AI music videos from X. Coming soon to iOS and Android."),
  ("privacy.html", "privacy/index.html", "/privacy/", "Privacy Policy – Slopcore Globe",
   "How the Slopcore Globe app handles your information: no login, no ads, no tracking, a random install ID for your playlist."),
  ("terms.html", "terms/index.html", "/terms/", "Terms of Use – Slopcore Globe",
   "Terms of Use for the Slopcore Globe app, including the Personal Playlist subscription."),
  ("404.html", "404.html", None, "Page not found – Slopcore Globe", "Page not found."),
]
def nav(path):
    items = [("/", "Home"), ("/privacy/", "Privacy"), ("/terms/", "Terms")]
    return "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for h, t in items)
def page(src, path, title, desc):
    body = (ROOT / "src" / src).read_text()
    cls = "wrap" if src in ("home.html", "404.html") else "wrap prose"
    canon = f'<link rel="canonical" href="https://slopcoreglobe.com{path}">\n' if path else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{canon}<meta name="theme-color" content="#000000">
<meta name="color-scheme" content="dark">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/site.css">
</head>
<body>
<header class="site-header"><div class="wrap"><a class="brand" href="/" aria-label="Slopcore Globe home"><img src="/apple-touch-icon.png" alt="" width="34" height="34"><span>Slopcore Globe</span></a><nav class="site-nav" aria-label="Main">{nav(path)}</nav></div></header>
<main class="{cls}">
{body.strip()}
</main>
<footer class="site-footer"><div class="wrap"><span>© 2026 Magnus Kyltveit · <a href="mailto:hello@slopcoreglobe.com">hello@slopcoreglobe.com</a></span><span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a rel="noopener" href="https://x.com/slopcoreglobe">@slopcoreglobe</a></span></div></footer>
</body>
</html>
"""
for src, out, path, title, desc in PAGES:
    p = ROOT / "public" / out
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(page(src, path, title, desc))
    print("wrote", p.relative_to(ROOT))
