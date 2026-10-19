# -*- coding: utf-8 -*-
"""Publicerings- och uppdateringsdatum per sida.

VARFÖR
Tidigare hade alla 199 sidor samma datePublished (2026-01-01) och samma
dateModified. Det är ett falskt påstående, och Google lär sig snabbt att
ignorera datum som aldrig skiljer sig åt — samma sak för lastmod i
sitemap.xml.

HUR
datum.json sparar för varje sida: när den först publicerades, när den
senast ändrades och ett fingeravtryck av innehållet. Vid varje bygge
jämförs fingeravtrycket. Har innehållet ändrats sätts dagens datum som
uppdateringsdatum — annars behålls det gamla. Datumet ändras alltså bara
när texten faktiskt gör det.

Kör bygget lokalt och checka in datum.json, så att samma datum gäller
när GitHub Actions bygger om sajten.
"""
import json, os, hashlib, datetime

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datum.json')
IDAG = datetime.date.today().isoformat()

try:
    _DB = json.load(open(FIL, encoding='utf-8'))
except (OSError, ValueError):
    _DB = {}
_ANDRAD = False


def _hash(d):
    # Bara det läsaren ser som innehåll. Mall, meny och sidfot räknas inte,
    # annars skulle en ny menypost "uppdatera" alla sidor på en gång.
    delar = [d.get('title', ''), d.get('desc', ''), d.get('h1', ''), d.get('lead', ''),
             d.get('body', ''), repr(d.get('faq', ''))]
    return hashlib.sha1('\x1f'.join(delar).encode('utf-8')).hexdigest()[:16]


def satt(d):
    """Lägger _pub och _mod på siddicten."""
    global _ANDRAD
    slug = d['slug']
    h = _hash(d)
    rad = _DB.get(slug)
    if rad is None:
        rad = {'pub': d.get('publicerad', IDAG), 'mod': IDAG, 'hash': h}
        _DB[slug] = rad
        _ANDRAD = True
    elif rad['hash'] != h:
        rad['mod'] = IDAG
        rad['hash'] = h
        _ANDRAD = True
    d['_pub'], d['_mod'] = rad['pub'], rad['mod']
    return d


def spara():
    if _ANDRAD:
        with open(FIL, 'w', encoding='utf-8') as f:
            json.dump(dict(sorted(_DB.items())), f, ensure_ascii=False, indent=1)
            f.write('\n')
