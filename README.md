# Bilförsäkringspriser.se

Statisk sajt. Ingen WordPress, ingen databas, inga tredjepartsanrop. HTML genereras
av `build.py` och rullas ut till Simply via GitHub Actions.

---

## Innan du sätter igång — fyra saker som måste göras

| # | Vad | Var |
|---|-----|-----|
| 1 | Byt ut affiliatelänken | `assets/v2.js`, konstanten `AFF_BASE` |
| 2 | Ersätt platshållarpriserna | `pages.py`, sök på `TODO` |
| 3 | Fyll i juridiskt namn, organisationsnummer och adress | `pages.py`, sidan `integritetspolicy` |
| 4 | Installera en cookiebanner | Se avsnittet längst ned |

Sajten kan driftsättas utan dessa, men den ska inte marknadsföras förrän de är gjorda.

---

## Så fungerar bygget

```
pages.py    ← allt innehåll bor här. Redigera den här filen.
build.py    ← mallen: header, hero, footer, schema, sitemap
```

Kör lokalt:

```bash
python3 build.py
```

Alla `index.html` och `sitemap.xml` skrivs om från grunden.
**Redigera aldrig de färdiga HTML-filerna** — de skrivs över vid nästa bygge.

Förhandsgranska:

```bash
python3 -m http.server 8000
# öppna http://localhost:8000
```

---

## GitHub → Simply

### 1. Skapa repot

```bash
cd /sökväg/till/bilforsakringspriser
git init
git add .
git commit -m "Första versionen"
git branch -M main
git remote add origin git@github.com:DITTNAMN/bilforsakringspriser.git
git push -u origin main
```

### 2. Hämta FTP-uppgifterna hos Simply

Kontrollpanelen → domänen → **File Manager** → **Logginformation**.

### 3. Lägg in dem som secrets på GitHub

Repot → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.

| Namn | Värde |
|------|-------|
| `FTP_SERVER` | `ftp.simply.com` |
| `FTP_USERNAME` | `bilforsakringspriser.se` |
| `FTP_PASSWORD` | lösenordet från Simply |

Målmappen är hårdkodad till `public_html/` i workflowet.

### 4. Kör deployen

Varje push till `main` rullar ut automatiskt. Du kan också starta den manuellt under
fliken **Actions** → **Deploy till Simply** → **Run workflow**.

> Workflowet kör `mirror --only-newer --continue` — det laddar upp nya och ändrade filer
> men **raderar ingenting** på servern. Byter du namn på en sida ligger den gamla kvar
> tills du tar bort den manuellt via FTP.
>
> `build.py`, `pages.py`, `*.md` och `bilder/` laddas aldrig upp. Källkoden stannar i
> repot och manuellt uppladdade bilder överlever varje deploy.

---

## Efter första driftsättningen

**Verifiera cachningen.** Simply honorerar inte alltid `mod_headers`:

```bash
curl -sI https://bilforsakringspriser.se/assets/v2.css | grep -i cache-control
```

Står det inte `max-age=31536000` — kontakta Simplys support och fråga om `mod_headers`
är aktiverat på ditt paket.

**Kontrollera omdirigeringarna.** Både `http://`, `www.` och adresser utan avslutande
snedstreck ska landa på den kanoniska adressen.

**Lägg till sajten i Google Search Console** och skicka in `sitemap.xml`.

---

## Att fylla i innan lansering

### Affiliatelänken

I `assets/v2.js`:

```js
var AFF_BASE = 'https://www.example-partner.se/jamfor';
```

`utm_content` sätts automatiskt utifrån sidans sökväg, så att det går att se vilken sida
som konverterar. Fråga partnern vilket fält de vidarebefordrar — vissa nätverk använder
`subid` i stället för `utm_content`, och då ska parameternamnet ändras.

### Priserna

Alla belopp i `pages.py` är markerade med konstanten `TODO` och visas som en gul ruta på
sidan. Ersätt dem med egna insamlade siffror. Använd samma jämförelseprofil överallt,
annars går tabellerna inte att jämföra:

> 40 år · 6 skadefria år · 1 500 mil/år · ort utanför storstad · 4 000 kr självrisk

**Källor att samla in från**

| Källa | Vad du får |
|-------|-----------|
| Konsumenternas Försäkringsbyrå | Oberoende betyg 1–5 på villkoren. Säljer ingenting |
| Bolagens egna prislistor | Priser du får citera med källhänvisning |
| Finansinspektionen | Register över tillståndspliktiga bolag |
| Trafikförsäkringsföreningen | Trafikförsäkringsavgiften |

Använd aldrig en konkurrerande jämförelsesajt som källa.

### Cookiebanner

Statistik- och marknadsföringscookies kräver samtycke innan de sätts. Välj en lösning som
blockerar tills samtycke lämnats, och länka den till `/cookiepolicy/`.

---

## Lägga till en sida

Lägg ett nytt objekt i listan `PAGES` i `pages.py`:

```python
{
 'slug': 'mitt-nya-amne',
 'key': True,                     # True ger högre prioritet i sitemap
 'title': 'Rubrik i sökresultatet — max 60 tecken',
 'desc':  'Beskrivning, 120–160 tecken.',
 'eyebrow': 'Guide',
 'h1': 'Rubrik på sidan',
 'lead': 'Ingress under rubriken.',
 'checks': ['Punkt ett', 'Punkt två', 'Punkt tre'],
 'sticky': 'Text i den klibbiga raden',
 'body': '''<section class="sec"><div class="wrap narrow">
   <h2>Rubrik</h2><p>Text.</p>
   <div class="cta"><h2>Se ditt pris</h2><div class="cta-inner">{PLATE}</div></div>
 </div></section>''',
 'faq': [('Fråga?', 'Svar.')],
 'rel': [('/', 'Vad kostar bilförsäkring?')],
},
```

`{PLATE}` byts automatiskt mot ett registreringsnummerfält med knapp.
`faq` genererar både synliga frågor och `FAQPage`-schema — lägg aldrig in schema för
frågor som inte syns på sidan.

Kör `python3 build.py`, committa och pusha.

---

## Byggblock som finns

| Klass | Vad det ger |
|-------|-------------|
| `.note` | Blå faktaruta |
| `.warn` | Gul varningsruta |
| `.src` | Grå källruta |
| `.tbl` + `<table>` | Tabell med vågrät scroll på mobil |
| `.stats` + `.stat` | Nyckeltal i rad |
| `.grid` + `.gc` | Kortlänkar till andra guider |
| `.split` | Två kolumner, för- och nackdelar |
| `.cards` + `.co` | Bolagskort med logotyp och pris |
| `.cta` | Uppmaningsblock med registreringsnummerfält |

---

## Prestanda

- Typsnitten är självhostade och subsatta till latin plus å, ä och ö. Inga anrop till
  Google Fonts.
- `v2.css` är cirka 4,6 KB gzippat, `v2.js` under 2 KB.
- Alla resurser versioneras med `?v=` i `build.py`. **Höj `V` när du ändrat css eller js**,
  annars ser återkommande besökare den gamla versionen i upp till ett år.
- Ingen JavaScript krävs för att läsa sajten. Registreringsnummerfältet är progressive
  enhancement.

---

## Checklista före lansering

- [ ] Affiliatelänken utbytt i `v2.js`
- [ ] Alla `TODO`-rutor borta ur `pages.py`
- [ ] Juridiskt namn, organisationsnummer och adress i integritetspolicyn
- [ ] Cookiebanner installerad och kopplad till `/cookiepolicy/`
- [ ] E-post `info@bilforsakringspriser.se` fungerar
- [ ] `curl -sI` visar `max-age=31536000` på `/assets/v2.css`
- [ ] Sajten tillagd i Google Search Console, `sitemap.xml` inskickad
- [ ] Kontrollerat i mobilvy att menyn och den klibbiga raden fungerar
