# Goblet — landing site

The public marketing site for Goblet. Static HTML, no build step, no framework,
no dependency on the app codebase — this folder is designed to live in its own
repository and its own Vercel project, on its own domain, so the app at
goblet.live and this site can never break each other.

## Deploy

1. Copy this folder's CONTENTS into a fresh repository (this README included).
2. Vercel → Add New → Project → import the repo. Framework preset: **Other**.
   No build command, no output directory — it's static files.
3. Add your domain under Settings → Domains and set the DNS records Vercel
   shows you.

## The two placeholders

- **App Store link** — `index.html` shows "Coming soon to the App Store" in two
  places. When the listing is live, replace both `<span class="btn btn-ghost">…`
  blocks with `<a class="btn btn-solid" href="https://apps.apple.com/…">…`.
- **Operating entity** — the footer and the contact blocks in privacy.html and
  terms.html say "Goblet" with a `TODO` comment beside them. Once company
  ownership is settled, name the entity (e.g. GOBLET SOMMELIER LLC) in all
  three places.

## App Store Connect

Point these fields at this site once it's on its domain:

- Privacy Policy URL → /privacy.html
- Support URL       → /support.html
- Marketing URL     → /

Those URLs must stay live for as long as the app is on the App Store; that is
this repo's one standing obligation.

## Notes

- `support@goblet.live` stays the contact address — email on that domain is
  independent of what the goblet.live website serves.
- Fonts load from Google Fonts and fall back to Georgia; everything else is
  local to this folder.
