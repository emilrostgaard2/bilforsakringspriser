# -*- coding: utf-8 -*-
"""Innehållet till bilforsakringspriser.se.

VIKTIGT OM PRISERNA
Alla belopp nedan är markerade med klassen "warn" och texten PLATSHÅLLARE.
De är INTE verifierade marknadspriser. Innan lansering ska de ersättas med
egna siffror insamlade från bolagens offentliga prislistor och från
Konsumenternas Försäkringsbyrå. Se README.md.
"""

TODO = ('<div class="warn"><strong>PLATSHÅLLARE — ska ersättas före lansering.</strong> '
        'Beloppen på den här sidan är exempelsiffror och inte insamlade marknadspriser. '
        'Fyll i egna uppgifter från bolagens prislistor innan sidan publiceras.</div>')

METOD = ('<div class="src"><p><strong>Så räknar vi.</strong> Alla priser gäller samma '
         'jämförelseprofil: 40 år, 15 000 km/år, ort utanför storstad, sex skadefria år '
         'och 4 000 kr i självrisk. Ändras en förutsättning ändras priset — ofta mycket. '
         'Läs mer i vår <a href="/redaktionell-metod/">redaktionella metod</a>.</p></div>')

PAGES = [

# ═══ START ═════════════════════════════════════════════════════════
{
 'slug': '', 'key': True,
 'title': 'Bilförsäkringspriser 2026 — jämför pris på trafik, halv och hel',
 'desc': 'Vad kostar en bilförsäkring? Jämför priser på trafikförsäkring, '
         'halvförsäkring och helförsäkring. Ange registreringsnumret och se ditt pris.',
 'eyebrow': 'Uppdaterad januari 2026',
 'h1': 'Vad kostar din bilförsäkring?',
 'lead': 'Skillnaden mellan billigaste och dyraste bolag är ofta flera tusen kronor om året '
         'för exakt samma bil. Här ser du vad de olika skyddsnivåerna kostar — och vad du '
         'faktiskt får för pengarna.',
 'checks': ['Tre skyddsnivåer förklarade: trafik, halv och hel',
            'Priser på samma jämförelseprofil, så att de går att ställa mot varandra',
            'Oberoende betyg från Konsumenternas Försäkringsbyrå'],
 'card_note': 'Det tar under två minuter',
 'sticky': 'Jämför bilförsäkring gratis',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Trafikförsäkring är det lagstadgade minimum
och täcker bara skador på andra. Halvförsäkring lägger till stöld, brand, glas och
räddning. Helförsäkring är den enda som ersätter skador på din egen bil vid en olycka
du själv orsakat.</p></div>

<div class="stats">
<div class="stat"><span class="stat-n">36</span><span class="stat-l">bilförsäkringar granskade av Konsumenternas</span></div>
<div class="stat"><span class="stat-n">1–5</span><span class="stat-l">betygsskala för villkoren</span></div>
<div class="stat"><span class="stat-n">3</span><span class="stat-l">skyddsnivåer att välja mellan</span></div>
<div class="stat"><span class="stat-n">23</span><span class="stat-l">länsbolag bara hos Länsförsäkringar</span></div>
</div>

<h2>De tre skyddsnivåerna</h2>
<p>Nästan all förvirring kring bilförsäkring handlar om skillnaden mellan de tre nivåerna.
Här är den kortaste möjliga förklaringen.</p>

<div class="tbl"><table>
<caption>Vad respektive nivå täcker</caption>
<thead><tr><th scope="col">Skydd</th><th scope="col">Trafik</th><th scope="col">Halv</th><th scope="col">Hel</th></tr></thead>
<tbody>
<tr><th scope="row">Lagstadgat</th><td>Ja</td><td>Nej</td><td>Nej</td></tr>
<tr><th scope="row">Skador på andra</th><td>Ja</td><td>Ja</td><td>Ja</td></tr>
<tr><th scope="row">Stöld och brand</th><td>Nej</td><td>Ja</td><td>Ja</td></tr>
<tr><th scope="row">Glas och räddning</th><td>Nej</td><td>Ja</td><td>Ja</td></tr>
<tr><th scope="row">Maskinskada</th><td>Nej</td><td>Ofta</td><td>Ofta</td></tr>
<tr><th scope="row">Egen bil vid egen vållad olycka</th><td>Nej</td><td>Nej</td><td>Ja</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<p>Skillnaden mellan halv och hel heter <strong>vagnskada</strong>. Det är den delen som
ersätter din egen bil när du kört in i något, blivit påkörd av en okänd förare eller
råkat ut för skadegörelse. På en nyare bil är det den viktigaste delen av hela försäkringen.</p>

<div class="grid">
<a class="gc" href="/trafikforsakring/"><span class="gc-t">Trafikförsäkring</span>
<span class="gc-d">Lagkravet. Vad det täcker, vad det inte täcker och vad trafikförsäkringsavgiften kostar om du struntar i den.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/halvforsakring/"><span class="gc-t">Halvförsäkring</span>
<span class="gc-d">Mellannivån. Passar bilar som är för värdefulla för enbart trafik men för gamla för hel.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/helforsakring/"><span class="gc-t">Helförsäkring</span>
<span class="gc-d">Full täckning med vagnskada. När den är nödvändig — och när den är onödig.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
</div>
</div></section>

<section class="sec alt"><div class="wrap narrow">
<h2>Vad påverkar priset mest?</h2>
<p>Bolagen väger faktorerna olika, och det är därför samma bil och samma förare kan få
offerter som skiljer flera tusen kronor. Det här är de sex som väger tyngst.</p>

<h3>1. Ålder och körvana</h3>
<p>Den enskilt största faktorn. En förare under 25 utan skadefria år betalar ofta det
dubbla mot en 45-åring med samma bil. Att stå som medförsäkrad på en förälders försäkring
bygger inte upp egen skadefri tid — det är en vanlig och dyr missuppfattning.</p>

<h3>2. Bostadsort</h3>
<p>Postnumret avgör risken för stöld och skadegörelse. Skillnaden mellan en storstadsdel
och en mindre ort kan vara 30–40 procent på exakt samma bil.</p>

<h3>3. Bilmodell och värde</h3>
<p>Reservdelspriser och skadefrekvens per modell är dokumenterade hos bolagen. En bil med
dyra delar och hög stöldrisk kostar mer, oavsett hur försiktigt du kör.</p>

<h3>4. Självrisk</h3>
<p>Den faktor du själv styr mest. Höjer du självrisken sjunker premien — men du ska kunna
betala beloppet den dag något händer.</p>

<h3>5. Årlig körsträcka</h3>
<p>Många överskattar sin körsträcka när de tecknar. Att rätta från 2 000 mil till 1 200 mil
tar fem minuter och märks direkt på premien.</p>

<h3>6. Skadefria år</h3>
<p>Skadefri tid följer dig, inte bilen. Byter du bolag ska du se till att den registreras
korrekt — annars börjar du om från noll.</p>

{METOD}
</div></section>

<section class="sec"><div class="wrap narrow">
<h2>Oberoende betyg — och varför de är värda att läsa</h2>
<p>Konsumenternas Försäkringsbyrå granskar villkoren i svenska bilförsäkringar och sätter
betyg från 1 till 5. De säljer ingenting och arbetar inte på uppdrag av något bolag, vilket
gör dem till den mest opartiska källan på marknaden.</p>
<p>I deras genomgång av 36 bilförsäkringar delade Länsförsäkringar, Paydrive och
Watercircles förstaplatsen bland grundprodukterna med 4,2 poäng. Bland de mest omfattande
försäkringarna låg Gjensidige Plus och Länsförsäkringar med alla tillägg i topp med 4,5 poäng.</p>
<div class="src"><p>Källa: Konsumenternas Försäkringsbyrå, jämförelse av 36 bilförsäkringar,
februari 2025. Betygen avser villkorens innehåll, inte priset.</p></div>

<h2>Guider för din situation</h2>
<p>Premien räknas fram olika beroende på vem du är och hur bilen används. Fem guider som tar
den vanligaste situationen först.</p>

<div class="grid">
<a class="gc" href="/billigaste-bilforsakringen/"><span class="gc-t">Billigaste bilförsäkringen</span>
<span class="gc-d">Vad som styr priset, vad du kan påverka och varför lägst pris inte alltid är billigast.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/bilforsakring-elbil/"><span class="gc-t">Elbil</span>
<span class="gc-d">Batteri, laddkabel och laddbox — vad som täcks av bilförsäkringen och vad som inte gör det.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/bilforsakring-ung-forare/"><span class="gc-t">Ung förare</span>
<span class="gc-d">Varför premien är högst under 25, vad ungdomssjälvrisk är och vilka genvägar som kostar.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/bilforsakring-pensionar/"><span class="gc-t">Pensionär</span>
<span class="gc-d">Körsträckan är den största hävstången när pendlingen försvinner.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
<a class="gc" href="/leasingbil-forsakring/"><span class="gc-t">Leasingbil</span>
<span class="gc-d">Leasinggivaren äger bilen och ställer kraven. Så läser du avtalet före offerten.</span>
<span class="gc-go">Läs guiden &rarr;</span></a>
</div>

<div class="cta">
<h2>Se ditt eget pris</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt. Kostnadsfritt och utan bindning.</p>
<div class="cta-inner">{{PLATE}}</div>
</div>
</div></section>''',
 'faq': [
   ('Vad kostar en bilförsäkring i Sverige?',
    'Priset beror på bil, ålder, bostadsort, körsträcka och vald självrisk. Skillnaden mellan '
    'billigaste och dyraste bolag är ofta flera tusen kronor om året för samma bil. Därför är '
    'det bara en offert på ditt eget registreringsnummer som ger ett rättvisande svar.'),
   ('Vad är skillnaden mellan halvförsäkring och helförsäkring?',
    'Helförsäkring innehåller vagnskada, som ersätter skador på din egen bil vid en olycka du '
    'själv orsakat. Halvförsäkring gör det inte. I övrigt täcker båda stöld, brand, glas, '
    'räddning och rättsskydd.'),
   ('Måste jag ha bilförsäkring?',
    'Ja. Trafikförsäkring är lagstadgad för alla fordon i trafik. Kör du utan betalar du en '
    'trafikförsäkringsavgift till Trafikförsäkringsföreningen som är betydligt dyrare än '
    'premien du sparat.'),
   ('När kan jag byta bilförsäkring?',
    'Normalt vid huvudförfallodagen med en månads uppsägningstid. Du kan även byta direkt vid '
    'bilköp, flytt eller om bolaget aviserar en premiehöjning.'),
   ('Följer mina skadefria år med när jag byter bolag?',
    'Ja, men bara om du ser till att de registreras. Be det gamla bolaget om ett intyg och '
    'kontrollera på första fakturan från det nya att åren finns med.'),
 ],
 'rel': [('/jamfor-bilforsakring/', 'Jämför bilförsäkring — så gör du'),
         ('/trafikforsakring/', 'Trafikförsäkring — lagkravet förklarat'),
         ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
         ('/helforsakring/', 'Helförsäkring — när behövs den?'),
         ('/redaktionell-metod/', 'Så samlar vi in priserna')],
},

# ═══ JÄMFÖR ════════════════════════════════════════════════════════
{
 'slug': 'jamfor-bilforsakring', 'key': True,
 'title': 'Jämför bilförsäkring 2026 — så hittar du rätt pris',
 'desc': 'Så jämför du bilförsäkring på riktigt: samma självrisk, samma tillägg och '
         'offerter i stället för listpriser. Steg för steg.',
 'eyebrow': 'Guide',
 'h1': 'Jämför bilförsäkring',
 'lead': 'Att jämföra bilförsäkring är inte svårt — det är omständligt. Här är metoden som '
         'gör att du faktiskt jämför samma sak, och inte bara läser prislappar bredvid varandra.',
 'checks': ['Jämför offerter, inte listpriser',
            'Sätt samma självrisk hos alla bolag innan du tittar på priset',
            'Kontrollera vad som redan ingår innan du köper till'],
 'sticky': 'Hämta din offert',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Ett listpris säger nästan ingenting.
Två offerter till samma belopp kan ha olika självrisk, olika tillägg och olika
verkstadsvillkor. Ställ in samma förutsättningar hos alla bolag — sedan är siffran meningsfull.</p></div>

<h2>Steg 1: Bestäm skyddsnivån först</h2>
<p>Innan du tittar på en enda krona ska du veta om du behöver trafik, halv eller hel.
Tumregeln handlar om bilens marknadsvärde: är den värd mindre än ungefär 30 000 kronor
blir vagnskadan sällan lönsam, eftersom ersättningen ändå begränsas av vad bilen är värd.</p>
<p>Har du en nyare bil finns ofta en <strong>vagnskadegaranti</strong> från tillverkaren de
första åren. Då är halvförsäkring tillräckligt, och att betala för helförsäkring innebär
att du köper samma skydd två gånger. Kontrollera garantins slutdatum i bilens papper.</p>

<h2>Steg 2: Lås självrisken</h2>
<p>Det här är det vanligaste felet. Ett bolag visar ett lägre pris helt enkelt för att
offerten har högre självrisk. Bestäm dig för ett belopp — 3 000, 4 000 eller 8 000 kronor —
och begär offert med exakt det hos samtliga.</p>

<h2>Steg 3: Kontrollera vad som redan ingår</h2>
<p>Bolagen paketerar olika. Assistans, hyrbil, maskinskada och allrisk kan vara inkluderade
hos ett bolag och kosta extra hos ett annat. Det billigaste grundpriset blir ibland det
dyraste totalpriset när du lagt till det du faktiskt behöver.</p>

<div class="tbl"><table>
<caption>Kontrollista att gå igenom för varje offert</caption>
<thead><tr><th scope="col">Punkt</th><th scope="col">Varför den spelar roll</th></tr></thead>
<tbody>
<tr><th scope="row">Självrisk</th><td>Måste vara samma i alla offerter för att de ska gå att jämföra</td></tr>
<tr><th scope="row">Vagnskada</th><td>Avgör skillnaden mellan halv och hel</td></tr>
<tr><th scope="row">Hyrbil</th><td>Antal dagar och om ersättningen är i pengar eller bil</td></tr>
<tr><th scope="row">Maskinskada</th><td>Gäller normalt bara upp till viss ålder och körsträcka</td></tr>
<tr><th scope="row">Verkstadsval</th><td>Fritt val eller bolagets nätverk — påverkar väntetid</td></tr>
<tr><th scope="row">Glas</th><td>Reparation är ofta gratis, byte kostar självrisk</td></tr>
<tr><th scope="row">Bindningstid</th><td>Vissa bolag har kortare uppsägningstid än ett år</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<h2>Steg 4: Räkna på hela året, inte månaden</h2>
<p>Månadspriser döljer skillnader. Fyrtio kronor i månaden låter försumbart och är
480 kronor om året. Jämför alltid årsbelopp.</p>

<h2>Steg 5: Ta in offerten innan du säger upp</h2>
<p>Den nya försäkringen ska börja gälla samma dag som den gamla upphör. Ett enda dygn
utan trafikförsäkring är olagligt och kan kosta betydligt mer än du sparat.</p>

{TODO}
{METOD}

<h2>Jämförelseschema — fyll i innan du väljer</h2>
<p>Det här är hela metoden på en sida. Skriv av tabellen, hämta tre offerter och fyll i den
kolumn för kolumn. Är två rutor olika mellan två offerter är priserna inte jämförbara, och
då ska du rätta offerten innan du jämför beloppen.</p>
<div class="tbl"><table>
<caption>Ta med samma uppgifter till varje bolag</caption>
<thead><tr><th scope="col">Post</th><th scope="col">Bolag 1</th><th scope="col">Bolag 2</th>
<th scope="col">Bolag 3</th></tr></thead>
<tbody>
<tr><th scope="row">Skyddsnivå</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Årspremie</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Grundsjälvrisk</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Vagnskadesjälvrisk</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Glassjälvrisk vid lagning</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Hyrbil, antal dagar</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Maskinskada, till vilken ålder</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Fritt verkstadsval</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Nykundsrabatt år ett</th><td>—</td><td>—</td><td>—</td></tr>
<tr><th scope="row">Pris år två utan rabatt</th><td>—</td><td>—</td><td>—</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<h2>Sju fällor som gör jämförelsen missvisande</h2>
<p>Nästan alla prisskillnader som ser dramatiska ut på papperet visar sig vid närmare
granskning bero på något av det här. Gå igenom listan innan du drar slutsatsen att ett bolag
är billigare än ett annat.</p>
<div class="tbl"><table>
<caption>Vanliga fel vid jämförelse</caption>
<thead><tr><th scope="col">Fällan</th><th scope="col">Varför den lurar dig</th>
<th scope="col">Så undviker du den</th></tr></thead>
<tbody>
<tr><th scope="row">Nykundsrabatt i priset</th>
<td>Rabatten gäller ofta bara första året</td><td>Fråga vad premien blir år två</td></tr>
<tr><th scope="row">Olika självrisk i offerterna</th>
<td>Högre självrisk ger lägre premie, inte bättre affär</td>
<td>Lås samma nivå i alla offerter</td></tr>
<tr><th scope="row">Månadspris mot årspris</th>
<td>Månadsbetalning innehåller normalt ett påslag</td><td>Räkna alltid om till år</td></tr>
<tr><th scope="row">Tillägg som redan ingår hos ett bolag</th>
<td>Den dyrare offerten kan innehålla mer</td><td>Jämför innehåll rad för rad</td></tr>
<tr><th scope="row">Fel körsträcka</th>
<td>Låg angiven sträcka ger lågt pris — och nedsatt ersättning</td>
<td>Ange den sträcka du faktiskt kör</td></tr>
<tr><th scope="row">Samlingsrabatt som förutsätter flytt av hemförsäkringen</th>
<td>Priset gäller bara om du flyttar allt</td><td>Be om priset utan samlingsrabatt</td></tr>
<tr><th scope="row">Bonus som inte registrerats</th>
<td>Offerten kan utgå från noll skadefria år</td><td>Skicka intyg innan du jämför</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<h2>Vad som är värt mest i villkoren</h2>
<p>Två offerter med samma pris kan skilja med tusenlappar den dag något händer. Det här är de
poster där skillnaderna mellan bolagen är störst, rangordnade efter hur ofta de faktiskt
utlöses.</p>
<div class="tbl"><table>
<caption>Villkorsposter i fallande ordning efter praktisk betydelse</caption>
<thead><tr><th scope="col">Post</th><th scope="col">Hur ofta den används</th>
<th scope="col">Vad du ska titta på</th></tr></thead>
<tbody>
<tr><th scope="row">Glassjälvrisk</th><td>Mycket ofta</td>
<td>Skillnaden mellan lagning och byte</td></tr>
<tr><th scope="row">Hyrbil</th><td>Ofta</td><td>Antal dagar och andel av kostnaden</td></tr>
<tr><th scope="row">Räddning och assistans</th><td>Ofta</td>
<td>Om hemtransport ingår, och varifrån</td></tr>
<tr><th scope="row">Maskinskada</th><td>Regelbundet på äldre bilar</td>
<td>Till vilken ålder och körsträcka den gäller</td></tr>
<tr><th scope="row">Djurkollision</th><td>Säsongsvis, mest höst</td>
<td>Om självrisken reduceras eller faller bort</td></tr>
<tr><th scope="row">Allrisk eller drulle</th><td>Sällan, men dyrt</td>
<td>Om den ingår eller kostar extra</td></tr>
<tr><th scope="row">Rättsskydd</th><td>Sällan</td><td>Takbeloppet vid tvist</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>
<p>Vill du gå djupare på självriskerna finns en genomgång av alla typer på sidan om
<a href="/sjalvrisk/">självrisk</a>, och en förklaring av hur bonusen påverkar priset under
<a href="/bonus-och-skadefria-ar/">skadefria år</a>.</p>

<h2>Var du hämtar offerterna</h2>
<p>Det finns tre vägar, och de ger olika svar. Använd helst två av dem, eftersom ingen enskild
källa täcker hela marknaden.</p>
<div class="tbl"><table>
<caption>Tre sätt att hämta pris</caption>
<thead><tr><th scope="col">Väg</th><th scope="col">Styrka</th><th scope="col">Svaghet</th></tr></thead>
<tbody>
<tr><th scope="row">Bolagets egen sajt</th><td>Exakt pris, alla rabatter räknas in</td>
<td>Tar tid — fem till tio minuter per bolag</td></tr>
<tr><th scope="row">Jämförelsetjänst</th><td>Flera offerter från ett formulär</td>
<td>Bara anslutna bolag, och tjänsten får provision</td></tr>
<tr><th scope="row">Ditt nuvarande bolag</th><td>Kan matcha ett konkurrerande pris</td>
<td>Sker sällan utan att du frågar uttryckligen</td></tr>
</tbody></table></div>
<p>Ett samtal till det nuvarande bolaget med en konkret offert i handen är den mest
underskattade åtgärden i hela processen. Har du ett skriftligt pris från en konkurrent är
det en förhandling, inte en förfrågan.</p>

<h2>När på året du bör jämföra</h2>
<p>Du får byta vid huvudförfallodagen med en månads uppsägningstid, vilket i praktiken betyder
att jämförelsen ska göras ungefär sex veckor innan. Sätt en påminnelse — datumet står på
försäkringsbrevet och är sällan detsamma som när du tecknade. Utöver det finns fyra
tillfällen då du får byta omgående: vid bilköp, vid ägarbyte, vid flytt och när bolaget
aviserar en premiehöjning. Det sista är det som flest missar, och det är samtidigt det bästa
förhandlingsläget du får. Hela regelverket står på sidan om
<a href="/byta-bilforsakring/">att byta bilförsäkring</a>.</p>

<h2>Om du bara har tio minuter</h2>
<p>Gör tre saker, i den här ordningen. Kontrollera att körsträckan i din nuvarande försäkring
stämmer med hur mycket du faktiskt kör. Kontrollera att alla dina skadefria år är
registrerade. Hämta sedan en offert hos ett bolag du inte har i dag, på exakt samma
skyddsnivå och självrisk. De tre stegen tar tio minuter tillsammans och fångar upp det mesta
av det som brukar vara fel. Vill du gå vidare därifrån är
<a href="/billigaste-bilforsakringen/">genomgången av vad som styr priset</a> nästa steg,
och <a href="/basta-bilforsakringen/">vår sammanställning av bolagen</a> hjälper dig välja
vilka du ska begära offert från.</p>

<div class="cta">
<h2>Börja med registreringsnumret</h2>
<p>Bilens uppgifter hämtas automatiskt. Du fyller inte i märke, modell eller årsmodell.</p>
<div class="cta-inner">{{PLATE}}</div>
</div>
</div></section>''',
 'faq': [
   ('Är jämförelsetjänster gratis?',
    'Ja för dig som konsument. Tjänsterna får ersättning från försäkringsbolagen när någon '
    'tecknar en försäkring. Det påverkar inte ditt pris, men det är värt att veta att inte '
    'alla bolag finns med hos alla tjänster.'),
   ('Varför får jag olika pris hos olika bolag för samma bil?',
    'Bolagen väger riskfaktorerna olika. Ett bolag kan vara hårt på ålder men milt på '
    'bostadsort, ett annat tvärtom. Därför lönar det sig att jämföra även om din situation '
    'inte har ändrats.'),
   ('Hur ofta bör jag jämföra?',
    'En gång om året vid huvudförfallodagen. Har du bytt bil, flyttat eller passerat en '
    'åldersgräns är det värt att göra det direkt.'),
   ('Påverkar en jämförelse min kreditvärdighet?',
    'Nej. Att begära offert på en bilförsäkring innebär ingen kreditupplysning. Det gäller '
    'däremot lån, som vissa jämförelsetjänster också förmedlar.'),
 ],
 'rel': [('/', 'Vad kostar bilförsäkring?'),
         ('/halvforsakring/', 'Halvförsäkring — vad ingår?'),
         ('/helforsakring/', 'Helförsäkring — när behövs den?'),
         ('/redaktionell-metod/', 'Så samlar vi in priserna')],
},

# ═══ TRAFIKFÖRSÄKRING ══════════════════════════════════════════════
{
 'slug': 'trafikforsakring', 'key': True,
 'title': 'Trafikförsäkring 2026 — lagkravet, priset och avgiften',
 'desc': 'Trafikförsäkring är lagstadgad i Sverige. Se vad den täcker, vad den inte '
         'täcker och vad trafikförsäkringsavgiften kostar om du kör oförsäkrad.',
 'eyebrow': 'Skyddsnivå 1 av 3',
 'h1': 'Trafikförsäkring',
 'lead': 'Det lagstadgade minimum. Den ersätter personskador och skador du orsakar på '
         'andras egendom — men inte en krona på din egen bil.',
 'checks': ['Obligatorisk för alla fordon som används i trafik',
            'Täcker personskador och skador på annans egendom',
            'Täcker aldrig skador på din egen bil'],
 'sticky': 'Se pris på trafikförsäkring',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Trafikförsäkring är enligt trafikskadelagen
obligatorisk för alla fordon i trafik. Den ersätter personskador — både dina och andras —
samt skador du orsakar på annans egendom. Din egen bil ingår inte.</p></div>

<h2>Vad trafikförsäkringen täcker</h2>
<ul>
<li>Personskador på förare, passagerare och andra trafikanter</li>
<li>Skador du orsakar på andras fordon och egendom</li>
<li>Skador på fasta föremål som staket, lyktstolpar och räcken</li>
</ul>

<h2>Vad den inte täcker</h2>
<ul>
<li>Skador på din egen bil — oavsett vem som orsakat dem</li>
<li>Stöld av bilen eller av saker i den</li>
<li>Brand, glasskador och skadegörelse</li>
<li>Bärgning och assistans vid driftstopp</li>
</ul>

<div class="warn"><p><strong>Den vanligaste missuppfattningen.</strong> Blir du påkörd av
någon annan ersätter <em>deras</em> trafikförsäkring din bil. Men är du själv vållande —
eller är motparten okänd, till exempel vid en parkeringsskada — står du utan ersättning
med enbart trafikförsäkring.</p></div>

<h2>Om du kör utan försäkring</h2>
<p>Ett fordon som är påställt i vägtrafikregistret ska vara trafikförsäkrat. Saknas
försäkringen tar Trafikförsäkringsföreningen ut en trafikförsäkringsavgift för varje dag
fordonet varit oförsäkrat. Avgiften är medvetet satt högre än vad en försäkring hade kostat,
just för att det inte ska löna sig att avstå.</p>
<p>Ska bilen stå still en period är lösningen att ställa av den i vägtrafikregistret — då
upphör både skatt och försäkringsplikt. Men den får inte köras, inte ens en kort sträcka.</p>

<h2>När räcker trafikförsäkring?</h2>
<p>I praktiken bara i två fall: bilen är värd så lite att en reparation ändå inte skulle
göras, eller så används den i princip inte. För allt däröver blir mellanskillnaden till
halvförsäkring liten i förhållande till vad du får.</p>

{TODO}
{METOD}

<div class="cta">
<h2>Ersättningen har ingen övre gräns för personskador</h2>
<p>Det här är den del av trafikförsäkringen som är svårast att föreställa sig, och samtidigt
den viktigaste. Ersättning för personskador enligt trafikskadelagen är inte beloppsbegränsad.
En allvarlig personskada kan innebära livslång ersättning för inkomstförlust, vård och
merkostnader — belopp som ingen privatperson skulle kunna betala själv. Ersättning för
skador på annans egendom är däremot begränsad, till 300 miljoner kronor per skadehändelse.
Det är den obegränsade personskadedelen som är hela skälet till att försäkringen är
lagstadgad.</p>

<div class="tbl"><table>
<caption>Vem som får ersättning ur trafikförsäkringen</caption>
<thead><tr><th scope="col">Skadad part</th><th scope="col">Ersätts ur din trafikförsäkring</th>
<th scope="col">Kommentar</th></tr></thead>
<tbody>
<tr><th scope="row">Du som förare</th><td>Ja, personskada</td>
<td>Även om du själv orsakat olyckan</td></tr>
<tr><th scope="row">Dina passagerare</th><td>Ja, personskada</td>
<td>Oavsett vem som var vållande</td></tr>
<tr><th scope="row">Motpartens förare och passagerare</th><td>Ja, personskada</td>
<td>Om du var vållande</td></tr>
<tr><th scope="row">Fotgängare och cyklister</th><td>Ja, personskada</td>
<td>Skyddet är starkt för oskyddade trafikanter</td></tr>
<tr><th scope="row">Motpartens bil</th><td>Ja, sakskada</td><td>Om du var vållande</td></tr>
<tr><th scope="row">Staket, lyktstolpar, byggnader</th><td>Ja, sakskada</td>
<td>Annans egendom omfattas</td></tr>
<tr><th scope="row">Din egen bil</th><td>Nej</td>
<td>Kräver helförsäkring, eller halvförsäkring vid brand och stöld</td></tr>
<tr><th scope="row">Saker i din egen bil</th><td>Nej</td>
<td>Hör till halvförsäkringen eller hemförsäkringen</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<h2>När ersättningen kan sättas ned</h2>
<p>Trafikförsäkringen är stark, men den är inte villkorslös. Ersättningen till dig själv kan
jämkas — alltså sättas ned — om du orsakat skadan under vissa omständigheter. Det påverkar
inte ersättningen till oskyldiga tredje parter, som alltid får sitt.</p>
<div class="tbl"><table>
<caption>Situationer som påverkar din egen ersättning</caption>
<thead><tr><th scope="col">Situation</th><th scope="col">Konsekvens</th></tr></thead>
<tbody>
<tr><th scope="row">Rattfylleri</th><td>Ersättningen till dig kan jämkas kraftigt</td></tr>
<tr><th scope="row">Grov vårdslöshet</th><td>Ersättningen till dig kan jämkas</td></tr>
<tr><th scope="row">Uppsåtlig skada</th><td>Ingen ersättning till den som orsakat den</td></tr>
<tr><th scope="row">Bilkörning utan körkort</th><td>Kan påverka ersättningen och är brottsligt</td></tr>
<tr><th scope="row">Passagerare i bilen</th><td>Får ersättning oavsett förarens beteende</td></tr>
</tbody></table></div>

<h2>Om motparten är oförsäkrad eller okänd</h2>
<p>Blir du påkörd av ett fordon som saknar trafikförsäkring, eller av en förare som kör från
platsen, ersätts din personskada ändå — av Trafikförsäkringsföreningen, som träder in i
det försäkringsbolagets ställe. Det är samma organisation som tar ut
<a href="/trafikforsakringsavgift/">trafikförsäkringsavgiften</a> av dem som kör oförsäkrat,
och avgifterna är det som finansierar skyddet. Skador på din egen bil vid smitning ersätts
dock inte den vägen — det regleras på vagnskadedelen i en
<a href="/helforsakring/">helförsäkring</a>, vilket är ett av de starkaste argumenten för
att inte nöja sig med trafikförsäkring i tätort.</p>

<h2>Utomlands och med släp</h2>
<p>Svensk trafikförsäkring gäller i hela EU och EES utan särskild åtgärd. Utanför det området
kan grönt kort krävas — kontrollera med bolaget innan avresa. Ett släpvagn som är kopplat
till bilen omfattas av bilens trafikförsäkring när det gäller skador släpet orsakar på annan,
men skador på själva släpet kräver egen försäkring. Samma logik som för bilen alltså: det
lagstadgade skyddet handlar om andra, inte om din egen egendom.</p>

<h2>Jämför trafikförsäkring</h2>
<p>Ange registreringsnumret och se priset hos flera bolag.</p>
<div class="cta-inner">{{PLATE}}</div>
</div>
</div></section>''',
 'faq': [
   ('Är trafikförsäkring obligatorisk?',
    'Ja. Enligt trafikskadelagen ska alla fordon som används i trafik ha trafikförsäkring. '
    'Kravet gäller så länge fordonet är påställt i vägtrafikregistret.'),
   ('Täcker trafikförsäkringen min egen bil?',
    'Nej. Den ersätter personskador och skador du orsakar på andras egendom. Skador på din '
    'egen bil kräver halv- eller helförsäkring.'),
   ('Vad händer om jag kör oförsäkrad?',
    'Trafikförsäkringsföreningen tar ut en avgift för varje dag fordonet varit oförsäkrat. '
    'Avgiften är avsiktligt högre än en vanlig premie.'),
   ('Kan jag slippa försäkring om bilen står still?',
    'Ja, men bara om du ställer av den i vägtrafikregistret. Då upphör försäkringsplikten — '
    'men bilen får inte köras.'),
 ],
 'rel': [('/halvforsakring/', 'Halvförsäkring — nästa nivå'),
         ('/helforsakring/', 'Helförsäkring — full täckning'),
         ('/jamfor-bilforsakring/', 'Så jämför du rätt'),
         ('/', 'Vad kostar bilförsäkring?')],
},

# ═══ HALVFÖRSÄKRING ════════════════════════════════════════════════
{
 'slug': 'halvforsakring', 'key': True,
 'title': 'Halvförsäkring bil 2026 — vad ingår och vad kostar den?',
 'desc': 'Halvförsäkring täcker stöld, brand, glas, räddning och rättsskydd utöver '
         'trafikförsäkringen. Se vad som ingår och när den räcker.',
 'eyebrow': 'Skyddsnivå 2 av 3',
 'h1': 'Halvförsäkring',
 'lead': 'Mellannivån, och för många bilar den mest rationella. Den täcker allt utom '
         'skador på din egen bil vid en olycka du själv orsakat.',
 'checks': ['Innehåller trafikförsäkringen plus stöld, brand, glas och räddning',
            'Saknar vagnskada — det är skillnaden mot helförsäkring',
            'Räcker ofta för bilar med vagnskadegaranti kvar'],
 'sticky': 'Se pris på halvförsäkring',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Halvförsäkring är trafikförsäkring plus ett
antal delmoment: stöld, brand, glas, räddning, rättsskydd och hos de flesta bolag även
maskinskada. Det som saknas är vagnskadan.</p></div>

<h2>Vad som normalt ingår</h2>
<div class="tbl"><table>
<caption>Delmoment i en typisk halvförsäkring</caption>
<thead><tr><th scope="col">Moment</th><th scope="col">Vad det innebär</th></tr></thead>
<tbody>
<tr><th scope="row">Stöld</th><td>Stöld av bilen, stöldförsök och skador i samband med inbrott</td></tr>
<tr><th scope="row">Brand</th><td>Brand, blixtnedslag och explosion</td></tr>
<tr><th scope="row">Glas</th><td>Sprickor och stenskott i rutor. Reparation är ofta gratis</td></tr>
<tr><th scope="row">Räddning</th><td>Bärgning vid driftstopp eller olycka</td></tr>
<tr><th scope="row">Rättsskydd</th><td>Ombudskostnader vid tvist som rör bilen</td></tr>
<tr><th scope="row">Maskinskada</th><td>Motor och drivlina, upp till viss ålder och körsträcka</td></tr>
<tr><th scope="row">Kris</th><td>Samtalsstöd efter en allvarlig händelse</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<h2>Det som inte ingår</h2>
<p>Vagnskada. Kör du in i ett räcke, backar in i en stolpe eller blir påkörd av någon som
smiter, står du utan ersättning för din egen bil. Det är hela skillnaden mot helförsäkring
— och för en nyare bil ofta den viktigaste delen.</p>

<h2>När halvförsäkring är rätt val</h2>
<ul>
<li><strong>Bilen har vagnskadegaranti kvar.</strong> Nya bilar har normalt garanti från
tillverkaren de första åren. Under den tiden köper en helförsäkring samma skydd två gånger.</li>
<li><strong>Bilen är värd 30 000–70 000 kronor.</strong> Vagnskadans ersättning begränsas av
marknadsvärdet, och premieskillnaden blir svår att räkna hem.</li>
<li><strong>Du kör lite.</strong> Låg körsträcka betyder lägre risk för just den typ av
skada vagnskadan täcker.</li>
</ul>

<div class="warn"><p><strong>Kontrollera maskinskadan.</strong> Den ingår hos de flesta men
gäller normalt bara upp till en viss ålder och körsträcka — ofta åtta år eller tio tusen mil.
Passerar bilen gränsen försvinner momentet utan att premien nödvändigtvis sjunker.</p></div>

{TODO}
{METOD}

<div class="cta">
<h2>Momenten ett och ett — vad de faktiskt gör</h2>
<p>Halvförsäkring säljs som ett paket, men den är sex eller sju separata skydd i samma avtal.
Det är först när man tittar på dem var för sig som det blir tydligt vilka som är värda något
för just din bil, och var bolagen faktiskt skiljer sig åt.</p>
<div class="tbl"><table>
<caption>Halvförsäkringens delar</caption>
<thead><tr><th scope="col">Moment</th><th scope="col">Vad det ersätter</th>
<th scope="col">Var bolagen skiljer sig</th></tr></thead>
<tbody>
<tr><th scope="row">Stöld</th><td>Stöld av bilen och inbrott i den</td>
<td>Krav på godkänt stöldskydd, och självriskens storlek</td></tr>
<tr><th scope="row">Brand</th><td>Brand, blixtnedslag, explosion</td>
<td>Om kortslutning i elsystemet räknas som brand</td></tr>
<tr><th scope="row">Glas</th><td>Vindruta, sidorutor, bakruta</td>
<td>Skillnaden mellan lagning och byte — ofta stor</td></tr>
<tr><th scope="row">Räddning</th><td>Bärgning och hemtransport</td>
<td>Om resan hem för passagerarna ingår</td></tr>
<tr><th scope="row">Rättsskydd</th><td>Ombudskostnader vid tvist om bilen</td>
<td>Takbeloppet</td></tr>
<tr><th scope="row">Maskinskada</th><td>Fel på motor, växellåda, styrsystem</td>
<td>Åldersgräns och körsträckegräns</td></tr>
<tr><th scope="row">Kris</th><td>Samtalsstöd efter en olycka</td>
<td>Antal behandlingar, ingår inte överallt</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<h2>Maskinskadedelen är den som tar slut först</h2>
<p>Maskinskada gäller bara upp till en viss ålder och körsträcka — gränserna varierar mellan
bolagen, och när bilen passerar dem försvinner momentet utan att premien nödvändigtvis
sjunker. Det är värt att kontrollera vid varje förnyelse, eftersom det är just på en äldre
bil man tror sig ha skyddet kvar. En motorskada på en bil som passerat gränsen är
ägarens problem, oavsett vilken nivå som står på försäkringsbrevet.</p>

<h2>Räkna på om halvförsäkring räcker</h2>
<p>Frågan är egentligen enkel: vad skulle du förlora om bilen blev totalskadad i en olycka du
själv orsakat? Det är precis den situation halvförsäkringen inte täcker. Sätt bilens
marknadsvärde mot vagnskadesjälvrisken, så ser du hur mycket
<a href="/helforsakring/">helförsäkringen</a> faktiskt kan betala ut.</p>
<div class="tbl"><table>
<caption>Vad vagnskadedelen skulle betala vid totalskada</caption>
<thead><tr><th scope="col">Bilens marknadsvärde</th><th scope="col">Vid 4 000 kr självrisk</th>
<th scope="col">Rimlig nivå</th></tr></thead>
<tbody>
<tr><th scope="row">15 000 kr</th><td>Cirka 11 000 kr</td><td>Trafik eller halv</td></tr>
<tr><th scope="row">30 000 kr</th><td>Cirka 26 000 kr</td><td>Halvförsäkring</td></tr>
<tr><th scope="row">60 000 kr</th><td>Cirka 56 000 kr</td><td>Halv eller hel — räkna på premien</td></tr>
<tr><th scope="row">120 000 kr</th><td>Cirka 116 000 kr</td><td>Helförsäkring</td></tr>
</tbody></table></div>
<p>Beloppen är räkneexempel på självrisken, inte prisuppgifter. Poängen är proportionen:
på en bil värd 15 000 kronor kostar vagnskadedelen mer i premie under några år än den
någonsin kan betala ut.</p>

<h2>Halvförsäkring på en bil som står i stan</h2>
<p>En invändning mot resonemanget ovan gäller om bilen står på gatan i en tätort.
Parkeringsskador utan känd motpart och skadegörelse regleras nämligen båda på vagnskadedelen,
och de drabbar bilar oavsett värde. Står bilen i garage på landsbygden är halvförsäkring
oftast rätt långt ned i värdeskalan — står den på gatan i
<a href="/bilforsakring-stockholm/">Stockholm</a> eller
<a href="/bilforsakring-malmo/">Malmö</a> förskjuts gränsen uppåt.</p>

<h2>Jämför halvförsäkring</h2>
<p>Ange registreringsnumret och se vad de olika bolagen tar.</p>
<div class="cta-inner">{{PLATE}}</div>
</div>
</div></section>''',
 'faq': [
   ('Vad är skillnaden mellan halvförsäkring och helförsäkring?',
    'Vagnskada. Helförsäkring ersätter skador på din egen bil vid en olycka du själv orsakat '
    'eller vid skadegörelse. Halvförsäkring gör det inte. Övriga moment är i stort sett lika.'),
   ('Ingår maskinskada i halvförsäkringen?',
    'Hos de flesta bolag, men bara upp till en viss ålder och körsträcka. Gränsen ligger ofta '
    'kring åtta år eller tio tusen mil. Kontrollera villkoren för just din bil.'),
   ('Täcker halvförsäkring stenskott?',
    'Ja, glasmomentet ingår. Reparation av ett stenskott är ofta kostnadsfri, medan ett helt '
    'rutbyte kostar självrisk. Laga skottet innan det spricker vidare.'),
   ('När ska jag gå från halv till hel?',
    'När bilens vagnskadegaranti går ut och bilen fortfarande är värd så mycket att du inte '
    'skulle klara en reparation ur egen ficka.'),
 ],
 'rel': [('/helforsakring/', 'Helförsäkring — full täckning'),
         ('/trafikforsakring/', 'Trafikförsäkring — lagkravet'),
         ('/jamfor-bilforsakring/', 'Så jämför du rätt'),
         ('/', 'Vad kostar bilförsäkring?')],
},

# ═══ HELFÖRSÄKRING ═════════════════════════════════════════════════
{
 'slug': 'helforsakring', 'key': True,
 'title': 'Helförsäkring bil 2026 — vagnskada, pris och när den behövs',
 'desc': 'Helförsäkring innehåller vagnskada och ersätter skador på din egen bil. '
         'Se när den är nödvändig, när den är onödig och vad den kostar.',
 'eyebrow': 'Skyddsnivå 3 av 3',
 'h1': 'Helförsäkring',
 'lead': 'Den enda nivån som ersätter din egen bil när du själv är vållande. Nödvändig på '
         'en nyare bil — och ofta bortkastad på en gammal.',
 'checks': ['Innehåller halvförsäkringen plus vagnskada',
            'Krävs nästan alltid vid leasing och billån',
            'Sällan lönsam när bilen är värd under 30 000 kronor'],
 'sticky': 'Se pris på helförsäkring',
 'body': f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Helförsäkring är halvförsäkring plus
vagnskada. Vagnskadan ersätter skador på din egen bil vid trafikolycka, skadegörelse och
annan yttre olyckshändelse — även när du själv orsakat dem.</p></div>

<h2>Vad vagnskadan täcker</h2>
<ul>
<li>Kollision där du själv är vållande</li>
<li>Dikeskörning och singelolyckor</li>
<li>Skadegörelse och parkeringsskador där motparten är okänd</li>
<li>Annan yttre olyckshändelse, som fallande föremål</li>
</ul>

<h2>När helförsäkring är nödvändig</h2>
<p><strong>Vid leasing och billån.</strong> Långivaren har säkerhet i bilen och kräver
i praktiken alltid helförsäkring. Kontraktet sätter ofta även ett tak för självrisken,
vilket betyder att det bästa spartipset — att höja självrisken — inte är tillgängligt för dig.</p>
<p><strong>På nyare bilar utan garanti kvar.</strong> När vagnskadegarantin gått ut och
bilen fortfarande är värd hundratusen eller mer är helförsäkring det enda som står mellan
dig och en oväntad räkning.</p>

<h2>När den är onödig</h2>
<p>Har bilen kvar sin vagnskadegaranti betalar du för samma skydd två gånger. Garantin gäller
normalt de första åren och framgår av bilens papper — kolla slutdatumet innan du tecknar.</p>
<p>Är bilen värd under ungefär 30 000 kronor begränsas ersättningen ändå av marknadsvärdet.
Då blir mellanskillnaden mellan halv och hel svår att räkna hem.</p>

<div class="warn"><p><strong>Restskuld är en egen risk.</strong> Vid totalskada ersätter
försäkringen bilens marknadsvärde. Är lånet större än så får du betala mellanskillnaden
själv. Det gäller särskilt de första åren, då värdeminskningen är brantast.</p></div>

<h2>Tillägg som ofta är värda pengarna</h2>
<ul>
<li><strong>Hyrbil.</strong> Har hushållet en bil märks ett verkstadsbesök direkt. Kontrollera
antal dagar och om du får bil eller kontant ersättning.</li>
<li><strong>Sänkt självrisk vid skadegörelse.</strong> Relevant om bilen står på gatan.</li>
<li><strong>Allrisk.</strong> Täcker missöden som inte passar in någon annanstans.</li>
</ul>

{TODO}
{METOD}

<div class="cta">
<h2>Skadetyperna som bara helförsäkringen tar</h2>
<p>Vagnskada beskrivs ofta som skyddet vid egen vållad krock, men det är den minst vanliga av
de situationer där momentet används. De flesta vagnskadeärenden handlar om något helt annat.</p>
<div class="tbl"><table>
<caption>Vanliga vagnskadeärenden</caption>
<thead><tr><th scope="col">Situation</th><th scope="col">Varför halvförsäkring inte hjälper</th></tr></thead>
<tbody>
<tr><th scope="row">Någon backar in i din parkerade bil och kör vidare</th>
<td>Ingen känd motpart att kräva ersättning av</td></tr>
<tr><th scope="row">Skadegörelse på gatan</th><td>Gärningspersonen är okänd</td></tr>
<tr><th scope="row">Du kör in i en stolpe eller en garageport</th><td>Du är själv vållande</td></tr>
<tr><th scope="row">Du kör i diket på halka</th><td>Ingen motpart finns</td></tr>
<tr><th scope="row">Grus från en lastbil skadar plåten</th>
<td>Motparten går sällan att identifiera</td></tr>
<tr><th scope="row">Du backar in i en annan bil</th><td>Din egen skada ersätts inte</td></tr>
</tbody></table></div>
<p>Mönstret är att det inte finns någon annan att skicka räkningen till. Det är exakt den
luckan vagnskadedelen fyller, och det är också därför den är den dyraste delen av premien.</p>

<h2>Vagnskadegaranti — därför kan en ny bil klara sig med halv</h2>
<p>Nya bilar säljs normalt med vagnskadegaranti från tillverkaren, oftast i tre år från första
registrering. Den täcker samma sak som vagnskadedelen, vilket betyder att helförsäkring är
onödig under garantitiden — halvförsäkring räcker. Två saker är värda att veta: garantin
gäller reparation hos märkesverkstad, och den upphör på dagen. Sätt en påminnelse när
treårsdagen närmar sig, för därefter står bilen utan vagnskadeskydd om ingen gör något.</p>
<div class="tbl"><table>
<caption>Skyddsnivå över bilens livslängd</caption>
<thead><tr><th scope="col">Bilens ålder</th><th scope="col">Vagnskadeskydd kommer från</th>
<th scope="col">Rimlig nivå</th></tr></thead>
<tbody>
<tr><th scope="row">0–3 år</th><td>Vagnskadegaranti från tillverkaren</td>
<td>Halvförsäkring</td></tr>
<tr><th scope="row">3–8 år</th><td>Vagnskadeförsäkring</td><td>Helförsäkring</td></tr>
<tr><th scope="row">8–12 år</th><td>Vagnskadeförsäkring, om värdet motiverar</td>
<td>Hel eller halv — räkna</td></tr>
<tr><th scope="row">Över 12 år</th><td>Sällan värt premien</td><td>Ofta halvförsäkring</td></tr>
</tbody></table></div>
<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>

<h2>Vagnskadesjälvrisken är den du kan påverka mest</h2>
<p>Till skillnad från glas- och stöldsjälvrisken är vagnskadesjälvrisken ofta valbar, och
spannet är brett. Att höja den är den mest direkta hävstången på premien som finns i en
helförsäkring — men bara om du klarar beloppet den dag det smäller. Tumregeln är att
mellanskillnaden ska gå ihop inom tre skadefria år, annars är höjningen inte värd det. Räkna
på det med hjälp av tabellen på sidan om <a href="/sjalvrisk/">självrisk</a>.</p>

<h2>Vad som händer vid totalskada</h2>
<p>Bilen bedöms som totalskadad när reparationen kostar mer än vad bilen är värd. Då får du
marknadsvärdet minus självrisken, inte vad du en gång betalade och inte vad en likvärdig bil
kostar hos en handlare. Skillnaden överraskar många, särskilt på bilar som är tre till fem år
gamla och har tappat mycket i värde. Det är också därför bilens restvärde är en faktor värd
att väga in redan vid bilköpet — märken som håller värdet ger mer tillbaka den dagen, vilket
du kan läsa mer om på våra <a href="/bilmarken/">märkessidor</a>.</p>

<h2>Jämför helförsäkring</h2>
<p>Ange registreringsnumret och se vad full täckning kostar hos olika bolag.</p>
<div class="cta-inner">{{PLATE}}</div>
</div>
</div></section>''',
 'faq': [
   ('Vad är vagnskada?',
    'Vagnskada ersätter skador på din egen bil vid trafikolycka, skadegörelse eller annan '
    'yttre olyckshändelse — även när du själv är vållande. Det är det enda som skiljer '
    'helförsäkring från halvförsäkring.'),
   ('Behöver jag helförsäkring om bilen har vagnskadegaranti?',
    'Nej. Under garantitiden täcker tillverkaren vagnskadan, och en helförsäkring innebär att '
    'du köper samma skydd två gånger. Kontrollera garantins slutdatum i bilens papper.'),
   ('Krävs helförsäkring vid leasing?',
    'I praktiken alltid. Leasingbolaget har säkerhet i bilen och accepterar sällan lägre '
    'skydd. Kontraktet kan dessutom sätta ett tak för hur hög självrisk du får välja.'),
   ('Lönar sig helförsäkring på en gammal bil?',
    'Sällan. Ersättningen begränsas av marknadsvärdet, så på en bil värd under ungefär '
    '30 000 kronor är halvförsäkring oftast det rationella valet.'),
 ],
 'rel': [('/halvforsakring/', 'Halvförsäkring — mellannivån'),
         ('/trafikforsakring/', 'Trafikförsäkring — lagkravet'),
         ('/jamfor-bilforsakring/', 'Så jämför du rätt'),
         ('/', 'Vad kostar bilförsäkring?')],
},

# ═══ OM OSS ════════════════════════════════════════════════════════
{
 'slug': 'om-oss',
 'title': 'Om Bilförsäkringspriser.se — oberoende jämförelse av bilförsäkring',
 'desc': 'Vilka vi är, hur vi arbetar och hur vi finansierar sajten. Vi säljer inga '
         'försäkringar och företräder inget bolag.',
 'eyebrow': 'Om sajten',
 'h1': 'Om oss',
 'lead': 'Bilförsäkringspriser.se är en oberoende jämförelsesajt för bilförsäkring. Vi '
         'säljer ingenting, förmedlar ingenting och företräder inget försäkringsbolag.',
 'checks': ['Ingen ägarkoppling till något försäkringsbolag',
            'Inga placeringar kan köpas',
            'Allt kommersiellt innehåll är märkt'],
 'sticky': 'Jämför bilförsäkring gratis',
 'body': '''
<section class="sec"><div class="wrap narrow">
<h2>Vad vi gör</h2>
<p>Vi samlar och förklarar priser och villkor på svenska bilförsäkringar, så att du kan
fatta ett beslut utan att först behöva lära dig branschens språk. Vi räknar på samma
jämförelseprofil varje gång, så att siffrorna går att ställa mot varandra.</p>

<h2>Vad vi inte gör</h2>
<p>Vi är inte försäkringsförmedlare. Vi ger inte individuell rådgivning, tecknar inga
försäkringar och har inget uppdrag att agera för din räkning. Innehållet är allmän
information — ditt eget pris och dina egna villkor får du hos bolaget.</p>

<h2>Vem som står bakom</h2>
<p>Emil Rostgaard Clausen, grundare och redaktör. Jag arbetar med sökmotoroptimering och
driver jämförelsesajter — inte med försäkringar. Jag är alltså ingen försäkringsexpert, och
den här sajten bygger inte på branschbakgrund utan på ett hantverk: att samla in uppgifter
systematiskt, ställa dem mot varandra på ett sätt som faktiskt går att jämföra, och alltid
redovisa var siffrorna kommer ifrån.</p>
<p>Bakgrunden är att jag sedan flera år driver motsvarande jämförelsesajter i Danmark, och
att jag där märkte hur svårt det är att få ett rakt svar på vad en bilförsäkring egentligen
kostar. Samma sak gäller i Sverige. Allt innehåll här är skrivet av mig utifrån bolagens
egna villkor och offentliga källor.</p>
<p>Det innebär också en gräns jag håller: jag skriver om hur försäkringarna fungerar och vad
de kostar, men jag rekommenderar inte vilken försäkring just du ska välja. Behöver du
oberoende vägledning i ett eget ärende är <a href="https://www.konsumenternas.se/"
rel="nofollow noopener" target="_blank">Konsumenternas Försäkringsbyrå</a> kostnadsfri och
säljer ingenting.</p>
<p>Hittar du ett fel, en föråldrad siffra eller något som är otydligt formulerat — hör av
dig. Jag rättar sakfel så snart jag kan och noterar väsentliga rättelser på sidan.</p>

<h2>Kontakt</h2>
<p>E-post: <a href="mailto:info@bilforsakringspriser.se">info@bilforsakringspriser.se</a></p>

<div class="src"><p>Läs mer om hur vi samlar in priser, vad som avgör en placering och hur
sajten finansieras i vår <a href="/redaktionell-metod/">redaktionella metod</a>.</p></div>
</div></section>''',
 'rel': [('/redaktionell-metod/', 'Redaktionell metod'),
         ('/integritetspolicy/', 'Integritetspolicy'),
         ('/cookiepolicy/', 'Cookiepolicy'),
         ('/', 'Vad kostar bilförsäkring?')],
},

# ═══ REDAKTIONELL METOD ════════════════════════════════════════════
{
 'slug': 'redaktionell-metod',
 'title': 'Redaktionell metod — så samlar vi in priser och tjänar pengar',
 'desc': 'Vår jämförelseprofil, våra källor, vad som avgör en placering och hur sajten '
         'finansieras. Full transparens.',
 'eyebrow': 'Transparens',
 'h1': 'Redaktionell metod',
 'lead': 'Den här sidan beskriver hur innehållet blir till, så att du själv kan bedöma om '
         'våra siffror är att lita på — och var du bör vara kritisk.',
 'checks': ['En fast jämförelseprofil för alla priser',
            'Källorna anges alltid',
            'Ingen placering kan köpas'],
 'sticky': 'Jämför bilförsäkring gratis',
 'body': '''
<section class="sec"><div class="wrap narrow">
<h2>Jämförelseprofilen</h2>
<p>Alla priser räknas på samma profil, så att de går att jämföra mellan bolag och sidor:</p>
<div class="tbl"><table>
<thead><tr><th scope="col">Parameter</th><th scope="col">Värde</th></tr></thead>
<tbody>
<tr><th scope="row">Ålder</th><td>40 år</td></tr>
<tr><th scope="row">Skadefria år</th><td>6</td></tr>
<tr><th scope="row">Körsträcka</th><td>1 500 mil per år</td></tr>
<tr><th scope="row">Bostadsort</th><td>Ort utanför de tre storstadsregionerna</td></tr>
<tr><th scope="row">Självrisk</th><td>4 000 kr</td></tr>
</tbody></table></div>
<p>Ändras en parameter ändras priset, ofta kraftigt. Siffrorna på sajten är därför
<strong>uppskattningar för jämförelse</strong> — inte offerter. Ditt eget pris ska alltid
hämtas hos bolaget.</p>

<h2>Källor</h2>
<ul>
<li>Konsumenternas Försäkringsbyrå — oberoende betygsättning av villkor</li>
<li>Bolagens egna offentligt tillgängliga prislistor och villkor</li>
<li>Finansinspektionens register över tillståndspliktiga bolag</li>
<li>Trafikförsäkringsföreningen för uppgifter om trafikförsäkringsavgift</li>
</ul>
<p>Vi använder aldrig den egna sajten som källa till egna påståenden, och vi hänvisar inte
till konkurrerande jämförelsesajter som dokumentation.</p>

<h2>Vad som avgör en placering</h2>
<p>Rangordningar bygger på pris för jämförelseprofilen. Betyg och omdömen som kommer från
Konsumenternas Försäkringsbyrå återges med källhänvisning och är inte våra egna
bedömningar. <strong>Ingen placering kan köpas.</strong> Ordningen skulle vara densamma
utan våra kommersiella avtal.</p>

<h2>Så finansieras sajten</h2>
<p>Sajten är gratis att använda. Vi får ersättning när någon klickar vidare via en
jämförelselänk och därefter tecknar en försäkring. Ersättningen påverkar inte ditt pris
och inte vår rangordning. Alla kommersiella länkar är märkta i koden med
<code>rel="sponsored"</code>.</p>

<h2>Uppdatering och rättelser</h2>
<p>Priser kontrolleras kvartalsvis. Ändrar ett bolag sina villkor mellan två kontroller kan
det dröja innan det slår igenom här. Hittar du ett fel, skriv till
<a href="mailto:info@bilforsakringspriser.se">info@bilforsakringspriser.se</a> — vi rättar
och skriver vad som rättats.</p>

<h2>Oberoende</h2>
<p>Vi ägs inte av, är inte anställda hos och finansieras inte av något försäkringsbolag.
Inget bolag får läsa texter innan publicering eller påverka formuleringar och placeringar.</p>
</div></section>''',
 'rel': [('/om-oss/', 'Om oss'),
         ('/integritetspolicy/', 'Integritetspolicy'),
         ('/jamfor-bilforsakring/', 'Så jämför du rätt')],
},

# ═══ INTEGRITETSPOLICY ═════════════════════════════════════════════
{
 'slug': 'integritetspolicy',
 'title': 'Integritetspolicy — Bilförsäkringspriser.se',
 'desc': 'Vilka personuppgifter vi behandlar, varför, hur länge och vilka rättigheter du '
         'har enligt dataskyddsförordningen.',
 'eyebrow': 'Juridik',
 'h1': 'Integritetspolicy',
 'lead': 'Vilka uppgifter vi behandlar, på vilken grund, hur länge vi sparar dem och vilka '
         'rättigheter du har. Senast uppdaterad januari 2026.',
 'checks': ['Du behöver inget konto för att läsa sajten',
            'Vi sparar inga registreringsnummer',
            'Du kan när som helst återkalla ditt samtycke'],
 'sticky': 'Jämför bilförsäkring gratis',
 'body': '''
<section class="sec"><div class="wrap narrow">
<h2>1. Personuppgiftsansvarig</h2>
<p>Bilförsäkringspriser.se är personuppgiftsansvarig för behandlingen av de uppgifter som
samlas in i samband med att du använder sajten. Kontakt:
<a href="mailto:info@bilforsakringspriser.se">info@bilforsakringspriser.se</a>.</p>
<div class="warn"><p><strong>Att fylla i före lansering:</strong> juridiskt namn,
organisationsnummer och postadress.</p></div>

<h2>2. Vilka uppgifter vi behandlar</h2>
<p>Du kan läsa hela sajten utan att skapa konto eller lämna personuppgifter.</p>
<h3>Registreringsnummer</h3>
<p>Anger du ett registreringsnummer i jämförelsefältet skickas det med som en parameter i
den adress du förs vidare till hos vår samarbetspartner. <strong>Vi sparar det inte i någon
databas.</strong> Ett registreringsnummer kan under vissa förutsättningar utgöra en
personuppgift, eftersom det går att koppla till en registrerad ägare.</p>
<h3>Tekniska uppgifter</h3>
<p>Webbservern registrerar automatiskt IP-adress, tidpunkt, hämtad sida, webbläsartyp och
hänvisande sida. Uppgifterna används för drift, felsökning och säkerhet.</p>
<h3>Statistik</h3>
<p>Med statistikcookies accepterade samlas aggregerade uppgifter in om vilka sidor som
besöks och på vilken enhetstyp. Syftet är att förbättra innehållet, inte att identifiera dig.</p>

<h2>3. Ändamål och rättslig grund</h2>
<div class="tbl"><table>
<thead><tr><th scope="col">Behandling</th><th scope="col">Ändamål</th><th scope="col">Rättslig grund</th></tr></thead>
<tbody>
<tr><th scope="row">Serverloggar</th><td>Drift och säkerhet</td><td>Berättigat intresse, art. 6.1 f</td></tr>
<tr><th scope="row">Nödvändiga cookies</th><td>Att sajten fungerar</td><td>Undantag i lag om elektronisk kommunikation</td></tr>
<tr><th scope="row">Statistikcookies</th><td>Förbättring av innehåll</td><td>Samtycke, art. 6.1 a</td></tr>
<tr><th scope="row">Vidareförmedling</th><td>Att du ska kunna få en offert</td><td>Din egen åtgärd, art. 6.1 b och f</td></tr>
</tbody></table></div>

<h2>4. Överföring till tredje part</h2>
<p>Klickar du på en jämförelselänk förs du vidare till vår samarbetspartner. Från och med
det att du lämnar sajten gäller partnerns egen integritetspolicy för de uppgifter du lämnar
där. Vi rekommenderar att du läser den.</p>
<p>Med hänvisningen följer tekniska spårningsparametrar — källa, medium och kampanj. De
används för att avräkna hänvisningar och innehåller inga uppgifter som identifierar dig som
person. Vi säljer inga personuppgifter.</p>

<h2>5. Lagringstid</h2>
<ul>
<li>Serverloggar: raderas eller anonymiseras senast efter sex månader</li>
<li>Statistikdata: sparas aggregerat i upp till 26 månader</li>
<li>Registreringsnummer: sparas inte av oss</li>
<li>E-post: raderas när ärendet är avslutat, senast efter två år</li>
</ul>

<h2>6. Dina rättigheter</h2>
<p>Enligt dataskyddsförordningen har du rätt till tillgång, rättelse, radering, begränsning,
invändning och dataportabilitet. Du kan även när som helst återkalla ett lämnat samtycke,
utan att det påverkar lagligheten av behandlingen dessförinnan. Skriv till
<a href="mailto:info@bilforsakringspriser.se">info@bilforsakringspriser.se</a>.</p>

<h2>7. Klagomål</h2>
<p>Är du missnöjd med hur vi behandlar dina uppgifter kan du vända dig till
Integritetsskyddsmyndigheten. Vi vill dock gärna höra från dig först, så att vi får en
chans att rätta till det.</p>

<h2>8. Ändringar</h2>
<p>Vi uppdaterar policyn när behandlingen förändras. Väsentliga ändringar aviseras på
startsidan.</p>
</div></section>''',
 'rel': [('/cookiepolicy/', 'Cookiepolicy'),
         ('/redaktionell-metod/', 'Redaktionell metod'),
         ('/om-oss/', 'Om oss')],
},

# ═══ COOKIEPOLICY ══════════════════════════════════════════════════
{
 'slug': 'cookiepolicy',
 'title': 'Cookiepolicy — Bilförsäkringspriser.se',
 'desc': 'Vilka cookies vi sätter, vad de gör, hur länge de lever och hur du väljer bort dem.',
 'eyebrow': 'Juridik',
 'h1': 'Cookiepolicy',
 'lead': 'Vilka cookies som används, vad de gör och hur du ändrar ditt val. Senast '
         'uppdaterad januari 2026.',
 'checks': ['Nödvändiga cookies kräver inget samtycke',
            'Statistik och marknadsföring kräver att du aktivt säger ja',
            'Du kan ändra ditt val när som helst'],
 'sticky': 'Jämför bilförsäkring gratis',
 'body': '''
<section class="sec"><div class="wrap narrow">
<h2>Vad är en cookie?</h2>
<p>En cookie är en liten textfil som en webbplats sparar i din webbläsare. Den kan komma
ihåg dina val mellan sidvisningar och används för att mäta hur sajten används. Cookies kan
inte sprida virus eller läsa andra filer på din enhet.</p>
<p>Reglerna följer av lagen om elektronisk kommunikation och dataskyddsförordningen. Kort
sagt: cookies som är nödvändiga för att sajten ska fungera får sättas utan ditt samtycke.
Allt annat kräver att du aktivt säger ja.</p>

<h2>Cookies på den här sajten</h2>
<div class="tbl"><table>
<thead><tr><th scope="col">Kategori</th><th scope="col">Ändamål</th><th scope="col">Livslängd</th><th scope="col">Samtycke</th></tr></thead>
<tbody>
<tr><th scope="row">Nödvändiga</th><td>Kommer ihåg ditt cookieval</td><td>Upp till 12 mån</td><td>Krävs ej</td></tr>
<tr><th scope="row">Statistik</th><td>Aggregerad mätning av besök</td><td>Upp till 24 mån</td><td>Krävs</td></tr>
<tr><th scope="row">Marknadsföring</th><td>Mätning av hänvisningar till partner</td><td>Upp till 12 mån</td><td>Krävs</td></tr>
</tbody></table></div>
<p>Vi använder inte cookies för att bygga profiler av enskilda personer, och vi säljer inga
uppgifter om dig.</p>

<h2>Vad händer när du klickar på en jämförelselänk?</h2>
<p>Du förs vidare till vår samarbetspartner med spårningsparametrar i adressen. De talar om
att hänvisningen kom härifrån och från vilken sida. Partnern kan sätta egna cookies på sin
egen domän — det ligger utanför vår kontroll, och du bör läsa deras cookiepolicy.</p>
<p>Spårningen är grunden för att vi kan driva sajten utan att ta betalt av dig. Läs mer i
vår <a href="/redaktionell-metod/">redaktionella metod</a>.</p>

<h2>Så ändrar du ditt val</h2>
<p>Du kan när som helst ändra ditt samtycke via cookieinställningarna längst ned på sidan.
Du kan också radera cookies direkt i webbläsaren:</p>
<ul>
<li><strong>Chrome:</strong> Inställningar → Sekretess och säkerhet → Cookies</li>
<li><strong>Safari:</strong> Inställningar → Avancerat → Hantera webbplatsdata</li>
<li><strong>Firefox:</strong> Inställningar → Sekretess och säkerhet → Kakor och webbplatsdata</li>
<li><strong>Edge:</strong> Inställningar → Cookies och webbplatsbehörigheter</li>
</ul>

<div class="warn"><p><strong>Att göra före lansering:</strong> installera en cookiebanner
som blockerar statistik- och marknadsföringscookies tills samtycke lämnats, och länka den
till den här sidan.</p></div>

<h2>Kontakt</h2>
<p>Frågor om cookies skickas till
<a href="mailto:info@bilforsakringspriser.se">info@bilforsakringspriser.se</a>.
Vill du klaga på vår användning kan du vända dig till Integritetsskyddsmyndigheten.</p>
</div></section>''',
 'rel': [('/integritetspolicy/', 'Integritetspolicy'),
         ('/redaktionell-metod/', 'Redaktionell metod'),
         ('/om-oss/', 'Om oss')],
},
]
