#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bygger bilforsakringspriser.se från en gemensam mall.

Kör:  python3 build.py
Alla sidor genereras om från grunden, så redigera innehållet här — inte i
de färdiga HTML-filerna.
"""
import os, json, re, html

BASE = 'https://bilforsakringspriser.se'
V = '20260101a'           # cache-stämpel — höj vid ändring i css/js
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

NAV = [
    ('/jamfor-bilforsakring/', 'Jämför priser'),
    ('/trafikforsakring/', 'Trafikförsäkring'),
    ('/halvforsakring/', 'Halvförsäkring'),
    ('/helforsakring/', 'Helförsäkring'),
    ('/om-oss/', 'Om oss'),
]

LOGO_SVG = ('<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#12263f"/>'
            '<rect x="12" y="22" width="40" height="20" rx="4" fill="none" stroke="#4a9fd8" stroke-width="4"/>'
            '<rect x="12" y="22" width="10" height="20" rx="4" fill="#4a9fd8"/>'
            '<path d="M29 36v-8m6 8v-8m6 8v-8" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/></svg>')

CK = ('<span class="ck"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" '
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></span>')

ARR = '<span class="arw" aria-hidden="true">&rarr;</span>'


def plate(pid, btn_text, note=''):
    """Registreringsnummerfält med knapp."""
    n = f'<p class="anchor-note">{note}</p>' if note else ''
    return f'''<div class="plate">
<span class="plate-eu" aria-hidden="true"><span class="plate-stars">&#9733;&nbsp;&#9733;<br>&#9733;</span><span class="plate-cc">S</span></span>
<input id="{pid}" data-plate type="text" inputmode="latin" placeholder="ABC 123" maxlength="7" aria-label="Registreringsnummer" autocomplete="off" spellcheck="false">
</span></div>
<button type="button" class="btn" data-go="{pid}">{btn_text} {ARR}</button>
<button type="button" class="btn-ghost" data-go="">Jag kan inte mitt registreringsnummer</button>
{n}'''.replace('</span></div>', '</div>', 1)


def hero(d):
    checks = ''.join(f'<li>{CK}<span>{c}</span></li>' for c in d.get('checks', []))
    crumbs = ''
    if d['slug']:
        crumbs = ('<nav class="crumbs" aria-label="Brödsmulor"><a href="/">Start</a> '
                  f'<span aria-hidden="true">/</span> <span>{d["h1"]}</span></nav>')
    return f'''<section class="hero"><div class="wrap hero-in">
<div>{crumbs}
<span class="eyebrow">{d["eyebrow"]}</span>
<h1>{d["h1"]}</h1>
<p class="lead">{d["lead"]}</p>
<ul class="checks">{checks}</ul>
</div>
<div><div class="card">
<span class="card-lab">Gratis jämförelse</span>
<p class="card-t">{d.get("card_t", "Se vad din bil kostar att försäkra")}</p>
<p class="card-s">{d.get("card_s", "Ange registreringsnumret, så hämtas bilens uppgifter automatiskt. Du fyller inte i märke, modell eller årsmodell.")}</p>
{plate("heroPlate", d.get("card_btn", "Jämför gratis nu"), d.get("card_note", ""))}
<div class="trust"><span>Kostnadsfritt</span><span>Ingen registrering</span><span>Ingen bindning</span></div>
</div></div>
</div></section>'''


def sticky(text):
    return f'''<div class="sticky"><div class="wrap sticky-in">
<div class="sticky-t">{text}<span>Kostnadsfritt och utan bindning</span></div>
<button type="button" class="btn" data-go="">Jämför nu {ARR}</button>
</div></div>'''


def footer():
    return f'''<footer class="ft"><div class="wrap">
<div class="ft-grid">
<div>
<h3>Bilförsäkringspriser.se</h3>
<p>Oberoende jämförelse av bilförsäkring i Sverige. Vi säljer inga försäkringar och företräder inget bolag.</p>
<p>Sidan innehåller kommersiella länkar. <a href="/redaktionell-metod/">Så tjänar vi pengar</a>.</p>
</div>
<div><h3>Försäkring</h3><ul>
<li><a href="/jamfor-bilforsakring/">Jämför priser</a></li>
<li><a href="/trafikforsakring/">Trafikförsäkring</a></li>
<li><a href="/halvforsakring/">Halvförsäkring</a></li>
<li><a href="/helforsakring/">Helförsäkring</a></li>
</ul></div>
<div><h3>Om sajten</h3><ul>
<li><a href="/om-oss/">Om oss</a></li>
<li><a href="/redaktionell-metod/">Redaktionell metod</a></li>
<li><a href="/integritetspolicy/">Integritetspolicy</a></li>
<li><a href="/cookiepolicy/">Cookiepolicy</a></li>
</ul></div>
</div>
<div class="ft-btm">
<span>&copy; 2026 Bilförsäkringspriser.se</span>
<span>Priser är redaktionella uppskattningar, inte offerter. Ditt eget pris beräknas av försäkringsbolaget.</span>
</div>
</div></footer>'''


def page(d):
    slug = d['slug']
    url = f'{BASE}/{slug}/' if slug else f'{BASE}/'
    nav = ''.join(
        f'<a href="{u}"{" aria-current=\"page\"" if u.strip("/") == slug else ""}>{t}</a>'
        for u, t in NAV)

    ld = [{
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": ([{"@type": "ListItem", "position": 1, "name": "Start", "item": BASE + "/"}]
                            + ([{"@type": "ListItem", "position": 2, "name": d["h1"], "item": url}] if slug else []))
    }] if slug else []

    if d.get('faq'):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}}
            for q, a in d['faq']]})

    ld.append({
        "@context": "https://schema.org", "@type": "Article",
        "headline": d['title'], "description": d['desc'],
        "inLanguage": "sv-SE",
        "author": {"@type": "Person", "name": "Emil Rostgaard Clausen",
                   "url": BASE + "/om-oss/", "jobTitle": "Ansvarig utgivare"},
        "publisher": {"@type": "Organization", "name": "Bilförsäkringspriser.se", "url": BASE + "/",
                      "logo": {"@type": "ImageObject", "url": BASE + "/assets/icon-512.png",
                               "width": 512, "height": 512}},
        "datePublished": "2026-01-01", "dateModified": "2026-01-01",
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}})

    if not slug:
        ld.append({"@context": "https://schema.org", "@type": "WebSite",
                   "name": "Bilförsäkringspriser.se", "url": BASE + "/", "inLanguage": "sv-SE"})

    ld_tags = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
                      for x in ld)

    faq_html = ''
    if d.get('faq'):
        items = ''.join(
            f'<div class="q"><button type="button" class="q-btn">{q}'
            f'<svg class="q-arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
            f'stroke-linecap="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>'
            f'<div class="q-a">{a}</div></div>' for q, a in d['faq'])
        faq_html = (f'<section class="sec alt"><div class="wrap narrow">'
                    f'<h2>{d.get("faq_h2", "Vanliga frågor")}</h2><div class="faq">{items}</div></div></section>')

    rel = ''
    if d.get('rel'):
        li = ''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in d['rel'])
        rel = f'<div class="wrap narrow"><nav class="rel" aria-label="Läs vidare"><h2>Läs vidare</h2><ul>{li}</ul></nav></div>'

    body_html = d['body'].replace('{PLATE}', plate('pagePlate', 'Jämför gratis nu'))

    return f'''<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d['title']}</title>
<meta name="description" content="{d['desc']}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="sv_SE">
<meta property="og:site_name" content="Bilförsäkringspriser.se">
<meta property="og:title" content="{d['title']}">
<meta property="og:description" content="{d['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/icon-512.png">
<meta name="twitter:card" content="summary">
<link rel="preload" as="font" type="font/woff2" crossorigin href="/assets/fonts/schibsted-grotesk.woff2">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#12263f">
<link rel="stylesheet" href="/assets/v2.css?v={V}">
<script src="/assets/v2.js?v={V}" defer></script>
{ld_tags}
</head>
<body>
<a class="sr-only" href="#main">Hoppa till innehållet</a>
<header class="hd"><div class="wrap hd-in">
<a class="logo" href="/">{LOGO_SVG}<span>Bilförsäkrings</span>priser.se</a>
<button type="button" class="burger" aria-label="Meny" aria-controls="nav"><span></span></button>
<nav class="nav" id="nav" aria-label="Huvudmeny">{nav}</nav>
<a class="hd-cta" href="#" data-go="">Jämför gratis</a>
</div></header>

<main id="main">
{hero(d)}
{body_html}
{faq_html}
{rel}
</main>

{sticky(d.get('sticky', 'Se vad din bil kostar att försäkra'))}
{footer()}
</body>
</html>'''


# ═══ INNEHÅLL ═══════════════════════════════════════════════════════
# Priserna nedan är MARKERADE SOM PLATSHÅLLARE. Ersätt dem med egna
# insamlade siffror innan lansering — se README.

import pages
PAGES = pages.PAGES

for d in PAGES:
    out = os.path.join(d['slug'], 'index.html') if d['slug'] else 'index.html'
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    open(out, 'w', encoding='utf-8').write(page(d))
    words = len(re.findall(r'[A-Za-zÅÄÖåäö0-9][\wÅÄÖåäö-]*',
                           re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', page(d))))
    print(f'{("/" + d["slug"] + "/") if d["slug"] else "/":34s} {words:5d} ord')

# ── Sitemap ─────────────────────────────────────────────────────────
urls = ''.join(
    f'\n  <url><loc>{BASE}/{d["slug"]}/</loc>' if d['slug'] else f'\n  <url><loc>{BASE}/</loc>'
    for d in PAGES)
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for d in PAGES:
    loc = f'{BASE}/{d["slug"]}/' if d['slug'] else f'{BASE}/'
    pri = '1.0' if not d['slug'] else ('0.9' if d.get('key') else '0.6')
    sm.append(f'  <url><loc>{loc}</loc><lastmod>2026-01-01</lastmod>'
              f'<changefreq>monthly</changefreq><priority>{pri}</priority></url>')
sm.append('</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
print(f'\nsitemap.xml: {len(PAGES)} adresser')
