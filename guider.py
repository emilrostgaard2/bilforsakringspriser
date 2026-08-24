# -*- coding: utf-8 -*-
"""Guidesidor: billigaste, elbil, leasing, pensionär och ung förare.

PRISERNA ÄR PLATSHÅLLARE
Alla pristabeller står med tankstreck och TODO-rutan ovanför. Strukturen är
klar — fyll i egna insamlade siffror innan lansering. Se README.md.

TABELLER
Varje sida har fyra till fem tabeller. De som inte innehåller pris är färdiga
att publicera direkt, eftersom de bygger på villkorslogik och på uppgifterna i
companies.py — inte på siffror vi ännu inte samlat in.
"""
from companies import BOLAG

TODO = ('<div class="warn"><strong>PLATSHÅLLARE — ska ersättas före lansering.</strong> '
        'Beloppen i tabellen är exempelplatser och inte insamlade marknadspriser.</div>')

METOD = ('<div class="src"><p><strong>Så räknar vi.</strong> Alla priser gäller samma '
         'jämförelseprofil: 40 år, 15 000 km/år, ort utanför storstad, sex skadefria år '
         'och 4 000 kr i självrisk. Ändras en förutsättning ändras priset — ofta mycket. '
         'Läs mer i vår <a href="/redaktionell-metod/">redaktionella metod</a>.</p></div>')

SWIPE = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>'


def _tbl(caption, kolumner, rader, swipe=True):
    """Bygger en tabell med radrubrik i första kolumnen."""
    th = ''.join(f'<th scope="col">{k}</th>' for k in kolumner)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    cap = f'<caption>{caption}</caption>' if caption else ''
    return (f'<div class="tbl"><table>{cap}<thead><tr>{th}</tr></thead>'
            f'<tbody>{tr}</tbody></table></div>' + (SWIPE if swipe and len(kolumner) > 3 else ''))


def bolagstabell(pris_kolumn=True):
    """Alla bolag med typ och oberoende betyg — data hämtas ur companies.py."""
    kol = ['Bolag', 'Typ', 'Konsumenternas', 'SKI']
    if pris_kolumn:
        kol.append('Pris per år')
    rader = []
    for b in BOLAG:
        rad = [f'<a href="/forsakringsbolag/{b["slug"]}/">{b["namn"]}</a>',
               b.get('typ') or '—',
               str(b['kons']).replace('.', ',') if b.get('kons') else '—',
               str(b['ski']).replace('.', ',') if b.get('ski') else '—']
        if pris_kolumn:
            rad.append('—')
        rader.append(rad)
    th = ''.join(f'<th scope="col">{k}</th>' for k in kol)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    return (f'<div class="tbl"><table><caption>Bolagen på marknaden — typ och oberoende '
            f'betyg</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
            + SWIPE)


SIDOR = [

# ═══ BILLIGASTE ════════════════════════════════════════════════════
{
 'slug': 'billigaste-bilforsakringen', 'key': True,
 'title': 'Billigaste bilförsäkringen 2026 — så hittar du den',
 'desc': 'Vilket bolag är billigast på bilförsäkring? Se vad som styr priset, '
         'vilka rabatter som finns och hur du sänker premien utan att tappa skydd.',
 'eyebrow': 'Guide',
 'h1': 'Billigaste bilförsäkringen',
 'lead': 'Det finns inget bolag som är billigast för alla. Priset räknas fram ur din bil, '
         'din ålder, ditt postnummer och din körsträcka — och bolagen viktar de faktorerna '
         'helt olika. Därför kan samma bil kosta dubbelt så mycket hos ett bolag som hos ett annat.',
 'checks': ['Vad som faktiskt styr premien — och vad du kan påverka',
            'Fem sätt att sänka priset utan att försämra skyddet',
            'Varför det billigaste priset inte alltid är den billigaste försäkringen'],
 'card_t': 'Se vilket bolag som är billigast för dig',
 'sticky': 'Hitta din billigaste bilförsäkring',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Ingen lista kan peka ut det billigaste bolaget
för just din bil, eftersom priset räknas fram individuellt. Det du kan göra är att förstå
vilka faktorer som väger tyngst, rätta till dem som är felaktiga i din nuvarande försäkring
och sedan begära offert från flera bolag på samma villkor.</p></div>

<h2>Prisbilden per skyddsnivå</h2>
<p>Steget från trafikförsäkring till halvförsäkring är oftast litet i kronor och stort i
skydd. Steget från halv till hel är det omvända: det är där premien verkligen stiger, eftersom
vagnskadedelen är den dyraste delen av en bilförsäkring.</p>
{_tbl('Vägledande årspremie per nivå',
      ['Nivå', 'Per år', 'Per månad', 'Andel av helförsäkring'],
      [['<a href="/trafikforsakring/">Trafikförsäkring</a>', '—', '—', '—'],
       ['<a href="/halvforsakring/">Halvförsäkring</a>', '—', '—', '—'],
       ['<a href="/helforsakring/">Helförsäkring</a>', '—', '—', '—']])}
{TODO}{METOD}

<h2>Vad som styr priset — och hur mycket du kan påverka</h2>
<p>Den här tabellen är den viktigaste på sidan. Många lägger tid på att jaga rabatter på
faktorer som knappt påverkar premien, samtidigt som de missar de två eller tre som gör
verklig skillnad.</p>
{_tbl('Premiefaktorer i fallande ordning',
      ['Faktor', 'Påverkan på premien', 'Kan du ändra den?'],
      [['Bilmodell och nypris', 'Mycket stor', 'Bara genom att byta bil'],
       ['Ålder på föraren', 'Mycket stor', 'Nej — men premien sjunker med åren'],
       ['Skadefria år (bonus)', 'Mycket stor', 'Byggs upp över tid, följer dig'],
       ['Bostadsort och postnummer', 'Stor', 'Bara vid flytt — men måste alltid vara rätt'],
       ['Årlig körsträcka', 'Stor', 'Ja, direkt — och ofta felaktigt angiven'],
       ['Vald självrisk', 'Måttlig till stor', 'Ja, direkt'],
       ['Var bilen står nattetid', 'Måttlig', 'Ja, om du har garage eller carport'],
       ['Betalningssätt', 'Liten', 'Ja — helår är billigare än månad'],
       ['Tilläggsförsäkringar', 'Liten till måttlig', 'Ja, direkt']],
      swipe=False)}

<h2>Fem sätt att sänka premien</h2>
<p>Ordningen är avsiktlig. De två första ger nästan alltid mest, och kostar dig ingenting
i skydd.</p>
{_tbl('Åtgärder och vad de brukar ge',
      ['Åtgärd', 'Effekt', 'Risk eller nackdel'],
      [['Rätta körsträckan till den verkliga', 'Stor om du överskattat',
        'Kör du mer än angivet kan ersättningen sänkas'],
       ['Se till att alla skadefria år är registrerade', 'Stor',
        'Ingen — men kräver intyg från förra bolaget'],
       ['Höj självrisken', 'Måttlig till stor',
        'Du betalar mer själv vid skada — räkna på mellanskillnaden'],
       ['Betala helår i stället för månad', 'Liten',
        'Hela beloppet dras på en gång'],
       ['Stryk tillägg du redan har på annat håll', 'Liten till måttlig',
        'Kontrollera först att du verkligen har skyddet någon annanstans']],
      swipe=False)}

<h2>Bolagen på marknaden</h2>
<p>Priset är bara ena halvan. Den andra är hur bolaget faktiskt beter sig när du väl behöver
det. Konsumenternas Försäkringsbyrå betygsätter villkorens innehåll på en skala från 1 till 5,
och Svenskt Kvalitetsindex mäter kundnöjdheten. Ett lågt pris hos ett bolag med svaga villkor
är ingen besparing.</p>
{bolagstabell()}
{TODO}
<p>Läs mer om enskilda bolag på våra <a href="/forsakringsbolag/">bolagssidor</a>, eller se
vad försäkringen kostar för just ditt märke bland våra <a href="/bilmarken/">bilmärken</a>.</p>

<h2>När det billigaste priset inte är billigast</h2>
<p>Två offerter går bara att jämföra om de innehåller samma sak. Den vanligaste fällan är att
det billigare priset gäller en högre självrisk, en kortare hyrbilsperiod eller en försäkring
utan maskinskada. Kontrollera fyra saker innan du väljer, och gör det på samma sätt i alla
offerter — hur du gör det steg för steg står i vår guide till
<a href="/jamfor-bilforsakring/">hur du jämför bilförsäkring</a>.</p>
{_tbl('Jämför alltid på samma villkor',
      ['Post', 'Att kontrollera'],
      [['Självrisk', 'Grundsjälvrisk, glassjälvrisk och eventuell ungdomssjälvrisk'],
       ['Hyrbil', 'Ingår den, och i hur många dagar?'],
       ['Maskinskada', 'Ingår den, och till vilken ålder och körsträcka?'],
       ['Verkstadsval', 'Får du välja verkstad fritt eller styr bolaget dig?']],
      swipe=False)}

<div class="grid">
<a class="gc" href="/bilforsakring-ung-forare/"><span class="gc-t">Ung förare</span>
<span class="gc-d">Under 25 år är premien som högst. Så sänker du den utan att riskera ersättningen.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/bilforsakring-pensionar/"><span class="gc-t">Pensionär</span>
<span class="gc-d">Körsträckan är den största hävstången när bilen används mindre.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/bilforsakring-elbil/"><span class="gc-t">Elbil</span>
<span class="gc-d">Batteri, laddkabel och bärgning — det som skiljer mot en bensinbil.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
</div>

<div class="cta"><h2>Se ditt eget pris</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om billig bilförsäkring',
 'faq': [
   ('Vilket bolag har billigast bilförsäkring?',
    'Det går inte att svara generellt, eftersom varje bolag räknar fram premien ur din bil, '
    'din ålder, ditt postnummer och din körsträcka med sin egen modell. Ett bolag som är '
    'billigast för en 25-åring i Malmö kan vara dyrast för en 60-åring i Umeå.'),
   ('Är det farligt att välja den billigaste bilförsäkringen?',
    'Nej, förutsatt att du jämfört samma innehåll. Kontrollera självrisk, hyrbilsdagar, '
    'maskinskada och verkstadsval innan du väljer — det är där de billiga offerterna oftast '
    'skiljer sig från de dyrare.'),
   ('Hur mycket sparar jag på att höja självrisken?',
    'Det varierar mellan bolagen. Räkna alltid på mellanskillnaden: om premien sjunker mindre '
    'än vad självrisken höjs, lönar det sig först om du är skadefri i flera år.'),
   ('Blir det billigare om jag betalar hela året på en gång?',
    'Oftast ja. Månadsbetalning innehåller normalt ett påslag som täcker administration och '
    'kreditrisk. Skillnaden är sällan stor, men den är enkel att ta.'),
   ('Kan jag byta till ett billigare bolag mitt under året?',
    'Normalt byter du vid huvudförfallodagen med en månads uppsägningstid. Du får dock byta '
    'direkt vid bilköp, ägarbyte eller om bolaget höjer premien under avtalstiden.'),
 ],
 'rel': [('/jamfor-bilforsakring/', 'Så jämför du offerter rätt'),
         ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
         ('/helforsakring/', 'Helförsäkring — när behövs den?'),
         ('/forsakringsbolag/', 'Alla försäkringsbolag'),
         ('/redaktionell-metod/', 'Så samlar vi in priserna')],
},

# ═══ ELBIL ═════════════════════════════════════════════════════════
{
 'slug': 'bilforsakring-elbil', 'key': True,
 'title': 'Bilförsäkring elbil 2026 — pris, batteriskydd och villkor',
 'desc': 'Vad kostar det att försäkra en elbil? Se vad batteriskyddet omfattar, '
         'vad som gäller för laddkabel och laddbox och hur premien skiljer sig mot bensin.',
 'eyebrow': 'Guide',
 'h1': 'Bilförsäkring för elbil',
 'lead': 'En elbil försäkras enligt samma tre nivåer som alla andra bilar, men tre saker '
         'skiljer: batteriet utgör en stor del av bilens värde, högvoltssystemet kräver '
         'certifierad verkstad, och bärgningen är mer komplicerad. Det är där villkoren '
         'behöver läsas extra noga.',
 'checks': ['Batteriet är ofta en tredjedel av bilens värde',
            'Laddkabel och laddbox täcks inte alltid av bilförsäkringen',
            'Högvoltssystem får bara repareras av certifierad verkstad'],
 'card_t': 'Se vad din elbil kostar att försäkra',
 'sticky': 'Jämför försäkring till din elbil',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Elbilar har historiskt legat högre i premie
än jämnstora bensinbilar, framför allt för att reparationerna är dyrare och verkstäderna
färre. Skillnaden krymper i takt med att volymerna växer, men den finns kvar — och den är
störst på märken med tunt verkstadsnät.</p></div>

<h2>Vad som skiljer en elbil från en bensinbil</h2>
{_tbl('Premiedrivande skillnader',
      ['Faktor', 'Elbil', 'Bensin- eller dieselbil'],
      [['Andel av värdet i en enskild komponent', 'Batteriet, ofta runt en tredjedel',
        'Ingen enskild komponent dominerar'],
       ['Verkstadsnät', 'Begränsat — kräver högvoltsbehörighet', 'I princip varje verkstad'],
       ['Bärgning', 'Kräver ofta bärgning på flak', 'Kan oftast bogseras'],
       ['Nypris i samma storleksklass', 'Högre', 'Lägre'],
       ['Vikt', 'Högre — större skada vid kollision', 'Lägre'],
       ['Skadestatistik', 'Yngre bestånd, tunnare underlag', 'Väldokumenterad']],
      swipe=False)}

<h2>Vägledande premie för elbil</h2>
{_tbl('Elbil — årspremie per nivå',
      ['Nivå', 'Per år', 'Per månad'],
      [['<a href="/trafikforsakring/">Trafikförsäkring</a>', '—', '—'],
       ['<a href="/halvforsakring/">Halvförsäkring</a>', '—', '—'],
       ['<a href="/helforsakring/">Helförsäkring</a>', '—', '—']],
      swipe=False)}
{TODO}{METOD}

<h2>Batteri, kabel och laddbox — vad täcks var?</h2>
<p>Den här tabellen är anledningen till att elbilsägare bör läsa villkoren i stället för att
utgå från att allt ingår. Gränsdragningen mellan bilförsäkring och hemförsäkring är den
vanligaste källan till besvikelse vid en skada.</p>
{_tbl('Vad som normalt hör till vilken försäkring',
      ['Utrustning', 'Hör oftast till', 'Att kontrollera i villkoren'],
      [['Drivbatteriet', 'Bilförsäkringen',
        'Om skador utanför garantin omfattas, och om kapacitetsförlust räknas som skada'],
       ['Laddkabel som följer bilen', 'Bilförsäkringen',
        'Om stöld av kabel ersätts och med vilken självrisk'],
       ['Fast laddbox på väggen', 'Villa- eller hemförsäkringen',
        'Om beloppet räcker och om installationen är fackmannamässig'],
       ['Brand som uppstår vid laddning', 'Beror på var branden startar',
        'Hur bolaget bedömer skador i garage under laddning'],
       ['Programvara och uppkopplade tjänster', 'Sällan någon av dem',
        'Om bolaget ersätter felaktig programuppdatering']],
      swipe=False)}

<h2>Elbilsmodeller och deras märkessidor</h2>
<p>Premien styrs mer av märke och modell än av drivlinan i sig. Här är de vanligaste
elbilsmärkena på svenska vägar med länk till respektive märkessida.</p>
{_tbl('Vanliga elbilar i Sverige',
      ['Märke', 'Exempel på modeller', 'Halvförsäkring', 'Helförsäkring'],
      [['<a href="/bilmarken/tesla/">Tesla</a>', 'Model 3, Model Y', '—', '—'],
       ['<a href="/bilmarken/volvo/">Volvo</a>', 'EX30, EX40', '—', '—'],
       ['<a href="/bilmarken/polestar/">Polestar</a>', 'Polestar 2, Polestar 4', '—', '—'],
       ['<a href="/bilmarken/volkswagen/">Volkswagen</a>', 'ID.3, ID.4', '—', '—'],
       ['<a href="/bilmarken/kia/">Kia</a>', 'EV6, Niro, EV9', '—', '—'],
       ['<a href="/bilmarken/hyundai/">Hyundai</a>', 'IONIQ 5, IONIQ 6', '—', '—'],
       ['<a href="/bilmarken/byd/">BYD</a>', 'Atto 3, Dolphin, Seal', '—', '—'],
       ['<a href="/bilmarken/mg/">MG</a>', 'MG4, ZS EV', '—', '—'],
       ['<a href="/bilmarken/xpeng/">XPeng</a>', 'G6, G9, P7', '—', '—'],
       ['<a href="/bilmarken/zeekr/">Zeekr</a>', 'X, 001, 7X', '—', '—']])}
{TODO}

<h2>Fyra frågor att ställa till bolaget</h2>
{_tbl('Checklista före tecknandet',
      ['Fråga', 'Varför den är viktig'],
      [['Omfattas batteriet av vagnskadedelen?',
        'Batteriet är den dyraste komponenten — undantag får stora konsekvenser'],
       ['Ersätts stulen laddkabel, och med vilken självrisk?',
        'Kabelstölder är vanliga och självrisken kan äta upp hela ersättningen'],
       ['Vilken verkstad hänvisas jag till?',
        'Högvoltsarbete kräver certifiering, vilket kan innebära längre transport'],
       ['Hur många dagar hyrbil ingår?',
        'Väntetid på delar till elbilar är ofta längre än på förbränningsbilar']],
      swipe=False)}

<div class="cta"><h2>Se vad din elbil kostar</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om elbilsförsäkring',
 'faq': [
   ('Är elbil dyrare att försäkra än bensinbil?',
    'Oftast något dyrare i samma storleksklass. Skälen är högre nypris, dyrare reparationer '
    'och ett smalare verkstadsnät. Skillnaden krymper i takt med att beståndet växer och '
    'skadestatistiken blir bättre underbyggd.'),
   ('Ingår batteriet i försäkringen?',
    'Batteriet omfattas normalt av samma skydd som resten av bilen, men villkoren skiljer sig '
    'mellan bolagen. Läs särskilt hur kapacitetsförlust behandlas — den räknas ofta som '
    'slitage och inte som skada, och hanteras då av garantin i stället.'),
   ('Täcks laddboxen av bilförsäkringen?',
    'Nej, en fast monterad laddbox hör normalt till villa- eller hemförsäkringen eftersom den '
    'sitter på fastigheten. Laddkabeln som följer med bilen hör däremot oftast till '
    'bilförsäkringen.'),
   ('Behöver jag helförsäkring till en ny elbil?',
    'Nya bilar har ofta vagnskadegaranti från tillverkaren i tre år. Under den tiden räcker '
    'halvförsäkring, eftersom garantin täcker det som annars är vagnskadedelen. Kontrollera '
    'alltid hur länge garantin gäller för just din bil.'),
   ('Kan vilken verkstad som helst laga min elbil?',
    'Nej. Arbete på högvoltssystemet kräver särskild behörighet, vilket gör att fritt '
    'verkstadsval är värt mindre på en elbil än på en bensinbil.'),
 ],
 'rel': [('/helforsakring/', 'Helförsäkring — när behövs den?'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/leasingbil-forsakring/', 'Försäkring på leasingbil'),
         ('/bilmarken/', 'Alla bilmärken'),
         ('/jamfor-bilforsakring/', 'Så jämför du offerter')],
},

# ═══ LEASING ═══════════════════════════════════════════════════════
{
 'slug': 'leasingbil-forsakring', 'key': True,
 'title': 'Försäkring på leasingbil 2026 — krav, självrisk och vagnskadegaranti',
 'desc': 'Vad krävs av försäkringen när du privatleasar? Se vem som äger bilen, '
         'varför helförsäkring nästan alltid krävs och när vagnskadegarantin räcker.',
 'eyebrow': 'Guide',
 'h1': 'Bilförsäkring vid leasing',
 'lead': 'Vid privatleasing äger du inte bilen — leasinggivaren gör det. Det förändrar både '
         'vilken nivå du måste teckna och vem som får ersättningen vid en skada. '
         'Leasingavtalet går före dina egna preferenser, och det är avtalet du ska läsa först.',
 'checks': ['Leasinggivaren äger bilen och ställer kraven på försäkringen',
            'Helförsäkring krävs normalt under hela avtalstiden',
            'Slitage och returskador regleras i avtalet, inte i försäkringen'],
 'card_t': 'Se vad försäkringen kostar på din leasingbil',
 'sticky': 'Jämför försäkring till leasingbilen',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Ingår försäkringen i leasingavtalet behöver du
inte göra något — men kontrollera vad som faktiskt ingår. Ingår den inte, ska du teckna den
nivå avtalet kräver, vilket i praktiken alltid är helförsäkring. Tecknar du en lägre nivå
bryter du mot avtalet.</p></div>

<h2>Leasingbil eller egen bil — vad skiljer?</h2>
{_tbl('Skillnaderna som påverkar försäkringen',
      ['Fråga', 'Privatleasing', 'Egen bil'],
      [['Vem äger bilen?', 'Leasinggivaren', 'Du'],
       ['Vem tecknar försäkringen?', 'Du, om den inte ingår i avtalet', 'Du'],
       ['Vem får ersättningen vid totalskada?', 'Leasinggivaren som ägare', 'Du'],
       ['Vilken nivå krävs?', 'Helförsäkring, enligt avtalet', 'Du väljer fritt'],
       ['Vem bestämmer självrisken?', 'Ofta avtalet', 'Du'],
       ['Vem väljer verkstad?', 'Ofta avtalet — märkesverkstad', 'Du, om villkoren tillåter']],
      swipe=False)}

<h2>Vagnskadegaranti eller vagnskadeförsäkring?</h2>
<p>Nya bilar säljs normalt med vagnskadegaranti från tillverkaren, oftast i tre år. Den täcker
samma sak som vagnskadedelen i en helförsäkring. Under garantitiden räcker det därför i regel
med halvförsäkring — men bara om leasingavtalet accepterar det, och det gör inte alla.</p>
{_tbl('De två sätten att få vagnskadeskydd',
      ['', 'Vagnskadegaranti', 'Vagnskadeförsäkring'],
      [['Vem står bakom?', 'Biltillverkaren', 'Ditt försäkringsbolag'],
       ['Hur länge gäller den?', 'Oftast tre år från första registrering', 'Så länge du betalar premien'],
       ['Var repareras bilen?', 'Märkesverkstad', 'Enligt villkoren i din försäkring'],
       ['Ingår i halvförsäkring?', 'Ja, som komplement', 'Nej — kräver helförsäkring'],
       ['Vad händer när den går ut?', 'Du behöver uppgradera till helförsäkring', 'Inget — skyddet fortsätter']],
      swipe=False)}

<h2>Vad avtalet kan kräva av din försäkring</h2>
<p>Gå igenom leasingavtalet innan du begär offert. Kraven nedan är de vanligaste, och flera av
dem påverkar priset direkt — vilket gör att den billigaste offerten på marknaden inte
nödvändigtvis är giltig för dig.</p>
{_tbl('Vanliga krav i leasingavtal',
      ['Krav', 'Vad det innebär för offerten'],
      [['Helförsäkring under hela avtalstiden', 'Du kan inte välja halv för att sänka priset'],
       ['Högsta tillåtna självrisk', 'Du kan inte höja självrisken hur långt som helst'],
       ['Reparation på märkesverkstad', 'Bolag med styrt verkstadsval kan bli problematiska'],
       ['Leasinggivaren noteras på försäkringen', 'Anges vid tecknandet — glöms ofta bort'],
       ['Krav på godkänt stöldskydd', 'Kan gälla särskilt eftertraktade modeller']],
      swipe=False)}

<h2>Vägledande premie på leasad bil</h2>
<p>Priset sätts på bilen och på dig som förare, precis som vanligt. Att bilen är leasad gör
den varken dyrare eller billigare i sig — men kravet på helförsäkring gör att du landar på
den dyraste nivån.</p>
{_tbl('Leasingbil — årspremie per nivå',
      ['Nivå', 'Per år', 'Per månad', 'Tillåten vid leasing?'],
      [['<a href="/trafikforsakring/">Trafikförsäkring</a>', '—', '—', 'Nej'],
       ['<a href="/halvforsakring/">Halvförsäkring</a>', '—', '—', 'Endast med vagnskadegaranti'],
       ['<a href="/helforsakring/">Helförsäkring</a>', '—', '—', 'Ja']])}
{TODO}{METOD}

<h2>Det försäkringen inte löser</h2>
<p>Vid återlämningen bedöms bilens skick mot avtalets slitagenorm. Repor, däckslitage och
saknad utrustning debiteras enligt avtalet och är inte försäkringsskador. En helförsäkring
skyddar dig alltså inte mot en returräkning — läs slitagebilagan innan du lämnar tillbaka bilen.</p>

<div class="cta"><h2>Se priset på din leasingbil</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om försäkring vid leasing',
 'faq': [
   ('Måste jag ha helförsäkring på en leasingbil?',
    'I princip alltid. Leasinggivaren äger bilen och kräver därför fullt skydd i avtalet. '
    'Undantaget är om bilen har vagnskadegaranti och avtalet uttryckligen accepterar '
    'halvförsäkring under garantitiden.'),
   ('Ingår försäkringen i privatleasingavtalet?',
    'Ibland. Vissa upplägg är helt paketerade med försäkring och service, andra lämnar '
    'försäkringen till dig. Står det inte tydligt i avtalet ska du fråga leasinggivaren '
    'innan bilen levereras.'),
   ('Vem får pengarna om leasingbilen totalskadas?',
    'Leasinggivaren, eftersom det är den som äger bilen. Din del regleras sedan enligt '
    'leasingavtalet, och det är också där du ser om du blir skyldig något mellanbelopp.'),
   ('Kan jag välja vilket försäkringsbolag jag vill?',
    'Normalt ja, så länge försäkringen uppfyller avtalets krav på nivå, självrisk och '
    'eventuellt verkstadsval. Kontrollera kraven innan du jämför offerter.'),
   ('Täcker försäkringen slitage vid återlämning?',
    'Nej. Slitage och returskador bedöms mot leasingavtalets norm och debiteras separat. '
    'Försäkringen täcker skador, inte normalt bruk.'),
 ],
 'rel': [('/helforsakring/', 'Helförsäkring — vad ingår?'),
         ('/halvforsakring/', 'Halvförsäkring — när räcker den?'),
         ('/bilforsakring-elbil/', 'Bilförsäkring för elbil'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/jamfor-bilforsakring/', 'Så jämför du offerter')],
},

# ═══ PENSIONÄR ═════════════════════════════════════════════════════
{
 'slug': 'bilforsakring-pensionar', 'key': True,
 'title': 'Bilförsäkring för pensionär 2026 — så sänker du premien',
 'desc': 'Bilförsäkring som pensionär: körsträckan är den största hävstången. '
         'Se vad som ändras när bilen används mindre och vilka tillägg som kan strykas.',
 'eyebrow': 'Guide',
 'h1': 'Bilförsäkring för pensionär',
 'lead': 'Pensioneringen förändrar sällan bilen, men nästan alltid hur den används. '
         'Pendlingen försvinner, körsträckan sjunker och bilen står oftare hemma — tre '
         'faktorer som alla drar premien nedåt. Problemet är att försäkringen inte justeras '
         'automatiskt. Du måste själv meddela ändringen.',
 'checks': ['Körsträckan är den enskilt största hävstången',
            'Många kör kvar på uppgifter från tiden som yrkesverksam',
            'Långa skadefria perioder har full effekt först när de är registrerade'],
 'card_t': 'Se vad din bil kostar att försäkra',
 'sticky': 'Jämför bilförsäkring som pensionär',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Den vanligaste dyra vanan bland nyblivna
pensionärer är att försäkringen fortfarande utgår från 2 000 mil om året, trots att bilen
numera går halva den sträckan. Ring bolaget och ändra — det är en av få åtgärder som sänker
premien utan att försämra skyddet.</p></div>

<h2>Vad som ändras vid pensioneringen</h2>
{_tbl('Förändringar som påverkar premien',
      ['Förändring', 'Effekt på premien', 'Måste du meddela bolaget?'],
      [['Kortare årlig körsträcka', 'Sänker', 'Ja — annars gäller gamla uppgifter'],
       ['Bilen står hemma dagtid i stället för på arbetsplatsen', 'Kan sänka', 'Ja, om parkering ändrats'],
       ['Fler skadefria år i rad', 'Sänker', 'Nej, men kontrollera att de registrerats'],
       ['Byte till mindre eller äldre bil', 'Sänker', 'Ja, vid ägarbyte'],
       ['Flytt till mindre ort', 'Sänker ofta', 'Ja, adress styr premien'],
       ['Make eller maka blir andra förare', 'Neutral till sänkande', 'Ja, ange rätt huvudsaklig förare']],
      swipe=False)}

<h2>Körsträckan — den största enskilda hävstången</h2>
<p>Körsträckan anges i intervall, och priset ändras i steg mellan intervallen. Ligger du
strax över en gräns kan en ärlig justering nedåt ge en tydlig sänkning. Ange aldrig lägre än
du faktiskt kör: överskrider du intervallet kan ersättningen sänkas vid en skada.</p>
{_tbl('Körsträckeintervall och premie',
      ['Intervall per år', 'Typisk förarprofil', 'Årspremie'],
      [['Upp till 1 000 mil', 'Bilen används mest lokalt', '—'],
       ['1 000–1 500 mil', 'Regelbundna resor, ingen pendling', '—'],
       ['1 500–2 000 mil', 'Motsvarar en normal pendlarprofil', '—'],
       ['Över 2 000 mil', 'Långa resor eller flera förare', '—']],
      swipe=False)}
{TODO}{METOD}

<h2>Skyddsnivå när bilen blir äldre</h2>
<p>Många behåller helförsäkringen långt efter att den slutat löna sig. Vagnskadedelen ersätter
bilens marknadsvärde, och på en bil som är värd 30 000 kronor med 4 000 kronor i självrisk är
det utrymmet litet. Det är just den avvägningen som avgör om
<a href="/halvforsakring/">halvförsäkring</a> räcker.</p>
{_tbl('Vilken nivå passar bilens värde?',
      ['Bilens marknadsvärde', 'Rimlig nivå', 'Motivering'],
      [['Under 25 000 kr', 'Trafik eller halv',
        'Vagnskadedelen kostar mer än den kan betala ut'],
       ['25 000–75 000 kr', 'Halvförsäkring',
        'Stöld, brand och glas är kvar — vagnskada blir tveksam'],
       ['Över 75 000 kr', 'Helförsäkring',
        'Vagnskadedelen har verkligt värde vid en egenvållad skada']],
      swipe=False)}

<h2>Tillägg som ofta kan strykas — och ett som sällan bör det</h2>
{_tbl('Genomgång av tilläggen',
      ['Tillägg', 'Vanlig bedömning'],
      [['Hyrbil', 'Behåll om bilen behövs dagligen, annars kan den ofta strykas'],
       ['Utökad rättsskydd', 'Kontrollera om du redan har rättsskydd i hemförsäkringen'],
       ['Assistans och bärgning', 'Behåll — värdet stiger med bilens ålder'],
       ['Maskinskada', 'Upphör ofta av sig själv vid en viss ålder eller körsträcka'],
       ['Djurkollision med låg självrisk', 'Behåll om du kör på landsväg i viltrika områden']],
      swipe=False)}

<p>Går du igenom listan tillsammans med din nuvarande försäkring hittar du oftast ett eller
två tillägg du betalar dubbelt för. Jämför sedan resultatet mot marknaden — så gör du det
<a href="/jamfor-bilforsakring/">steg för steg</a>, och de generella prisfaktorerna hittar
du på sidan om <a href="/billigaste-bilforsakringen/">billigaste bilförsäkringen</a>.</p>

<div class="cta"><h2>Se ditt pris med rätt körsträcka</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om bilförsäkring för pensionärer',
 'faq': [
   ('Blir bilförsäkringen billigare när man går i pension?',
    'Inte automatiskt. Premien sjunker först när bolaget känner till att körsträckan minskat, '
    'och den uppgiften måste du lämna själv. Många betalar i flera år för en körsträcka de '
    'inte längre har.'),
   ('Finns det pensionärsrabatt på bilförsäkring?',
    'Enskilda bolag och medlemsorganisationer förhandlar ibland fram rabatter för äldre eller '
    'för medlemmar. Kontrollera vad din organisation erbjuder, men jämför alltid rabatten mot '
    'marknadspriset — en rabatt på ett högt grundpris kan fortfarande vara dyr.'),
   ('Blir premien högre igen när man blir riktigt gammal?',
    'Premien sjunker med åldern under större delen av vuxenlivet och planar sedan ut. Hos '
    'vissa bolag stiger den något i de högsta åldersgrupperna. Det är ett skäl att jämföra om '
    'igen efter att du fyllt 75.'),
   ('Ska jag behålla helförsäkringen på en äldre bil?',
    'Räkna på det. Vagnskadedelen ersätter marknadsvärdet minus självrisken, så på en bil värd '
    'under 25 000 kronor är utrymmet litet. Halvförsäkring behåller ändå stöld, brand, glas '
    'och räddning.'),
   ('Vad händer om jag kör längre än den angivna körsträckan?',
    'Bolaget kan sätta ned ersättningen vid en skada, eftersom premien beräknats på fel '
    'underlag. Ändra hellre uppgiften i förväg — det kostar mindre än en nedsatt ersättning.'),
 ],
 'rel': [('/halvforsakring/', 'Halvförsäkring — räcker den?'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/jamfor-bilforsakring/', 'Så jämför du offerter'),
         ('/helforsakring/', 'Helförsäkring — när behövs den?'),
         ('/forsakringsbolag/', 'Alla försäkringsbolag')],
},

# ═══ UNG FÖRARE ════════════════════════════════════════════════════
{
 'slug': 'bilforsakring-ung-forare', 'key': True,
 'title': 'Bilförsäkring för unga 2026 — pris under 25 och ungdomssjälvrisk',
 'desc': 'Varför är bilförsäkring så dyr för unga? Se hur premien faller med åldern, '
         'vad ungdomssjälvrisk innebär och vilka genvägar som kan kosta dig ersättningen.',
 'eyebrow': 'Guide',
 'h1': 'Bilförsäkring för unga förare',
 'lead': 'Under 25 år är premien som högst, och det beror inte på hur du kör utan på hur '
         'gruppen kör. Statistiskt är unga förare inblandade i fler och dyrare skador, och '
         'eftersom du saknar skadefria år finns det ingenting som väger upp det ännu.',
 'checks': ['Premien faller tydligt vid 25 och igen runt 30',
            'Ungdomssjälvrisk kan tillkomma om föraren är under 24',
            'Att registrera fel ägare kan sänka ersättningen vid skada'],
 'card_t': 'Se vad din bil kostar att försäkra',
 'sticky': 'Jämför bilförsäkring för unga',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Det finns inga trick som gör ung förare
billig. Det finns däremot fyra lagliga åtgärder som fungerar, och en genväg — att låta en
förälder stå som ägare på en bil du själv kör dagligen — som kan leda till nedsatt ersättning
just när du behöver försäkringen.</p></div>

<h2>Hur premien faller med åldern</h2>
{_tbl('Åldersintervall och premie',
      ['Ålder', 'Relativ premienivå', 'Vad som förändras', 'Årspremie'],
      [['18–20 år', 'Högst', 'Ingen bonus, ingen körhistorik', '—'],
       ['21–24 år', 'Mycket hög', 'Första skadefria åren börjar räknas', '—'],
       ['25–29 år', 'Tydligt lägre', 'Åldersgränsen för ungdomssjälvrisk passerad', '—'],
       ['30 år och uppåt', 'Normal', 'Bonusen börjar väga tungt', '—']])}
{TODO}{METOD}

<h2>Ungdomssjälvrisk — det som inte syns i priset</h2>
<p>Flera bolag lägger på en extra självrisk om föraren vid skadetillfället är under en viss
ålder, ofta 24 år. Den syns inte i årspremien och dyker upp först vid skadan. Två offerter
med samma pris kan därför skilja med tusenlappar i praktiken.</p>
{_tbl('Att kontrollera i villkoren',
      ['Post', 'Fråga att ställa'],
      [['Ungdomssjälvrisk', 'Vid vilken ålder tillkommer den, och med vilket belopp?'],
       ['Gäller den alla förare?', 'Även när bilen lånas ut till en yngre kompis?'],
       ['Kan den försvinna?', 'Bortfaller den efter ett visst antal skadefria år?'],
       ['Gäller den alla skadetyper?', 'Eller bara vagnskada?']],
      swipe=False)}

<h2>Fyra åtgärder som faktiskt sänker priset</h2>
{_tbl('Vad som fungerar för unga förare',
      ['Åtgärd', 'Effekt', 'Att tänka på'],
      [['Välj en billigare och svagare bil', 'Mycket stor',
        'Bilmodellen väger tyngst av allt när du saknar bonus'],
       ['Ange rätt och låg körsträcka', 'Stor',
        'Måste stämma — överskriden sträcka kan sänka ersättningen'],
       ['Börja på trafik eller halv på en billig bil', 'Stor',
        'Helförsäkring är sällan motiverad på en bil värd några tiotusen'],
       ['Höj självrisken medvetet', 'Måttlig',
        'Kräver att du har pengarna tillgängliga om det smäller']],
      swipe=False)}
<p>Vilken nivå som passar beror på bilens värde. Är bilen värd mindre än självrisken plus
några tiotusen kronor är <a href="/halvforsakring/">halvförsäkring</a> nästan alltid
rätt val — <a href="/helforsakring/">helförsäkring</a> blir intressant först på en nyare bil.</p>

<h2>Genvägen som kostar</h2>
<p>Att registrera bilen på en förälder med lång bonus sänker premien på papperet. Men
försäkringen bygger på att uppgiften om vem som är huvudsaklig brukare stämmer. Är det du som
kör bilen dagligen är uppgiften felaktig, och bolaget kan sätta ned ersättningen eller neka
den helt vid en skada. Bonusen är dessutom personlig och byggs upp åt den som står på
försäkringen — inte åt dig.</p>
{_tbl('Rätt och fel sätt att dela bil med föräldrarna',
      ['Situation', 'Bedömning'],
      [['Föräldern äger och kör bilen, du lånar den ibland', 'Korrekt — ange dig som ytterligare förare'],
       ['Du kör bilen dagligen, föräldern står som ägare', 'Felaktig uppgift — risk för nedsatt ersättning'],
       ['Ni delar bilen ungefär lika', 'Ange den som kör mest som huvudsaklig brukare'],
       ['Du köper bilen med lån från föräldern', 'Du står som ägare och bygger egen bonus']],
      swipe=False)}

<p>När du har fått ordning på bilval och nivå är nästa steg att jämföra offerter på samma
villkor. De generella prisfaktorerna hittar du på sidan om
<a href="/billigaste-bilforsakringen/">billigaste bilförsäkringen</a>, och en genomgång av
bolagen finns bland våra <a href="/forsakringsbolag/">försäkringsbolag</a>.</p>

<div class="cta"><h2>Se ditt pris som ung förare</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om bilförsäkring för unga',
 'faq': [
   ('Varför är bilförsäkring så dyr för unga?',
    'Premien bygger på statistik för hela åldersgruppen, inte på dig personligen. Unga förare '
    'är inblandade i fler och dyrare skador, och utan skadefria år finns det ännu ingenting '
    'som väger upp den bilden.'),
   ('När blir bilförsäkringen billigare?',
    'Det största enskilda steget kommer vid 25 år, när ungdomssjälvrisken faller bort hos de '
    'flesta bolag. Därefter sjunker premien successivt i takt med att de skadefria åren '
    'byggs upp.'),
   ('Vad är ungdomssjälvrisk?',
    'En extra självrisk som tillkommer om föraren vid skadetillfället är under en viss ålder, '
    'ofta 24 år. Den syns inte i årspremien utan först vid skadan, och den kan gälla även när '
    'du lånar ut bilen.'),
   ('Kan mina föräldrar stå på försäkringen för att sänka priset?',
    'Bara om de faktiskt är bilens huvudsakliga brukare. Kör du bilen dagligen är uppgiften '
    'felaktig, och bolaget kan sätta ned eller neka ersättning vid en skada. Du bygger '
    'dessutom ingen egen bonus.'),
   ('Behöver jag helförsäkring på min första bil?',
    'Sällan. Vagnskadedelen ersätter marknadsvärdet minus självrisken, och på en billig '
    'förstabil är det utrymmet litet. Halvförsäkring behåller stöld, brand, glas och räddning '
    'till en betydligt lägre premie.'),
 ],
 'rel': [('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
         ('/trafikforsakring/', 'Trafikförsäkring — lagkravet'),
         ('/jamfor-bilforsakring/', 'Så jämför du offerter'),
         ('/forsakringsbolag/', 'Alla försäkringsbolag')],
},
]
