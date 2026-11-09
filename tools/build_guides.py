#!/usr/bin/env python3
"""Builds the wine guides (gobletlanding/guides/) from guides_content.py.

The pages borrow the site's own look from faq.html (the style block, the
header and the footer), so a guide is indistinguishable from the rest of the
site. Run it after editing the copy or the shared chrome:

    python3 tools/build_guides.py

Each guide gets: its own title and description (within Google's display
lengths), a canonical URL, Open Graph and Twitter tags, Article,
BreadcrumbList and FAQPage structured data, a visible FAQ that matches the
FAQPage data word for word, links to related guides, and the store badges.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'gobletlanding'
SITE = 'https://www.gobletai.app'
TODAY = '2026-11-09'

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from guides_content import GUIDES  # noqa: E402

faq_html = (ROOT / 'faq.html').read_text()
STYLE = re.search(r'<style>.*?</style>', faq_html, re.S).group(0)
HEADER = re.search(r'<header class="site">.*?</header>', faq_html, re.S).group(0)
FOOTER = re.search(r'<footer class="site">.*?</footer>', faq_html, re.S).group(0)
BADGES = re.search(r'<span class="store-badges">.*?</a></span>', HEADER, re.S).group(0)


def rooted(fragment):
    """The guides live one folder down: make the site's relative links absolute."""
    fragment = re.sub(r'href="index\.html"', 'href="/"', fragment)
    fragment = re.sub(r'(href|src)="(?!https?:|/|#|mailto:)([^"]+)"', r'\1="/\2"', fragment)
    return fragment


def header(current):
    h = rooted(HEADER).replace(' aria-current="page"', '')
    if current:
        h = h.replace(f'href="{current}"', f'href="{current}" aria-current="page"', 1)
    return h


GUIDE_CSS = '''<style>
.crumbs{font-size:.82rem;color:var(--gray);margin-bottom:.9rem}
.crumbs a{color:var(--gray);text-decoration:none}.crumbs a:hover{color:var(--ink)}
.article{padding:1rem 0 3rem}
.article .card-l{background:#fff;border:1px solid var(--line);border-radius:1.4rem;box-shadow:0 12px 30px rgba(67,32,43,.10);padding:2.2rem}
@media(max-width:640px){.article .card-l{padding:1.4rem 1.15rem}}
.article .lead{font-size:1.08rem;color:rgba(10,10,10,.85)}
.article h2{font-size:1.35rem;font-weight:800;letter-spacing:-.02em;margin:2.2rem 0 .6rem}
.article p{color:rgba(10,10,10,.8);margin-top:.7rem}
.article ul,.article ol{padding-left:1.35rem;margin-top:.6rem;color:rgba(10,10,10,.8)}
.article li{margin-top:.4rem}
.article a{color:var(--gold);font-weight:600}
.article .tbl{overflow-x:auto;margin-top:1rem;-webkit-overflow-scrolling:touch}
.article table{width:100%;border-collapse:collapse;font-size:.9rem;min-width:30rem}
.article th,.article td{text-align:left;vertical-align:top;padding:.6rem .7rem;border-bottom:1px solid var(--line)}
.article th{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--gray)}
.article .meta{font-size:.82rem;color:var(--gray);margin-top:.6rem}
.cta{margin-top:2.4rem;background:#2c1418;color:#f6ece0;border-radius:1.2rem;padding:1.6rem 1.5rem;text-align:center}
.cta h2{color:#f6ece0;margin:0 0 .4rem;font-size:1.3rem}
.cta p{color:rgba(246,236,224,.82);margin:0 auto 1.1rem;max-width:32rem}
.faq-h{margin-top:2.6rem}
.faq-q{border-top:1px solid var(--line);padding:1rem 0}
.faq-q h3{font-size:1.02rem;font-weight:800;letter-spacing:-.01em}
.faq-q p{margin-top:.35rem}
.related{display:grid;gap:.8rem;grid-template-columns:repeat(auto-fit,minmax(min(14rem,100%),1fr));margin-top:1rem}
.related a{display:block;background:#faf6ee;border:1px solid var(--line);border-radius:.9rem;padding:.9rem 1rem;text-decoration:none;color:var(--ink);font-weight:700}
.related a span{display:block;font-size:.8rem;font-weight:500;color:var(--gray);margin-top:.2rem}
.guide-grid{display:grid;gap:1.1rem;grid-template-columns:repeat(auto-fit,minmax(min(17rem,100%),1fr));margin-top:1.4rem}
.guide-card{display:block;background:#fff;border:1px solid var(--line);border-radius:1.2rem;padding:1.4rem;text-decoration:none;color:var(--ink);box-shadow:0 12px 30px rgba(67,32,43,.08)}
.guide-card h2{font-size:1.12rem;font-weight:800;letter-spacing:-.015em;margin-top:.35rem}
.guide-card p{font-size:.9rem;color:var(--gray);margin-top:.45rem}
</style>'''


def head(title, description, path, jsonld):
    url = SITE + path
    t, d = html.escape(title), html.escape(description)
    ld = '\n'.join(
        f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in jsonld)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#ead9bc">
<meta name="apple-itunes-app" content="app-id=6811731965">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Goblet">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Goblet: While Other Apps Know Wine, Goblet Knows You. Scan a bottle, a wine list or a shelf.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
{STYLE}
{GUIDE_CSS}
{ld}
</head>'''


PUBLISHER = {'@type': 'Organization', 'name': 'Goblet', 'url': SITE + '/',
             'logo': {'@type': 'ImageObject', 'url': SITE + '/assets/apple-touch-icon.png'}}


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))


def wrap_tables(body):
    return body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')


def build_guide(g, by_slug):
    path = f"/guides/{g['slug']}.html"
    faq_ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in g['faq']]}
    article_ld = {'@context': 'https://schema.org', '@type': 'Article', 'headline': g['h1'],
                  'description': g['description'], 'image': SITE + '/assets/og-image.jpg',
                  'datePublished': TODAY, 'dateModified': TODAY,
                  'author': {'@type': 'Organization', 'name': 'Goblet', 'url': SITE + '/'},
                  'publisher': PUBLISHER, 'mainEntityOfPage': SITE + path, 'inLanguage': 'en'}
    crumbs_ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Wine guides', 'item': SITE + '/guides/'},
        {'@type': 'ListItem', 'position': 3, 'name': g['h1'], 'item': SITE + path}]}
    faq_block = ''.join(
        f'<div class="faq-q"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>' for q, a in g['faq'])
    related = ''.join(
        f'<a href="/guides/{s}.html">{by_slug[s]["h1"]}<span>{by_slug[s]["kicker"]}</span></a>'
        for s in g['related'])
    page = f'''{head(g['title'], g['description'], path, [article_ld, crumbs_ld, faq_ld])}
<body>
{header('/guides/')}
<main>
<article class="wrap narrow article" style="max-width:48rem">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/guides/">Wine guides</a> › {html.escape(g['kicker'])}</nav>
<div class="card-l">
<p class="kicker">{html.escape(g['kicker'])}</p>
<h1 style="font-size:clamp(1.9rem,5vw,2.6rem);margin-top:.45rem">{g['h1']}</h1>
<p class="meta">By the Goblet team · Updated <time datetime="{TODAY}">9 November 2026</time></p>
<p class="lead" style="margin-top:1.1rem">{g['intro']}</p>
{wrap_tables(g['body'])}
<div class="cta">
<h2>Know which wine you’ll love, in one photo</h2>
<p>Goblet scans a bottle, a wine list or a whole shelf and scores every wine for your own palate. Free on iPhone and Android.</p>
{rooted(BADGES)}
</div>
<h2 class="faq-h">Frequently asked questions</h2>
{faq_block}
<h2>Keep reading</h2>
<div class="related">{related}</div>
</div>
</article>
</main>
{rooted(FOOTER)}</body></html>
'''
    (ROOT / 'guides').mkdir(exist_ok=True)
    (ROOT / 'guides' / f"{g['slug']}.html").write_text(page)
    return path


def build_hub():
    path = '/guides/'
    title = 'Wine Guides: Choosing, Pairing and Tasting Wine | Goblet'
    desc = ('Plain-English wine guides: how to choose from a wine list, read a label, pair food and wine, '
            'buy a good bottle, taste like a pro, and find the wine you actually like.')
    items = {'@context': 'https://schema.org', '@type': 'ItemList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'url': f"{SITE}/guides/{g['slug']}.html", 'name': g['h1']}
        for i, g in enumerate(GUIDES)]}
    crumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Wine guides', 'item': SITE + '/guides/'}]}
    cards = ''.join(
        f'<a class="guide-card" href="/guides/{g["slug"]}.html"><p class="kicker">{html.escape(g["kicker"])}</p>'
        f'<h2>{g["h1"]}</h2><p>{html.escape(strip_tags(g["description"]))}</p></a>' for g in GUIDES)
    page = f'''{head(title, desc, path, [items, crumbs])}
<body>
{header('/guides/')}
<main>
<section class="page-hero"><p class="kicker">Learn wine</p><h1 style="margin-top:.5rem">Wine guides</h1>
<p class="sub">Everything worth knowing to choose, pair and enjoy wine, in plain English. No jargon you are not told the meaning of.</p></section>
<section class="wrap" style="padding:1rem 1.4rem 3rem"><div class="guide-grid">{cards}</div>
<div class="cta" style="max-width:46rem;margin-left:auto;margin-right:auto">
<h2>Or let Goblet choose</h2>
<p>Scan a bottle, a wine list or a shelf and Goblet scores every wine for your palate, out of 10, with the reason in plain English.</p>
{rooted(BADGES)}
</div></section>
</main>
{rooted(FOOTER)}</body></html>
'''
    (ROOT / 'guides' / 'index.html').write_text(page)
    return path


def main():
    by_slug = {g['slug']: g for g in GUIDES}
    for g in GUIDES:
        assert len(g['title']) <= 60, (g['slug'], len(g['title']))
        assert 110 <= len(g['description']) <= 155, (g['slug'], len(g['description']))
        for s in g['related']:
            assert s in by_slug, s
        print(build_guide(g, by_slug))
    print(build_hub())


if __name__ == '__main__':
    main()
