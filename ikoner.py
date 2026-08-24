#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genererar samtliga ikoner ur logotypen i menyraden.

VARFÖR
Logotypen fanns tidigare på två ställen: som LOGO_SVG i build.py och som
en handskriven kopia i assets/favicon.svg. Två kopior driver isär förr
eller senare. Nu är LOGO_SVG enda källa — allt annat genereras.

KÖR EFTER VARJE ÄNDRING AV LOGOTYPEN
    python3 ikoner.py

SKRIVER
    assets/favicon.svg          skalbar, används av moderna webbläsare
    assets/favicon-32.png       fallback
    assets/apple-touch-icon.png 180 px, iOS hemskärm
    assets/icon-192.png         PWA och Android
    assets/icon-512.png         PWA, och og:image för sidor utan egen bild
    favicon.ico                 16+32+48 px, äldre webbläsare och Google
"""
import io
import os
import re

import cairosvg
from PIL import Image

ROT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROT)

# Hämta logotypen direkt ur build.py — ingen andra kopia.
kalla = open('build.py', encoding='utf-8').read()
m = re.search(r"LOGO_SVG = \((.*?)\)\n\n", kalla, re.S)
if not m:
    raise SystemExit('Hittade inte LOGO_SVG i build.py')
bitar = re.findall(r"'([^']*)'", m.group(1))
inre = ''.join(bitar).replace('viewBox="0 0 64 64" aria-hidden="true"', '')

# inre innehåller '<svg viewBox=... >…</svg>' — plocka ut allt mellan taggarna
inre = re.sub(r'^\s*<svg[^>]*>', '', inre)
inre = re.sub(r'</svg>\s*$', '', inre).strip()

SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" '
       'height="64" role="img" aria-label="Bilförsäkringspriser.se">'
       + inre + '</svg>')

open('assets/favicon.svg', 'w', encoding='utf-8').write(SVG + '\n')


def png(storlek, mal):
    data = cairosvg.svg2png(bytestring=SVG.encode('utf-8'),
                            output_width=storlek, output_height=storlek)
    open(mal, 'wb').write(data)
    return Image.open(io.BytesIO(data))


png(32, 'assets/favicon-32.png')
png(180, 'assets/apple-touch-icon.png')
png(192, 'assets/icon-192.png')
png(512, 'assets/icon-512.png')

bild = png(256, '/tmp/ico-kalla.png')
bild.save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])

for f in ('assets/favicon.svg', 'assets/favicon-32.png', 'assets/apple-touch-icon.png',
          'assets/icon-192.png', 'assets/icon-512.png', 'favicon.ico'):
    print(f'{f:32s} {os.path.getsize(f):>7,} B'.replace(',', ' '))
print('\nAlla ikoner genererade ur LOGO_SVG i build.py.')
