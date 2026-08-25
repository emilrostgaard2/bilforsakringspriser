# -*- coding: utf-8 -*-
"""Genererar bolagssidor och märkessidor.

UNIKHET
Varje sida får egen sektionsordning, egna H2-rubriker och en egen ingress som
bygger på något faktiskt utmärkande för bolaget eller märket. Gemensamma
avsnitt finns i flera varianter som fördelas så att grannsidor aldrig delar
formulering. Målet är att inga två sidor delar skelett.
"""
import re, os
from companies import BOLAG
from brands import MARKEN, BILD
import jamforelse

TODO = ('<div class="warn"><strong>PLATSHÅLLARE — ersätts före lansering.</strong> '
        'Beloppen är exempelsiffror, inte insamlade marknadspriser.</div>')

PROFIL = ('<div class="src"><p><strong>Jämförelseprofil.</strong> 40 år, 1 500 mil per år, '
          'ort utanför storstad, sex skadefria år och 4 000 kr i självrisk. '
          '<a href="/redaktionell-metod/">Så räknar vi</a>.</p></div>')

# ── Varianter av återkommande text ──────────────────────────────────
BYTA = [
 ('Så här går uppsägningen till',
  'Skriftligt, en månad före huvudförfallodagen. Datumet står på försäkringsbrevet och är '
  'sällan detsamma som när du tecknade — kontrollera det innan du sätter en påminnelse.'),
 ('Undantagen från uppsägningstiden',
  'Köper du bil, flyttar eller får en premiehöjning aviserad får du byta omgående. Det sista '
  'är den möjlighet flest missar, och det är samtidigt den bästa förhandlingssituationen.'),
 ('Låt inte dagarna glappa',
  'Nya försäkringen ska starta samma dygn som den gamla upphör. Utan trafikförsäkring '
  'debiterar Trafikförsäkringsföreningen en avgift som är satt högre än premien.'),
 ('Bonusintyget avgör ditt första år',
  'Skadefri tid är din, inte bolagets. Utan intyg hamnar du i sämsta klassen och betalar '
  'onödigt mycket det första året.'),
 ('Uppsägning vid huvudförfallodagen',
  'Huvudregeln är en månads skriftlig uppsägning till förfallodagen. Datumet står på ditt '
  'försäkringsbrev — det är sällan detsamma som när du tecknade.'),
 ('När du får byta direkt',
  'Vid bilköp, flytt och när bolaget aviserar en premiehöjning får du byta omgående, oavsett '
  'vad som annars gäller. Premiehöjningen är den de flesta missar.'),
 ('Teckna nytt innan du säger upp',
  'Den nya försäkringen ska gälla från samma dag som den gamla upphör. Ett dygn utan '
  'trafikförsäkring är olagligt och kostar mer i avgift än du sparat.'),
 ('Se till att dina skadefria år följer med',
  'Skadefri tid tillhör dig, inte bolaget. Begär intyg vid uppsägningen och kontrollera på '
  'första fakturan att åren registrerats — annars börjar du om från noll.'),
]

SKADA = [
 [('Säkra platsen', 'Vid personskada ringer du 112. I annat fall varningstriangel och '
   'fotografering av båda bilarna innan något flyttas.'),
  ('Fyll i skadeanmälan på plats', 'Motpartens namn, registreringsnummer och bolag. En '
   'blankett undertecknad av båda avgör så gott som alltid en senare tvist om vållande.'),
  ('Anmäl inom några dagar', 'Sen anmälan är en av de vanligaste orsakerna till att '
   'ersättning sätts ned. Anmäl digitalt — det ger tidsstämplad kvittens.'),
  ('Räkna på självrisk och premiepåslag', 'Är skadan mindre än självrisken plus '
   'premiehöjningen över tre år är det billigare att betala själv.')],
 [('De första trettio minuterna', 'Det är där ärendet vinns eller förloras. Fotografera från '
   'flera vinklar, notera tid och väglag och ta kontaktuppgifter på vittnen.'),
  ('Dokumentationen är ditt ansvar', 'Det är du som ska göra sannolikt vad som hänt. Bilder '
   'och blankett väger tyngre än din egen redogörelse.'),
  ('Anmälan och handläggning', 'De flesta ärenden avgörs inom en till tre veckor. Tvist om '
   'vållande drar ut på tiden, särskilt när motpartens bolag är inblandat.'),
  ('Följden för premien', 'Skada där du är vållande kostar normalt bonussteg och höjer '
   'premien i flera år. Skada utan eget vållande gör det som regel inte.')],
 [('Larma och säkra', 'Personskada eller misstanke om skadegörelse innebär kontakt med '
   'polis och ett diarienummer — ofta ett villkor för ersättning.'),
  ('Bevis som håller', 'Foton från fyra vinklar, närbild på skadan, bild på båda '
   'registreringsskyltarna och på omgivningen. Två minuter som avgör ärendet.'),
  ('Anmäl med allt bifogat', 'Skicka bilder, blankett och eventuellt diarienummer i samma '
   'anmälan. Ärenden som behöver kompletteras tar betydligt längre tid.'),
  ('Verkstad och hyrbil', 'Fråga om fritt verkstadsval och om hyrbil ingår redan vid '
   'anmälan. Det är då du har mest att säga till om.')],
 [('Stanna och säkra platsen', 'Varningstriangel först, dokumentation sedan. Ordningen '
   'spelar roll både för säkerheten och för trovärdigheten i ärendet.'),
  ('Blanketten är starkare än minnet', 'Den gemensamma skadeanmälan undertecknad av båda '
   'parter avgör ärendet när uppgifterna går isär två veckor senare.'),
  ('Anmäl utan dröjsmål', 'Villkoren kräver anmälan så snart det är möjligt. En anmälan som '
   'kommer flera veckor senare utan god anledning kan kosta dig en del av ersättningen.'),
  ('Fråga om ersättningsbil direkt', 'Är bilen hushållets enda märks ett verkstadsbesök '
   'omgående. Kontrollera antal dagar och om du får bil eller pengar.')],
 [('Ring 112 vid personskada', 'Annars markera platsen och fotografera båda fordonen och '
   'deras placering på vägen innan något flyttas.'),
  ('Notera vittnen innan de kör vidare', 'Namn och telefonnummer. I ärenden där vållandet '
   'bestrids är det ofta vittnesuppgifterna som fäller avgörandet.'),
  ('Digital anmälan går snabbast', 'Bifoga bilder direkt. Enklare skador kan då avgöras på '
   'några dagar i stället för på flera veckor.'),
  ('Väg ersättningen mot bonusförlusten', 'Begär en beräkning av premiepåslaget innan du '
   'anmäler en skada under ungefär 10 000 kronor.')],
]

BETYG_UTAN = [
 'Bolaget saknar värde i Svenskt Kvalitetsindex branschmätning, vilket normalt beror på att '
 'marknadsandelen ännu inte är tillräcklig för statistisk tillförlitlighet. Det säger '
 'ingenting om kvaliteten — bara att underlaget är för tunt.',
 'Det finns ingen SKI-siffra att luta sig mot här. Mätningen kräver en viss marknadsandel för '
 'att bli statistiskt hållbar, och nyare aktörer hamnar därför utanför tills de vuxit.',
 'Oberoende kundnöjdhetsdata saknas för bolaget. Läs villkoren i stället — de går att '
 'jämföra oavsett hur många kunder bolaget har.',
]


def _sec(inner):
    return f'<section class="sec"><div class="wrap narrow">{inner}</div></section>\n'


def _sec_alt(inner):
    return f'<section class="sec alt"><div class="wrap narrow">{inner}</div></section>\n'


# ═══ BOLAGSSIDOR ════════════════════════════════════════════════════
def bolagssidor():
    sidor = []
    for i, b in enumerate(BOLAG):
        H = b['h2']
        fakta = ''.join(
            f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in b['fakta'])

        betyg_rader = []
        if b['ski']:
            betyg_rader.append(
                f'<tr><th scope="row">Svenskt Kvalitetsindex 2025</th><td>{str(b["ski"]).replace(".", ",")} '
                f'av 100</td><td>{"Mycket nöjda kunder" if b["ski"] >= 75 else "Nöjda kunder"}</td></tr>')
        if b['kons']:
            betyg_rader.append(
                f'<tr><th scope="row">Konsumenternas Försäkringsbyrå</th>'
                f'<td>{str(b["kons"]).replace(".", ",")} av 5</td><td>{b["kons_produkt"]}</td></tr>')

        if betyg_rader:
            betyg = (f'<h2>{H["betyg"]}</h2>'
                     f'<p>Två oberoende källor mäter svenska försäkringsbolag. Svenskt Kvalitetsindex '
                     f'mäter vad kunderna tycker; Konsumenternas Försäkringsbyrå bedömer villkorens '
                     f'innehåll och säljer ingenting själva.</p>'
                     f'<div class="tbl"><table><thead><tr><th scope="col">Mätning</th>'
                     f'<th scope="col">Resultat</th><th scope="col">Avser</th></tr></thead>'
                     f'<tbody>{"".join(betyg_rader)}</tbody></table></div>'
                     f'<div class="src"><p>Källa: Svenskt Kvalitetsindex, branschmätning bilförsäkring '
                     f'2025, och Konsumenternas Försäkringsbyrå. Betygen avser villkor respektive '
                     f'kundnöjdhet — inte pris.</p></div>')
        else:
            betyg = f'<h2>{H["betyg"]}</h2><p>{BETYG_UTAN[i % len(BETYG_UTAN)]}</p>'

        ja = ''.join(f'<li>{x}</li>' for x in b['passar'])
        nej = ''.join(f'<li>{x}</li>' for x in b['passar_ej'])

        byta_par = [BYTA[(i * 3 + k) % len(BYTA)] for k in range(3)]
        skada_steg = SKADA[i % len(SKADA)]

        S = {
         'pris': (f'<h2>{H["pris"]}</h2>'
                  f'<div class="tbl"><table><caption>{b["namn"]} — vägledande årspremie</caption>'
                  f'<thead><tr><th scope="col">Nivå</th><th scope="col">Per år</th>'
                  f'<th scope="col">Per månad</th></tr></thead><tbody>'
                  f'<tr><th scope="row"><a href="/trafikforsakring/">Trafikförsäkring</a></th>'
                  f'<td>—</td><td>—</td></tr>'
                  f'<tr><th scope="row"><a href="/halvforsakring/">Halvförsäkring</a></th>'
                  f'<td>—</td><td>—</td></tr>'
                  f'<tr><th scope="row"><a href="/helforsakring/">Helförsäkring</a></th>'
                  f'<td>—</td><td>—</td></tr>'
                  f'</tbody></table></div>{TODO}{PROFIL}'),
         'villkor': (f'<h2>{H["villkor"]}</h2><p>{b["sammanfattning"]}</p>'
                     f'<div class="tbl"><table><caption>Fakta om {b["namn"]}</caption>'
                     f'<tbody>{fakta}</tbody></table></div>'),
         'betyg': betyg,
         'passar': (f'<h2>{H["passar"]}</h2>'
                    f'<p>Vi rekommenderar inte alla bolag till alla. Här är båda sidorna.</p>'
                    f'<div class="split"><div><h3>Ett bra val om</h3><ul>{ja}</ul></div>'
                    f'<div><h3>Välj något annat om</h3><ul>{nej}</ul></div></div>'),
         'byta': (f'<h2>{H["byta"]}</h2>'
                  + ''.join(f'<h3>{t}</h3><p>{p}</p>' for t, p in byta_par)),
         'skada': (f'<h2>{H["skada"]}</h2>'
                   + ''.join(f'<h3>{n}. {t}</h3><p>{p}</p>'
                             for n, (t, p) in enumerate(skada_steg, 1))),
        }

        body = ''.join((_sec_alt if n % 2 else _sec)(S[k])
                       for n, k in enumerate(b['ordning']))
        body += _sec(
            f'<div class="cta"><h2>Jämför {b["kort"]} med andra bolag</h2>'
            f'<p>Ange registreringsnumret och se vad du får betala hos flera bolag.</p>'
            f'<div class="cta-inner">{{PLATE}}</div></div>')

        faq = [
         (f'Vad kostar bilförsäkring hos {b["namn"]}?',
          f'Priset beror på bil, ålder, bostadsort, körsträcka och självrisk. Skillnaden mellan '
          f'billigaste och dyraste bolag är ofta flera tusen kronor om året för samma bil, så '
          f'hämta en offert på ditt eget registreringsnummer.'),
         (f'Är {b["namn"]} ett bra försäkringsbolag?',
          b['sammanfattning'].split('.')[0] + '.'),
         (f'Hur säger jag upp min försäkring hos {b["namn"]}?',
          'Huvudregeln är en månads skriftlig uppsägning till huvudförfallodagen. Vid bilköp, '
          'flytt eller aviserad premiehöjning får du byta direkt. Begär alltid intyg på dina '
          'skadefria år samtidigt.'),
         (f'Vem passar {b["namn"]} bäst för?',
          b['passar'][0] + '. ' + b['passar'][1] + '.'),
        ]

        rel = [('/forsakringsbolag/', 'Alla försäkringsbolag'),
               ('/jamfor-bilforsakring/', 'Så jämför du rätt'),
               ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
               ('/helforsakring/', 'Helförsäkring — när behövs den?')]
        for o in BOLAG:
            if o['slug'] != b['slug'] and len(rel) < 6:
                rel.append((f'/forsakringsbolag/{o["slug"]}/', f'{o["namn"]} — omdöme'))

        sidor.append({
         'slug': f'forsakringsbolag/{b["slug"]}', 'key': True,
         'title': f'{b["namn"]} bilförsäkring — omdöme, villkor och pris 2026',
         'desc': f'{b["namn"]} bilförsäkring: villkor, betyg, vem det passar för och hur du '
                 f'säger upp. Jämför med andra bolag på ditt registreringsnummer.',
         'eyebrow': b['typ'],
         'h1': f'{b["namn"]} bilförsäkring',
         'lead': b['sammanfattning'].split('. ')[0] + '.',
         'checks': [f'{k}: {v}' for k, v in b['fakta'][:3]],
         'card_t': f'Jämför {b["kort"]} med marknaden',
         'sticky': f'Jämför {b["kort"]} med andra bolag',
         'body': body, 'faq': faq, 'rel': rel,
         'faq_h2': f'Vanliga frågor om {b["namn"]}',
        })
    return sidor


# ═══ MÄRKESSIDOR ════════════════════════════════════════════════════
MARKE_H2 = [
 {'pris': 'Vad kostar det att försäkra en {n}?', 'varfor': 'Det här styr premien på en {n}',
  'modeller': 'Priset skiljer sig mellan modellerna', 'valj': 'Trafik, halv eller hel till din {n}?',
  'spara': 'Så sänker du premien'},
 {'pris': '{n} bilförsäkring — priserna för 2026', 'varfor': 'Varför {n} kostar som den gör',
  'modeller': 'Modell för modell', 'valj': 'Vilken skyddsnivå passar din {n}?',
  'spara': 'Fem sätt att betala mindre'},
 {'pris': 'Premien på en {n}', 'varfor': 'Det som avgör priset',
  'modeller': 'Vanliga {n}-modeller i Sverige', 'valj': 'Rätt skyddsnivå för din {n}',
  'spara': 'Sänk kostnaden utan att tappa skydd'},
 {'pris': 'Försäkringskostnad för {n}', 'varfor': 'Tre saker som påverkar din premie',
  'modeller': 'Modellerna och vad de betyder för priset', 'valj': 'Halv eller hel till din {n}?',
  'spara': 'Konkreta sätt att spara'},
]

MARKE_ORD = [
 ['pris', 'varfor', 'modeller', 'valj', 'spara'],
 ['varfor', 'pris', 'valj', 'modeller', 'spara'],
 ['pris', 'modeller', 'varfor', 'spara', 'valj'],
 ['varfor', 'valj', 'pris', 'modeller', 'spara'],
 ['pris', 'valj', 'varfor', 'modeller', 'spara'],
]

PRIS_INTRO = [
 'Tabellen visar vägledande årspremie på vår jämförelseprofil. Ditt eget pris sätts av bolaget '
 'utifrån bil, ålder, bostadsort och skadehistorik.',
 'Beloppen nedan gäller en standardprofil och är till för att kunna jämföras mellan märken. '
 'Din faktiska premie kan ligga både över och under.',
 'Så här ser prisbilden ut på vår fasta jämförelseprofil. Skillnaden mellan billigaste och '
 'dyraste bolag är ofta större än skillnaden mellan två bilmodeller.',
 'Priserna räknas på samma profil för alla märken på sajten, så att tabellerna går att '
 'ställa mot varandra. Hämta alltid en egen offert innan du bestämmer dig.',
]

MODELL_INTRO = [
 'Motor, årsmodell och utrustningsnivå flyttar premien mer än de flesta räknar med. Här är de '
 '{n}-modeller som är vanligast på svenska vägar.',
 'Inom samma märke kan premien skilja rejält mellan modellerna. Vikt, effekt och nypris är de '
 'tre faktorer som styr mest.',
 'Det är sällan märket ensamt som avgör priset — modellen gör minst lika mycket. Nedan de '
 'vanligaste {n}-modellerna i Sverige.',
 'Premien följer bilens värde och skadestatistik, och båda varierar kraftigt inom ett och '
 'samma märke.',
]

FAQ_KOSTAR = [
 'Priset styrs av modell, årsmodell, din ålder, var du bor och vilken självrisk du väljer. '
 'Skillnaden mellan bolagen är ofta flera tusen kronor om året för exakt samma bil.',
 'Det avgörs av bilens värde och din egen profil. Två personer med samma {n} kan få offerter '
 'som skiljer flera tusen kronor, beroende på ålder, postnummer och skadefria år.',
 'Det finns inget generellt svar. Bolagen viktar riskfaktorerna olika, och därför är det bara '
 'en offert på ditt eget registreringsnummer som ger ett rättvisande besked.',
 'Premien beräknas individuellt. Bilens ersättningsvärde sätter ramen, medan din ålder och '
 'körsträcka avgör var i ramen du hamnar.',
]

FAQ_HEL = [
 'Har bilen kvar vagnskadegaranti räcker halvförsäkring — annars betalar du för samma skydd '
 'två gånger. Är bilen värd under ungefär 30 000 kronor blir helförsäkring sällan lönsam.',
 'Det beror på bilens värde och om garantin gått ut. Vid leasing och billån är helförsäkring '
 'däremot i praktiken alltid ett krav från långivaren.',
 'Räkna på marknadsvärdet. Kaskoersättningen begränsas av vad bilen är värd, så på en äldre '
 'bil äts premieskillnaden snabbt upp.',
 'Så länge du inte skulle klara en reparation ur egen ficka är svaret ja. När bilens värde '
 'sjunkit under några tiotusen kronor vänder kalkylen.',
]

FAQ_BILLIGAST = [
 'Det varierar med din profil. Bolagen viktar ålder, bostadsort och körsträcka olika, så det '
 'bolag som är billigast för en granne kan vara dyrast för dig.',
 'Ingen aktör är billigast för alla. Vissa bolag är milda mot unga förare men hårda mot '
 'storstadsadresser, andra tvärtom.',
 'Det går inte att svara på generellt. Hämta minst tre offerter med samma självrisk och '
 'samma tillägg, så blir jämförelsen rättvis.',
 'Prisbilden ändras mellan åren när bolagen justerar sina modeller. Därför lönar det sig att '
 'jämföra varje år även om din situation är oförändrad.',
]

VALJ = {
 'volym':
  '<p>Volymmärken har ett stort bestånd i Sverige, och det påverkar valet av skyddsnivå. '
  'Reservdelar är billiga och finns hos de flesta verkstäder, vilket gör en reparation '
  'överkomlig även utan vagnskada. På en {n} som passerat åtta till tio år är '
  'halvförsäkring därför ofta det ekonomiskt rimliga valet.</p>',
 'premium':
  '<p>På premiummärken är steget till helförsäkring mer motiverat än på volymbilar. '
  'Reservdelarna kostar mer, och en reparation som hade landat på tiotusen kronor på en '
  'vanlig bil kan lätt dubbleras på en {n}. Så länge bilen är värd över hundratusen '
  'kronor är vagnskadan svår att argumentera bort.</p>',
 'elbil':
  '<p>På elbilar är valet inte bara mellan halv och hel — det handlar också om batteriet. '
  'Kontrollera att villkoren uttryckligen nämner drivbatteriet vid kortslutning och yttre '
  'skada, inte bara vid brand. Tillverkarens garanti täcker kapacitetstapp, inte fysisk '
  'skada. På en {n} utgör batteriet en stor del av värdet, vilket i praktiken gör '
  'helförsäkring till ett krav.</p>',
 'budget':
  '<p>Här är frågan snarare om du behöver helförsäkring alls. Kaskoersättningen begränsas '
  'av marknadsvärdet, och på en {n} med några år på nacken kan premieskillnaden vara '
  'svår att räkna hem. Trafikförsäkring plus halvförsäkring täcker stöld, brand och glas — '
  'de skador som verkligen gör ont på en billig bil.</p>',
 'suv':
  '<p>SUV-formatet påverkar valet på två sätt. Bilarna är bredare och längre, vilket gör '
  'parkeringsskador vanligare och dyrare — en stötfångare med sensorer kostar mångdubbelt '
  'mot en slät. Har din {n} dessutom fyrhjulsdrift finns fler komponenter som kan ta '
  'skada. Båda talar för helförsäkring så länge bilen har ett värde att skydda.</p>',
}

SPARA = [
 [('Höj självrisken', 'Det är den faktor du styr mest. Kan du bära 8 000 kr i stället för '
   '4 000 sjunker premien märkbart — men beloppet ska gå att betala den månad skadan sker.'),
  ('Ange rätt körsträcka', 'Många överskattar sin körning när de tecknar. Att rätta från '
   '2 000 till 1 200 mil tar fem minuter.'),
  ('Samla försäkringarna', 'Bil och hem i samma bolag ger normalt rabatt räknat på hela '
   'premien, inte bara på bilen.'),
  ('Anmäl inte småskador', 'Räkna på premiepåslaget över tre år innan du anmäler en skada '
   'under ungefär 10 000 kr.')],
 [('Se över skyddsnivån först', 'Vagnskadegaranti på en nyare bil gör helförsäkring '
   'överflödig under garantitiden — du betalar annars för samma skydd två gånger.'),
  ('Jämför med samma självrisk', 'Ett lägre pris beror ofta bara på att offerten har högre '
   'självrisk. Lås beloppet innan du jämför.'),
  ('Kontrollera vad som redan ingår', 'Assistans, hyrbil och allrisk paketeras olika. Det '
   'billigaste grundpriset blir ibland det dyraste totalpriset.'),
  ('Begär intyg på skadefria år', 'Utan det placeras du i sämsta bonusklassen hos det nya '
   'bolaget.')],
 [('Parkera bilen inlåst om du kan', 'Garage eller carport dokumenterat ger rabatt hos de '
   'flesta bolag, särskilt i storstad.'),
  ('Välj mindre fälgar', 'Stora fälgar är dyra att ersätta och tar oftare skada mot '
   'trottoarkanter. De täcks bara av helförsäkring.'),
  ('Jämför årspris, inte månadspris', 'Fyrtio kronor i månaden låter försumbart och är '
   '480 kronor om året.'),
  ('Se över försäkringen varje år', 'Bolagen viktar riskfaktorer olika och ändrar sina '
   'modeller. Det lönar sig även när din situation är oförändrad.')],
 [('Räkna på årsbelopp', 'Månadspriser döljer skillnader. Trettio kronor i månaden är 360 '
   'kronor om året — och det är ofta där bolagen skiljer sig.'),
  ('Fråga vad självrisken faktiskt är per moment', 'Glas, stöld och vagnskada har olika '
   'självrisk hos samma bolag. Ett lågt totalpris kan dölja en hög vagnskadesjälvrisk.'),
  ('Undvik dubbelt skydd', 'Har bilen kvar vagnskadegaranti betalar du för samma sak två '
   'gånger med helförsäkring. Kontrollera slutdatumet i bilens papper.'),
  ('Meddela när något ändras', 'Kortare pendling, ny adress eller färre förare i hushållet '
   'påverkar premien direkt — men bara om du berättar det.')],
 [('Titta på vad som redan ingår', 'Assistans, hyrbil och allrisk paketeras olika. Det '
   'billigaste grundpriset kan bli det dyraste totalpriset när du lagt till det du behöver.'),
  ('Var realistisk om körsträckan', 'Överskattad körsträcka är den vanligaste onödiga '
   'kostnaden. Läs av mätarställningen två år bakåt och räkna.'),
  ('Fundera på om du behöver kasko alls', 'Under ungefär 30 000 kronor i marknadsvärde är '
   'halvförsäkring oftast det rationella valet.'),
  ('Byt inte bara på pris', 'Ett bolag med sämre skadehantering kostar dig mer den dag något '
   'händer än vad du sparat på premien i tre år.')],
 [('Höj självrisken om ekonomin bär', 'Steget från 4 000 till 8 000 kronor sänker premien '
   'märkbart. Sätt undan mellanskillnaden så att beloppet finns när det behövs.'),
  ('Parkera inlåst och dokumentera det', 'Garage eller carport ger rabatt hos de flesta '
   'bolag — men bara om du anger det vid tecknandet.'),
  ('Samla hushållets bilar', 'Två bilar i samma bolag ger normalt rabatt på båda, räknat på '
   'den samlade premien.'),
  ('Begär bonusintyg varje gång du byter', 'Det tar fem minuter och är gratis. Utan det '
   'kostar bytet mer än det sparar det första året.')],
]


def markessidor():
    sidor = []
    for i, m in enumerate(MARKEN):
        n = m['namn']
        H = {k: v.replace('{n}', n) for k, v in MARKE_H2[i % len(MARKE_H2)].items()}
        ordning = MARKE_ORD[i % len(MARKE_ORD)]
        punkter = ''.join(f'<li>{x}</li>' for x in m['punkter'])
        modeller = ''.join(f'<tr><th scope="row">{n} {mo}</th><td>—</td><td>—</td></tr>'
                           for mo in m['modeller'])
        spara = SPARA[i % len(SPARA)]

        # Bild: finns filen bilder/<slug>.webp används den automatiskt.
        # Alt-text och bildtext hämtas från BILD, annars generisk reserv.
        har_bild = os.path.exists(f'bilder/{m["slug"]}.webp')
        b = BILD.get(m['slug'], {})
        bild_alt = b.get('alt', f'{n} — bilförsäkring och pris')
        bild_cap = b.get('cap', f'{n} — det här påverkar försäkringspremien.')

        S = {
         'pris': (f'<h2>{H["pris"]}</h2>'
                  f'<p>{PRIS_INTRO[(i * 3) % len(PRIS_INTRO)]}</p>'
                  f'<div class="tbl"><table><caption>{n} — vägledande årspremie</caption>'
                  f'<thead><tr><th scope="col">Nivå</th><th scope="col">Per år</th>'
                  f'<th scope="col">Per månad</th></tr></thead><tbody>'
                  f'<tr><th scope="row"><a href="/trafikforsakring/">Trafikförsäkring</a></th><td>—</td><td>—</td></tr>'
                  f'<tr><th scope="row"><a href="/halvforsakring/">Halvförsäkring</a></th><td>—</td><td>—</td></tr>'
                  f'<tr><th scope="row"><a href="/helforsakring/">Helförsäkring</a></th><td>—</td><td>—</td></tr>'
                  f'</tbody></table></div>{TODO}{PROFIL}'),
         'varfor': (f'<h2>{H["varfor"]}</h2>' + (
             f'<div class="media{" rev" if i % 2 else ""}">'
             f'<figure><img src="/bilder/{m["slug"]}.webp" alt="{bild_alt}" '
             f'width="1200" height="750" loading="lazy" decoding="async">'
             f'<figcaption>{bild_cap}</figcaption></figure>'
             f'<div class="media-t"><p>{m["karakteristik"]}</p></div></div>'
             f'<ul>{punkter}</ul>'
             if har_bild
             else f'<p>{m["karakteristik"]}</p><ul>{punkter}</ul>')),
         'modeller': (f'<h2>{H["modeller"]}</h2>'
                      f'<p>{MODELL_INTRO[(i * 5) % len(MODELL_INTRO)].replace("{n}", n)}</p>'
                      f'<div class="tbl"><table><thead><tr><th scope="col">Modell</th>'
                      f'<th scope="col">Halvförsäkring</th><th scope="col">Helförsäkring</th>'
                      f'</tr></thead><tbody>{modeller}</tbody></table></div>'),
         'valj': (f'<h2>{H["valj"]}</h2>' + VALJ[m['grupp']].replace('{n}', n)
                  + f'<p>{m["punkter"][2] if len(m["punkter"]) > 2 else m["punkter"][0]} '
                    f'Det är värt att väga in när du väljer mellan '
                    f'<a href="/halvforsakring/">halvförsäkring</a> och '
                    f'<a href="/helforsakring/">helförsäkring</a>. Se också vår guide till '
                    f'<a href="/jamfor-bilforsakring/">hur du jämför offerter</a>.</p>'),
         'spara': (f'<h2>{H["spara"]}</h2>'
                   + ''.join(f'<h3>{t}</h3><p>{p}</p>' for t, p in spara)),
        }

        body = ''.join((_sec_alt if k % 2 else _sec)(S[s])
                       for k, s in enumerate(ordning))
        body += _sec(
            f'<div class="cta"><h2>Se vad din {n} kostar</h2>'
            f'<p>Ange registreringsnumret — bilens uppgifter hämtas automatiskt.</p>'
            f'<div class="cta-inner">{{PLATE}}</div></div>')

        faq = [
         (f'Vad kostar bilförsäkring till en {n}?', FAQ_KOSTAR[(i * 3) % len(FAQ_KOSTAR)].replace('{n}', n)),
         (f'Är {n} dyr att försäkra?',
          m['karakteristik'].split('. ')[0] + '.'),
         (f'Behöver jag helförsäkring till min {n}?', FAQ_HEL[(i * 7) % len(FAQ_HEL)]),
         (f'Vilket bolag är billigast till {n}?', FAQ_BILLIGAST[(i * 5) % len(FAQ_BILLIGAST)]),
        ]

        rel = [('/bilmarken/', 'Alla bilmärken'),
               ('/jamfor-bilforsakring/', 'Så jämför du rätt'),
               ('/halvforsakring/', 'Halvförsäkring'),
               ('/helforsakring/', 'Helförsäkring')]
        # Guidelänk som passar märkets profil — ger tematisk intern länkning.
        if m['grupp'] == 'elbil':
            rel.append(('/bilforsakring-elbil/', 'Bilförsäkring för elbil'))
        elif m['grupp'] == 'budget':
            rel.append(('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'))
        elif m['grupp'] == 'premium':
            rel.append(('/leasingbil-forsakring/', 'Försäkring vid leasing'))
        else:
            rel.append(('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'))
        samma = [o for o in MARKEN if o['grupp'] == m['grupp'] and o['slug'] != m['slug']][:2]
        for o in samma:
            rel.append((f'/bilmarken/{o["slug"]}/', f'{o["namn"]} bilförsäkring'))

        sidor.append({
         'slug': f'bilmarken/{m["slug"]}', 'key': True,
         'title': f'{n} bilförsäkring 2026 — pris, skydd och jämförelse',
         'desc': f'Vad kostar det att försäkra en {n}? Se vad som påverkar premien, '
                 f'vilken skyddsnivå som passar och hur du jämför bolagen.',
         'eyebrow': f'{m["ursprung"]}',
         'h1': f'{n} bilförsäkring',
         'lead': m['karakteristik'].split('. ')[0] + '.',
         'checks': m['punkter'],
         'card_t': f'Se priset på din {n}',
         'sticky': f'Jämför försäkring till din {n}',
         'body': body, 'faq': faq, 'rel': rel,
         'faq_h2': f'Vanliga frågor om {n} bilförsäkring',
         **({'bild': f'/bilder/{m["slug"]}.webp', 'bild_alt': bild_alt} if har_bild else {}),
        })
    return sidor


# ═══ HUBBSIDOR ══════════════════════════════════════════════════════
def hubbar():
    bkort = ''.join(
        f'<a class="gc" href="/forsakringsbolag/{b["slug"]}/">'
        f'<span class="gc-t">{b["namn"]}</span>'
        f'<span class="gc-d">{b["sammanfattning"].split(". ")[0]}.</span>'
        f'<span class="gc-go">Läs omdömet &rarr;</span></a>' for b in BOLAG)

    rader = ''.join(
        f'<tr><th scope="row"><a href="/forsakringsbolag/{b["slug"]}/">{b["namn"]}</a></th>'
        f'<td>{str(b["ski"]).replace(".", ",") if b["ski"] else "—"}</td>'
        f'<td>{str(b["kons"]).replace(".", ",") if b["kons"] else "—"}</td>'
        f'<td>{b["typ"]}</td></tr>'
        for b in sorted(BOLAG, key=lambda x: -(x['ski'] or 0)))

    hub_bolag = {
     'slug': 'forsakringsbolag', 'key': True,
     'title': 'Försäkringsbolag bilförsäkring — jämför 16 bolag 2026',
     'desc': 'Alla större bilförsäkringsbolag i Sverige med betyg från SKI och '
             'Konsumenternas Försäkringsbyrå. Se vem som passar din situation.',
     'eyebrow': 'Översikt',
     'h1': 'Försäkringsbolag för bil',
     'lead': 'Sexton bolag som säljer bilförsäkring i Sverige, med oberoende betyg där de '
             'finns. Vi säljer inga försäkringar och företräder inget bolag.',
     'checks': ['Betyg från Svenskt Kvalitetsindex och Konsumenternas Försäkringsbyrå',
                'Både de stora bolagen och de digitala utmanarna',
                'Vem varje bolag passar — och vem det inte passar'],
     'sticky': 'Jämför alla bolag gratis',
     'body': jamforelse.sektion(
        'Jämför bilförsäkring från 16 bolag',
        'Alla bolag på den svenska marknaden med oberoende betyg, villkorsfakta och '
        'självrisker. Filtrera på skyddsnivå och fäll ut ett bolag för att se vad som '
        'faktiskt ingår.')
      + _sec(
        '<h2>Bolagen rangordnade efter kundnöjdhet</h2>'
        '<p>Svenskt Kvalitetsindex mäter vad kunderna tycker, på en skala från 0 till 100. '
        'Konsumenternas Försäkringsbyrå bedömer i stället villkorens innehåll, från 1 till 5. '
        'De mäter alltså två olika saker — ett bolag kan ha nöjda kunder och medelmåttiga '
        'villkor, eller tvärtom.</p>'
        '<div class="tbl"><table><thead><tr><th scope="col">Bolag</th>'
        '<th scope="col">SKI 2025</th><th scope="col">Konsumenternas</th>'
        '<th scope="col">Typ</th></tr></thead><tbody>' + rader + '</tbody></table></div>'
        '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>'
        '<div class="src"><p>Källa: Svenskt Kvalitetsindex, branschmätning bilförsäkring 2025, '
        'och Konsumenternas Försäkringsbyrå. Streck betyder att data saknas — för SKI normalt '
        'att marknadsandelen är för liten för statistisk tillförlitlighet.</p></div>')
      + _sec_alt('<h2>Alla bolag</h2><div class="grid">' + bkort + '</div>')
      + _sec('<div class="cta"><h2>Se vad du får betala</h2>'
             '<p>Ange registreringsnumret och jämför bolagen på din egen bil.</p>'
             '<div class="cta-inner">{PLATE}</div></div>'),
     'faq': [
      ('Vilket försäkringsbolag är bäst för bil?',
       'Det beror på din situation. Dina Försäkringar hade högst kundnöjdhet i SKI 2025 med '
       '80,2 poäng, medan Folksams Bilförsäkring Stor fick högst villkorsbetyg av '
       'Konsumenternas med 4,6 av 5. Det bolag som passar dig avgörs av din bil, din ålder och '
       'var du bor.'),
      ('Vad är skillnaden mellan SKI och Konsumenternas betyg?',
       'SKI mäter kundnöjdhet genom att fråga kunderna. Konsumenternas Försäkringsbyrå läser '
       'villkoren och bedömer innehållet. Ett bolag kan ha nöjda kunder och samtidigt '
       'medelmåttiga villkor.'),
      ('Är de digitala bolagen sämre?',
       'Inte nödvändigtvis. Flera av dem har starka villkor och konkurrenskraftiga priser. '
       'De saknar ofta SKI-data eftersom marknadsandelen ännu är för liten för mätningen.'),
      ('Kan jag byta bolag när som helst?',
       'Normalt vid huvudförfallodagen med en månads uppsägningstid. Vid bilköp, flytt eller '
       'aviserad premiehöjning får du byta direkt.'),
     ],
     'rel': [('/jamfor-bilforsakring/', 'Så jämför du rätt'),
             ('/bilmarken/', 'Alla bilmärken'),
             ('/redaktionell-metod/', 'Så samlar vi in data'),
             ('/', 'Vad kostar bilförsäkring?')],
     'faq_h2': 'Vanliga frågor om försäkringsbolag',
    }

    grupper = {}
    for m in MARKEN:
        grupper.setdefault(m['grupp'], []).append(m)
    namn_grupp = {'volym': 'Volymmärken', 'premium': 'Premiummärken',
                  'elbil': 'Elbilsmärken', 'budget': 'Budgetmärken', 'suv': 'SUV och terräng'}
    sektioner = ''
    for g, lista in grupper.items():
        kort = ''.join(
            f'<a class="gc" href="/bilmarken/{x["slug"]}/">'
            f'<span class="gc-t">{x["namn"]}</span>'
            f'<span class="gc-d">{x["punkter"][0]}</span>'
            f'<span class="gc-go">Se guiden &rarr;</span></a>' for x in lista)
        sektioner += f'<h2>{namn_grupp.get(g, g.capitalize())}</h2><div class="grid">{kort}</div>'

    hub_marken = {
     'slug': 'bilmarken', 'key': True,
     'title': 'Bilförsäkring per bilmärke — jämför pris för ditt märke 2026',
     'desc': 'Vad kostar det att försäkra din bil? Se guider för alla stora bilmärken på den '
             'svenska marknaden och vad som påverkar premien för just ditt.',
     'eyebrow': 'Översikt',
     'h1': 'Bilförsäkring per märke',
     'lead': 'Bilmärket avgör mer av premien än de flesta tror — genom reservdelspriser, '
             'skadefrekvens och hur brett verkstadsnätet är. Här är guiderna för de märken '
             'som säljs i Sverige.',
     'checks': ['Vad som gör just ditt märke dyrt eller billigt att försäkra',
                'Vanliga modeller och hur de skiljer sig i pris',
                'Vilken skyddsnivå som passar din bils ålder och värde'],
     'sticky': 'Jämför försäkring på din bil',
     'body': _sec(
        '<h2>Varför bilmärket påverkar premien</h2>'
        '<p>Tre saker avgör: vad reservdelarna kostar, hur ofta modellen är inblandad i skador '
        'och hur många verkstäder som kan reparera den. Ett märke med stort bestånd i Sverige '
        'har billigare delar och fler verkstäder — och därmed lägre premie — även om bilarna '
        'kostar lika mycket att köpa.</p>'
        '<p>Det förklarar varför en Skoda kostar mindre att försäkra än en likvärdig Audi '
        'trots att de delar plattform, och varför nya märken på marknaden prissätts '
        'försiktigt tills skadestatistiken vuxit.</p>')
      + _sec_alt(sektioner)
      + _sec('<div class="cta"><h2>Se priset på din bil</h2>'
             '<p>Ange registreringsnumret — märke, modell och årsmodell hämtas automatiskt.</p>'
             '<div class="cta-inner">{PLATE}</div></div>'),
     'faq': [
      ('Vilket bilmärke är billigast att försäkra?',
       'Märken med lågt nypris och enkel teknik ligger lägst — Dacia och Fiat är typiska '
       'exempel. Kaskopremien beräknas på vad bilen kostar att ersätta, så inköpspriset slår '
       'igenom direkt.'),
      ('Varför är premium dyrare att försäkra?',
       'Reservdelarna kostar mer, verkstadsnätet är smalare och bilarna har oftare '
       'förarassistans som måste kalibreras efter en reparation. En vindruta med sensorer '
       'kostar mångdubbelt mot en utan.'),
      ('Är elbilar dyrare att försäkra?',
       'På helförsäkring oftast ja, eftersom batteriet utgör en stor del av bilens värde. '
       'Skillnaden varierar dock mycket mellan märken — en Kia EV6 prissätts inte som en Tesla.'),
      ('Påverkar bilens ålder premien?',
       'Ja, på två sätt. Äldre bilar har lägre ersättningsvärde vilket sänker kaskopremien, '
       'men de saknar ofta modern förarassistans vilket kan höja skaderisken.'),
     ],
     'rel': [('/forsakringsbolag/', 'Alla försäkringsbolag'),
             ('/jamfor-bilforsakring/', 'Så jämför du rätt'),
             ('/helforsakring/', 'Behöver du helförsäkring?'),
             ('/', 'Vad kostar bilförsäkring?')],
     'faq_h2': 'Vanliga frågor om bilmärken och försäkring',
    }
    return [hub_bolag, hub_marken]


def alla():
    return hubbar() + bolagssidor() + markessidor()
