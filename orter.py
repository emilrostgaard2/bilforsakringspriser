# -*- coding: utf-8 -*-
"""Ortssidor — Stockholm, Göteborg och Malmö.

UNIKHET
Varje ort har egen ingress, egna H2-rubriker, egen sektionsordning och
egna stadsdelsavsnitt. Ingen text återanvänds mellan orterna. Det är
avgörande här: ortssidor är den sidtyp som lättast blir mallutfyllnad
och som Google är hårdast mot när den blir det.

Premieindex hämtas från data.ORTER och visas som "—" tills det är
insamlat. Vi påstår alltså aldrig en procentsiffra vi inte har.
"""
import data

SWIPE = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>'


def _t(caption, kol, rader, swipe=False):
    th = ''.join(f'<th scope="col">{k}</th>' for k in kol)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    return (f'<div class="tbl"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead>'
            f'<tbody>{tr}</tbody></table></div>{SWIPE if swipe else ""}')


def _pristabell(ort):
    o = data.ORTER[ort]
    return _t(f'{o["namn"]} — vägledande årspremie',
              ['Nivå', 'Per år', 'Per månad', 'Index mot riket'],
              [['<a href="/trafikforsakring/">Trafikförsäkring</a>', '—', '—',
                data.betyg(o['index'])],
               ['<a href="/halvforsakring/">Halvförsäkring</a>', '—', '—',
                data.betyg(o['index'])],
               ['<a href="/helforsakring/">Helförsäkring</a>', '—', '—',
                data.betyg(o['index'])]], swipe=True)


SIDOR = [

# ═══ STOCKHOLM ═════════════════════════════════════════════════════
{
 'slug': 'bilforsakring-stockholm', 'key': True,
 'title': 'Bilförsäkring Stockholm — pris, postnummer och parkeringsskador',
 'desc': 'Varför är bilförsäkring dyrare i Stockholm? Se hur postnumret påverkar '
         'premien, vilka skadetyper som dominerar och vad du kan göra åt det.',
 'eyebrow': 'Stockholms län',
 'h1': 'Bilförsäkring i Stockholm',
 'lead': 'Stockholm är det dyraste området i landet att försäkra en bil i, och orsaken är '
         'inte att stockholmare kör sämre. Det är trafiktätheten, gatuparkeringen och '
         'stöldstatistiken som räknas in — tre faktorer som alla följer av att många bilar '
         'trängs på liten yta.',
 'checks': ['Postnumret väger tyngre här än någon annanstans i landet',
            'Parkeringsskador utan känd motpart är den vanligaste skadan',
            'Garageplats kan sänka premien märkbart'],
 'card_t': 'Se vad din bil kostar i Stockholm',
 'sticky': 'Jämför bilförsäkring i Stockholm',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Bor du i Stockholm är de två saker som
faktiskt går att påverka var bilen står nattetid och hur långt du kör. Båda ska stämma med
verkligheten i försäkringsbrevet — och hos många gör de inte det.</p></div>

<h2>Prisbilden i Stockholm</h2>
{_pristabell('stockholm')}
{data.saknas_ruta('ortsindex och priser')}
{data.profil_ruta()}

<h2>Varför postnumret väger så tungt här</h2>
<p>Försäkringsbolagen sätter premien på postnummernivå, inte på kommunnivå. Skillnaden mellan
två adresser inom samma stad kan vara större än skillnaden mellan två landsändar. Det som
skiljer är skadefrekvensen i just det området: hur ofta bilar blir påkörda vid parkering, hur
ofta de blir stulna eller uppbrutna, och hur mycket trafik som passerar.</p>

<h2>Skadetyperna som dominerar i innerstaden</h2>
{_t('Vanliga skador i tät stadsmiljö',
    ['Skadetyp', 'Varför den är vanlig här', 'Vilken nivå som täcker'],
    [['Parkeringsskada utan känd motpart', 'Trång gatuparkering, hög omsättning på platser',
      'Endast helförsäkring'],
     ['Skadegörelse', 'Bilar står oskyddade på gatan nattetid', 'Endast helförsäkring'],
     ['Stöld ur bilen', 'Många bilar per kvarter gör urvalet stort', 'Halv och hel'],
     ['Glasskada', 'Mycket trafik ger fler stenskott', 'Halv och hel'],
     ['Backningsolyckor', 'Trånga garage och snäva infarter', 'Endast helförsäkring']],
    swipe=True)}
<p>Notera mönstret: tre av fem regleras på vagnskadedelen, som bara finns i
<a href="/helforsakring/">helförsäkring</a>. Det är därför halvförsäkring är en sämre affär i
innerstan än på landsbygden, även på en äldre bil.</p>

<h2>Det som faktiskt går att göra</h2>
<p>Har du tillgång till garage eller parkeringshus ska det anges — det är en av få uppgifter
som sänker premien direkt. Kör du bara till sommarstället och tillbaka är körsträckan
troligen lägre än vad som står i avtalet. Och pendlar du med kollektivtrafik och använder
bilen på helgerna hamnar du i ett lägre körsträckeintervall än standardvalet.</p>
<p>Bilmärket spelar också in i storstad på ett sätt det inte gör på landet: modeller som är
överrepresenterade i stöldstatistiken prissätts hårdare här. Se vad som gäller för
<a href="/bilmarken/mercedes/">Mercedes</a>, <a href="/bilmarken/bmw/">BMW</a> och
<a href="/bilmarken/land-rover/">Land Rover</a>, som alla har den profilen.</p>
{data.kontrollerad()}

<div class="cta"><h2>Se ditt Stockholmspris</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om bilförsäkring i Stockholm',
 'faq': [
   ('Varför är bilförsäkring dyrare i Stockholm?',
    'För att skadefrekvensen är högre. Fler bilar på mindre yta ger fler parkeringsskador, '
    'mer skadegörelse och fler stölder, och premien speglar den lokala statistiken på '
    'postnummernivå.'),
   ('Kan jag använda en adress utanför stan för att få lägre pris?',
    'Nej. Premien ska beräknas på den adress där bilen normalt står. Uppger du fel adress '
    'kan ersättningen sättas ned eller nekas vid en skada.'),
   ('Lönar sig garageplats i Stockholm?',
    'Ofta ja, både i premie och i praktiken. Garage eller parkeringshus minskar risken för '
    'skadegörelse och parkeringsskador, vilket är de två vanligaste skadorna i innerstaden.'),
   ('Behöver jag helförsäkring i innerstan?',
    'Överväg det även på en äldre bil. Parkeringsskador utan känd motpart och skadegörelse '
    'regleras båda på vagnskadedelen, som bara finns i helförsäkringen.'),
   ('Påverkar trängselskatt försäkringen?',
    'Nej, trängselskatten är en avgift till staten och har ingen koppling till premien. '
    'Däremot påverkar din faktiska körsträcka priset.'),
 ],
 'rel': [('/helforsakring/', 'Helförsäkring — vad ingår?'),
         ('/bilforsakring-goteborg/', 'Bilförsäkring i Göteborg'),
         ('/bilforsakring-malmo/', 'Bilförsäkring i Malmö'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/sjalvrisk/', 'Självrisk förklarad')],
},

# ═══ GÖTEBORG ══════════════════════════════════════════════════════
{
 'slug': 'bilforsakring-goteborg', 'key': True,
 'title': 'Bilförsäkring Göteborg — vad premien styrs av i Västsverige',
 'desc': 'Bilförsäkring i Göteborg: se vad som skiljer premien mot riket, hur '
         'stadsdelen påverkar priset och vilka skador som är vanligast i regionen.',
 'eyebrow': 'Västra Götaland',
 'h1': 'Bilförsäkring i Göteborg',
 'lead': 'Göteborg ligger mellan storstadstaxan och riksgenomsnittet. Staden är mer utspridd '
         'än Stockholm, andelen boende med egen parkering är högre, och det syns i premien — '
         'men skillnaden mellan centrala Göteborg och kranskommunerna är samtidigt stor.',
 'checks': ['Stor spridning mellan centrala lägen och kranskommuner',
            'Högre andel egen parkering än i Stockholms innerstad',
            'Kustklimatet ger andra skadetyper än i inlandet'],
 'card_t': 'Se vad din bil kostar i Göteborg',
 'sticky': 'Jämför bilförsäkring i Göteborg',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Spridningen inom Göteborgsområdet är större
än skillnaden mot riksgenomsnittet. Bor du i en kranskommun med egen uppfart betalar du
sannolikt mindre än en granne några kilometer bort som gatuparkerar.</p></div>

<h2>Vad det kostar i Göteborg</h2>
{_pristabell('goteborg')}
{data.saknas_ruta('ortsindex och priser')}
{data.profil_ruta()}

<h2>Skillnaden mellan centrum och kranskommun</h2>
<p>Premien beräknas på postnummer, och Göteborgsregionen rymmer båda ytterligheterna. I de
centrala stadsdelarna gäller samma logik som i alla täta stadsmiljöer: gatuparkering,
skadegörelse och påkörning vid parkering. I Mölndal, Partille, Kungsbacka och Härryda ser
bilden annorlunda ut, med högre andel villaparkering och lägre skadefrekvens.</p>
{_t('Vad som skiljer mellan lägena',
    ['Faktor', 'Centrala Göteborg', 'Kranskommun'],
    [['Vanligaste parkering', 'Gata eller gemensamt garage', 'Egen uppfart eller carport'],
     ['Dominerande skadetyp', 'Parkeringsskada och skadegörelse', 'Kollision i trafik'],
     ['Körsträcka per år', 'Ofta låg', 'Ofta högre — pendling'],
     ['Vikten av vagnskada', 'Hög', 'Måttlig'],
     ['Effekt av garageplats', 'Stor', 'Mindre — redan normen']],
    swipe=True)}

<h2>Klimatet som premiefaktor</h2>
<p>Västkusten har fler nederbördsdagar än inlandet, och våt vägbana är en faktor i
kollisionsstatistiken. Saltet och fukten påverkar också korrosion, men det är en
garantifråga snarare än en försäkringsfråga — rost räknas som slitage och ersätts inte av
någon nivå. Däremot är räddnings- och assistansmomentet mer värt här än många tror, eftersom
en stor del av regionen ligger utanför tät bebyggelse.</p>

<h2>Det som sänker premien i Göteborg</h2>
<p>Samma tre saker som överallt, men i den här ordningen lokalt: rätt angiven körsträcka,
rätt uppgift om var bilen står nattetid, och rätt skyddsnivå för bilens ålder. Gäller det en
äldre bil på egen uppfart i en kranskommun är <a href="/halvforsakring/">halvförsäkring</a>
ofta rätt — samma bil i Majorna talar för <a href="/helforsakring/">helförsäkring</a>.</p>
{data.kontrollerad()}

<div class="cta"><h2>Se ditt Göteborgspris</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om bilförsäkring i Göteborg',
 'faq': [
   ('Är bilförsäkring dyrare i Göteborg än i resten av landet?',
    'Något dyrare i de centrala delarna, medan kranskommunerna ofta ligger nära eller under '
    'riksgenomsnittet. Spridningen inom regionen är större än skillnaden mot riket.'),
   ('Spelar det roll vilken stadsdel jag bor i?',
    'Ja. Premien beräknas på postnummer, och skillnaden mellan en central stadsdel och en '
    'kranskommun kan vara betydande för exakt samma bil och förare.'),
   ('Behöver jag helförsäkring i Göteborg?',
    'Det beror mer på var bilen står än på att den står i Göteborg. Gatuparkering i centrala '
    'lägen talar för helförsäkring, egen uppfart i kranskommun gör halvförsäkring rimligare '
    'på en äldre bil.'),
   ('Påverkar vädret på västkusten premien?',
    'Indirekt. Fler nederbördsdagar syns i kollisionsstatistiken. Rostskador ersätts däremot '
    'inte alls, eftersom de räknas som slitage.'),
   ('Vad händer med premien om jag flyttar inom regionen?',
    'Den kan ändras, eftersom adressen är en av de tyngre faktorerna. Meddela bolaget vid '
    'flytt — det är dessutom ett tillfälle då du får byta bolag.'),
 ],
 'rel': [('/bilforsakring-stockholm/', 'Bilförsäkring i Stockholm'),
         ('/bilforsakring-malmo/', 'Bilförsäkring i Malmö'),
         ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/basta-bilforsakringen/', 'Bästa bilförsäkringen')],
},

# ═══ MALMÖ ═════════════════════════════════════════════════════════
{
 'slug': 'bilforsakring-malmo', 'key': True,
 'title': 'Bilförsäkring Malmö — pris, stöldrisk och skånska förutsättningar',
 'desc': 'Bilförsäkring i Malmö: se hur postnumret påverkar premien, varför '
         'stöldskyddet väger tungt i Skåne och vad som gäller vid körning till Danmark.',
 'eyebrow': 'Skåne',
 'h1': 'Bilförsäkring i Malmö',
 'lead': 'Malmö är en av de dyrare orterna att försäkra bil i, och stöldmomentet är det som '
         'skiljer mest. Skåne har dessutom en förutsättning ingen annan del av landet har: '
         'många kör regelbundet över Öresund, vilket ställer egna krav på villkoren.',
 'checks': ['Stöldskyddet väger tyngre här än i övriga landet',
            'Postnummernivån ger stora skillnader inom staden',
            'Körning utomlands kräver egen kontroll av villkoren'],
 'card_t': 'Se vad din bil kostar i Malmö',
 'sticky': 'Jämför bilförsäkring i Malmö',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> I Malmö är två saker värda extra
uppmärksamhet: vad bolaget kräver i stöldskydd, och vad som gäller när bilen körs utanför
Sverige. Båda står i villkoren, ingen av dem syns i priset.</p></div>

<h2>Prisbilden i Malmö</h2>
{_pristabell('malmo')}
{data.saknas_ruta('ortsindex och priser')}
{data.profil_ruta()}

<h2>Stöldskyddet — den lokala skillnaden</h2>
<p>Flera bolag ställer skarpare krav på stöldskydd i vissa postnummerområden, och de kraven
är villkor för att ersättning ska betalas ut. Det kan handla om godkänt larm, spårsändare
eller att bilen ska stå inlåst nattetid. Uppfylls kravet inte den natt bilen försvinner kan
ersättningen sättas ned — även om premien betalats.</p>
{_t('Kontrollera detta i villkoren',
    ['Fråga', 'Varför den är viktig i Malmö'],
    [['Krävs godkänt stöldskydd på min modell?', 'Kravet varierar med modell och postnummer'],
     ['Krävs spårsändare?', 'Vanligt på eftertraktade SUV-modeller'],
     ['Gäller kravet nattetid eller dygnet runt?', 'Avgör var bilen får stå'],
     ['Vad är stöldsjälvrisken?', 'Skiljer sig mer mellan bolagen än övriga självrisker'],
     ['Täcks stöld ur bilen?', 'Lösöre i bilen kan höra till hemförsäkringen']],
    swipe=False)}

<h2>Att köra över Öresund</h2>
<p>Svensk bilförsäkring gäller normalt i hela EU och EES, vilket täcker resor till Danmark
och vidare ned i Europa. Två saker är ändå värda att kontrollera innan en regelbunden
pendling: hur assistansmomentet fungerar utomlands, och om hyrbil ingår när bilen står på
verkstad i ett annat land. Det är där skillnaderna mellan bolagen är som störst, och det
märks först den dag något går fel.</p>

<h2>Skyddsnivå och stadsdel</h2>
<p>Som i alla större städer beräknas premien per postnummer, och skillnaden mellan
stadsdelarna kan vara betydande. Där gatuparkering är normen dominerar samma skadetyper som
i övriga storstäder — parkeringsskada och skadegörelse, båda på vagnskadedelen. Det gör
<a href="/helforsakring/">helförsäkring</a> mer motiverad än bilens ålder ensam skulle
antyda, och gör det värt att läsa <a href="/sjalvrisk/">självriskvillkoren</a> noga.</p>
{data.kontrollerad()}

<div class="cta"><h2>Se ditt Malmöpris</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om bilförsäkring i Malmö',
 'faq': [
   ('Är bilförsäkring dyr i Malmö?',
    'Malmö ligger bland de dyrare orterna, och det är framför allt stöldmomentet som skiljer '
    'mot mindre orter. Skillnaden mellan olika postnummer inom staden är samtidigt stor.'),
   ('Gäller min svenska bilförsäkring i Danmark?',
    'Ja, svensk bilförsäkring gäller normalt i hela EU och EES. Kontrollera däremot hur '
    'assistans och hyrbil fungerar utomlands — där skiljer sig bolagen åt.'),
   ('Måste jag ha spårsändare i bilen?',
    'Vissa bolag kräver det för särskilt stöldutsatta modeller, ibland kopplat till '
    'postnummer. Kravet står i villkoren och är en förutsättning för ersättning, inte ett råd.'),
   ('Vad händer om stöldskyddskravet inte var uppfyllt?',
    'Ersättningen kan sättas ned eller nekas helt. Det är därför kraven ska läsas innan du '
    'tecknar, inte efter att bilen försvunnit.'),
   ('Täcks saker som stjäls ur bilen?',
    'Delvis. Fast monterad utrustning hör till bilförsäkringen, medan lösa ägodelar ofta hör '
    'till hemförsäkringen. Kontrollera båda villkoren.'),
 ],
 'rel': [('/bilforsakring-stockholm/', 'Bilförsäkring i Stockholm'),
         ('/bilforsakring-goteborg/', 'Bilförsäkring i Göteborg'),
         ('/sjalvrisk/', 'Självrisk förklarad'),
         ('/helforsakring/', 'Helförsäkring — vad ingår?'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen')],
},
]
