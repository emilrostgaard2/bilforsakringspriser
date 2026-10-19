# -*- coding: utf-8 -*-
"""Tio nya sidor (oktober 2026): pris per månad, 18-åring, bilköp, utan bonus,
viltolycka, uppsägning, vagnskadegaranti, körsträcka, glasskada och utomlands.

KÄLLOR
Varje siffra på sidorna har en länkad källa med månad och år. Inga egna
priser, betyg eller statistik. Där villkoren skiljer mellan bolag står det
kvalitativt ("kontrollera villkoren").

PARTNERKORT
Endast 'gofido' får visas här. Dina Försäkringars annonsregler tillåter inte
annons intill rådgivande innehåll — lägg aldrig till 'dina-forsakringar'.
"""
import kort

SWIPE = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>'


def _t(caption, kol, rader, swipe=None):
    th = ''.join(f'<th scope="col">{k}</th>' for k in kol)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    s = SWIPE if (swipe if swipe is not None else len(kol) > 3) else ''
    return (f'<div class="tbl"><table><caption>{caption}</caption><thead><tr>{th}</tr>'
            f'</thead><tbody>{tr}</tbody></table></div>{s}')


def _l(url, text):
    """Extern källänk."""
    return f'<a href="{url}" rel="noopener" target="_blank">{text}</a>'


def _cta(rubrik, text='Ange registreringsnumret så hämtas bilens uppgifter automatiskt.'):
    """In-body-CTA. {PLATE} byts mot regnummerfältet i build.py."""
    return (f'<div class="cta"><h2>{rubrik}</h2>\n<p>{text}</p>\n'
            '<div class="cta-inner">{PLATE}</div></div>')


def _kort(rubrik, ingress):
    return kort.sektion(rubrik, ingress, ['gofido'], smal=True)


# ── Källor som återkommer ───────────────────────────────────────────
TFF_AVG = 'https://www.tff.se/sv/krav/avgift-for-oforsakrade-fordon/'
TFF_ANTAL = 'https://www.tff.se/sv/krav/hur-manga-fordon-ar-oforsakrade/'
TFF_GRONT = 'https://www.tff.se/sv/mer-innehall/utomlands/gront-kort---resa-utomlands-med-fordon/'
TS_FORS = 'https://www.transportstyrelsen.se/sv/vagtrafik/fordon/aga-kopa-eller-salja-fordon/trafikforsakring/'
TS_AGAR = 'https://www.transportstyrelsen.se/sv/vagtrafik/fordon/aga-kopa-eller-salja-fordon/agarbyte/'
TRAFA = 'https://www.trafa.se/vagtrafik/fordon/'
VIBIL = 'https://www.vibilagare.se/nyheter/bilforsakringen-blir-dyrare-har-ar-anledningen'
DPS = 'https://www.dagensps.se/privatekonomi/bilforsakringarna-blir-dyrare-har-betalar-du-minst/'
STOLD = 'https://www.dagensps.se/motor/farre-bilstolder-men-var-tredje-bil-ar-fortfarande-borta/'
LF_VILT = 'https://via.tt.se/pressmeddelande/4560494/viltolyckorna-blir-allt-vanligare-och-dyrare?lang=sv'
NV_VILT = ('https://www.naturvardsverket.se/om-oss/aktuellt/nyheter-och-pressmeddelanden/'
           '2026/februari/trafikolyckor-med-klovvilt-kvar-pa-hoga-nivaer/')
POL_VILT = 'https://polisen.se/lagar-och-regler/trafik-och-fordon/viltolyckor/'
VILT = 'https://www.viltolycka.se'
KONS = 'https://www.konsumenternas.se/'
KONS_JMF = ('https://www.konsumenternas.se/konsumentstod/jamforelser/fordons---batforsakringar/'
            'jamfor-bilforsakringar/')
KONS_FAQ = 'https://www.konsumenternas.se/fragor-och-svar/forsakring/bilforsakringar?qaid=N9970'
KONS_GAR = ('https://www.konsumenternas.se/forsakringar/fordonsforsakringar/bilforsakringar/'
            'tillagg-och-garantier/')
KONS_UTL = ('https://www.konsumenternas.se/forsakringar/fordonsforsakringar/bilforsakringar/'
            'kora-egen-bil-utomlands/')
KONS_HYR = ('https://www.konsumenternas.se/forsakringar/fordonsforsakringar/bilforsakringar/'
            'hyra-bil-utomlands/')
KONS_AGARE = ('https://www.konsumenternas.se/konsumentstod/lag-ratt/rattsfall-och-beslut/'
              'sakforsakringar/fordonsforsakringar/agare-och-huvudsaklig-brukare/')
KONS_RATT = ('https://www.konsumenternas.se/arkiv---nyheter-bloggar-och-poddar/nyheter/2023/'
             'mars/forsakra-bilen-ratt----annars-galler-inte-forsakringen/')
KONS_VILT = ('https://www.konsumenternas.se/arkiv---nyheter-bloggar-och-poddar/nyheter/2023/'
             'oktober/hogsasong-for-viltolyckor--jamfor-bilforsakringarnas-skydd/')
FAL = ('https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/'
       'forsakringsavtalslag-2005104_sfs-2005-104/')


SIDOR = [

# ═══ 1. PRIS PER MÅNAD ═════════════════════════════════════════════
{
 'slug': 'bilforsakring-pris-per-manad', 'key': True,
 'title': 'Vad kostar bilförsäkring per månad? Pris 2026',
 'desc': 'En helförsäkring kostade i snitt 6 581 kr om året 2025, cirka 550 kr i månaden. '
         'Se vad som styr priset och vad månadsbetalning kostar extra.',
 'eyebrow': 'Pris',
 'h1': 'Vad kostar bilförsäkring per månad?',
 'lead': 'Snittpremien för en helförsäkring låg på 6 581 kronor om året 2025, enligt '
         'Compricer. Det motsvarar ungefär 550 kronor i månaden. Ditt eget pris kan ändå hamna '
         'långt ifrån snittet, eftersom bil, ålder, bostadsort och körsträcka räknas in.',
 'checks': ['Snittet för helförsäkring: cirka 550 kr i månaden 2025',
            'Månadsbetalning kan kosta mer än helårsbetalning',
            'Bil, ålder och postnummer väger tyngst i priset'],
 'card_t': 'Se vad din bil kostar per månad',
 'sticky': 'Se din månadskostnad för bilförsäkring',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> En genomsnittlig helförsäkring kostade
6 581 kronor om året 2025, alltså ungefär 550 kronor i månaden. Halvförsäkring och ren
trafikförsäkring kostar mindre, och unga förare i storstad betalar betydligt mer. Betalar du
per månad kan det tillkomma en avgift, så jämför alltid årskostnaden.</p></div>

<h2>Vad snittpriset bygger på</h2>
<p>Den mest aktuella offentliga siffran kommer från Compricers Bilförsäkringskollen. Där
steg snittpremien för helförsäkring från 6 247 till 6 581 kronor om året mellan 2024 och 2025,
en ökning på 5,3 procent. Siffran gäller försäkringar som sålts via Compricer, inte alla
bilar i Sverige. Den är alltså en riktpunkt, inte ett marknadspris.</p>
{_t('Snittpremie för helförsäkring, 2025',
    ['Mått', 'Per år', 'Per månad (omräknat)'],
    [['Riket, snitt 2025', '6 581 kr', 'ca 548 kr'],
     ['Riket, snitt 2024', '6 247 kr', 'ca 521 kr'],
     ['Högst: Botkyrka', '9 291 kr', 'ca 774 kr'],
     ['Lägst: Lycksele', '4 066 kr', 'ca 339 kr']],
    swipe=False)}
<div class="src"><p>Källa: Compricer Bilförsäkringskollen, rapporterad av
{_l(VIBIL, 'Vi Bilägare')} och {_l(DPS, 'Dagens PS')} (februari 2026). Avser helförsäkringar
sålda via Compricer. Månadsbeloppen är årspremien delad med tolv, avrundat.</p></div>
<p>Skillnaden mellan Botkyrka och Lycksele är mer än dubbelt så stor som skillnaden mellan
2024 och 2025. Det visar att <em>var</em> du bor ofta betyder mer för priset än hur
marknaden rör sig ett enskilt år.</p>

{_cta('Se vad just din bil kostar per månad')}

<h2>Per månad eller per år — vad är skillnaden?</h2>
<p>Försäkringen är ett årsavtal, även om du betalar varje månad. Premien räknas fram för ett
helt år och delas sedan upp. Det betyder två saker:</p>
<ul>
<li><strong>Månadsbetalning kan ha ett påslag.</strong> Många bolag tar en avi- eller
administrationsavgift, eller räknar ett något högre pris vid delbetalning. Hur stort påslaget
är skiljer sig mellan bolagen — fråga efter totalkostnaden för året i båda fallen.</li>
<li><strong>Autogiro kostar ofta minst av delbetalningarna.</strong> Pappersfaktura varje
månad är det som oftast kostar extra.</li>
<li><strong>Du binds inte hårdare av att betala månadsvis.</strong> Reglerna för när du får
<a href="/byta-bilforsakring/">byta bilförsäkring</a> är desamma oavsett betalningssätt.</li>
</ul>
{_t('Betalningssätt att jämföra',
    ['Betalningssätt', 'Vanligt upplägg', 'Att fråga bolaget'],
    [['Helår', 'Hela premien på en gång', 'Ger det rabatt jämfört med månad?'],
     ['Halvår eller kvartal', 'Två eller fyra avier', 'Tillkommer aviavgift per avi?'],
     ['Månad, autogiro', 'Dras automatiskt', 'Är priset samma som vid helår?'],
     ['Månad, faktura', 'Ny faktura varje månad', 'Hur stor är fakturaavgiften?']],
    swipe=False)}

<h2>Vad som styr ditt månadspris</h2>
<p>Bolagen räknar med sina egna modeller, men samma faktorer återkommer överallt. Ordningen
nedan är ungefärlig — hur mycket varje faktor väger skiljer mellan bolagen.</p>
{_t('De vanligaste prisfaktorerna',
    ['Faktor', 'Varför den påverkar', 'Kan du ändra den?'],
    [['Skyddsnivå', 'Vagnskada är den dyraste delen', 'Ja — välj nivå efter bilens värde'],
     ['Bilmodell och värde', 'Dyrare reparationer och delar', 'Bara vid bilbyte'],
     ['Förarens ålder', 'Unga förare har fler skador', 'Nej, men priset sjunker med åren'],
     ['Skadefria år', 'Ger bonus i premien', 'Byggs upp över tid'],
     ['Postnummer', 'Stöld, trafik och skadegörelse skiljer', 'Bara vid flytt'],
     ['Körsträcka', 'Fler mil ger högre risk', 'Ja — ange den verkliga'],
     ['Självrisk', 'Högre självrisk sänker premien', 'Ja, direkt']],
    swipe=False)}
<p>Stöldrisken är ett exempel på varför bilmodell spelar roll. Enligt Larmtjänst stals
4 135 bilar i Sverige 2025, jämfört med 5 336 året innan, och 31 procent av dem hittades
aldrig. Volvo var det mest stulna märket ({_l(STOLD, 'Larmtjänst via Dagens PS')}, 2026).
Modeller som stjäls ofta får normalt högre premie för stöldmomentet.</p>

<h2>Trafik, halv eller hel — så skiljer sig månadskostnaden</h2>
<p>Den <a href="/trafikforsakring/">obligatoriska trafikförsäkringen</a> kostar minst eftersom
den bara täcker skador på andra. En <a href="/halvforsakring/">halvförsäkring</a> lägger till
stöld, brand, glas, räddning och rättsskydd. Det stora prissteget kommer med
<a href="/helforsakring/">helförsäkring</a>, där vagnskadan även ersätter skador på din egen bil
när du själv orsakat olyckan. Har bilen kvar sin
<a href="/vagnskadegaranti/">vagnskadegaranti</a> kan halvförsäkring räcka de första åren.</p>

<h2>Fem sätt att få ner månadskostnaden</h2>
<ol>
<li><strong>Kontrollera körsträckan.</strong> Kör du mindre än du angav betalar du för mil du
aldrig kör. Läs mer om <a href="/korstracka-mil-per-ar/">hur mil per år påverkar priset</a>.</li>
<li><strong>Säkerställ att alla skadefria år är registrerade.</strong> Se
<a href="/bonus-och-skadefria-ar/">så fungerar bonusen</a>.</li>
<li><strong>Räkna på en högre självrisk</strong> — men bara om du har pengarna den dag något
händer.</li>
<li><strong>Byt betalningssätt</strong> till helår eller autogiro om det tar bort avgifter.</li>
<li><strong>Jämför bolag.</strong> Enligt Compricer har 34 procent av bilägarna aldrig bytt
bolag, och ett byte kan spara upp till runt 2 000 kronor om året
({_l(DPS, 'Dagens PS')}, februari 2026).</li>
</ol>

<h2>Oberoende hjälp</h2>
<p>{_l(KONS, 'Konsumenternas Försäkringsbyrå')} ger kostnadsfri och opartisk vägledning och
har en egen {_l(KONS_JMF, 'jämförelse av bilförsäkringars villkor')}. Den visar inte priser,
men den visar vad som ingår — vilket är det du behöver veta för att två månadspriser ska gå att
jämföra. Vår guide <a href="/jamfor-bilforsakring/">så jämför du bilförsäkring</a> går igenom
hur du gör det steg för steg.</p>
</div></section>
{_kort('Begär offert och jämför månadspriset',
    'Månadspriset räknas fram individuellt. Gofido är ett digitalt alternativ att hämta en egen offert från, så att du har något konkret att jämföra med din nuvarande premie.')}''',
 'faq_h2': 'Vanliga frågor om månadskostnaden',
 'faq': [
   ('Vad kostar en bilförsäkring i månaden i snitt?',
    'En helförsäkring kostade i snitt 6 581 kronor om året 2025 enligt Compricers '
    'Bilförsäkringskollen, vilket motsvarar cirka 550 kronor i månaden. Siffran gäller '
    'försäkringar sålda via Compricer, och ditt eget pris kan bli både högre och lägre.'),
   ('Är det dyrare att betala bilförsäkringen per månad?',
    'Det kan vara det. Många bolag tar en avi- eller administrationsavgift vid delbetalning, '
    'särskilt med pappersfaktura. Be bolaget om totalkostnaden för ett år vid månads- och '
    'helårsbetalning så ser du skillnaden.'),
   ('Varför kostar min bilförsäkring mer än snittet?',
    'De vanligaste orsakerna är låg ålder, få skadefria år, ett postnummer i storstad, en '
    'dyr eller stöldutsatt bilmodell och lång körsträcka. Kontrollera också att du inte har '
    'helförsäkring på en bil där halvförsäkring hade räckt.'),
   ('Vilken kommun har dyrast bilförsäkring?',
    'I Compricers mätning för 2025 var Botkyrka dyrast med 9 291 kronor om året för '
    'helförsäkring, och Lycksele lägst med 4 066 kronor. Mätningen gäller försäkringar '
    'sålda via Compricer.'),
   ('Kan jag sluta betala en månad om jag inte kör bilen?',
    'Nej. Slutar du betala kan bolaget säga upp försäkringen, och en påställd bil utan '
    'trafikförsäkring ger trafikförsäkringsavgift per dag. Står bilen still länge är det '
    'avställning som gäller.'),
 ],
 'rel': [('/jamfor-bilforsakring/', 'Jämför bilförsäkring på rätt sätt'),
         ('/halvforsakring/', 'Vad ingår i halvförsäkring?'),
         ('/helforsakring/', 'När lönar sig helförsäkring?'),
         ('/sjalvrisk/', 'Självrisk — räkna på mellanskillnaden'),
         ('/korstracka-mil-per-ar/', 'Körsträckans betydelse för priset')],
},

# ═══ 2. 18 ÅR ══════════════════════════════════════════════════════
{
 'slug': 'bilforsakring-18-ar', 'key': True,
 'title': 'Bilförsäkring 18 år 2026 – pris och så sänker du den',
 'desc': 'Som 18-åring betalar du mer för bilförsäkringen. Se varför, varför målvakt-'
         'upplägg är en risk och fem lagliga sätt att sänka priset.',
 'eyebrow': 'Ung förare',
 'h1': 'Bilförsäkring för 18-åring – pris och hur du sänker den',
 'lead': 'En 18-åring utan skadefria år hör till den grupp som betalar mest för '
         'bilförsäkring. Att låta en förälder stå som ägare för att få ner priset är en risk: '
         'stämmer inte uppgifterna kan ersättningen utebli när något händer. Det finns '
         'lagliga sätt att sänka priset.',
 'checks': ['Försäkringen ska stå på den som äger och kör bilen',
            'Fel ägare kan innebära att ersättningen uteblir',
            'Enklare bil, kortare körsträcka och högre självrisk sänker priset'],
 'card_t': 'Se vad bilförsäkringen kostar för dig',
 'sticky': 'Jämför bilförsäkring som 18-åring',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Bilförsäkring för en 18-åring är dyr
eftersom unga förare statistiskt har fler skador och ännu inga skadefria år. Teckna
försäkringen i ditt eget namn om det är du som äger och kör bilen, och sänk priset genom
bilval, rätt körsträcka och självrisk — inte genom att skriva bilen på en förälder.</p></div>

<h2>Varför det är dyrt att vara 18</h2>
<p>Premien bygger på hur ofta en viss grupp förare råkar ut för skador och hur dyra skadorna
blir. Nyblivna förare ligger högt på båda. Till det kommer att du börjar från noll
<a href="/bonus-och-skadefria-ar/">skadefria år</a>, vilket är den rabatt som äldre förare har
byggt upp. Hos många bolag tillkommer dessutom en ungdomssjälvrisk — en extra självrisk om
föraren vid skadan är under en viss ålder. Den syns inte i premien, men den slår till om något
händer. Läs mer i vår <a href="/sjalvrisk/">genomgång av självrisker</a>.</p>
{_t('Det som gör försäkringen dyr — och vad du kan göra',
    ['Orsak', 'Kan du påverka?', 'Så gör du'],
    [['Ålder', 'Nej', 'Priset sjunker normalt år för år'],
     ['Inga skadefria år', 'Över tid', 'Kör skadefritt — bonusen byggs upp'],
     ['Bilens värde och effekt', 'Ja', 'Välj en enklare, billigare bil'],
     ['Körsträcka', 'Ja', 'Ange den verkliga — inte en gissning'],
     ['Skyddsnivå', 'Ja', 'Halv i stället för hel på en äldre bil'],
     ['Självrisk', 'Ja', 'Högre självrisk ger lägre premie']],
    swipe=False)}

{_cta('Se vad bilförsäkringen kostar för dig')}

<h2>Målvaktsförsäkring — därför ska du undvika den</h2>
<p>Ett vanligt upplägg är att en förälder står som ägare och försäkringstagare, fast det är
18-åringen som har bilen och kör den. Det kallas ibland målvakt eller bulvan. Problemet är att
försäkringen bygger på att uppgifterna om ägare och huvudsaklig förare stämmer.</p>
<ul>
<li><strong>Ersättningen kan utebli.</strong> Konsumenternas Försäkringsbyrå skriver att om
det anses stå fel ägare och huvudsaklig användare kan du bli utan ersättning vid en skada
({_l(KONS_RATT, 'Konsumenternas')}, mars 2023).</li>
<li><strong>Bevisbördan ligger på er.</strong> I en
{_l(KONS_AGARE, 'sammanställning av rättsfall')} visar Konsumenternas att det inte räcker att
stå som ägare eller betala kostnaderna — försäkringstagaren måste kunna visa att hen verkligen
äger och huvudsakligen använder bilen. I ett hovrättsfall från 2008 nekades ersättning efter en
brand, eftersom det var barnbarnet som i praktiken använde bilen.</li>
<li><strong>Medvetet felaktiga uppgifter kan vara försäkringsbedrägeri.</strong> Det är inte
en gråzon att uppge fel person för att få lägre pris.</li>
</ul>
<p>Det är helt i sin ordning att låna föräldrarnas bil då och då. Problemet uppstår när bilen
i praktiken är din. Tänk också på att många bolag vill veta om bilen lånas ut till förare
under 24 eller 25 år, och att ungdomssjälvrisk ofta gäller även när du lånar.</p>

<h2>Fem lagliga sätt att sänka priset</h2>
<h3>1. Välj en enklare bil</h3>
<p>En äldre, vanlig bil med måttlig motoreffekt är billigare att försäkra än en ny eller
sportig. Är bilen värd lite kan en <a href="/halvforsakring/">halvförsäkring</a> räcka, och då
försvinner den dyraste delen av premien: vagnskadan.</p>
<h3>2. Ange rätt körsträcka</h3>
<p>Kör du mest till skola och jobb blir det ofta färre mil än man tror. Ange den verkliga
siffran — inte för lågt, eftersom ersättningen kan sättas ned om du kört mer. Se
<a href="/korstracka-mil-per-ar/">hur körsträckan påverkar priset</a>.</p>
<h3>3. Räkna på högre självrisk</h3>
<p>En högre självrisk sänker premien. Gör det bara om du har pengarna undanlagda om något
händer.</p>
<h3>4. Bygg skadefria år så tidigt det går</h3>
<p>Skadefria år följer dig som person. Hos vissa bolag kan tid som registrerad förare eller
medförsäkrad räknas in — fråga hur just ditt bolag gör. Läs mer om att
<a href="/bilforsakring-utan-bonus/">teckna bilförsäkring utan bonus</a>.</p>
<h3>5. Jämför flera bolag</h3>
<p>Bolagen bedömer unga förare olika, så skillnaderna mellan offerterna kan vara stora.
Jämför samma skyddsnivå och samma självrisk hos alla.</p>

<h2>Checklista innan du tecknar</h2>
{_t('Fem saker att kontrollera',
    ['Kontrollera', 'Varför'],
    [['Att du står som ägare och försäkringstagare', 'Annars riskerar du ersättningen'],
     ['Ungdomssjälvriskens storlek', 'Den läggs ovanpå övriga självrisker'],
     ['Om helförsäkring behövs', 'På en billig bil kan halv räcka'],
     ['Körsträckan', 'För högt kostar, för lågt kan ge nedsatt ersättning'],
     ['Startdatum', 'Försäkringen ska gälla från dagen du blir ägare']],
    swipe=False)}
<p>Fler råd för förare under 25 hittar du i vår guide
<a href="/bilforsakring-ung-forare/">bilförsäkring för ung förare</a>. Köper du din första bil
finns också en genomgång av <a href="/kopa-bil-forsakring/">vad som gäller från dag 1</a>.</p>
</div></section>
{_kort('Hämta en egen offert som 18-åring',
    'För unga förare skiljer sig bolagens bedömning ofta mycket. Gofido är ett digitalt bolag att begära offert hos, så att du har ett konkret pris att jämföra med andra.')}''',
 'faq_h2': 'Vanliga frågor om bilförsäkring för 18-åringar',
 'faq': [
   ('Varför är bilförsäkring så dyr för en 18-åring?',
    'Unga förare har statistiskt fler och dyrare skador, och en 18-åring har ännu inga '
    'skadefria år som ger rabatt. Därför ligger premien högt de första åren och sjunker '
    'normalt i takt med ålder och skadefri körning.'),
   ('Kan mina föräldrar stå som ägare till min bil?',
    'Bara om de faktiskt äger och huvudsakligen använder bilen. Står fel person som ägare '
    'och huvudsaklig förare kan ersättningen utebli vid en skada, och medvetet felaktiga '
    'uppgifter kan vara försäkringsbedrägeri.'),
   ('Vad är ungdomssjälvrisk?',
    'En extra självrisk som många bolag tar ut om föraren vid skadan är under en viss ålder, '
    'ofta 24 eller 25 år. Den läggs till de vanliga självriskerna och gäller ofta även när en '
    'ung förare lånar någon annans bil.'),
   ('Hur sänker jag bilförsäkringen som 18-åring?',
    'Välj en enklare bil, ange den verkliga körsträckan, räkna på en högre självrisk och '
    'överväg halvförsäkring om bilen är värd lite. Jämför sedan flera bolag på samma villkor.'),
   ('Räknas skadefria år från att jag tog körkort?',
    'Normalt räknas de från att du själv haft en bilförsäkring. Vissa bolag kan ta hänsyn till '
    'tid som registrerad förare eller medförsäkrad — fråga ditt bolag hur de gör.'),
 ],
 'rel': [('/bilforsakring-ung-forare/', 'Bilförsäkring för ung förare'),
         ('/bilforsakring-utan-bonus/', 'Bilförsäkring utan bonus'),
         ('/bonus-och-skadefria-ar/', 'Så byggs skadefria år upp'),
         ('/sjalvrisk/', 'Ungdomssjälvrisk och andra självrisker'),
         ('/kopa-bil-forsakring/', 'Försäkring när du köper bil')],
},

# ═══ 3. KÖPA BIL ═══════════════════════════════════════════════════
{
 'slug': 'kopa-bil-forsakring', 'key': True,
 'title': 'Köpa bil 2026: så fungerar försäkringen från dag 1',
 'desc': 'När du köper bil ska trafikförsäkringen gälla från dagen ägarbytet registreras. '
         'Se vad som gäller vid köp av privatperson och av bilhandlare.',
 'eyebrow': 'Bilköp',
 'h1': 'Försäkring när du köper bil – det här gäller från dag 1',
 'lead': 'Som köpare ska du ha trafikförsäkring från den dag ägarbytet registreras hos '
         'Transportstyrelsen, om bilen är påställd. Säljarens försäkring avanmäls automatiskt '
         'samma dag. Teckna därför din försäkring innan du hämtar bilen.',
 'checks': ['Datumet i vägtrafikregistret är det som gäller',
            'Säljarens försäkring upphör automatiskt vid registrerat ägarbyte',
            'Oförsäkrad dag ger trafikförsäkringsavgift — 202 kr per dygn'],
 'card_t': 'Försäkra bilen du ska köpa',
 'sticky': 'Teckna försäkring innan du hämtar bilen',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Försäkringen följer den registrerade ägaren.
Från den dag ägarbytet förs in i vägtrafikregistret är det du som ska ha trafikförsäkring,
och säljarens försäkring avanmäls automatiskt. Teckna din försäkring med startdatum samma dag
— helst innan affären görs upp.</p></div>

<h2>Vem försäkrar bilen vid ägarbytet?</h2>
<p>Transportstyrelsen är tydlig: det är fordonets registrerade ägare som ska teckna
trafikförsäkring, och det är datumet som förs in i vägtrafikregistret som gäller vid ägarbyte
({_l(TS_FORS, 'Transportstyrelsen, trafikförsäkring')}). Är bilen påställd ska köparen ha
försäkring från ägarbytesdagen, och säljarens försäkring avanmäls automatiskt när ägarbytet
registrerats ({_l(TS_AGAR, 'Transportstyrelsen, ägarbyte')}, hämtat oktober 2026).</p>
{_t('Före, under och efter ägarbytet',
    ['Tidpunkt', 'Vems försäkring gäller?', 'Att tänka på'],
    [['Före registrerat ägarbyte', 'Säljarens', 'Provkörning sker på säljarens försäkring'],
     ['Ägarbytesdagen', 'Köparens', 'Teckna med startdatum samma dag'],
     ['Efter ägarbytet', 'Köparens', 'Säljarens upphör automatiskt'],
     ['Om bilen är avställd', 'Ingen trafikförsäkring krävs', 'Ställ på först när den ska köras']],
    swipe=False)}

{_cta('Ta fram ett pris på bilen innan du köper')}

<h2>Köp av privatperson</h2>
<p>Vid privatköp gör ni ägarbytet själva. Görs det i Transportstyrelsens e-tjänst registreras
det samma dag, och ni kan inte välja ett annat datum. Säljaren behöver logga in med
e-legitimation. Skickar ni i stället in den gula delen av registreringsbeviset (del 2) med
post ska anmälan vara framme inom tio dagar från överlåtelsen — kommer den senare blir
ankomstdagen ägarbytesdatum ({_l(TS_AGAR, 'Transportstyrelsen')}).</p>
<p>Det praktiska rådet blir därför: teckna din försäkring innan ni gör ägarbytet i
e-tjänsten, och kör inte iväg förrän du har ett försäkringsbekräftat startdatum. Det kostar
ingenting att teckna några timmar för tidigt.</p>
<ul>
<li>Kontrollera säljarens identitet och att hen är registrerad ägare.</li>
<li>Kontrollera i Transportstyrelsens fordonsuppgifter om bilen är kreditköpt — annars kan du
i värsta fall få betala två gånger.</li>
<li>Kontrollera om bilen är påställd eller avställd, och om den har körförbud.</li>
</ul>

<h2>Köp av bilhandlare</h2>
<p>Köper du av en handlare anmäler handlaren ägarbytet digitalt, och registreringsbevisen
skickas därefter till dig med post. Försäkringsplikten är densamma: från registrerad
ägarbytesdag ska bilen vara försäkrad av dig.</p>
<p>Många handlare erbjuder en försäkring i samband med köpet, ibland med en introduktionsperiod.
Det kan vara smidigt, men det är inte ett krav. Jämför erbjudandet med andra bolag, och
kontrollera vad som händer när en eventuell rabatterad period går ut. Är bilen ny har den ofta
<a href="/vagnskadegaranti/">vagnskadegaranti</a>, vilket påverkar vilken skyddsnivå du behöver.</p>
{_t('Privatperson eller handlare',
    ['Fråga', 'Privatköp', 'Handlare'],
    [['Vem anmäler ägarbytet?', 'Ni själva', 'Handlaren, digitalt'],
     ['När gäller ägarbytet?', 'Registreringsdagen', 'Registreringsdagen'],
     ['Försäkring erbjuds vid köpet?', 'Nej', 'Ofta'],
     ['Vagnskadegaranti?', 'Följer med om den är giltig', 'Ofta på nya bilar']],
    swipe=False)}

<h2>Vad kostar det att glömma?</h2>
<p>En påställd bil som inte är försäkrad ger trafikförsäkringsavgift från
Trafikförsäkringsföreningen. För en privat personbil är den 202 kronor per dag, med en
minimiavgift på 200 kronor ({_l(TFF_AVG, 'TFF')}, oktober 2026). Tre dagars glapp mellan
ägarbyte och försäkring kostar alltså mer än 600 kronor — utan att du fått något skydd för
pengarna. Läs mer om <a href="/trafikforsakringsavgift/">trafikförsäkringsavgiften</a>.</p>
<p>År 2025 var i genomsnitt 43 073 fordon oförsäkrade per dag, jämfört med 63 323 år 2017
({_l(TFF_ANTAL, 'TFF')}). Ett försenat ägarbyte är en vanlig orsak.</p>

<h2>Vilken skyddsnivå behöver den nya bilen?</h2>
<p>Trafikförsäkring är lagkrav. Utöver det handlar valet om bilens värde och om du har råd att
stå för en skada själv. En äldre bil med lågt värde klarar sig ofta med
<a href="/halvforsakring/">halvförsäkring</a>. En nyare bil utan vagnskadegaranti, eller en bil
med lån, kräver i praktiken <a href="/helforsakring/">helförsäkring</a>. Har du
<a href="/bonus-och-skadefria-ar/">skadefria år</a> från en tidigare bil följer de med dig.</p>
</div></section>
{_kort('Begär offert på bilen du ska köpa',
    'Har du registreringsnumret kan du få ett pris redan innan affären är klar. Gofido är ett digitalt alternativ att jämföra med handlarens erbjudande.')}''',
 'faq_h2': 'Vanliga frågor om försäkring vid bilköp',
 'faq': [
   ('När måste jag ha försäkring på bilen jag köpt?',
    'Från den dag ägarbytet registreras i vägtrafikregistret, om bilen är påställd. Det är '
    'registreringsdatumet som gäller, inte dagen du hämtar bilen eller betalar.'),
   ('Gäller säljarens försäkring när jag kör hem bilen?',
    'Inte efter att ägarbytet registrerats. Säljarens försäkring avanmäls automatiskt den '
    'dagen, så köparen behöver ha en egen försäkring med startdatum samma dag.'),
   ('Vad händer om jag glömmer att försäkra bilen?',
    'Trafikförsäkringsföreningen tar ut trafikförsäkringsavgift för varje oförsäkrad dag. För '
    'en privat personbil är den 202 kronor per dag med en minimiavgift på 200 kronor '
    '(oktober 2026).'),
   ('Måste jag ta bilhandlarens försäkring?',
    'Nej. Du får välja vilket bolag du vill. Jämför handlarens erbjudande med andra bolag och '
    'kontrollera vad som gäller när en eventuell rabatterad period är slut.'),
   ('Följer vagnskadegarantin med en begagnad bil?',
    'Ja, enligt Konsumenternas Försäkringsbyrå följer garantin med bilen vid ägarbyte så länge '
    'den är giltig, normalt tre år från första registreringsdag. Kontrollera villkoren för just '
    'det märket.'),
 ],
 'rel': [('/trafikforsakringsavgift/', 'Avgiften för oförsäkrade fordon'),
         ('/trafikforsakring/', 'Vad trafikförsäkringen täcker'),
         ('/vagnskadegaranti/', 'Vagnskadegaranti på nya bilar'),
         ('/saga-upp-bilforsakring/', 'Säga upp försäkringen vid försäljning'),
         ('/avstalld-bil/', 'Avställd bil och försäkring')],
},

# ═══ 4. UTAN BONUS ═════════════════════════════════════════════════
{
 'slug': 'bilforsakring-utan-bonus', 'key': True,
 'title': 'Bilförsäkring utan bonus 2026 – för nya bilägare',
 'desc': 'Har du inga skadefria år? Så tecknar du din första bilförsäkring, vad som kan '
         'räknas in från tidigare och hur du bygger upp bonusen snabbare.',
 'eyebrow': 'Ny bilägare',
 'h1': 'Bilförsäkring utan bonus – för dig som är ny bilägare',
 'lead': 'Utan skadefria år börjar du på bolagets grundpris, utan bonusrabatt. Det går ändå '
         'utmärkt att teckna försäkring, och bonusen byggs upp för varje skadefritt år. Har du '
         'kört som förare på någon annans försäkring kan vissa bolag ta hänsyn till det.',
 'checks': ['Alla kan teckna trafikförsäkring — bonus är inget krav',
            'Bonusen byggs upp år för år och följer dig mellan bolag',
            'Fråga om tid som förare på annans bil kan räknas in'],
 'card_t': 'Se vad din första bilförsäkring kostar',
 'sticky': 'Jämför bilförsäkring utan bonus',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Utan skadefria år får du ingen bonusrabatt,
så premien blir högre än för en erfaren bilägare. Du kan alltid teckna trafikförsäkring, och
varje skadefritt år sänker priset. Fråga bolaget om tidigare körning — som förare på en
förälders eller partners bil — kan räknas in.</p></div>

<h2>Vad bonus är och varför den saknas</h2>
<p>Bonus är bolagens rabatt för att du inte haft skador som du själv vållat. Den räknas i
<a href="/bonus-och-skadefria-ar/">skadefria år</a>: ju fler år, desto större rabatt, upp till
bolagets tak. Bonusen är personlig och följer dig, inte bilen. Det betyder att den som aldrig
haft en egen försäkring börjar från noll — oavsett ålder och hur länge man haft körkort.</p>
{_t('Vanliga situationer utan bonus',
    ['Situation', 'Vad som gäller', 'Att fråga bolaget'],
    [['Första bilen efter körkortet', 'Noll skadefria år', 'Kan körtid som förare räknas?'],
     ['Kört förälderns eller partnerns bil', 'Bonusen står på ägaren', 'Kan ni dela eller överföra?'],
     ['Haft tjänstebil i flera år', 'Ofta ingen egen bonus', 'Kan arbetsgivaren intyga?'],
     ['Flyttat hem från utlandet', 'Utländsk bonus räknas inte alltid', 'Godtas intyg från utländskt bolag?'],
     ['Uppehåll utan bil i många år', 'Bonusen kan ha nollställts', 'Hur länge sparas den?']],
    swipe=False)}
<p>Reglerna i tabellens högerkolumn är bolagsspecifika. Det finns inget lagkrav på att bolag
ska räkna in körning på någon annans försäkring — men flera gör det i någon form, så det är
alltid värt att fråga.</p>

{_cta('Se ditt pris utan bonus')}

<h2>Fem sätt att hålla nere priset de första åren</h2>
<ol>
<li><strong>Välj bil med försäkringen i åtanke.</strong> Modell, värde och stöldrisk påverkar
priset mycket. Ta fram ett pris innan du köper — se
<a href="/kopa-bil-forsakring/">försäkring vid bilköp</a>.</li>
<li><strong>Välj skyddsnivå efter bilens värde.</strong> En äldre bil klarar sig ofta med
<a href="/halvforsakring/">halvförsäkring</a>.</li>
<li><strong>Ange rätt körsträcka.</strong> Se <a href="/korstracka-mil-per-ar/">hur mil per år
påverkar priset</a>.</li>
<li><strong>Räkna på en högre <a href="/sjalvrisk/">självrisk</a>.</strong></li>
<li><strong>Jämför flera bolag.</strong> Bolagen sätter olika grundpris för kunder utan bonus.</li>
</ol>

<h2>Så byggs bonusen upp</h2>
<p>Varje år utan egen vållad skada ger ett skadefritt år till. Hur snabbt rabatten växer och
var taket ligger skiljer sig mellan bolagen. Det som normalt <em>inte</em> påverkar bonusen är
skador där en motpart är vållande, glasreparationer och räddning. Viltolyckor påverkar ofta
inte bonusen, men det står i villkoren — se <a href="/viltolycka-forsakring/">viltolycka och
försäkring</a>.</p>
{_t('Vad påverkar bonusen?',
    ['Händelse', 'Påverkar bonusen?'],
    [['Kollision där du är vållande', 'Ja, normalt'],
     ['Kollision där motparten är vållande', 'Normalt nej'],
     ['Stenskott som lagas', 'Normalt nej'],
     ['Stöld eller brand', 'Ofta nej — kontrollera villkoren'],
     ['Viltolycka', 'Ofta nej — kontrollera villkoren']],
    swipe=False)}

<h2>När du byter bolag senare</h2>
<p>Bonusen följer med dig, men den överförs inte alltid automatiskt. Be ditt gamla bolag om
ett intyg på dina skadefria år och kontrollera att de syns på första fakturan hos det nya
bolaget. Hur själva bytet går till står i vår guide <a href="/byta-bilforsakring/">byta
bilförsäkring</a>. Enligt Compricer har 34 procent av bilägarna aldrig bytt bolag
({_l(DPS, 'Dagens PS')}, februari 2026) — för den som börjat utan bonus kan det vara extra
värt att jämföra igen när de första skadefria åren är på plats.</p>

<h2>Att tänka på om du är ung</h2>
<p>Är du under 25 tillkommer ofta en ungdomssjälvrisk. Låt inte en förälder stå som ägare för
att låna deras bonus — det kan göra att ersättningen uteblir. Läs mer i
<a href="/bilforsakring-18-ar/">bilförsäkring för 18-åring</a> och
<a href="/bilforsakring-ung-forare/">ung förare</a>.</p>
</div></section>
{_kort('Börja med en egen offert',
    'Utan bonus skiljer sig bolagens grundpris åt. Gofido är ett digitalt alternativ att hämta en första offert från, så att du har något att jämföra med.')}''',
 'faq_h2': 'Vanliga frågor om bilförsäkring utan bonus',
 'faq': [
   ('Kan jag teckna bilförsäkring utan skadefria år?',
    'Ja. Alla bilägare kan teckna trafikförsäkring, och de flesta bolag erbjuder även halv- '
    'och helförsäkring till kunder utan bonus. Priset blir högre eftersom bonusrabatten saknas.'),
   ('Kan jag få räkna in år som förare på mina föräldrars bil?',
    'Det beror på bolaget. Bonusen står normalt på försäkringstagaren, men vissa bolag tar '
    'hänsyn till tid som registrerad förare eller medförsäkrad. Fråga innan du tecknar.'),
   ('Hur lång tid tar det att bygga upp full bonus?',
    'Det skiljer sig mellan bolagen, eftersom var och en har sin egen bonustrappa och sitt '
    'eget tak. Varje år utan egen vållad skada ger ett skadefritt år till.'),
   ('Följer bonusen med om jag byter bolag?',
    'Ja, skadefria år är personliga och följer dig. Be det gamla bolaget om ett intyg och '
    'kontrollera att bonusen syns på första fakturan hos det nya.'),
   ('Räknas bonus från ett utländskt försäkringsbolag?',
    'Ibland. Vissa svenska bolag godtar ett intyg om skadefri körning från ett utländskt bolag. '
    'Ta med intyget och fråga hur bolaget värderar det.'),
 ],
 'rel': [('/bonus-och-skadefria-ar/', 'Bonus och skadefria år'),
         ('/bilforsakring-18-ar/', 'Bilförsäkring som 18-åring'),
         ('/byta-bilforsakring/', 'Ta med bonusen när du byter'),
         ('/halvforsakring/', 'Halvförsäkring på äldre bil'),
         ('/jamfor-bilforsakring/', 'Jämför offerter på samma villkor')],
},

# ═══ 5. VILTOLYCKA ═════════════════════════════════════════════════
{
 'slug': 'viltolycka-forsakring', 'key': True,
 'title': 'Viltolycka 2026: vilken försäkring gäller?',
 'desc': 'Krockat med vilt? Se vilken del av bilförsäkringen som ersätter skadan, vad som '
         'gäller för självrisk och vad lagen kräver att du gör på platsen.',
 'eyebrow': 'Skada',
 'h1': 'Viltolycka: vilken försäkring gäller och vad blir självrisken?',
 'lead': 'Skador på din egen bil vid en viltolycka ersätts i första hand av vagnskadan i en '
         'helförsäkring. Vissa halvförsäkringar har ett eget moment eller reparationsbidrag för '
         'djurkollision. Kör du på exempelvis älg, rådjur eller vildsvin måste du enligt lag '
         'märka ut platsen och ringa polisen.',
 'checks': ['Helförsäkringens vagnskada ersätter skadan på din bil',
            'Vissa halvförsäkringar har reparationsbidrag — kontrollera villkoren',
            'Polisanmälan är obligatorisk för bland annat älg, rådjur och vildsvin'],
 'card_t': 'Se vad helförsäkring kostar för din bil',
 'sticky': 'Kontrollera ditt skydd vid viltolycka',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Har du helförsäkring ersätts skadan på din
bil av vagnskadan, och flera bolag har en lägre självrisk vid viltolycka. Med halvförsäkring
får du ersättning bara om villkoren har ett särskilt djurkollisionsmoment. Med enbart
trafikförsäkring betalar du skadan på din egen bil själv.</p></div>

<h2>Vilken försäkring betalar?</h2>
{_t('Viltolycka per skyddsnivå',
    ['Skyddsnivå', 'Skada på din bil', 'Kommentar'],
    [['<a href="/trafikforsakring/">Trafikförsäkring</a>', 'Nej',
      'Täcker personskador, inte din egen bil'],
     ['<a href="/halvforsakring/">Halvförsäkring</a>', 'Ibland',
      'Vissa bolag har reparationsbidrag vid djurkollision'],
     ['<a href="/helforsakring/">Helförsäkring</a>', 'Ja, via vagnskadan',
      'Flera bolag har lägre självrisk vid viltolycka']],
    swipe=False)}
<p>Konsumenternas Försäkringsbyrå har jämfört hur bolagen hanterar viltolyckor och visar
både vilka helförsäkringar som har lägre självrisk vid viltolyckor och vilka halvförsäkringar
som ger reparationsbidrag vid djurkollision ({_l(KONS_VILT, 'Konsumenternas')}, oktober 2023).
Skyddet skiljer sig alltså mellan bolagen — läs villkoren för just din försäkring eller använd
deras {_l(KONS_JMF, 'jämförelse av bilförsäkringar')}.</p>
<p>Personskador — på dig och dina passagerare — ersätts av trafikförsäkringen oavsett nivå.
Har bilen <a href="/vagnskadegaranti/">vagnskadegaranti</a> kan den täcka skadan på bilen i
stället för en vagnskadeförsäkring.</p>

{_cta('Se vad helförsäkring kostar för din bil')}

<h2>Självrisken vid viltolycka</h2>
<p>Hos många bolag gäller en särskild, ofta lägre, självrisk vid kollision med djur jämfört
med den vanliga vagnskadesjälvrisken. Det finns inget enhetligt belopp på marknaden, så
kontrollera villkoren hos ditt bolag. Två saker påverkar vad du till slut betalar:</p>
<ul>
<li><strong>Om du gör polisanmälan.</strong> Den är ett lagkrav för vissa djur, och bolagen
kan kräva den för att ersätta skadan.</li>
<li><strong>Vilken självrisk du valt.</strong> Har du valt en hög grundsjälvrisk kan den
påverka även viltskador. Läs mer om <a href="/sjalvrisk/">självriskens olika delar</a>.</li>
</ul>
<p>En viltolycka påverkar ofta inte bonusen, men även det står i villkoren. Se
<a href="/bonus-och-skadefria-ar/">bonus och skadefria år</a>.</p>

<h2>Det här kräver lagen på olycksplatsen</h2>
<p>Kolliderar du med björn, varg, järv, lodjur, älg, hjort, rådjur, utter, vildsvin,
mufflonfår eller örn ska du snarast märka ut olycksplatsen och anmäla till polisen genom att
ringa 112. Det gäller även om djuret inte verkar skadat eller ligger dött på platsen. Att låta
bli är ett brott enligt jaktförordningen och kan ge dagsböter. Kollision med ren ska också
anmälas ({_l(POL_VILT, 'Polisen')}, hämtat oktober 2026).</p>
{_t('Gör så här efter en viltolycka',
    ['Steg', 'Vad du gör'],
    [['1. Stanna och varna', 'Varningsblinkers och varningstriangel'],
     ['2. Ring 112', 'Anmäl olyckan till polisen'],
     ['3. Märk ut platsen', 'Där djuret försvann — med markeringsremsa, plastpåse eller liknande'],
     ['4. Närma dig inte djuret', 'Ett skadat djur kan vara farligt'],
     ['5. Anmäl till försäkringsbolaget', 'Ange polisens diarienummer om du fått det']],
    swipe=False)}
<p>Markeringen hjälper eftersöksjägaren att hitta djuret. Mer om hur du gör finns på
{_l(VILT, 'viltolycka.se')}, Nationella viltolycksrådets webbplats.</p>

<h2>Viltolyckor i siffror</h2>
<p>År 2025 rapporterades 72 320 viltolyckor på svenska vägar, enligt statistik från
Nationella viltolycksrådet som Länsförsäkringar redovisat. Rådjur står för den absoluta
majoriteten. Naturvårdsverket anger drygt 73 300 trafikolyckor med klövvilt för samma år —
skillnaden beror på olika avgränsningar.</p>
{_t('Viltolyckor 2025 per djurslag',
    ['Djurslag', 'Antal olyckor'],
    [['Rådjur', '49 168'], ['Vildsvin', '9 759'], ['Dovhjort', '6 284'], ['Älg', '5 582'],
     ['Kronhjort', '418'], ['Utter', '261'], ['Örn', '104'],
     ['Övriga, bland annat björn, lo och varg', '744'], ['Totalt', '72 320']],
    swipe=False)}
<div class="src"><p>Källor: {_l(LF_VILT, 'Länsförsäkringar via TT')} (september 2026) och
{_l(NV_VILT, 'Naturvårdsverket')} (februari 2026).</p></div>
<p>Enligt samma pressmeddelande hade Länsförsäkringar 14 636 skadeanmälningar för
djurkollision 2025, nästan 25 procent fler än 2021, och utbetalningarna har ökat med över
50 procent sedan 2021. En orsak är dyrare reparationer: kameror och sensorer i moderna bilar
behöver ofta bytas eller kalibreras. Oktober och november sticker ut som de mest olycksdrabbade
månaderna.</p>

<h2>Anmälan till försäkringsbolaget</h2>
<p>När djuret är omhändertaget och platsen markerad anmäler du skadan på bilen till ditt
försäkringsbolag, precis som Länsförsäkringar uppmanar i sitt pressmeddelande. Ju mer
underlag du har, desto smidigare går skadehanteringen.</p>
<ul>
<li><strong>Polisens ärendenummer</strong> eller uppgift om när och var du anmälde.</li>
<li><strong>Bilder</strong> på bilen, platsen och gärna spår av djuret, till exempel hår på
stötfångaren.</li>
<li><strong>Plats och tidpunkt</strong> så exakt som möjligt.</li>
<li><strong>Vittnen</strong>, om det fanns några.</li>
</ul>
<p>Går bilen inte att köra vidare ingår räddning och bärgning normalt i halv- och
helförsäkringen. Krockar du med ett djur utan att ha halv- eller helförsäkring betalar du
reparationen själv, men du ska ändå göra polisanmälan om djuret omfattas av lagkravet. Har en
passagerare skadats gäller trafikförsäkringen. Kontrollera också om ditt bolag erbjuder
krisstöd — Konsumenternas noterar att vissa bolag gör det efter viltolyckor.</p>

<h2>Minska risken</h2>
<ul>
<li>Sänk farten där det finns viltvarningsskyltar och där viltstängslet tar slut.</li>
<li>Var extra uppmärksam i gryning och skymning.</li>
<li>Använd helljus när det är möjligt.</li>
<li>Ser du ett djur — räkna med fler. Vildsvin och dovhjort rör sig ofta i grupp.</li>
<li>Bromsa så hårt du kan och undvik häftiga undanmanövrar.</li>
</ul>
</div></section>''',
 'faq_h2': 'Vanliga frågor om viltolycka och försäkring',
 'faq': [
   ('Täcker halvförsäkring viltolycka?',
    'Ibland. Vissa halvförsäkringar har ett särskilt moment eller ett reparationsbidrag vid '
    'djurkollision, andra har det inte. Kontrollera villkoren hos ditt bolag. Med '
    'helförsäkring ersätts skadan via vagnskadan.'),
   ('Måste jag polisanmäla en viltolycka?',
    'Ja, om du kolliderat med björn, varg, järv, lodjur, älg, hjort, rådjur, utter, '
    'vildsvin, mufflonfår eller örn. Du ska märka ut platsen och ringa 112. Att låta bli kan '
    'ge dagsböter enligt jaktförordningen. Kollision med ren ska också anmälas.'),
   ('Vad blir självrisken vid en viltolycka?',
    'Det beror på bolaget. Flera bolag har en lägre självrisk vid viltolycka än vid annan '
    'vagnskada när du har helförsäkring. Beloppet står i villkoren.'),
   ('Påverkar en viltolycka min bonus?',
    'Ofta inte, eftersom du normalt inte anses vållande. Det är ändå bolagets villkor som '
    'avgör, så kontrollera vad som gäller hos ditt bolag.'),
   ('Hur många viltolyckor sker i Sverige?',
    'Under 2025 rapporterades 72 320 viltolyckor enligt Nationella viltolycksrådets statistik, '
    'varav 49 168 med rådjur. Naturvårdsverket anger drygt 73 300 olyckor med klövvilt samma år.'),
 ],
 'rel': [('/helforsakring/', 'Helförsäkring och vagnskada'),
         ('/halvforsakring/', 'Vad ingår i halvförsäkring?'),
         ('/sjalvrisk/', 'Självrisk vid olika skador'),
         ('/bonus-och-skadefria-ar/', 'Hur skador påverkar bonusen'),
         ('/glasskada-bil/', 'Glasskada och stenskott')],
},

# ═══ 6. SÄGA UPP ═══════════════════════════════════════════════════
{
 'slug': 'saga-upp-bilforsakring', 'key': True,
 'title': 'Säga upp bilförsäkring 2026 – sälja, byta, ställa av',
 'desc': 'När får du säga upp bilförsäkringen? Se vad som gäller vid försäljning, byte av '
         'bolag och avställning — och hur du undviker trafikförsäkringsavgift.',
 'eyebrow': 'Uppsägning',
 'h1': 'Säga upp bilförsäkring – vid försäljning, byte eller avställning',
 'lead': 'Säljer du bilen avanmäls försäkringen automatiskt när ägarbytet registrerats. Vid '
         'byte av bolag säger du upp till förfallodagen, och ofta sköter det nya bolaget det. '
         'Ställer du av bilen behövs ingen trafikförsäkring — men säg aldrig upp en påställd bil '
         'utan att ny försäkring tar vid.',
 'checks': ['Vid försäljning upphör försäkringen automatiskt',
            'Vid byte: låt den nya börja samma dag som den gamla slutar',
            'Påställd bil utan försäkring ger avgift från dag ett'],
 'card_t': 'Jämför innan du säger upp',
 'sticky': 'Jämför ny försäkring innan du säger upp',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Du behöver sällan säga upp bilförsäkringen
själv. Vid försäljning avanmäls den automatiskt när ägarbytet registrerats, och vid byte säger
det nya bolaget ofta upp den gamla åt dig. Det viktiga är att en påställd bil aldrig står utan
trafikförsäkring en enda dag.</p></div>

<h2>Tre situationer, tre regelverk</h2>
{_t('Så upphör bilförsäkringen',
    ['Situation', 'Hur försäkringen upphör', 'Risk att se upp för'],
    [['Du säljer bilen', 'Automatiskt när ägarbytet registrerats', 'Ägarbytet måste vara registrerat'],
     ['Du byter bolag', 'Uppsägning till försäkringstidens slut', 'Glapp mellan gammal och ny'],
     ['Du ställer av bilen', 'Trafikförsäkringen kan sägas upp', 'Bilen får inte köras'],
     ['Bilen skrotas', 'När avregistreringen registrerats', 'Spara skrotningsintyget'],
     ['Bolaget höjer premien', 'Du kan säga upp i förtid', 'Ny försäkring ska vara klar']],
    swipe=False)}
<p>Transportstyrelsen anger att du kan säga upp trafikförsäkringen när du säljer, ställer av
eller avregistrerar fordonet, eller när du tecknat ny försäkring hos ett annat bolag. Det är
datumet som förs in i vägtrafikregistret som gäller vid ägarbyte, avställning och
avregistrering ({_l(TS_FORS, 'Transportstyrelsen')}, hämtat oktober 2026).</p>

<h2>När du säljer bilen</h2>
<p>Säljarens försäkring avanmäls automatiskt när ägarbytet registrerats
({_l(TS_AGAR, 'Transportstyrelsen, ägarbyte')}). Du behöver alltså inte kontakta bolaget —
men ägarbytet måste faktiskt vara registrerat. Görs det i e-tjänsten sker det samma dag.
Skickas registreringsbeviset med post och kommer fram sent blir ankomstdagen ägarbytesdatum,
och fram till dess står du kvar som ägare.</p>
<p>Har du betalat i förskott får du normalt tillbaka premien för den tid som återstår. Hur det
räknas står i villkoren. Köparen behöver ha egen försäkring från ägarbytesdagen — se
<a href="/kopa-bil-forsakring/">försäkring när du köper bil</a>.</p>

{_cta('Se vad en ny försäkring skulle kosta')}

<h2>När du byter bolag</h2>
<p>Enligt försäkringsavtalslagen får du när som helst säga upp försäkringen att upphöra vid
försäkringstidens utgång. Har du tecknat en motsvarande försäkring hos ett annat bolag förnyas
den gamla inte automatiskt ({_l(FAL, 'Försäkringsavtalslagen 3 kap. 3–4 §§')}). I praktiken
sköter det nya bolaget ofta uppsägningen åt dig — fråga uttryckligen om de gör det.</p>
<p>Du kan också säga upp i förtid om behovet av försäkringen faller bort, om bolaget ändrar
villkoren eller vid annan väsentlig förändring (3 kap. 6 §). Hela bytesprocessen beskrivs i
<a href="/byta-bilforsakring/">byta bilförsäkring</a>.</p>
<div class="warn"><p><strong>Säg aldrig upp först.</strong> Teckna den nya försäkringen med
startdatum, och låt den gamla upphöra samma dag. Ett glapp på ett dygn ger
trafikförsäkringsavgift.</p></div>

<h2>När du ställer av bilen</h2>
<p>En avställd bil behöver ingen trafikförsäkring. Du får alltså säga upp den. Men bilen kan
fortfarande bli stulen, brinna eller vandaliseras, och många bolag erbjuder därför en
avställningsförsäkring som täcker sådant till en lägre kostnad. Kör inte bilen förrän den är
påställd och försäkrad igen. Läs mer om <a href="/avstalld-bil/">försäkring av avställd bil</a>.</p>

<h2>Vad ett glapp kostar</h2>
<p>En påställd bil utan försäkring ger trafikförsäkringsavgift från Trafikförsäkringsföreningen.
Sedan 1 april 2025 sjunker avgiften till 50 procent från dag 91 och till 25 procent från
dag 181.</p>
{_t('Trafikförsäkringsavgift per dag',
    ['Fordon', 'Avgift per dag'],
    [['Privat personbil', '202 kr'], ['MC över 125 cc', '224 kr'], ['Lätt MC', '34 kr'],
     ['Minimiavgift', '200 kr'], ['Veteranfordon 30 år eller äldre', '50 procent lägre']],
    swipe=False)}
<div class="src"><p>Källa: {_l(TFF_AVG, 'Trafikförsäkringsföreningen')}, oktober 2026.</p></div>
<p>Avgiften stoppas bara av en tecknad försäkring eller en registrerad avställning. Läs mer om
<a href="/trafikforsakringsavgift/">trafikförsäkringsavgiften</a>.</p>

<h2>Om bolaget säger upp dig</h2>
<p>Även bolaget kan avsluta försäkringen. Betalas inte premien i tid får bolaget säga upp
försäkringen, och uppsägningen får verkan fjorton dagar efter att den skickats om premien
fortfarande är obetald ({_l(FAL, 'Försäkringsavtalslagen 5 kap. 2 §')}). Är bilen påställd
står den då oförsäkrad, och avgiften börjar löpa. Får du en påminnelse eller ett
uppsägningsbesked: betala direkt eller teckna ny försäkring samma dag.</p>
{_t('Vem som säger upp — och vad du behöver göra',
    ['Situation', 'Vem säger upp?', 'Din åtgärd'],
    [['Försäljning', 'Sker automatiskt', 'Kontrollera att ägarbytet registrerats'],
     ['Byte av bolag', 'Ofta det nya bolaget', 'Bekräfta startdatum och slutdatum'],
     ['Avställning', 'Du själv', 'Välj eventuellt avställningsförsäkring'],
     ['Obetald premie', 'Bolaget', 'Betala eller teckna nytt omedelbart']],
    swipe=False)}

<h2>Så säger du upp</h2>
<ul>
<li>Gör det skriftligt — via bolagets webb, app eller e-post — och spara bekräftelsen.</li>
<li>Ange registreringsnummer och vilket datum försäkringen ska upphöra.</li>
<li>Kontrollera att eventuell återbetalning av förskottspremie kommer.</li>
<li>Be om intyg på dina skadefria år om du ska teckna nytt senare.</li>
</ul>
<p>Är du osäker på vad som gäller i din situation kan du få kostnadsfri och oberoende
vägledning hos {_l(KONS, 'Konsumenternas Försäkringsbyrå')}. Tänk också på att bonusen inte
försvinner när du säger upp en försäkring — den följer dig som person, men bolagen sparar
uppgiften olika länge. Har du ingen bil på ett tag kan det därför vara klokt att spara intyget
tills du tecknar nästa försäkring.</p>
</div></section>''',
 'faq_h2': 'Vanliga frågor om att säga upp bilförsäkringen',
 'faq': [
   ('Måste jag säga upp bilförsäkringen när jag säljer bilen?',
    'Nej. Enligt Transportstyrelsen avanmäls säljarens försäkring automatiskt när ägarbytet '
    'registrerats i vägtrafikregistret. Kontrollera bara att ägarbytet faktiskt är registrerat.'),
   ('Kan jag säga upp bilförsäkringen när som helst?',
    'Du kan när som helst säga upp den att upphöra vid försäkringstidens slut. I förtid får du '
    'säga upp vid exempelvis försäljning, avställning, villkorsändring eller om behovet av '
    'försäkringen försvinner.'),
   ('Vad händer om bilen är oförsäkrad några dagar?',
    'Trafikförsäkringsföreningen tar ut trafikförsäkringsavgift för varje dag. För en privat '
    'personbil är den 202 kronor per dag med en minimiavgift på 200 kronor (oktober 2026).'),
   ('Behöver en avställd bil försäkring?',
    'Ingen trafikförsäkring krävs för en avställd bil. Många väljer ändå en '
    'avställningsförsäkring som täcker exempelvis stöld och brand medan bilen står.'),
   ('Får jag tillbaka pengar om jag säger upp i förtid?',
    'Har du betalat i förskott får du normalt tillbaka premien för den återstående tiden. Hur '
    'det räknas står i bolagets villkor.'),
 ],
 'rel': [('/byta-bilforsakring/', 'Byta bilförsäkring steg för steg'),
         ('/trafikforsakringsavgift/', 'Trafikförsäkringsavgiften förklarad'),
         ('/avstalld-bil/', 'Försäkring för avställd bil'),
         ('/kopa-bil-forsakring/', 'Försäkring när du köper bil'),
         ('/bonus-och-skadefria-ar/', 'Spara intyget om skadefria år')],
},

# ═══ 7. VAGNSKADEGARANTI ═══════════════════════════════════════════
{
 'slug': 'vagnskadegaranti', 'key': True,
 'title': 'Vagnskadegaranti 2026 – behövs helförsäkring på ny bil?',
 'desc': 'Vagnskadegarantin ersätter skador på en ny bil, ofta i tre år. Se vad den täcker, '
         'hur självrisken skiljer sig och när halvförsäkring räcker.',
 'eyebrow': 'Ny bil',
 'h1': 'Vagnskadegaranti – behöver du helförsäkring på ny bil?',
 'lead': 'En vagnskadegaranti motsvarar vagnskadedelen i en helförsäkring och följer nästan '
         'alltid med en helt ny bil, ofta i tre år från första registreringsdag. Så länge den '
         'gäller räcker det i många fall med halvförsäkring. Kontrollera villkoren för ditt märke.',
 'checks': ['Gäller ofta tre år från första registreringsdag',
            'Följer med bilen vid ägarbyte under garantitiden',
            'Högre självrisk och kortare anmälningstid än vanlig vagnskada'],
 'card_t': 'Se pris på halvförsäkring för din nya bil',
 'sticky': 'Jämför försäkring för bil med vagnskadegaranti',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Har bilen vagnskadegaranti betalar du ofta
för samma skydd två gånger om du också har helförsäkring. En halvförsäkring kompletterar
garantin med stöld, brand, glas och räddning. Byt till helförsäkring när garantin går ut —
eller tidigare, om villkoren i garantin inte passar dig.</p></div>

<h2>Vad är en vagnskadegaranti?</h2>
<p>Vagnskadegarantin ges av bilmärkets svenska generalagent och motsvarar en
vagnskadeförsäkring: den ersätter skador på din egen bil vid exempelvis kollision,
dikeskörning eller skadegörelse. Den administreras av något av de vanliga försäkringsbolagen.
Enligt Konsumenternas Försäkringsbyrå följer den nästan alltid med en helt ny bil och gäller
normalt i tre år från bilens första registreringsdatum
({_l(KONS_GAR, 'Konsumenternas, tillägg och garantier')}, hämtat oktober 2026). Längden kan
skilja mellan märken — kontrollera villkoren.</p>
{_t('Vagnskadegaranti jämfört med vagnskadeförsäkring',
    ['Egenskap', 'Vagnskadegaranti', 'Vagnskada i helförsäkring'],
    [['Vem ger skyddet?', 'Bilmärkets generalagent', 'Ditt försäkringsbolag'],
     ['Hur länge?', 'Ofta tre år från första registrering', 'Så länge du betalar'],
     ['Kostnad', 'Ingår i bilköpet', 'Del av premien'],
     ['Självrisk', 'Högre, plus moms', 'Valbar hos många bolag'],
     ['Anmälningstid', 'Kan vara så kort som 30 dagar', 'Normalt längre'],
     ['Geografi', 'Bara i Sverige', 'Ofta även utomlands'],
     ['Vid ägarbyte', 'Följer bilen', 'Följer ägaren']])}
<div class="src"><p>Källa: {_l(KONS_GAR, 'Konsumenternas Försäkringsbyrå')} (hämtat oktober
2026). Villkoren skiljer mellan märken.</p></div>

{_cta('Se vad halvförsäkring kostar för din nya bil')}

<h2>Behöver du helförsäkring när garantin gäller?</h2>
<p>Konsumenternas skriver att de flesta nya bilar har tre års vagnskadegaranti och att en
halvförsäkring då oftast räcker ({_l(KONS_FAQ, 'Konsumenternas')}). En
<a href="/halvforsakring/">halvförsäkring</a> täcker det garantin inte gör: stöld, brand, glas,
räddning och rättsskydd. Ihop ger de ett skydd som liknar en
<a href="/helforsakring/">helförsäkring</a>.</p>
<p>Det finns ändå skäl att välja helförsäkring redan från början:</p>
<ul>
<li><strong>Du kör ofta utomlands.</strong> Garantin gäller bara i Sverige. Läs mer om
<a href="/bilforsakring-utomlands/">bilförsäkring utomlands</a>.</li>
<li><strong>Du vill ha lägre självrisk.</strong> Garantins självrisk är högre och moms tillkommer
på beloppet.</li>
<li><strong>Du vill ha tillägg</strong> som hyrbil eller självriskreducering, som ibland bara
finns i helförsäkringen.</li>
<li><strong>Bilen är importerad.</strong> Bilar köpta utomlands och införda till Sverige omfattas
inte av garantin.</li>
</ul>

<h2>Varför premien skiljer sig mellan bolagen</h2>
<p>Bolagen prissätter helförsäkring på en bil med garanti olika. Några räknar in att garantin
täcker vagnskadan och tar ett lägre pris de första åren, andra gör inte det. Vissa
märkesförsäkringar — som säljs via bilhandlaren och administreras av ett försäkringsbolag —
är byggda kring garantin. Jämför därför både halv och hel hos flera bolag, och kontrollera hur
priset förändras när garantin går ut. Läs mer om <a href="/jamfor-bilforsakring/">hur du jämför
offerter rätt</a>.</p>

<h2>När garantin går ut</h2>
<p>Notera datumet för bilens första registrering — det är normalt därifrån garantin räknas, inte
från dagen du köpte bilen. Köper du en begagnad bil som är ett eller två år gammal har du alltså
bara resten av garantitiden kvar. Garantin följer med bilen vid ägarbyte så länge den är giltig.</p>
{_t('Skyddsnivå under bilens första år',
    ['Bilens ålder', 'Vanligt upplägg', 'Att göra'],
    [['0–3 år, garanti gäller', 'Halvförsäkring + garanti', 'Kontrollera garantins villkor'],
     ['Garantin går ut', 'Byt till helförsäkring', 'Ta in offerter i god tid'],
     ['Äldre bil, högt värde', 'Helförsäkring', 'Räkna på självrisken'],
     ['Äldre bil, lågt värde', 'Halvförsäkring', 'Vagnskadan kan kosta mer än den ger']],
    swipe=False)}
<p>Leasar du bilen kan leasingavtalet kräva helförsäkring oavsett garanti — se
<a href="/leasingbil-forsakring/">försäkring av leasingbil</a>.</p>

<h2>Räkna på helårskostnaden</h2>
<p>Valet mellan halv och hel under garantitiden handlar i grunden om pengar och bekvämlighet.
Ställ upp tre siffror innan du bestämmer dig:</p>
<ol>
<li><strong>Prisskillnaden</strong> mellan halv- och helförsäkring hos samma bolag.</li>
<li><strong>Självrisken i garantin</strong> inklusive moms, jämfört med vagnskadesjälvrisken i
helförsäkringen.</li>
<li><strong>Hur ofta du kör utomlands</strong>, där garantin inte gäller.</li>
</ol>
<p>Är prisskillnaden liten kan helförsäkringen vara värd det för den lägre självrisken och
skyddet utomlands. Är den stor och du kör mest i Sverige räcker garantin och halvförsäkringen
ofta långt. Kom ihåg att ditt val inte påverkar bonusen på samma sätt: en skada som ersätts av
garantin hanteras av garantigivaren, medan en skada på helförsäkringen kan påverka dina
<a href="/bonus-och-skadefria-ar/">skadefria år</a>. Kontrollera hur ditt bolag och garantin
hanterar just det.</p>

<h2>Vid skada</h2>
<p>Anmäl skadan direkt. Anmälningstiden i garantin kan vara så kort som 30 dagar från
skadetillfället. Följ garantins anvisningar om verkstad, och spara kvitton och bilder. Har du
också en halvförsäkring hos ett försäkringsbolag och skadan gäller exempelvis glas eller stöld
är det halvförsäkringen som ska ha anmälan, inte garantin. Osäker? Ring ditt försäkringsbolag
först — de vet ofta vilken part som ska hantera skadan och kan hänvisa vidare.</p>
</div></section>''',
 'faq_h2': 'Vanliga frågor om vagnskadegaranti',
 'faq': [
   ('Hur länge gäller vagnskadegarantin?',
    'Ofta i tre år från bilens första registreringsdag, enligt Konsumenternas '
    'Försäkringsbyrå. Längden och villkoren kan skilja mellan märken, så kontrollera vad som '
    'gäller för din bil.'),
   ('Behöver jag helförsäkring om bilen har vagnskadegaranti?',
    'Ofta räcker halvförsäkring, eftersom garantin motsvarar vagnskadan. Helförsäkring kan '
    'ändå vara värd det om du kör utomlands, vill ha lägre självrisk eller vill ha tillägg '
    'som bara finns i helförsäkringen.'),
   ('Gäller vagnskadegarantin utomlands?',
    'Nej. Enligt Konsumenternas Försäkringsbyrå gäller vagnskadegaranti bara i Sverige. '
    'Ska du köra utomlands behöver du en vagnskadeförsäkring för att ha motsvarande skydd där.'),
   ('Följer vagnskadegarantin med när jag köper en begagnad bil?',
    'Ja, garantin följer med bilen vid ägarbyte så länge den är giltig. Tiden räknas från '
    'bilens första registreringsdag, inte från ditt köp.'),
   ('Är självrisken högre i vagnskadegarantin?',
    'Ja, enligt Konsumenternas är självrisken högre än i en vanlig vagnskadeförsäkring, och '
    'moms tillkommer på självriskbeloppet.'),
 ],
 'rel': [('/halvforsakring/', 'Halvförsäkring som komplement'),
         ('/helforsakring/', 'Helförsäkring när garantin gått ut'),
         ('/leasingbil-forsakring/', 'Försäkring av leasingbil'),
         ('/bilforsakring-elbil/', 'Försäkring av ny elbil'),
         ('/kopa-bil-forsakring/', 'Försäkring när du köper bil')],
},

# ═══ 8. KÖRSTRÄCKA ═════════════════════════════════════════════════
{
 'slug': 'korstracka-mil-per-ar', 'key': True,
 'title': 'Körsträcka bilförsäkring 2026 – så påverkar mil per år',
 'desc': 'Körsträckan anges i svenska mil (10 km) och styr priset på bilförsäkringen. Se hur '
         'intervallen fungerar och vad som händer om du kör längre än du angett.',
 'eyebrow': 'Prisfaktor',
 'h1': 'Körsträcka: så påverkar mil per år priset på bilförsäkringen',
 'lead': 'Bolagen räknar körsträcka i svenska mil, där en mil är tio kilometer. Ju längre du '
         'kör, desto högre risk och premie. Kör du mer än du angett kan ersättningen sättas ned '
         'vid en skada, så ange en realistisk siffra och ändra den om dina vanor förändras.',
 'checks': ['1 svensk mil = 10 kilometer',
            'Bolagen räknar i intervall, exempelvis upp till 1 000 eller 1 500 mil',
            'För låg uppgift kan ge nedsatt ersättning vid skada'],
 'card_t': 'Se ditt pris med rätt körsträcka',
 'sticky': 'Jämför pris med din verkliga körsträcka',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Ange hur många mil du faktiskt kör per år —
en svensk mil är tio kilometer. För högt värde gör att du betalar för mil du aldrig kör. För
lågt värde kan göra att ersättningen sätts ned om något händer. Ändrar sig dina körvanor
ändrar du uppgiften hos bolaget.</p></div>

<h2>Mil, inte kilometer</h2>
<p>I Sverige anges körsträcka för försäkring nästan alltid i mil. Det är en vanlig felkälla:
den som tänker i kilometer och skriver 15 000 har uppgett tio gånger mer än 1 500 mil.
Omvandlingen är enkel — dela antalet kilometer med tio.</p>
{_t('Från kilometer till mil',
    ['Kilometer per år', 'Svenska mil per år', 'Ungefär per vecka'],
    [['5 000 km', '500 mil', 'ca 10 mil'],
     ['10 000 km', '1 000 mil', 'ca 19 mil'],
     ['15 000 km', '1 500 mil', 'ca 29 mil'],
     ['20 000 km', '2 000 mil', 'ca 38 mil'],
     ['30 000 km', '3 000 mil', 'ca 58 mil']],
    swipe=False)}

<h2>Så fungerar intervallen</h2>
<p>De flesta bolag låter dig välja ett intervall i stället för en exakt siffra, exempelvis upp
till 1 000, 1 500, 2 000 eller 2 500 mil per år. Hur intervallen ser ut och hur mycket varje
steg påverkar priset skiljer mellan bolagen. Det gör att två bolag kan reagera helt olika på
samma ändring.</p>
<p>Körsträckan påverkar framför allt de delar av försäkringen där risken växer med körningen:
trafikskador och vagnskada. Stöld- och brandmomenten påverkas mindre. Därför slår körsträckan
hårdast på en <a href="/helforsakring/">helförsäkring</a>.</p>

{_cta('Se vad din körsträcka betyder för priset')}

<h2>Så räknar du ut din körsträcka</h2>
<ol>
<li><strong>Läs av mätarställningen</strong> i dag och jämför med en tidigare avläsning,
exempelvis från förra besiktningen eller ett servicekvitto.</li>
<li><strong>Räkna om till ett år.</strong> Har det gått åtta månader och 900 mil blir det
ungefär 1 350 mil per år.</li>
<li><strong>Lägg till förändringar.</strong> Nytt jobb, längre pendling eller en planerad
semesterresa med bilen ska räknas in.</li>
<li><strong>Välj intervall med lite marginal</strong> — men inte mer än du behöver.</li>
</ol>

<h2>Vad händer om du kör längre?</h2>
<p>Många bolag har villkor som gör att ersättningen kan sättas ned om bilen körts betydligt mer
än du uppgett. Hur nedsättningen räknas står i villkoren, och vid en skada kan bolaget be om
bilens mätarställning. Det enklaste skyddet är att höra av dig till bolaget när dina vanor
ändras — då justeras premien för resten av året.</p>
{_t('Vanliga situationer',
    ['Situation', 'Vad du bör göra'],
    [['Du har fått längre till jobbet', 'Höj körsträckan direkt'],
     ['Du har börjat jobba hemifrån', 'Sänk körsträckan — och premien'],
     ['Du har lånat ut bilen under en period', 'Räkna med lånarens körning'],
     ['Du har kört mer än angett i år', 'Kontakta bolaget och justera'],
     ['Du har gått i pension', 'Ofta färre mil — se över uppgiften']],
    swipe=False)}

<h2>Körsträcka och maskinskada</h2>
<p>Mätarställningen spelar också roll på ett annat sätt. Maskinskadeförsäkringen, som ingår i
många halv- och helförsäkringar, gäller normalt bara till en viss ålder eller ett visst antal
mil. Enligt Konsumenternas Försäkringsbyrå ligger gränsen ofta på 8–12 år eller 10 000–15 000
mil, och det räcker att en av gränserna passerats för att skyddet ska upphöra. Vissa bolag har
högre gränser för elbilar och laddhybrider ({_l(KONS_FAQ, 'Konsumenternas')}, hämtat oktober
2026). Det är alltså två olika saker: den årliga körsträckan styr priset, medan bilens totala
mätarställning styr om maskinskadan gäller.</p>

<h2>Elbil och laddhybrid</h2>
<p>Elbilar körs ofta lika långt som andra bilar, men laddhybrider kan ha en annan profil. Även
här är det den totala körsträckan som räknas, oavsett om milen gått på el eller bränsle. Enligt
Trafikanalys fanns omkring 5,04 miljoner personbilar i trafik vid slutet av 2025, varav 9 procent
var rena elbilar ({_l(TRAFA, 'Trafikanalys, Fordon 2025')}, februari 2026). Läs mer i vår guide
<a href="/bilforsakring-elbil/">bilförsäkring för elbil</a>.</p>

<h2>Fler förare på samma bil</h2>
<p>Körsträckan gäller bilen, inte föraren. Delar flera i hushållet på bilen ska allas körning
räknas ihop. Lånar en vuxen son eller dotter bilen under sommaren, eller kör en partner den
till jobbet ett par dagar i veckan, ska det synas i den årliga siffran. Det är ett vanligt skäl
till att körsträckan i försäkringen blir för låg — man räknar bara med sin egen körning.
Tänk också på att många bolag vill veta om förare under 24 eller 25 år kör bilen.</p>

<h2>Låg körsträcka — vad det kan ge</h2>
<p>För den som kör lite är körsträckan ofta den enklaste hävstången på priset, eftersom den går
att ändra direkt. Det gäller till exempel <a href="/bilforsakring-pensionar/">pensionärer</a>
och den som har bilen som komplement till kollektivtrafik. Står bilen helt still under en
längre period kan <a href="/avstalld-bil/">avställning</a> vara ett alternativ. Fler sätt att
sänka priset finns i <a href="/bilforsakring-pris-per-manad/">vad kostar bilförsäkring per
månad</a>.</p>
</div></section>''',
 'faq_h2': 'Vanliga frågor om körsträcka och bilförsäkring',
 'faq': [
   ('Hur långt är en mil i bilförsäkringen?',
    'En svensk mil är tio kilometer. Kör du 15 000 kilometer per år motsvarar det 1 500 mil. '
    'Det är mil som anges när du tecknar bilförsäkring i Sverige.'),
   ('Vad händer om jag kör mer än jag angett?',
    'Hos många bolag kan ersättningen sättas ned vid en skada om bilen körts betydligt mer än '
    'du uppgett. Kontakta bolaget när dina körvanor ändras, så justeras premien i stället.'),
   ('Kan bolaget kontrollera min körsträcka?',
    'Ja. Vid en skada kan bolaget be om bilens mätarställning och jämföra med tidigare '
    'avläsningar, exempelvis från besiktning eller service.'),
   ('Blir försäkringen billigare om jag sänker körsträckan?',
    'Oftast ja, särskilt för helförsäkring där vagnskadan påverkas mest. Hur mycket priset '
    'ändras skiljer mellan bolagen. Ange alltid den verkliga körsträckan.'),
   ('Påverkar mätarställningen maskinskadeförsäkringen?',
    'Ja. Maskinskadan gäller ofta bara till en viss ålder eller mätarställning, enligt '
    'Konsumenternas ofta 8–12 år eller 10 000–15 000 mil. Passeras en av gränserna upphör '
    'skyddet.'),
 ],
 'rel': [('/bilforsakring-pris-per-manad/', 'Vad bilförsäkring kostar per månad'),
         ('/bilforsakring-pensionar/', 'Bilförsäkring för pensionärer'),
         ('/helforsakring/', 'Helförsäkring och vagnskada'),
         ('/avstalld-bil/', 'Ställa av bilen'),
         ('/jamfor-bilforsakring/', 'Jämför offerter på samma körsträcka')],
},

# ═══ 9. GLASSKADA ══════════════════════════════════════════════════
{
 'slug': 'glasskada-bil', 'key': True,
 'title': 'Glasskada på bilen 2026 – självrisk och stenskott',
 'desc': 'Glasskador ingår i halv- och helförsäkring. Se varför ett lagat stenskott ofta '
         'kostar lite eller inget, och vad självrisken blir vid byte av vindruta.',
 'eyebrow': 'Skada',
 'h1': 'Glasskada på bilen – självrisk och vad som gäller',
 'lead': 'Glasskador på bilens rutor ingår i halvförsäkring och helförsäkring, men inte i '
         'enbart trafikförsäkring. Lagning av ett stenskott är billig och hos flera bolag helt '
         'utan självrisk. Byte av hela vindrutan ger en betydligt högre självrisk.',
 'checks': ['Glasmomentet ingår i halv- och helförsäkring',
            'Lagning av stenskott: låg eller ingen självrisk hos flera bolag',
            'Glastak och soltak omfattas ofta inte av glasförsäkringen'],
 'card_t': 'Se pris på halvförsäkring med glasskydd',
 'sticky': 'Jämför glassjälvrisk mellan bolagen',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Laga stenskott direkt. Lagning kostar dig
normalt 0–200 kronor i självrisk, medan byte av vindrutan ofta ger en självrisk på runt
2 000 kronor eller en procentandel av kostnaden. Glasskadan ingår i halv- och helförsäkring.
Har du bara trafikförsäkring betalar du själv.</p></div>

<h2>Vilken försäkring täcker glasskador?</h2>
{_t('Glasskydd per skyddsnivå',
    ['Skyddsnivå', 'Glasskada på rutor', 'Kommentar'],
    [['<a href="/trafikforsakring/">Trafikförsäkring</a>', 'Nej', 'Täcker bara skador på andra'],
     ['<a href="/halvforsakring/">Halvförsäkring</a>', 'Ja', 'Glasmomentet ingår'],
     ['<a href="/helforsakring/">Helförsäkring</a>', 'Ja', 'Innehåller halvförsäkringen']],
    swipe=False)}
<p>Glasförsäkringen ersätter sprickor och stenskott i vindruta, sidorutor och bakruta. Enligt
Konsumenternas Försäkringsbyrå ersätter den däremot inte glasskador som uppstått vid en
kollision eller dikeskörning — då är det vagnskadan som gäller. Glastak och soltak omfattas
inte heller av glasförsäkringen, utan kräver vagnskadeförsäkring
({_l(KONS_FAQ, 'Konsumenternas')}, hämtat oktober 2026).</p>

<h2>Självrisk: lagning eller byte</h2>
<p>Bolagen styr medvetet kunderna mot att laga i stället för att byta, eftersom en lagning
kostar en bråkdel. Därför är självrisken vid lagning låg — hos flera bolag är den noll.</p>
{_t('Vanlig självrisk vid glasskada',
    ['Åtgärd', 'Vanlig självrisk', 'När det gäller'],
    [['Lagning av stenskott', '0–200 kr', 'Skottet är litet och inte i förarens synfält'],
     ['Byte av vindruta', 'Ofta ca 2 000 kr eller 35 % av kostnaden, minst 1 000 kr',
      'Sprickan har spridit sig eller skottet sitter illa'],
     ['Byte av sido- eller bakruta', 'Enligt bolagets glassjälvrisk', 'Krossad eller sprucken ruta']])}
<div class="src"><p>Källa: {_l(KONS_FAQ, 'Konsumenternas Försäkringsbyrå')} (hämtat oktober
2026). Beloppen är typiska nivåer — exakt självrisk står i ditt bolags villkor.</p></div>
<p>Självrisken för glas är en av de som skiljer mest mellan bolagen. Jämför den i offerterna,
och se vår genomgång av <a href="/sjalvrisk/">alla självrisker i bilförsäkringen</a>.</p>

{_cta('Se pris på försäkring med glasskydd')}

<h2>Vänta inte med stenskottet</h2>
<p>Ett litet stenskott kan spricka ut vid temperaturväxlingar, i kyla eller när bilen kör över
ojämnheter. Då går rutan inte längre att laga och du får betala den högre självrisken för byte.
Täck gärna skottet med en bit genomskinlig tejp tills det lagas, så att smuts och fukt inte
tränger in.</p>
<ul>
<li>Kontakta ditt försäkringsbolag eller en glasverkstad som bolaget samarbetar med.</li>
<li>Fråga om bolaget har krav på vilken verkstad du använder.</li>
<li>Sitter skottet i förarens synfält kan det krävas byte i stället för lagning.</li>
</ul>

<h2>Lagning går snabbt</h2>
<p>En lagning av ett stenskott tar normalt en kort stund och görs genom att skottet fylls med
en härdande plast. Den syns oftast lite efteråt, men stoppar sprickan från att växa. Ett byte
av vindrutan tar längre tid, och på bilar med kamera i rutan tillkommer kalibrering. Fråga
verkstaden hur lång tid det tar för din bil innan du bokar.</p>

<h2>Dyrare byte på nyare bilar</h2>
<p>Många nyare bilar har kameror och sensorer för förarassistans bakom vindrutan. Vid byte
behöver de ofta kalibreras, vilket gör hela jobbet dyrare. Självrisken styrs av ditt bolags
villkor, men är den procentbaserad slår en dyrare ruta igenom på vad du betalar. Länsförsäkringar
lyfter samma utveckling för viltskador: kameror och sensorer gör reparationerna dyrare
({_l(LF_VILT, 'Länsförsäkringar via TT')}, september 2026). Läs mer om
<a href="/viltolycka-forsakring/">viltolycka och försäkring</a>.</p>

<h2>Glasskada eller vagnskada?</h2>
<p>Hur rutan gick sönder avgör vilken del av försäkringen som betalar. Det spelar roll
eftersom självrisken och påverkan på bonusen skiljer sig.</p>
{_t('Vilken del av försäkringen gäller?',
    ['Orsak till skadan', 'Ersätts av', 'Krävs'],
    [['Stenskott under körning', 'Glasförsäkringen', 'Halv- eller helförsäkring'],
     ['Spricka utan känd orsak', 'Glasförsäkringen', 'Halv- eller helförsäkring'],
     ['Krossad ruta vid inbrott', 'Ofta stöld- eller glasmomentet', 'Halv- eller helförsäkring'],
     ['Ruta skadad vid kollision', 'Vagnskadan', 'Helförsäkring'],
     ['Skadat glastak eller soltak', 'Vagnskadan', 'Helförsäkring']],
    swipe=False)}
<p>Vid inbrott beror det på bolaget om skadan på rutan räknas som glasskada eller stöld- och
skadegörelseskada, och därmed vilken självrisk som gäller. Det står i villkoren.</p>

<h2>Påverkar en glasskada bonusen?</h2>
<p>Normalt inte. Glasskador räknas oftast inte som en skada som sänker dina
<a href="/bonus-och-skadefria-ar/">skadefria år</a>. Kontrollera ändå villkoren hos ditt bolag.</p>

<h2>Jämför glasvillkoren</h2>
<p>Eftersom glasskador är bland de vanligaste skadorna på en bil är glasvillkoren värda att
jämföra innan du väljer bolag. Fråga efter självrisken vid lagning och vid byte, om
självrisken är ett fast belopp eller en procentandel, om du får välja verkstad fritt och om
kalibrering av kameror ingår. {_l(KONS_JMF, 'Konsumenternas jämförelse av bilförsäkringar')}
visar villkoren sida vid sida, och vår guide <a href="/jamfor-bilforsakring/">så jämför du
bilförsäkring</a> hjälper dig att ställa offerterna mot varandra.</p>

<h2>Checklista vid glasskada</h2>
{_t('Så gör du',
    ['Steg', 'Vad du gör'],
    [['1. Fotografera skadan', 'Bild på skottet och var det sitter'],
     ['2. Tejpa över', 'Genomskinlig tejp skyddar mot smuts och fukt'],
     ['3. Kontakta bolaget', 'Fråga om anvisad verkstad och självrisk'],
     ['4. Boka lagning snabbt', 'Innan skottet spricker ut'],
     ['5. Kontrollera kalibrering', 'Vid byte på bil med kamera i vindrutan']],
    swipe=False)}
</div></section>''',
 'faq_h2': 'Vanliga frågor om glasskada på bil',
 'faq': [
   ('Ingår glasskada i halvförsäkring?',
    'Ja, glasmomentet ingår i både halvförsäkring och helförsäkring. Har du bara '
    'trafikförsäkring ersätts inte glasskador på din egen bil.'),
   ('Kostar det något att laga ett stenskott?',
    'Hos flera bolag är lagning av stenskott helt utan självrisk, och enligt Konsumenternas '
    'Försäkringsbyrå ligger självrisken vid lagning normalt på 0–200 kronor. Kontrollera '
    'ditt bolags villkor.'),
   ('Vad är självrisken när vindrutan måste bytas?',
    'Enligt Konsumenternas är den ofta runt 2 000 kronor eller 35 procent av kostnaden, med '
    'ett lägsta belopp på 1 000 kronor. Exakt belopp står i ditt bolags villkor.'),
   ('Täcker glasförsäkringen glastaket?',
    'Oftast inte. Enligt Konsumenternas omfattas glastak och soltak inte av glasförsäkringen, '
    'utan kräver vagnskadeförsäkring, alltså helförsäkring.'),
   ('Påverkar en glasskada min bonus?',
    'Normalt inte. Glasskador räknas oftast inte som en skada som sänker dina skadefria år, '
    'men kontrollera villkoren hos ditt bolag.'),
 ],
 'rel': [('/halvforsakring/', 'Halvförsäkring och glasmomentet'),
         ('/sjalvrisk/', 'Glassjälvrisk och andra självrisker'),
         ('/helforsakring/', 'Helförsäkring och glastak'),
         ('/viltolycka-forsakring/', 'Viltolycka och självrisk'),
         ('/jamfor-bilforsakring/', 'Jämför självrisk mellan bolag')],
},

# ═══ 10. UTOMLANDS ═════════════════════════════════════════════════
{
 'slug': 'bilforsakring-utomlands', 'key': True,
 'title': 'Bilförsäkring utomlands 2026 – gröna kortet och hyrbil',
 'desc': 'Din trafikförsäkring gäller i hela EU/EES och fler länder. Se var du behöver grönt '
         'kort, vad halv- och helförsäkring täcker utomlands och om hyrbil.',
 'eyebrow': 'Utomlands',
 'h1': 'Bilförsäkring utomlands och gröna kortet',
 'lead': 'Din svenska trafikförsäkring gäller i hela EU och EES och i flera länder till, '
         'utan att du behöver grönt kort. Ett fåtal länder, bland annat Turkiet, Marocko och '
         'Ukraina, kräver grönt kort som du beställer från ditt bolag. Halv- och helförsäkringen '
         'gäller ofta också utomlands, men med tidsgränser.',
 'checks': ['Grönt kort behövs inte i EU/EES, Schweiz, Storbritannien med flera',
            'Krävs bland annat i Turkiet, Marocko, Tunisien och Ukraina',
            'Halv- eller helförsäkringen upphör ofta efter cirka 180 dagar utomlands'],
 'card_t': 'Se vad helförsäkring kostar för din bil',
 'sticky': 'Kontrollera bilförsäkringen före resan',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Kör du i EU, EES, Schweiz, Storbritannien
eller på Balkan gäller din svenska trafikförsäkring utan grönt kort. Reser du till exempelvis
Turkiet, Marocko eller Ukraina ska du ha grönt kort, som du beställer gratis från ditt
försäkringsbolag i god tid. Kontrollera också att halv- eller helförsäkringen gäller under
hela resan.</p></div>

<h2>Var behöver du grönt kort?</h2>
<p>Det gröna kortet är ett bevis på att bilen är trafikförsäkrad i Sverige. I de länder som
ingår i systemet gäller den svenska trafikförsäkringen, så du behöver inte köpa lokal
försäkring.</p>
{_t('Grönt kort — var det krävs',
    ['Krav', 'Länder'],
    [['Grönt kort behövs inte', 'Alla EU-länder, Andorra, Bosnien-Hercegovina, Island, '
      'Liechtenstein, Montenegro, Norge, Schweiz, Serbien och Storbritannien'],
     ['Grönt kort krävs', 'Albanien, Azerbajdzjan, Marocko, Moldavien, Nordmakedonien, '
      'Tunisien, Turkiet och Ukraina'],
     ['Särskild gränsförsäkring', 'Kosovo — köps vid gränsstationen']],
    swipe=False)}
<div class="src"><p>Källa: {_l(TFF_GRONT, 'Trafikförsäkringsföreningen, grönt kort')}
(hämtat oktober 2026). Kontrollera listan före avresa — den kan ändras.</p></div>
<p>Kommer du till ett land som kräver grönt kort utan att ha det måste du köpa en
gränsförsäkring vid gränsen. Den täcker skador som bilen orsakar andra, men inte din egen bil.
Ta också med registreringsbeviset och försäkringsbeviset — vissa länder kräver att du kan visa
dem.</p>

<h2>Så beställer du grönt kort</h2>
<p>Du beställer kortet från ditt försäkringsbolag. Bolaget utfärdar det för den tid du planerar
att vara utomlands, som längst för den period försäkringen är betald. Gör det i god tid före
resan — kortet ska finnas med i bilen.</p>

{_cta('Se vad helförsäkring kostar inför resan')}

<h2>Vad gäller för halv- och helförsäkring utomlands?</h2>
<p>Den <a href="/trafikforsakring/">obligatoriska trafikförsäkringen</a> täcker skador på andra
enligt reglerna i landet där olyckan sker. Skydd för din egen bil — stöld, brand, glas,
räddning och vagnskada — kommer från din <a href="/halvforsakring/">halvförsäkring</a> eller
<a href="/helforsakring/">helförsäkring</a>. Enligt Konsumenternas Försäkringsbyrå upphör halv-
eller helförsäkringen ofta efter cirka 180 dagar i sträck utomlands, och därefter gäller bara
trafikförsäkringen ({_l(KONS_UTL, 'Konsumenternas, köra egen bil utomlands')}, hämtat oktober
2026). Det kan också finnas geografiska begränsningar — fråga ditt bolag före resan.</p>
{_t('Ditt skydd utomlands',
    ['Del', 'Gäller utomlands?', 'Att kontrollera'],
    [['Trafikförsäkring', 'Ja, i gröna kort-länderna', 'Grönt kort där det krävs'],
     ['Halvförsäkring', 'Ofta, med tidsgräns', 'Hur länge och i vilka länder'],
     ['Räddning och hemtransport', 'Ofta, ingår i halv', 'Vem du ringer vid stopp'],
     ['Vagnskada (hel)', 'Ofta, med tidsgräns', 'Självrisk utomlands'],
     ['Vagnskadegaranti', 'Nej, bara i Sverige', 'Behövs helförsäkring för resan?']],
    swipe=False)}
<p>Har bilen <a href="/vagnskadegaranti/">vagnskadegaranti</a> i stället för vagnskadeförsäkring
är det viktigt att veta att garantin bara gäller i Sverige. Kör du på semester i Europa med en
ny bil på halvförsäkring saknar du alltså skydd för skador du själv orsakar på bilen.</p>

<h2>Om olyckan är framme</h2>
<ul>
<li>Ha en skadeanmälningsblankett i bilen och fyll i den tillsammans med motparten.</li>
<li>Kontakta alltid ditt försäkringsbolag vid akuta åtgärder som bärgning och reparation.</li>
<li>Är motparten vållande hanteras skadan av det utländska bolagets representant i Sverige,
enligt reglerna i landet där olyckan skedde. Trafikförsäkringsföreningen kan hjälpa dig hitta
representanten.</li>
<li>Ofta krävs en skadeanmälan underskriven av båda parter eller en polisrapport.</li>
</ul>

<h2>Hyrbil utomlands</h2>
<p>Hyr du bil utomlands gäller normalt inte din egen bilförsäkring för hyrbilen — det är
uthyrarens försäkring som gäller. Konsumenternas råder dig att kontrollera i hyresavtalet vad
självrisken är, eftersom den kan vara mycket hög ({_l(KONS_HYR, 'Konsumenternas, hyra bil utomlands')}). Innan du köper till självriskskydd hos uthyraren:</p>
<ul>
<li>Kontrollera om din hemförsäkring eller reseförsäkring har ett självriskskydd för hyrbil.</li>
<li>Kontrollera ditt betalkort — många kortföretag står för en del av självrisken om hyrbilen
betalas med kortet.</li>
<li>Skilj på självriskreducering (ersättning upp till ett belopp) och självriskeliminering
(hela självrisken ersätts).</li>
</ul>

<h2>Längre vistelser och flytt</h2>
<p>Ska bilen vara utomlands en längre period — en vintersäsong i Spanien eller ett halvår i
arbete — räcker det inte att tänka på resan. Halv- och helförsäkringen kan upphöra efter en viss
tid, och då gäller bara trafikförsäkringen. Fråga ditt bolag hur länge skyddet gäller och om det
går att förlänga. Flyttar du permanent och registrerar bilen i ett annat land är det det landets
regler som gäller, och den svenska försäkringen ska sägas upp när bilen avregistreras i Sverige.
Läs mer om att <a href="/saga-upp-bilforsakring/">säga upp bilförsäkringen</a>.</p>

<h2>Före avresan</h2>
{_t('Checklista',
    ['Kontrollera', 'Varför'],
    [['Grönt kort', 'Krävs i vissa länder utanför EU/EES'],
     ['Registrerings- och försäkringsbevis', 'Kan behöva visas'],
     ['Hur länge halv/hel gäller utomlands', 'Ofta en tidsgräns'],
     ['Räddningsnumret till ditt bolag', 'Vid stopp eller olycka'],
     ['Hyrbilens självrisk', 'Kan vara mycket hög']],
    swipe=False)}
</div></section>''',
 'faq_h2': 'Vanliga frågor om bilförsäkring utomlands',
 'faq': [
   ('Gäller min bilförsäkring i Europa?',
    'Trafikförsäkringen gäller i hela EU och EES samt i flera andra länder, bland annat '
    'Schweiz, Storbritannien och Serbien. Halv- och helförsäkringen gäller ofta också, men '
    'med tidsgränser — enligt Konsumenternas upphör de ofta efter cirka 180 dagar utomlands.'),
   ('Vilka länder kräver grönt kort?',
    'Enligt Trafikförsäkringsföreningen krävs grönt kort i Albanien, Azerbajdzjan, Marocko, '
    'Moldavien, Nordmakedonien, Tunisien, Turkiet och Ukraina. I Kosovo köper du en särskild '
    'gränsförsäkring vid gränsen.'),
   ('Hur får jag ett grönt kort?',
    'Du beställer det från ditt försäkringsbolag. Bolaget utfärdar det för den tid du '
    'planerar att vara utomlands, som längst för den period försäkringen är betald. Beställ i '
    'god tid före resan.'),
   ('Gäller vagnskadegarantin utomlands?',
    'Nej, vagnskadegarantin gäller bara i Sverige. Har du halvförsäkring och vagnskadegaranti '
    'saknar du skydd för egenvållade skador på bilen när du kör utomlands.'),
   ('Täcker min bilförsäkring en hyrbil utomlands?',
    'Normalt inte. Det är uthyrarens försäkring som gäller. Kontrollera självrisken i '
    'hyresavtalet och om din hemförsäkring, reseförsäkring eller ditt betalkort har ett '
    'självriskskydd för hyrbil.'),
 ],
 'rel': [('/trafikforsakring/', 'Vad trafikförsäkringen täcker'),
         ('/helforsakring/', 'Helförsäkring och vagnskada'),
         ('/vagnskadegaranti/', 'Vagnskadegaranti gäller bara i Sverige'),
         ('/halvforsakring/', 'Räddning och hemtransport i halvförsäkring'),
         ('/sjalvrisk/', 'Självrisk vid skada')],
},

]
