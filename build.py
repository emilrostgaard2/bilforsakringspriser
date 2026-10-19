#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bygger bilforsakringspriser.se från en gemensam mall.

Kör:  python3 build.py
Alla sidor genereras om från grunden, så redigera innehållet här — inte i
de färdiga HTML-filerna.
"""
import os, json, re, html
import data, forfattare, datum

BASE = 'https://bilforsakringspriser.se'
KONTAKT = 'info@bilforsakringspriser.se'
V = '20261019a'           # cache-stämpel — höj vid ändring i css/js
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# Menyn. Undermenyer hålls under sju poster så att de ryms i en spalt.
# Ortssidorna ligger medvetet bara i sidfoten — de är för smala för menyn.
NAV = [
    ('/jamfor-bilforsakring/', 'Jämför'),
    ('Skyddsnivåer', [
        ('/trafikforsakring/', 'Trafikförsäkring'),
        ('/halvforsakring/', 'Halvförsäkring'),
        ('/helforsakring/', 'Helförsäkring'),
        ('/sjalvrisk/', 'Självrisk'),
    ]),
    ('Guider', [
        ('/basta-bilforsakringen/', 'Bästa bilförsäkringen'),
        ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
        ('/byta-bilforsakring/', 'Byta bilförsäkring'),
        ('/bonus-och-skadefria-ar/', 'Bonus och skadefria år'),
        ('/bilforsakring-pris-per-manad/', 'Pris per månad'),
        ('/trafikforsakringsavgift/', 'Trafikförsäkringsavgift'),
        ('/viltolycka-forsakring/', 'Viltolycka'),
    ]),
    ('Din situation', [
        ('/bilforsakring-elbil/', 'Elbil'),
        ('/leasingbil-forsakring/', 'Leasingbil'),
        ('/bilforsakring-ung-forare/', 'Ung förare'),
        ('/bilforsakring-pensionar/', 'Pensionär'),
        ('/bilforsakring-18-ar/', '18-åring'),
        ('/kopa-bil-forsakring/', 'Köpa bil'),
    ]),
    ('Bolag', [
        ('/forsakringsbolag/folksam/', 'Folksam'),
        ('/forsakringsbolag/lansforsakringar/', 'Länsförsäkringar'),
        ('/forsakringsbolag/if/', 'If'),
        ('/forsakringsbolag/trygg-hansa/', 'Trygg-Hansa'),
        ('/forsakringsbolag/hedvig/', 'Hedvig'),
        ('»', '/forsakringsbolag/', 'Se alla 16 bolag'),
    ]),
    ('Bilmärken', [
        ('/bilmarken/volvo/', 'Volvo'),
        ('/bilmarken/volkswagen/', 'Volkswagen'),
        ('/bilmarken/toyota/', 'Toyota'),
        ('/bilmarken/tesla/', 'Tesla'),
        ('/bilmarken/bmw/', 'BMW'),
        ('»', '/bilmarken/', 'Se alla 37 märken'),
    ]),
]

DD_ARR = ('<svg class="dd-arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
          'stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')


def navbar(slug):
    """Menyn. Undermenyernas länkar är riktiga <a> i HTML — de finns för
    crawlern även utan JavaScript, och ligger dessutom i sidfoten.

    En post som börjar med '»' blir en avslutande "se alla"-länk."""
    ut = []
    for i, (a, b) in enumerate(NAV):
        if isinstance(b, list):
            oppen = any(p[-2].strip('/') == slug for p in
                        [(x if len(x) == 3 else ('', x[0], x[1])) for x in b])
            delar = []
            for post in b:
                alla = len(post) == 3
                u, t = (post[1], post[2]) if alla else post
                nu = ' aria-current="page"' if u.strip('/') == slug else ''
                kl = ' class="dd-alla"' if alla else ''
                pil = ' &rarr;' if alla else ''
                delar.append(f'<a href="{u}"{nu}{kl}>{t}{pil}</a>')
            ut.append(
                f'<div class="nav-item{" here" if oppen else ""}">'
                f'<button type="button" class="nav-btn" aria-expanded="false" '
                f'aria-controls="dd{i}">{a}{DD_ARR}</button>'
                f'<div class="dd" id="dd{i}">{"".join(delar)}</div></div>')
        else:
            nu = ' aria-current="page"' if a.strip('/') == slug else ''
            ut.append(f'<a href="{a}"{nu}>{b}</a>')
    return ''.join(ut)

LOGO_SVG = ('<svg viewBox="0 0 64 64" aria-hidden="true">'
            '<rect width="64" height="64" rx="14" fill="#12263f"/>'
            '<path d="M32 8 13.5 14v14.6c0 11.2 7.6 21 18.5 23.4 10.9-2.4 18.5-12.2 18.5-23.4V14z" fill="#4a9fd8"/>'
            '<path d="M22 36.5c0-.6.1-1.2.4-1.7l2.6-5.2a2.6 2.6 0 0 1 2.3-1.4h9.4a2.6 2.6 0 0 1 2.3 1.4'
            'l2.6 5.2c.3.5.4 1.1.4 1.7v4.1a1.7 1.7 0 0 1-1.7 1.7h-1.5a1.7 1.7 0 0 1-1.7-1.7v-.9'
            'H26.9v.9a1.7 1.7 0 0 1-1.7 1.7h-1.5A1.7 1.7 0 0 1 22 40.6z" fill="#fff"/>'
            '<path d="M25.6 34.4h12.8l-1.8-3.6a1 1 0 0 0-.9-.6h-7.4a1 1 0 0 0-.9.6z" fill="#12263f"/></svg>')

CK = ('<span class="ck"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" '
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></span>')

ARR = '<span class="arw" aria-hidden="true">&rarr;</span>'


# Knappen går till en annonslänk. Marknadsföringslagen kräver att
# reklam går att känna igen som reklam, så raden nedan ska stå kvar så
# länge målet är en affiliatelänk — och tas bort om det slutar vara det.
ANNONSNOTER = [
 'Annonslänk. Vi kan få ersättning om du tecknar via Zmarta, vilket inte påverkar ditt pris.',
 'Knappen går till Zmarta via en annonslänk. Ersättningen vi får påverkar inte vad du betalar.',
 'Annonslänk till jämförelsetjänsten Zmarta. Vi får ersättning, du betalar samma pris.',
 'Detta är en annonslänk. Zmarta ersätter oss för förmedlade kunder — ditt pris är detsamma.',
 'Annonslänk. Vi tjänar pengar när någon tecknar via Zmarta, men priset för dig är oförändrat.',
 'Länken är en annonslänk till Zmarta. Vår ersättning läggs inte på din premie.',
 'Annonslänk till Zmarta. Vi får betalt av dem, aldrig av dig.',
]


def annonsnot(slug):
    """Annonsmärkning under knappen.

    Marknadsföringslagen kräver att reklam går att känna igen som reklam,
    så raden ska stå kvar så länge målet är en affiliatelänk. Sju
    formuleringar, valda per sida — varje variant säger samma sak
    fullständigt, men samma mening hamnar inte på tvåhundra sidor."""
    i = sum(ord(c) for c in (slug or 'start'))
    return (f'<p class="plate-ad">{ANNONSNOTER[i % len(ANNONSNOTER)]} '
            f'<a href="/redaktionell-metod/">Så finansieras sajten</a>.</p>')


def plate(pid, btn_text, note='', slug=''):
    """Registreringsnummerfält med knapp."""
    n = f'<p class="anchor-note">{note}</p>' if note else ''
    return f'''<div class="plate">
<span class="plate-eu" aria-hidden="true"><span class="plate-stars">&#9733;&nbsp;&#9733;<br>&#9733;</span><span class="plate-cc">S</span></span>
<input id="{pid}" data-plate type="text" inputmode="latin" placeholder="ABC 123" maxlength="7" aria-label="Registreringsnummer" autocomplete="off" spellcheck="false">
</span></div>
<button type="button" class="btn" data-go="{pid}">{btn_text} {ARR}</button>
<button type="button" class="btn-ghost" data-go="">Fortsätt utan registreringsnummer</button>
{n}{annonsnot(slug)}'''.replace('</span></div>', '</div>', 1)


MANAD = ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti',
         'september', 'oktober', 'november', 'december']


def svdatum(iso):
    a, m, dg = iso.split('-')
    return f'{int(dg)} {MANAD[int(m) - 1]} {a}'


def _upd(d):
    """Synligt uppdateringsdatum och byline under ingressen.

    Samma datum som dateModified i schemat — Google och AI-sök jämför
    dem, och ett datum som bara finns i koden räknas inte som färskt."""
    if d['slug'] in ('integritetspolicy', 'cookiepolicy'):
        return ''
    import forfattare as _f
    return (f'<p class="upd">Uppdaterad <time datetime="{d["_mod"]}">{svdatum(d["_mod"])}</time>'
            f'<span aria-hidden="true">&middot;</span>'
            f'<span>Av <a href="{_f.FORFATTARE["sida"]}">{_f.FORFATTARE["namn"]}</a></span></p>')


def hero(d):
    checks = ''.join(f'<li>{CK}<span>{c}</span></li>' for c in d.get('checks', []))
    crumbs = ''
    if d['slug']:
        dele = d['slug'].split('/')
        mid = ''
        if len(dele) > 1:
            far = {'forsakringsbolag': 'Försäkringsbolag', 'bilmarken': 'Bilmärken'}.get(dele[0], dele[0])
            mid = f'<a href="/{dele[0]}/">{far}</a> <span aria-hidden="true">/</span> '
        # Modellsidor har tre nivåer: Start / Bilmärken / Volvo / Volvo XC60.
        # Utan mellanledet tappar besökaren vägen tillbaka till märket.
        if len(dele) > 2:
            import brands as _b
            _namn = {x['slug']: x['namn'] for x in _b.MARKEN}.get(dele[1], dele[1].title())
            mid += (f'<a href="/{dele[0]}/{dele[1]}/">{_namn}</a> '
                    f'<span aria-hidden="true">/</span> ')
        crumbs = ('<nav class="crumbs" aria-label="Brödsmulor"><a href="/">Start</a> '
                  f'<span aria-hidden="true">/</span> {mid}<span>{d["h1"]}</span></nav>')
    return f'''<section class="hero"><div class="wrap hero-in">
<div>{crumbs}
<span class="eyebrow">{d["eyebrow"]}</span>
<h1>{d["h1"]}</h1>
<p class="lead">{d["lead"]}</p>
{_upd(d)}
<ul class="checks">{checks}</ul>
</div>
<div><div class="card">
<span class="card-lab">Gratis jämförelse</span>
<p class="card-t">{d.get("card_t", "Se vad din bil kostar att försäkra")}</p>
<p class="card-s">{d.get("card_s", "Fortsätt till Zmarta och jämför offerter från flera bolag i ett och samma formulär. Bilens uppgifter hämtas via registreringsnumret.")}</p>
{plate("heroPlate", d.get("card_btn", "Jämför gratis nu"), d.get("card_note", ""), d["slug"])}
<div class="trust"><span>Kostnadsfritt</span><span>Ingen bindning</span><span>Flera bolag i ett formulär</span></div>
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
<p class="ft-h">Bilförsäkringspriser.se</p>
<p>Oberoende jämförelse av bilförsäkring i Sverige. Vi säljer inga försäkringar och företräder inget bolag.</p>
<p>Sidan innehåller kommersiella länkar. <a href="/redaktionell-metod/">Så tjänar vi pengar</a>.</p>
</div>
<div><p class="ft-h">Försäkring</p><ul>
<li><a href="/jamfor-bilforsakring/">Jämför priser</a></li>
<li><a href="/trafikforsakring/">Trafikförsäkring</a></li>
<li><a href="/halvforsakring/">Halvförsäkring</a></li>
<li><a href="/helforsakring/">Helförsäkring</a></li>
</ul></div>
<div><p class="ft-h">Guider</p><ul>
<li><a href="/basta-bilforsakringen/">Bästa bilförsäkringen</a></li>
<li><a href="/billigaste-bilforsakringen/">Billigaste bilförsäkringen</a></li>
<li><a href="/bilforsakring-elbil/">Bilförsäkring elbil</a></li>
<li><a href="/leasingbil-forsakring/">Försäkring vid leasing</a></li>
<li><a href="/bilforsakring-ung-forare/">Ung förare</a></li>
<li><a href="/bilforsakring-pensionar/">Pensionär</a></li>
<li><a href="/bilforsakring-18-ar/">18-åring</a></li>
<li><a href="/bilforsakring-utan-bonus/">Utan bonus</a></li>
<li><a href="/bilforsakring-pris-per-manad/">Pris per månad</a></li>
<li><a href="/kopa-bil-forsakring/">Köpa bil</a></li>
<li><a href="/saga-upp-bilforsakring/">Säga upp</a></li>
</ul></div>
<div><p class="ft-h">Fakta</p><ul>
<li><a href="/sjalvrisk/">Självrisk</a></li>
<li><a href="/byta-bilforsakring/">Byta bilförsäkring</a></li>
<li><a href="/bonus-och-skadefria-ar/">Bonus och skadefria år</a></li>
<li><a href="/trafikforsakringsavgift/">Trafikförsäkringsavgift</a></li>
<li><a href="/avstalld-bil/">Avställd bil</a></li>
<li><a href="/viltolycka-forsakring/">Viltolycka</a></li>
<li><a href="/glasskada-bil/">Glasskada</a></li>
<li><a href="/vagnskadegaranti/">Vagnskadegaranti</a></li>
<li><a href="/bilforsakring-utomlands/">Utomlands</a></li>
<li><a href="/korstracka-mil-per-ar/">Körsträcka</a></li>
</ul></div>
<div><p class="ft-h">Orter</p><ul>
<li><a href="/bilforsakring-stockholm/">Stockholm</a></li>
<li><a href="/bilforsakring-goteborg/">Göteborg</a></li>
<li><a href="/bilforsakring-malmo/">Malmö</a></li>
</ul></div>
<div><p class="ft-h">Om sajten</p><ul>
<li><a href="/om-oss/">Om oss</a></li>
<li><a href="/redaktionell-metod/">Redaktionell metod</a></li>
<li><a href="/integritetspolicy/">Integritetspolicy</a></li>
<li><a href="/cookiepolicy/">Cookiepolicy</a></li>
</ul></div>
</div>
<div class="ft-btm">
<span>&copy; 2026 Bilförsäkringspriser.se &middot; Ansvarig utgivare: Emil Rostgaard Clausen &middot; <a href="mailto:{KONTAKT}">{KONTAKT}</a></span>
<span>Priser är redaktionella uppskattningar, inte offerter. Ditt eget pris beräknas av försäkringsbolaget.</span>
</div>
</div></footer>'''


# Trafikförsäkringsavgift per dag, från Trafikförsäkringsföreningen.
# Källa: https://www.tff.se/sv/krav/avgift-for-oforsakrade-fordon/
# (sidan uppdaterad oktober 2026). Kontrollera satserna varje januari.
TFA = {'kalla': 'https://www.tff.se/sv/krav/avgift-for-oforsakrade-fordon/',
       'datum': 'oktober 2026', 'min': 200,
       'satser': [('Personbil (privat)', 202), ('Motorcykel över 125 cc', 224),
                  ('Lätt motorcykel', 34)]}


def tfa_kalkylator():
    """Räknar ut avgiften för en period utan trafikförsäkring.

    Ingen annan svensk sajt har en sådan räknare — TFF publicerar bara
    tabellen. Fungerar utan JS som en vanlig tabell med satserna."""
    opt = ''.join(f'<option value="{v}">{t} — {v} kr/dag</option>' for t, v in TFA['satser'])
    return f'''<section class="sec"><div class="wrap narrow">
<h2>Räkna ut trafikförsäkringsavgiften</h2>
<p>Välj fordonstyp och hur många dagar fordonet varit utan trafikförsäkring. Från dag 91
sjunker dagsavgiften till 50 procent och från dag 181 till 25 procent.</p>
<form class="kalk" data-tfa data-min="{TFA['min']}" onsubmit="return false">
<div class="kalk-rad">
<label>Fordonstyp<select>{opt}</select></label>
<label>Dagar utan försäkring<input type="number" inputmode="numeric" min="1" max="3650" value="30"></label>
</div>
<p class="kalk-res" aria-live="polite">Uppskattad avgift beräknas när sidan laddats.</p>
<p class="kalk-not">Uppskattning utifrån satserna hos
<a href="{TFA['kalla']}" target="_blank" rel="noopener">Trafikförsäkringsföreningen</a>
({TFA['datum']}), minimiavgift {TFA['min']} kr. Beslutet om din avgift fattas av TFF.
Veteranfordon 30 år och äldre har lägre avgift.</p>
</form></div></section>'''


def page(d):
    slug = d['slug']
    url = f'{BASE}/{slug}/' if slug else f'{BASE}/'
    nav = navbar(slug)

    bc = [{"@type": "ListItem", "position": 1, "name": "Start", "item": BASE + "/"}]
    if slug:
        dele = slug.split('/')
        if len(dele) > 1:
            far = {'forsakringsbolag': 'Försäkringsbolag', 'bilmarken': 'Bilmärken'}.get(dele[0], dele[0])
            bc.append({"@type": "ListItem", "position": 2, "name": far, "item": f"{BASE}/{dele[0]}/"})
        # Tre nivåer: /bilmarken/volvo/xc60/ ska ha Volvo som eget steg,
        # annars tappar brödsmulan mellanledet i sökresultatet.
        if len(dele) > 2:
            import brands as _b
            _namn = {x['slug']: x['namn'] for x in _b.MARKEN}.get(dele[1], dele[1].title())
            bc.append({"@type": "ListItem", "position": 3, "name": _namn,
                       "item": f"{BASE}/{dele[0]}/{dele[1]}/"})
        bc.append({"@type": "ListItem", "position": len(bc) + 1, "name": d["h1"], "item": url})

    # Ett sammanhängande @graph med fasta @id:n. Organisation, webbplats
    # och författare beskrivs en gång och refereras sedan — det är så
    # Google och AI-sök knyter ihop sidorna till samma utgivare.
    ORG, SITE, PERS = BASE + '/#org', BASE + '/#website', BASE + '/#emil'
    graf = [
        {"@type": "Organization", "@id": ORG, "name": "Bilförsäkringspriser.se", "url": BASE + "/",
         "email": KONTAKT,
         "logo": {"@type": "ImageObject", "url": BASE + "/assets/icon-512.png", "width": 512, "height": 512},
         "founder": {"@id": PERS}},
        {"@type": "WebSite", "@id": SITE, "name": "Bilförsäkringspriser.se", "url": BASE + "/",
         "inLanguage": "sv-SE", "publisher": {"@id": ORG}},
        {**forfattare.schema(BASE), "@id": PERS, "worksFor": {"@id": ORG}},
    ]
    typ = ('CollectionPage' if slug in ('bilmarken', 'forsakringsbolag')
           else 'AboutPage' if slug == 'om-oss'
           else 'WebPage')
    sida = {"@type": typ, "@id": url + "#webpage", "url": url, "name": d['title'],
            "description": d['desc'], "inLanguage": "sv-SE", "isPartOf": {"@id": SITE},
            "datePublished": d['_pub'], "dateModified": d['_mod']}
    if slug:
        sida["breadcrumb"] = {"@id": url + "#breadcrumb"}
        graf.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": bc})
    graf.append(sida)

    # Artikel bara där det är en artikel — inte på startsidan, hubbar
    # eller juridiska sidor.
    if slug and typ == 'WebPage' and slug not in ('integritetspolicy', 'cookiepolicy', 'redaktionell-metod'):
        art = {"@type": "Article", "@id": url + "#article", "headline": d['h1'],
               "description": d['desc'], "inLanguage": "sv-SE",
               "author": {"@id": PERS}, "publisher": {"@id": ORG},
               "datePublished": d['_pub'], "dateModified": d['_mod'],
               "mainEntityOfPage": {"@id": url + "#webpage"}, "isPartOf": {"@id": SITE}}
        if d.get('bild'):
            art["image"] = {"@type": "ImageObject", "url": BASE + d['bild'], "width": 1200,
                            "height": 750, "caption": d.get('bild_alt', d['h1'])}
        graf.append(art)
    else:
        sida["author"] = {"@id": PERS}
        sida["publisher"] = {"@id": ORG}

    if d.get('faq'):
        graf.append({"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"},
                     "mainEntity": [
            {"@type": "Question", "name": re.sub(r'<[^>]+>', '', q),
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}}
            for q, a in d['faq']]})

    ld_tags = ('<script type="application/ld+json">'
               + json.dumps({"@context": "https://schema.org", "@graph": graf}, ensure_ascii=False)
               + '</script>')

    # Startsidan har breda partnerkort högst upp; då ska FAQ, läs vidare
    # och författarrutan linjera med dem i stället för att hoppa in.
    wr = 'wrap' if slug == '' else 'wrap narrow'

    faq_html = ''
    if d.get('faq'):
        items = ''.join(
            f'<div class="q"><button type="button" class="q-btn">{q}'
            f'<svg class="q-arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
            f'stroke-linecap="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>'
            f'<div class="q-a">{a}</div></div>' for q, a in d['faq'])
        faq_html = (f'<section class="sec alt"><div class="{wr}">'
                    f'<h2>{d.get("faq_h2", "Vanliga frågor")}</h2><div class="faq">{items}</div></div></section>')

    rel = ''
    if d.get('rel'):
        li = ''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in d['rel'])
        rel = f'<div class="{wr}"><nav class="rel" aria-label="Läs vidare"><h2>Läs vidare</h2><ul>{li}</ul></nav></div>'

    body_html = d['body'].replace('{PLATE}', plate('pagePlate', 'Jämför gratis nu', slug=slug))
    if slug == 'trafikforsakringsavgift':
        body_html = tfa_kalkylator() + body_html

    # Sidor med egen bild delas med stor förhandsvisning, övriga med logotypen.
    if d.get('bild'):
        og_bild = (f'<meta property="og:image" content="{BASE}{d["bild"]}">\n'
                   f'<meta property="og:image:width" content="1200">\n'
                   f'<meta property="og:image:height" content="750">\n'
                   f'<meta property="og:image:alt" content="{html.escape(d.get("bild_alt", d["h1"]), quote=True)}">\n'
                   f'<meta name="twitter:card" content="summary_large_image">')
    else:
        og_bild = (f'<meta property="og:image" content="{BASE}/assets/icon-512.png">\n'
                   f'<meta name="twitter:card" content="summary">')

    return f'''<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d['title']}</title>
<meta name="description" content="{d['desc']}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{'website' if not slug else 'article'}">
<meta name="author" content="Emil Rostgaard Clausen">
<meta property="og:locale" content="sv_SE">
<meta property="og:site_name" content="Bilförsäkringspriser.se">
<meta property="og:title" content="{d['title']}">
<meta property="og:description" content="{d['desc']}">
<meta property="og:url" content="{url}">
{og_bild}
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
<a class="logo" href="/">{LOGO_SVG}<span class="logo-t"><b>Bilförsäkrings</b>priser.se</span></a>
<button type="button" class="burger" aria-label="Meny" aria-controls="nav"><span></span></button>
<nav class="nav" id="nav" aria-label="Huvudmeny">{nav}</nav>
<button type="button" class="hd-cta" data-go="">Jämför gratis</button>
</div></header>

<main id="main">
{hero(d)}
{body_html}
{faq_html}
{rel}
</main>

{forfattare.ruta(wr)}

{sticky(d.get('sticky', 'Se vad din bil kostar att försäkra'))}
{footer()}
</body>
</html>'''


# ═══ INNEHÅLL ═══════════════════════════════════════════════════════
# Priserna nedan är MARKERADE SOM PLATSHÅLLARE. Ersätt dem med egna
# insamlade siffror innan lansering — se README.

import pages, generators, guider, fakta, orter, topplista, modellsidor
PAGES = (pages.PAGES + generators.alla() + guider.SIDOR
         + [topplista.sidan()] + fakta.SIDOR + orter.SIDOR
         + modellsidor.sidor())
try:
    import nya
    PAGES += nya.SIDOR
except ImportError:
    pass

for d in PAGES:
    datum.satt(d)
datum.spara()

for d in PAGES:
    out = os.path.join(d['slug'], 'index.html') if d['slug'] else 'index.html'
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    open(out, 'w', encoding='utf-8').write(page(d))
    words = len(re.findall(r'[A-Za-zÅÄÖåäö0-9][\wÅÄÖåäö-]*',
                           re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', page(d))))
    print(f'{("/" + d["slug"] + "/") if d["slug"] else "/":34s} {words:5d} ord')

# ── Sitemap ─────────────────────────────────────────────────────────
# lastmod är sidans eget uppdateringsdatum. priority och changefreq är
# borttagna: Google ignorerar dem, och samma värde på alla sidor sade
# ändå ingenting.
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for d in PAGES:
    loc = f'{BASE}/{d["slug"]}/' if d['slug'] else f'{BASE}/'
    sm.append(f'  <url><loc>{loc}</loc><lastmod>{d["_mod"]}</lastmod></url>')
sm.append('</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
print(f'\nsitemap.xml: {len(PAGES)} adresser')

# ── 404 ─────────────────────────────────────────────────────────────
# Byggs från samma mall som allt annat, så att css-versionen och menyn
# alltid stämmer. noindex sätts i efterhand.
_404 = {'slug': '', 'title': 'Sidan finns inte — Bilförsäkringspriser.se',
        'desc': 'Sidan du sökte finns inte. Här är guiderna de flesta letar efter.',
        'eyebrow': 'Fel 404', 'h1': 'Sidan finns inte',
        'lead': 'Adressen kan ha ändrats eller skrivits fel. Här är sidorna de flesta letar efter.',
        '_pub': data.UPPDATERAD, '_mod': data.UPPDATERAD,
        'body': '<section class="sec"><div class="wrap narrow"><ul>'
                + ''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in [
                    ('/jamfor-bilforsakring/', 'Jämför bilförsäkring'),
                    ('/bilforsakring-pris-per-manad/', 'Vad kostar bilförsäkring per månad?'),
                    ('/halvforsakring/', 'Halvförsäkring'), ('/helforsakring/', 'Helförsäkring'),
                    ('/forsakringsbolag/', 'Alla försäkringsbolag'), ('/bilmarken/', 'Bilmärken och modeller')])
                + '</ul></div></section>'}
h = page(_404)
h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">',
              '<meta name="robots" content="noindex, follow">')
h = re.sub(r'<link rel="canonical"[^>]*>\n', '', h)
h = re.sub(r'<script type="application/ld\+json">.*?</script>', '', h, flags=re.S)
h = h.replace('<p class="upd">', '<p class="upd" hidden>')
open('404.html', 'w', encoding='utf-8').write(h)

# ── llms.txt ────────────────────────────────────────────────────────
# Kort karta över sajten för AI-sökmotorer (llmstxt.org). Den ersätter
# inte sitemap.xml, men talar om vad sajten är och var svaren finns.
_grupper = [
    ('Jämföra och priser', ['', 'jamfor-bilforsakring', 'bilforsakring-pris-per-manad',
                            'billigaste-bilforsakringen', 'basta-bilforsakringen', 'byta-bilforsakring']),
    ('Skyddsnivåer och villkor', ['trafikforsakring', 'halvforsakring', 'helforsakring', 'sjalvrisk',
                                  'vagnskadegaranti', 'glasskada-bil', 'viltolycka-forsakring']),
    ('Regler och avgifter', ['trafikforsakringsavgift', 'avstalld-bil', 'saga-upp-bilforsakring',
                             'kopa-bil-forsakring', 'bonus-och-skadefria-ar', 'korstracka-mil-per-ar',
                             'bilforsakring-utomlands']),
    ('Förare och bil', ['bilforsakring-ung-forare', 'bilforsakring-18-ar', 'bilforsakring-utan-bonus',
                        'bilforsakring-pensionar', 'bilforsakring-elbil', 'leasingbil-forsakring']),
    ('Bolag och bilmärken', ['forsakringsbolag', 'bilmarken']),
    ('Om sajten', ['om-oss', 'redaktionell-metod']),
]
_per = {d['slug']: d for d in PAGES}
rader = ['# Bilförsäkringspriser.se', '',
         '> Oberoende svensk guide till bilförsäkring: vad trafik-, halv- och helförsäkring '
         'täcker, vad som påverkar priset, regler för trafikförsäkringsavgift, avställning och '
         'ägarbyte, samt genomgångar av 16 försäkringsbolag och drygt 120 bilmodeller. Siffror '
         'redovisas med källa och datum. Sajten förmedlar inga försäkringar och innehåller '
         'annonslänkar, vilket redovisas på /redaktionell-metod/.', '',
         f'Senast uppdaterad: {max(d["_mod"] for d in PAGES)}. Ansvarig utgivare: Emil Rostgaard Clausen ({KONTAKT}).', '']
for rubrik, slugs in _grupper:
    rader.append(f'## {rubrik}')
    for sl in slugs:
        if sl in _per:
            d = _per[sl]
            rader.append(f'- [{d["h1"]}]({BASE}/{sl + "/" if sl else ""}): {d["desc"]}')
    rader.append('')
rader += ['## Valfritt', f'- [Sitemap med alla sidor]({BASE}/sitemap.xml)', '']
open('llms.txt', 'w', encoding='utf-8').write('\n'.join(rader))
print('llms.txt och 404.html skrivna')
