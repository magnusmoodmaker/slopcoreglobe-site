#!/usr/bin/env bash
# Builds public/ and publishes it to the gh-pages branch (GitHub Pages source).
# Cloudflare-only files (_headers, _redirects) are left out. No CNAME until DNS is approved.
set -euo pipefail
cd "$(dirname "$0")"
python3 build.py
tmp=$(mktemp -d)
cp -r public/. "$tmp"/
rm -f "$tmp/_headers" "$tmp/_redirects"
touch "$tmp/.nojekyll"
src_rev=$(git rev-parse --short HEAD)
git -C "$tmp" init -q -b gh-pages
git -C "$tmp" add -A
git -C "$tmp" commit -qm "Deploy site from main@${src_rev}"
git -C "$tmp" push -q --force "$(git remote get-url origin)" gh-pages
rm -rf "$tmp"
echo "Deployed main@${src_rev} to gh-pages"
