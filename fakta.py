# -*- coding: utf-8 -*-
"""Faktasidor — de sökningar konkurrenterna svarar dåligt på.

Ingen av sidorna här kräver insamlade priser. De bygger på hur svensk
bilförsäkring fungerar och kan publiceras som de är. Självrisktabellen
fylls i från bolagens villkor, inte från offerter — den går alltså att
göra klar utan en enda offertförfrågan.

H2-strukturen är medvetet olika på varje sida. Ingen mall återanvänds.
"""
from companies import BOLAG
import data

SWIPE = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>'


def _t(caption, kol, rader, swipe=None):
    th = ''.join(f'<th scope="col">{k}</th>' for k in kol)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    s = SWIPE if (swipe if swipe is not None else len(kol) > 3) else ''
    return (f'<div class="tbl"><table><caption>{caption}</caption><thead><tr>{th}</tr>'
            f'</thead><tbody>{tr}</tbody></table></div>{s}')


def sjalvrisktabell():
    """Per bolag, direkt ur villkoren. Unik på den svenska marknaden."""
    rader = []
    for b in BOLAG:
        s = data.SJALVRISK.get(b['slug'], {})
        rader.append([f'<a href="/forsakringsbolag/{b["slug"]}/">{b["namn"]}</a>',
                      data.kr(s.get('trafik')), data.kr(s.get('vagn')),
                      data.kr(s.get('glas')), data.kr(s.get('stold')),
                      data.kr(s.get('maskin'))])
    return _t('Självrisk per skadetyp och bolag',
              ['Bolag', 'Trafik', 'Vagnskada', 'Glas', 'Stöld', 'Maskinskada'], rader)


SIDOR = [

# ═══ SJÄLVRISK ═════════════════════════════════════════════════════
{
 'slug': 'sjalvrisk', 'key': True,
 'title': 'Självrisk bilförsäkring — alla typer förklarade och jämförda',
 'desc': 'Grundsjälvrisk, glassjälvrisk, stöldsjälvrisk och ungdomssjälvrisk. '
         'Se vad varje typ innebär, vad den kostar och när det lönar sig att höja den.',
 'eyebrow': 'Faktasida',
 'h1': 'Självrisk på bilförsäkring',
 'lead': 'Självrisk är den del av skadan du betalar själv. Det som förvirrar är att en '
         'bilförsäkring inte har en självrisk utan fem till sju olika, en per skadetyp — '
         'och det är där två offerter med samma pris kan skilja med tusenlappar.',
 'checks': ['En självrisk per skadetyp, inte en för hela försäkringen',
            'Glas- och stöldsjälvrisk skiljer sig mest mellan bolagen',
            'Ungdomssjälvrisk syns inte i årspremien'],
 'card_t': 'Se pris på din självrisknivå',
 'sticky': 'Jämför självrisk mellan bolagen',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Höjd självrisk sänker premien, men bara om
mellanskillnaden går ihop. Räkna alltid: om premien sjunker 400 kronor om året när
självrisken höjs 2 000 kronor, tjänar du på det först efter fem skadefria år.</p></div>

<h2>De självrisker som finns i en bilförsäkring</h2>
{_t('Självrisktyper och när de gäller',
    ['Typ', 'Gäller vid', 'Ingår i'],
    [['Trafiksjälvrisk', 'Skador du orsakar på andra', 'Trafik, halv och hel'],
     ['Vagnskadesjälvrisk', 'Skador på din egen bil vid egen vållad olycka', 'Endast hel'],
     ['Glassjälvrisk', 'Stenskott och krossad ruta', 'Halv och hel'],
     ['Stöldsjälvrisk', 'Stöld av eller ur bilen', 'Halv och hel'],
     ['Brandsjälvrisk', 'Brand i eller på bilen', 'Halv och hel'],
     ['Maskinskadesjälvrisk', 'Fel på motor, växellåda eller styrsystem', 'Ofta halv och hel'],
     ['Räddningssjälvrisk', 'Bärgning och hemtransport', 'Halv och hel'],
     ['Ungdomssjälvrisk', 'Förare under en viss ålder, ofta 24 år', 'Läggs till övriga'],
     ['Djurkollisionssjälvrisk', 'Kollision med vilt', 'Ofta reducerad i halv och hel']],
    swipe=False)}

<h2>Reparation eller byte — skillnaden på glasrutan</h2>
<p>Glassjälvrisken är den som slår oftast till i praktiken. Nästan alla bolag har en låg
självrisk vid lagning av ett stenskott och en betydligt högre vid byte av hela rutan, just
för att styra dig mot lagning. Väntar du för länge spricker rutan, och då gäller den högre
självrisken. På bilar med förarassistans bakom vindrutan tillkommer dessutom kalibrering,
vilket är den verkliga kostnadsdrivaren på nyare bilar.</p>

<h2>Självrisk per bolag</h2>
<p>Beloppen står i respektive bolags villkor och gäller oavsett vilken bil du har. De är
alltså jämförbara rakt av — till skillnad från premien.</p>
{sjalvrisktabell()}
{data.saknas_ruta('självriskbeloppen')}
{data.kontrollerad()}

<h2>Lönar det sig att höja självrisken?</h2>
{_t('Räkneexempel på mellanskillnaden',
    ['Om premien sjunker', 'Och självrisken höjs', 'Går det ihop efter'],
    [['400 kr/år', '2 000 kr', 'Fem skadefria år'],
     ['800 kr/år', '2 000 kr', 'Två och ett halvt skadefritt år'],
     ['1 200 kr/år', '4 000 kr', 'Drygt tre skadefria år'],
     ['500 kr/år', '4 000 kr', 'Åtta skadefria år — sällan värt det']],
    swipe=False)}
<p>Tumregeln: höj självrisken bara om du har pengarna tillgängliga den dag det smäller, och
bara om mellanskillnaden går ihop inom tre år. Läs mer om
<a href="/billigaste-bilforsakringen/">vad mer som styr premien</a>.</p>

<div class="cta"><h2>Se ditt pris på olika självrisknivåer</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om självrisk',
 'faq': [
   ('Hur många självrisker har en bilförsäkring?',
    'Normalt fem till sju, en per skadetyp. Det finns alltså ingen enda självrisk som gäller '
    'hela försäkringen, vilket är den vanligaste missuppfattningen.'),
   ('Betalar jag flera självrisker vid samma skada?',
    'Ja, om skadan omfattar flera moment. Blir bilen stulen och återfinns skadad kan både '
    'stöld- och vagnskadesjälvrisk tas ut. Det står i villkoren hur bolaget hanterar det.'),
   ('Vad är ungdomssjälvrisk?',
    'En extra självrisk som läggs till de vanliga om föraren vid skadetillfället är under en '
    'viss ålder, ofta 24 år. Den syns inte i årspremien och gäller ofta även när du lånar '
    'ut bilen.'),
   ('Är det billigare att laga ett stenskott än att byta rutan?',
    'För dig ja, eftersom självrisken vid lagning normalt är betydligt lägre. Vänta inte — '
    'spricker skottet ut måste rutan bytas, och då gäller den högre självrisken.'),
   ('Kan jag ha noll i självrisk?',
    'På trafikdelen erbjuder vissa bolag noll. På vagnskada finns i praktiken alltid en '
    'självrisk. Låg självrisk innebär alltid högre premie.'),
 ],
 'rel': [('/helforsakring/', 'Helförsäkring — vad ingår?'),
         ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/bilforsakring-ung-forare/', 'Ung förare'),
         ('/jamfor-bilforsakring/', 'Så jämför du offerter')],
},

# ═══ BYTA ══════════════════════════════════════════════════════════
{
 'slug': 'byta-bilforsakring', 'key': True,
 'title': 'Byta bilförsäkring — huvudförfallodag, uppsägning och bonus',
 'desc': 'När får du byta bilförsäkring? Se reglerna för huvudförfallodag, '
         'uppsägningstid och hur du flyttar med dina skadefria år utan att tappa bonus.',
 'eyebrow': 'Faktasida',
 'h1': 'Byta bilförsäkring',
 'lead': 'Att byta bolag är gratis, tar tjugo minuter och är den enskilt största besparingen '
         'de flesta kan göra på sin bilförsäkring. Det som stoppar folk är osäkerhet om när '
         'man får byta — och rädslan för att stå oförsäkrad en dag i glappet.',
 'checks': ['Huvudförfallodagen är den vanliga bytespunkten',
            'Vid bilköp och ägarbyte får du byta direkt',
            'Skadefria år följer dig — men måste registreras'],
 'card_t': 'Se vad du kan spara på att byta',
 'sticky': 'Jämför innan du byter',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Säg aldrig upp den gamla försäkringen först.
Teckna den nya med startdatum, och låt den gamla löpa ut samma dag. Ett glapp på ett dygn
utan trafikförsäkring kostar mer i avgift än du sparat på hela bytet.</p></div>

<h2>När får du byta?</h2>
{_t('Bytestillfällen och vad som krävs',
    ['Situation', 'Får du byta?', 'Att tänka på'],
    [['Vid huvudförfallodagen', 'Ja', 'Normalt en månads uppsägningstid'],
     ['Du köper en ny bil', 'Ja, direkt', 'Gamla försäkringen upphör vid ägarbytet'],
     ['Du säljer bilen', 'Ja, automatiskt', 'Upphör när ägarbytet registrerats'],
     ['Bolaget höjer premien', 'Ja', 'Villkorsändring ger rätt att säga upp'],
     ['Du flyttar', 'Beror på bolaget', 'Adressen ska alltid uppdateras'],
     ['Mitt under avtalstiden utan skäl', 'Nej', 'Vänta till huvudförfallodagen']],
    swipe=False)}

<h2>Vad är huvudförfallodag?</h2>
<p>Det är den dag ditt försäkringsavtal förnyas, vanligtvis ett år efter att du tecknade det.
Den står på försäkringsbrevet och på fakturan. Uppsägningen ska normalt vara hos bolaget
senast en månad före den dagen — men i praktiken sköter det nya bolaget uppsägningen åt dig
när du tecknar. Fråga uttryckligen om de gör det.</p>

<h2>Bytet steg för steg</h2>
{_t('Sex steg, i den här ordningen',
    ['Steg', 'Vad du gör'],
    [['1. Ta fram nuvarande villkor', 'Notera självrisker, tillägg och körsträcka'],
     ['2. Begär offert på samma innehåll', 'Annars jämför du inte samma sak'],
     ['3. Kontrollera skadefria år', 'Be gamla bolaget om intyg'],
     ['4. Teckna den nya med startdatum', 'Samma dag som den gamla löper ut'],
     ['5. Låt nya bolaget säga upp den gamla', 'Eller gör det själv skriftligt'],
     ['6. Kontrollera första fakturan', 'Att bonusen faktiskt följt med']],
    swipe=False)}

<h2>Bonusen — det som oftast går fel</h2>
<p>Skadefria år är personliga och följer med dig mellan bolag, men de överförs inte
automatiskt. Det nya bolaget utgår från vad du uppger tills de fått intyg. Kontrollera
första fakturan: ligger premien högre än offerten är det nästan alltid bonusen som inte
registrerats. Läs mer om <a href="/bonus-och-skadefria-ar/">hur bonusen byggs upp</a>.</p>

<h2>Fyra myter om att byta</h2>
{_t('Vad som faktiskt gäller',
    ['Påstående', 'Stämmer det?'],
    [['Man förlorar bonusen när man byter', 'Nej — den följer dig, med intyg'],
     ['Lojala kunder får bäst pris', 'Sällan — nykundsrabatter går till nya kunder'],
     ['Det tar månader att byta', 'Nej — den nya försäkringen gäller från angivet datum'],
     ['Man måste ha kvar samma bolag på hem och bil', 'Nej — men samlingsrabatten försvinner']],
    swipe=False)}
{data.kontrollerad()}

<div class="cta"><h2>Se vad du betalar hos ett annat bolag</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om att byta bilförsäkring',
 'faq': [
   ('När kan jag byta bilförsäkring?',
    'Vid huvudförfallodagen med normalt en månads uppsägningstid. Du får också byta direkt '
    'vid bilköp, vid ägarbyte och om bolaget ändrar premien eller villkoren under '
    'avtalstiden.'),
   ('Förlorar jag mina skadefria år om jag byter bolag?',
    'Nej. Åren är personliga och följer med dig, men de överförs inte automatiskt. Be det '
    'gamla bolaget om intyg och kontrollera på första fakturan att de registrerats.'),
   ('Måste jag säga upp den gamla försäkringen själv?',
    'Oftast sköter det nya bolaget uppsägningen, men fråga uttryckligen. Säg aldrig upp den '
    'gamla innan den nya är tecknad — ett glapp utan trafikförsäkring blir dyrt.'),
   ('Vad händer med försäkringen när jag säljer bilen?',
    'Den upphör automatiskt när ägarbytet registrerats hos Transportstyrelsen. Du behöver '
    'inte säga upp den separat, men kontrollera att återbetalningen av den oanvända premien '
    'kommer.'),
   ('Kan bolaget neka mig att teckna?',
    'Ett bolag får neka i vissa fall, till exempel efter många skador. Trafikförsäkring '
    'måste dock alltid gå att få någonstans, eftersom den är lagstadgad.'),
 ],
 'rel': [('/jamfor-bilforsakring/', 'Så jämför du offerter'),
         ('/bonus-och-skadefria-ar/', 'Bonus och skadefria år'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/basta-bilforsakringen/', 'Bästa bilförsäkringen'),
         ('/trafikforsakringsavgift/', 'Trafikförsäkringsavgift')],
},

# ═══ BONUS ═════════════════════════════════════════════════════════
{
 'slug': 'bonus-och-skadefria-ar', 'key': True,
 'title': 'Skadefria år och bonus på bilförsäkring — så fungerar det',
 'desc': 'Hur många skadefria år behövs för full bonus? Se hur bonusen byggs upp, '
         'vad som händer vid en skada och hur du flyttar med den mellan bolag.',
 'eyebrow': 'Faktasida',
 'h1': 'Skadefria år och bonus',
 'lead': 'Skadefria år är den enda premiefaktor du bygger upp helt själv, och på lång sikt '
         'den som betyder mest. Den följer dig som person, inte bilen — och det är också '
         'därför den kan gå förlorad på sätt som förvånar många.',
 'checks': ['Bonusen är personlig och följer inte bilen',
            'Full effekt nås först efter flera år i rad',
            'En skada nollställer inte allt — men kostar år'],
 'card_t': 'Se ditt pris med rätt antal skadefria år',
 'sticky': 'Kontrollera att din bonus är registrerad',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Bonusen är personlig, byggs upp ett år i
taget och måste registreras hos varje nytt bolag med intyg. Den vanligaste förlusten sker
inte vid en skada, utan vid ett byte där ingen kom ihåg att skicka intyget.</p></div>

<h2>Så byggs bonusen upp</h2>
<p>Varje helt försäkringsår utan skada räknas som ett skadefritt år. Bolagen använder olika
skalor, men principen är densamma: premien sjunker stegvis tills du nått bolagets högsta
nivå, därefter ger fler år ingen ytterligare effekt.</p>
{_t('Bonusens utveckling',
    ['Antal skadefria år', 'Vad som händer med premien'],
    [['0 år', 'Högsta nivån — gäller nya förare och den som haft skador'],
     ['1–3 år', 'Tydlig sänkning för varje år'],
     ['4–6 år', 'Fortsatt sänkning, men i mindre steg'],
     ['7 år och uppåt', 'Nära eller på bolagets högsta nivå'],
     ['Efter en skada', 'Du tappar år enligt bolagets regler, inte alltid alla']],
    swipe=False)}

<h2>Vad som händer vid en skada</h2>
<p>Det är bara skador där bolaget betalar ut ersättning på din egen försäkring som påverkar
bonusen. Glasreparation, räddning och skador där en motpart är vållande gör det normalt inte.
Blir du påkörd bakifrån av någon annan, och den skadan regleras mot motpartens försäkring,
behåller du dina år.</p>
{_t('Påverkar skadan bonusen?',
    ['Händelse', 'Påverkar bonusen'],
    [['Du kör in i en stolpe, vagnskada betalas ut', 'Ja'],
     ['Du blir påkörd av en vållande motpart', 'Normalt nej'],
     ['Stenskott som lagas', 'Normalt nej'],
     ['Bilen stjäls', 'Beror på bolaget — fråga uttryckligen'],
     ['Viltolycka', 'Ofta nej, men kontrollera villkoren'],
     ['Skadegörelse av okänd person', 'Ofta ja, eftersom det regleras på vagnskada']],
    swipe=False)}

<h2>Bonus mellan personer och bolag</h2>
<p>Bonusen kan normalt flyttas mellan makar och sambor som varit försäkrade tillsammans, men
inte från förälder till barn. Det är därför genvägen att låta en förälder stå som ägare på
en ungdomsbil inte bygger något åt ungdomen — läs mer under
<a href="/bilforsakring-ung-forare/">bilförsäkring för unga</a>. Mellan bolag följer bonusen
alltid med, förutsatt att intyget skickas — se
<a href="/byta-bilforsakring/">hur du byter bolag</a>.</p>
{data.kontrollerad()}

<div class="cta"><h2>Se ditt pris med din bonus</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om skadefria år',
 'faq': [
   ('Hur många skadefria år behöver jag för full bonus?',
    'Det varierar mellan bolagen, men de flesta når högsta nivån efter ungefär sju år. '
    'Därefter ger fler skadefria år ingen ytterligare sänkning.'),
   ('Följer bonusen med bilen eller med mig?',
    'Med dig. Den är personlig, vilket betyder att du behåller den när du byter bil och att '
    'en köpare inte ärver din bonus när du säljer.'),
   ('Förlorar jag alla år vid en skada?',
    'Sällan alla. De flesta bolag drar av ett antal år enligt en fastställd regel. Hur många '
    'står i villkoren, och det är en av de saker som faktiskt är värd att jämföra.'),
   ('Kan jag flytta bonus från min make eller sambo?',
    'Ofta ja, om ni varit försäkrade tillsammans. Från förälder till barn går det normalt '
    'inte, eftersom bonusen är knuten till den som stått som försäkringstagare.'),
   ('Vad händer med bonusen om jag är utan bil ett tag?',
    'De flesta bolag låter bonusen ligga kvar en period, ofta något eller några år. Blir '
    'uppehållet längre kan den nollställas — fråga bolaget innan du säljer bilen.'),
 ],
 'rel': [('/byta-bilforsakring/', 'Byta bilförsäkring'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/bilforsakring-ung-forare/', 'Ung förare'),
         ('/sjalvrisk/', 'Självrisk förklarad'),
         ('/jamfor-bilforsakring/', 'Så jämför du offerter')],
},

# ═══ TRAFIKFÖRSÄKRINGSAVGIFT ═══════════════════════════════════════
{
 'slug': 'trafikforsakringsavgift', 'key': True,
 'title': 'Trafikförsäkringsavgift — vad den kostar och hur du slipper den',
 'desc': 'Kör du utan trafikförsäkring tar Trafikförsäkringsföreningen ut en avgift '
         'som är betydligt högre än premien. Se hur den räknas och hur du stoppar den.',
 'eyebrow': 'Faktasida',
 'h1': 'Trafikförsäkringsavgift',
 'lead': 'Trafikförsäkringsavgiften är inte en böter utan en avgift som '
         'Trafikförsäkringsföreningen tar ut för varje dag ett fordon står oförsäkrat. Den '
         'är medvetet satt högre än vad en försäkring kostar, och den löper vidare tills du '
         'antingen tecknar en försäkring eller ställer av bilen.',
 'checks': ['Avgiften räknas per dag, inte som ett engångsbelopp',
            'Den är avsiktligt högre än premien hos vilket bolag som helst',
            'Den stoppas bara av tecknad försäkring eller avställning'],
 'card_t': 'Teckna försäkring och stoppa avgiften',
 'sticky': 'Stoppa avgiften — teckna försäkring',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Har du fått ett krav ska du agera samma dag.
Avgiften löper per dygn och stoppas först den dag en försäkring börjar gälla eller bilen är
avställd hos Transportstyrelsen. Att bestrida kravet stoppar den inte.</p></div>

<h2>Varför avgiften finns</h2>
<p>Alla fordon som används i trafik i Sverige ska ha trafikförsäkring. Den som ändå kör
oförsäkrad skjuter över risken på alla andra, eftersom skador som oförsäkrade orsakar
ersätts av Trafikförsäkringsföreningen — som i sin tur finansieras av försäkringsbolagen och
därmed av alla andra bilägare. Avgiften är konstruerad så att det aldrig ska löna sig att
avstå från försäkring.</p>

<h2>Vad som utlöser avgiften</h2>
{_t('Situationer som ger avgift',
    ['Situation', 'Ger avgift?', 'Så undviker du den'],
    [['Bilen är påställd men oförsäkrad', 'Ja, per dag', 'Teckna försäkring eller ställ av'],
     ['Du har köpt bil men inte tecknat ännu', 'Ja, från ägarbytesdagen', 'Teckna samma dag'],
     ['Försäkringen sagts upp för utebliven betalning', 'Ja', 'Betala eller teckna nytt'],
     ['Bilen är avställd', 'Nej', 'Avställningen ska vara registrerad'],
     ['Bilen är avregistrerad', 'Nej', 'Kräver skrotningsintyg'],
     ['Glapp på några dagar vid byte av bolag', 'Ja, för de dagarna', 'Låt datumen överlappa']],
    swipe=False)}

<h2>Det vanligaste misstaget: bilköpet</h2>
<p>Försäkringsplikten börjar den dag du står som ägare, inte den dag du hämtar bilen.
Registreras ägarbytet på tisdagen och du tecknar försäkring på fredagen har det gått tre
avgiftsbelagda dygn. Teckna försäkringen innan eller samma dag som ägarbytet registreras —
det är gratis att ha den några timmar för tidigt.</p>

<h2>Om du fått ett krav</h2>
{_t('Vad du gör, i den här ordningen',
    ['Steg', 'Åtgärd'],
    [['1', 'Teckna försäkring eller ställ av bilen — samma dag'],
     ['2', 'Kontrollera vilka datum kravet avser'],
     ['3', 'Har du haft försäkring under perioden: skicka bevis till föreningen'],
     ['4', 'Är kravet riktigt: betala, avgiften växer inte när den väl stoppats'],
     ['5', 'Kontrollera hos Transportstyrelsen att fordonet står rätt registrerat']],
    swipe=False)}
<p>Ska bilen inte användas ett tag är avställning nästan alltid rätt lösning — läs vad som
gäller under <a href="/avstalld-bil/">avställd bil</a>. Ska den användas är
<a href="/trafikforsakring/">trafikförsäkring</a> det billigaste lagliga alternativet.</p>
{data.kontrollerad()}

<div class="cta"><h2>Teckna försäkring i dag</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om trafikförsäkringsavgift',
 'faq': [
   ('Vad är trafikförsäkringsavgift?',
    'En avgift som Trafikförsäkringsföreningen tar ut för varje dag ett påställt fordon '
    'saknar trafikförsäkring. Den är avsiktligt högre än vad en försäkring kostar.'),
   ('Är trafikförsäkringsavgift en böter?',
    'Nej, det är en civilrättslig avgift och inte en påföljd från polis eller domstol. Den '
    'kan drivas in på vanligt sätt om den inte betalas.'),
   ('Hur stoppar jag avgiften?',
    'Genom att teckna trafikförsäkring eller ställa av fordonet hos Transportstyrelsen. '
    'Avgiften löper till och med dagen innan något av det sker.'),
   ('Måste jag betala om bilen stått stilla?',
    'Ja, om den varit påställd. Det är registreringen som avgör, inte om bilen faktiskt '
    'körts. En bil som står på gatan påställd är avgiftspliktig.'),
   ('Kan jag bestrida avgiften?',
    'Ja, om du haft försäkring under perioden eller fordonet varit avställt. Skicka bevis '
    'till föreningen — men teckna försäkring först, eftersom ett bestridande inte stoppar '
    'avgiften.'),
 ],
 'rel': [('/trafikforsakring/', 'Trafikförsäkring — lagkravet'),
         ('/avstalld-bil/', 'Avställd bil'),
         ('/byta-bilforsakring/', 'Byta bilförsäkring'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
         ('/jamfor-bilforsakring/', 'Så jämför du offerter')],
},

# ═══ AVSTÄLLD BIL ══════════════════════════════════════════════════
{
 'slug': 'avstalld-bil', 'key': True,
 'title': 'Avställd bil och försäkring — vad krävs och vad täcks?',
 'desc': 'Måste en avställd bil vara försäkrad? Se vad avställning innebär, '
         'vad en avställningsförsäkring täcker och när det lönar sig att ställa av.',
 'eyebrow': 'Faktasida',
 'h1': 'Avställd bil och försäkring',
 'lead': 'En avställd bil får inte köras och behöver därför ingen trafikförsäkring. Men den '
         'kan fortfarande brinna, bli stulen eller vandaliseras där den står — och då är '
         'den oförsäkrad om du sagt upp allt.',
 'checks': ['Avställd bil kräver ingen trafikförsäkring',
            'Den kan fortfarande stjälas eller brinna',
            'Avställningsförsäkring kostar en bråkdel av en vanlig premie'],
 'card_t': 'Se vad försäkringen kostar när bilen ställs på igen',
 'sticky': 'Jämför pris inför påställningen',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Ställ av bilen hos Transportstyrelsen, säg
upp trafikdelen — men behåll ett skydd mot stöld och brand om bilen har ett värde. Det är
den kombinationen som är både laglig och billig.</p></div>

<h2>Vad avställning innebär</h2>
<p>Avställning är en registreringsåtgärd hos Transportstyrelsen, inte något du gör hos
försäkringsbolaget. Från den dag fordonet är avställt upphör både fordonsskatt och kravet på
trafikförsäkring. Bilen får då inte användas i trafik över huvud taget — inte ens för en kort
flytt till en annan parkeringsplats.</p>

<h2>Påställd eller avställd</h2>
{_t('Skillnaderna',
    ['', 'Påställd', 'Avställd'],
    [['Får köras', 'Ja', 'Nej'],
     ['Trafikförsäkring krävs', 'Ja', 'Nej'],
     ['Fordonsskatt', 'Ja', 'Nej'],
     ['Risk för trafikförsäkringsavgift', 'Ja, om oförsäkrad', 'Nej'],
     ['Kan stjälas eller brinna', 'Ja', 'Ja — risken finns kvar'],
     ['Besiktningskrav', 'Ja', 'Vilande tills påställning']],
    swipe=False)}

<h2>Avställningsförsäkring — vad den täcker</h2>
<p>Den kallas också garageförsäkring eller uppställningsförsäkring och innehåller normalt
stöld, brand och ibland glas. Vagnskada och trafik ingår inte, eftersom bilen inte får köras.
Premien är låg just för att den största risken — att köra — är borta.</p>
{_t('Vad som normalt ingår',
    ['Moment', 'Ingår i avställningsförsäkring'],
    [['Trafikskador', 'Nej — bilen får inte köras'],
     ['Stöld och inbrott', 'Ja'],
     ['Brand', 'Ja'],
     ['Glas', 'Ofta'],
     ['Skadegörelse', 'Beror på bolaget'],
     ['Vagnskada', 'Nej'],
     ['Maskinskada', 'Nej']],
    swipe=False)}

<h2>När lönar det sig att ställa av?</h2>
{_t('Vanliga situationer',
    ['Situation', 'Rimlig åtgärd'],
    [['Bilen står över vintern', 'Ställ av och behåll stöld- och brandskydd'],
     ['Bilen ska säljas om några månader', 'Ställ av tills köparen finns'],
     ['Du är utomlands ett halvår', 'Ställ av — men kontrollera var bilen står'],
     ['Bilen står i väntan på reparation', 'Ställ av om den inte ska köras'],
     ['Bilen ska skrotas', 'Avregistrera i stället, inte bara ställa av']],
    swipe=False)}
<p>Ska bilen på vägen igen ställer du på den hos Transportstyrelsen och tecknar
<a href="/trafikforsakring/">trafikförsäkring</a> samma dag — annars börjar
<a href="/trafikforsakringsavgift/">trafikförsäkringsavgiften</a> löpa direkt.</p>
{data.kontrollerad()}

<div class="cta"><h2>Se priset inför påställningen</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>''',
 'faq_h2': 'Vanliga frågor om avställd bil',
 'faq': [
   ('Måste en avställd bil vara försäkrad?',
    'Nej, kravet på trafikförsäkring gäller bara påställda fordon. Men bilen kan fortfarande '
    'stjälas eller brinna, så ett stöld- och brandskydd är ofta värt pengarna om bilen har '
    'ett värde.'),
   ('Vad kostar en avställningsförsäkring?',
    'Betydligt mindre än en vanlig försäkring, eftersom den största risken — själva körandet '
    '— är borta. Den täcker normalt stöld, brand och ibland glas.'),
   ('Får jag flytta en avställd bil några meter?',
    'Nej. En avställd bil får inte användas i trafik alls. Ska den flyttas måste den ställas '
    'på och vara försäkrad, eller transporteras på flak.'),
   ('Hur ställer jag av bilen?',
    'Hos Transportstyrelsen, inte hos försäkringsbolaget. Avställningen gäller från den dag '
    'den registreras, och det är den registreringen som avgör.'),
   ('Vad händer om jag glömmer att ställa på bilen innan jag kör?',
    'Fordonet är då oförsäkrat i trafik, vilket ger trafikförsäkringsavgift och kan få '
    'konsekvenser vid en skada. Ställ på och teckna försäkring innan bilen rullar.'),
 ],
 'rel': [('/trafikforsakringsavgift/', 'Trafikförsäkringsavgift'),
         ('/trafikforsakring/', 'Trafikförsäkring — lagkravet'),
         ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
         ('/byta-bilforsakring/', 'Byta bilförsäkring'),
         ('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen')],
},
]
