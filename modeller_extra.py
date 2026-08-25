# -*- coding: utf-8 -*-
"""Modellspecifikt tillägg: citerade priser och rena textavsnitt.

VARFÖR FILEN FINNS
modeller.py rymmer grundfakta. Här ligger tre saker till, som är det
som faktiskt avgör om en modellsida rankar:

1. PRISER — publicerade prisuppgifter för just den modellen, med källa,
   profil och datum. Andras siffror, tydligt märkta som andras. Vår
   egen insamling ligger fortfarande i data.PRIS och är tom.
2. DIREKTSVAR — ett svar på fyrtio till sextio ord direkt under en
   frågerubrik. Det är formatet AI-översikter och utvalda utdrag
   plockar. Skriv det som ett fullständigt svar, inte som en inledning.
3. AGARE och JAMFOR — löpande text utan tabell. Sidorna blev tabelltunga
   och det är både sämre att läsa och sämre för långa sökfraser.

KÄLLKRAV FÖR PRISER
Varje post ska ha bolag eller nivå, belopp, källans egen profil, källa
och datum. Saknas något: ta inte med posten. En siffra utan profil är
värdelös eftersom den inte går att jämföra med något.
"""

# ─── Citerade prisuppgifter per modell ─────────────────────────────
PRISER = {
 'xc60': [
  {'vad': 'Trafikförsäkring, lägst i källans jämförelse', 'bolag': 'Evoli',
   'belopp': 'omkring 194 kr/mån', 'profil': 'Källans jämförelse för XC60',
   'kalla': 'Bilförsäkringarna.se', 'datum': 'augusti 2026'},
  {'vad': 'Halvförsäkring, lägst i samma jämförelse', 'bolag': 'Evoli',
   'belopp': 'omkring 281 kr/mån', 'profil': 'Källans jämförelse för XC60',
   'kalla': 'Bilförsäkringarna.se', 'datum': 'augusti 2026'},
  {'vad': 'Helförsäkring, lägst i samma jämförelse', 'bolag': 'Evoli',
   'belopp': 'omkring 501 kr/mån', 'profil': 'Källans jämförelse för XC60',
   'kalla': 'Bilförsäkringarna.se', 'datum': 'augusti 2026'},
  {'vad': 'Snittpris över alla nivåer', 'bolag': 'Samtliga i källans urval',
   'belopp': '472 kr/mån', 'profil': 'XC60, man 31 år, Göteborg, 2 000 mil/år',
   'kalla': 'Försäkras.se', 'datum': 'augusti 2026'},
  {'vad': 'Helförsäkring, spann över årsmodeller', 'bolag': 'Marknaden',
   'belopp': 'cirka 7 000–18 000 kr/år', 'profil': 'Varierar med årsmodell, ort och '
   'körsträcka', 'kalla': 'Försäkringsklok.se', 'datum': 'mars 2026'},
 ],
 'xc40': [
  {'vad': 'Helförsäkring, startpris', 'bolag': 'Premiva',
   'belopp': 'från 549 kr/mån',
   'profil': 'XC40 2019, Göteborg, förare 36 år, 1 500 mil/år',
   'kalla': 'Billigastbilförsäkring.se', 'datum': 'augusti 2026'},
  {'vad': 'Helförsäkring, startpris', 'bolag': 'Compricer',
   'belopp': 'från 580 kr/mån',
   'profil': 'XC40 2019, Göteborg, förare 36 år, 1 500 mil/år',
   'kalla': 'Billigastbilförsäkring.se', 'datum': 'augusti 2026'},
 ],
 'v70': [
  {'vad': 'Helförsäkring, typiskt spann', 'bolag': 'Marknaden',
   'belopp': '350–900 kr/mån',
   'profil': 'Varierar med årsmodell, förarens ålder och bostadsort',
   'kalla': 'BilKoll', 'datum': 'maj 2026'},
  {'vad': 'Helförsäkring, startpris i källans undersökning', 'bolag': 'Lägsta av åtta bolag',
   'belopp': 'från 860 kr/mån', 'profil': 'V70 2013, förare 31 år, Stockholm',
   'kalla': 'Tryggt.nu', 'datum': 'april 2026'},
 ],
}

# Marknadens publicerade spann — används för modeller där vi inte hittat
# modellspecifika uppgifter. Alltid med källa och alltid märkt som
# marknadssiffror, aldrig som modellens pris.
SPANN = [
  {'niva': 'Trafikförsäkring', 'spann': '169–335 kr/mån',
   'kalla': 'Tryggvi', 'datum': 'juli 2026'},
  {'niva': 'Halvförsäkring', 'spann': 'från omkring 260 kr/mån',
   'kalla': 'Försäkras.se', 'datum': 'augusti 2026'},
  {'niva': 'Helförsäkring', 'spann': 'från omkring 347 kr/mån',
   'kalla': 'Försäkras.se', 'datum': 'augusti 2026'},
  {'niva': 'Snitt över alla nivåer', 'spann': '451 kr/mån (5 406 kr/år)',
   'kalla': 'Zmarta', 'datum': '2025'},
]

# ─── Direktsvar och löptext per modell ─────────────────────────────
EXTRA = {

'xc60': {
 'direktsvar':
  'Publicerade prisexempel för Volvo XC60 ligger på omkring 194 kr i månaden för '
  'trafikförsäkring, 281 kr för halvförsäkring och 501 kr för helförsäkring hos det '
  'billigaste bolaget i jämförelserna. Snittet över alla nivåer landar runt 472 kr i '
  'månaden. Ditt eget pris beror på ålder, bostadsort, körsträcka och skadefria år.',
 'agare':
  'Den typiska XC60-ägaren är mellan 40 och 60 år, bor i villa eller radhus och kör mellan '
  '1 200 och 2 000 mil om året. Det är en profil försäkringsbolagen gillar: förutsägbara '
  'körsträckor, bil på egen uppfart och lång skadefri historik. Det är också förklaringen '
  'till att XC60 sällan hamnar högt i premiestatistiken trots att det är en stor och '
  'förhållandevis dyr bil. Andrahandsmarknaden är stor, vilket betyder att många XC60 i dag '
  'ägs av personer som köpt bilen begagnad efter tre år som tjänstebil. Har du gjort det ska '
  'du vara noga med att ange din egen körsträcka och inte utgå från vad bilen kört tidigare — '
  'tjänstebilar rullar ofta dubbelt så långt som privatbilar, och en felaktigt hög uppgift '
  'kostar dig pengar varje månad.',
 'jamfor':
  'Ställd mot en BMW X3 eller Audi Q5 i samma storleksklass ligger XC60 normalt lägre i '
  'premie. Skillnaden handlar inte om bilarnas säkerhet utan om reservdelspriser och '
  'verkstadsnät: Volvo har fler verkstäder per capita i Sverige än de tyska premiummärkena, '
  'och konkurrensen mellan dem pressar reparationskostnaden. Jämfört med den egna V60 ligger '
  'XC60 däremot något högre, eftersom SUV-formatet ger fler parkeringsskador och ett högre '
  'ersättningsvärde.',
 'lang': ('Är Volvo XC60 T8 dyrare att försäkra än bensinversionen?',
  'Ja. T8 Recharge är en laddhybrid med både förbränningsmotor och elektrisk drivlina, vilket '
  'ger fler dyra komponenter och ett högre ersättningsvärde. Räkna med en märkbart högre '
  'premie än på en B4 eller B5, och kontrollera särskilt att batteriet omfattas av '
  'vagnskadedelen.'),
},

'xc40': {
 'direktsvar':
  'Publicerade prisexempel för Volvo XC40 börjar runt 549 kr i månaden för helförsäkring på '
  'en 2019 års modell i Göteborg med en 36-årig förare och 1 500 mil om året. Är du yngre än '
  'så ligger premien högre — XC40 har en yngre ägarprofil än övriga Volvomodeller, och '
  'förarens ålder väger tyngre än bilens storlek.',
 'agare':
  'XC40 är den Volvo som oftast köps av förare under 35, och den enda i utbudet där '
  'ägarprofilen drar upp genomsnittspremien i stället för att hålla den nere. Många exemplar '
  'går på privatleasing, vilket i sig inte påverkar priset men däremot ställer krav på '
  'skyddsnivån: leasingavtal kräver nästan alltid helförsäkring under hela avtalstiden. '
  'Bilen används mycket i pendling, och det märks i skadebilden. Stenskott är '
  'överrepresenterade, inte för att förarna kör hårt utan för att motorvägsmil är den enda '
  'faktor som verkligen styr hur ofta rutan tar skada.',
 'jamfor':
  'Mot en VW T-Roc eller Audi Q3 står sig XC40 väl i premie, framför allt tack vare '
  'delstillgången. Mot syskonet EX40 — samma kaross men eldriven — ligger bensinversionen '
  'lägre, eftersom batteriet utgör en stor del av elbilens ersättningsvärde och arbete på '
  'högvoltssystemet kräver certifierad verkstad. Skillnaden mellan de två är den tydligaste '
  'illustrationen av att drivlinan påverkar premien mer än karossen.',
 'lang': ('Vad kostar det att försäkra en Volvo XC40 för en 25-åring?',
  'Betydligt mer än prisexemplen antyder, eftersom de flesta bygger på förare i 35-årsåldern. '
  'Under 25 tillkommer dessutom ungdomssjälvrisk hos flera bolag, vilket inte syns i '
  'årspremien utan först vid skadan. Jämför alltid på ditt eget registreringsnummer och fråga '
  'uttryckligen om ungdomssjälvrisken.'),
},

'v60': {
 'direktsvar':
  'Volvo V60 hör till de billigare bilarna att försäkra i sin storleksklass. Skadefrekvensen '
  'är lägre än för märkets SUV-modeller, ägarprofilen är äldre och en stor del av beståndet '
  'står på egen uppfart. Marknadens publicerade snitt över alla nivåer ligger på omkring 451 '
  'kr i månaden, och V60 hamnar normalt under det.',
 'agare':
  'V60 ärvde V70:s roll som familjekombin, och därmed också dess ägarprofil: 45 till 65 år, '
  'villa, en till två bilar i hushållet och körsträckor som ligger stadigt kring 1 500 mil om '
  'året. Det är den profil som ger lägst premie av alla, eftersom både ålder, boende och '
  'körsträcka pekar åt samma håll. En stor del av beståndet har gått som tjänstebil de första '
  'tre åren, vilket betyder att begagnatutbudet är stort och att många exemplar har hög '
  'körsträcka men välskött servicehistorik.',
 'jamfor':
  'Mot XC60 ligger V60 normalt lägre, med samma motor och årsmodell. Två saker förklarar det: '
  'kombin har lägre marknadsvärde och drabbas av färre parkeringsskador eftersom den är '
  'smalare och lägre. Mot en Skoda Superb Combi eller VW Passat Sportscombi är skillnaden '
  'liten — alla tre har stora bestånd, god delstillgång och en ägarprofil som bolagen känner '
  'väl.',
 'lang': ('Är Volvo V60 billigare att försäkra än en SUV i samma storlek?',
  'Ja, normalt. Kombiformatet ger färre parkerings- och backningsskador, och marknadsvärdet '
  'är lägre än för en jämngammal XC60. Båda faktorerna drar premien nedåt. Skillnaden är '
  'störst i storstadsområden där parkeringsskador väger tyngst i statistiken.'),
},

'v90': {
 'direktsvar':
  'Volvo V90 kostar mer att försäkra än V60, men mindre än nypriset antyder. Premien följer '
  'marknadsvärdet, och V90 tappar kraftigt i värde de första fyra åren. En begagnad V90 '
  'hamnar därför ofta i samma premieläge som en nyare och mindre bil.',
 'agare':
  'V90 är i hög grad en före detta tjänstebil. Under de tre första åren rullar bilen ofta 3 '
  '000 mil om året i en företagsflotta, för att sedan säljas vidare till en privatägare som '
  'kör en tredjedel så mycket. Det gör att den vanligaste felkällan i offerten på just den här '
  'modellen är körsträckan: många utgår från vad bilen kört, inte vad de själva kommer att '
  'köra. Att rätta den uppgiften är ofta den enskilt största besparingen en V90-ägare kan '
  'göra, och den kostar ingenting i skydd.',
 'jamfor':
  'Mot en Mercedes E-klass kombi eller BMW 5-serie Touring ligger V90 lägre i premie, av samma '
  'skäl som gäller hela Volvos utbud: fler verkstäder och billigare delar. Mot systermodellen '
  'S90 är skillnaden liten i teknik men märkbar i värde — kombin efterfrågas mer på den '
  'svenska begagnatmarknaden och behåller därmed ett högre ersättningsvärde.',
 'lang': ('Vilken skyddsnivå passar en begagnad Volvo V90?',
  'Helförsäkring så länge bilen är värd över 100 000 kr, vilket i praktiken innebär exemplar '
  'upp till omkring sex år. Därefter bör du räkna: vagnskadedelen ersätter marknadsvärdet '
  'minus självrisken, och på en tio år gammal V90 är det utrymmet ofta för litet för att '
  'motivera premien.'),
},

'xc90': {
 'direktsvar':
  'Volvo XC90 ligger högst i premie av Volvos modeller. Bilens värde, storlek och '
  'stöldbegärlighet driver priset, och flera bolag ställer krav på godkänt stöldskydd eller '
  'spårsändare i vissa postnummerområden. Kravet är en förutsättning för ersättning, inte ett '
  'råd.',
 'agare':
  'XC90 köps oftast av barnfamiljer som behöver sju säten och av hushåll som drar släp eller '
  'husvagn. Båda användningarna påverkar försäkringen. Sju passagerare betyder högre '
  'exponering för personskador, vilket trafikdelen täcker utan beloppsgräns. Släpvagnskörning '
  'betyder att du bör kontrollera att släpet har egen försäkring — bilens trafikförsäkring '
  'täcker skador släpet orsakar på annan, men inte skador på släpet självt.',
 'jamfor':
  'Mot BMW X5 och Audi Q7 ligger XC90 något lägre i premie men i samma stöldriskklass. Det är '
  'värt att veta att skillnaden mellan bolagen är större på den här modellen än på mindre '
  'bilar: kraven på stöldskydd varierar, och ett bolag som kräver spårsändare kan ha ett lägre '
  'pris än ett som inte gör det. Jämför därför både premie och krav, inte bara premie.',
 'lang': ('Måste jag ha spårsändare i min Volvo XC90?',
  'Det beror på bolaget och på var du bor. Flera bolag ställer krav på godkänt stöldskydd '
  'eller spårsändare för stora SUV-modeller i vissa postnummerområden. Kravet står i '
  'villkoren, och uppfylls det inte den natt bilen försvinner kan ersättningen sättas ned '
  'eller nekas helt.'),
},

's60': {
 'direktsvar':
  'Volvo S60 kostar ungefär detsamma att försäkra som V60, eftersom bilarna delar teknik, '
  'delkatalog och verkstadsnät. Skillnaden ligger i marknadsvärdet, där kombin står något '
  'starkare på den svenska begagnatmarknaden.',
 'agare':
  'S60 är en ovanlig syn i Sverige jämfört med kombin, och ägarprofilen skiljer sig något: '
  'fler stadsboende, kortare körsträckor och färre släpvagnsdragare. Det påverkar skadebilden '
  'i en riktning som är gynnsam — färre viltolyckor — och en som inte är det, nämligen fler '
  'parkeringsskador. Eftersom beståndet är litet dyker S60 sällan upp i prisjämförelser, och '
  'de siffror som finns bygger nästan alltid på V60. Begär offert på registreringsnumret i '
  'stället för att utgå från listor.',
 'jamfor':
  'Mot en BMW 3-serie eller Audi A4 sedan ligger S60 lägre i premie, framför allt på grund av '
  'reservdelspriserna. Polestar Engineered-versionen är undantaget: den hamnar i en högre '
  'effektklass och prissätts därefter, ofta i nivå med de tyska konkurrenternas '
  'prestandaversioner.',
 'lang': ('Varför hittar jag så få prisexempel på Volvo S60?',
  'För att beståndet är litet. Svenska köpare väljer kombi, och jämförelsesajter utgår från de '
  'vanligaste modellerna. Premien skiljer sig dock marginellt från V60 eftersom bilarna delar '
  'teknik — använd V60-siffror som riktmärke och hämta sedan egen offert.'),
},

's90': {
 'direktsvar':
  'Volvo S90 har det minsta beståndet av Volvos storbilar, vilket gör att bolagens priser '
  'skiljer sig mer på den här modellen än på vanligare bilar. Här lönar det sig särskilt att '
  'begära fler än tre offerter.',
 'agare':
  'S90 har i stor utsträckning gått som representations- och tjänstebil, och en stor del av '
  'beståndet har därför höga körsträckor och hög utrustningsnivå. Det senare påverkar '
  'premien mer än många tror: utrustningsnivån styr ersättningsvärdet, och skillnaden mellan '
  'en enkelt utrustad och en fullt utrustad S90 kan vara sexsiffrig. Kontrollera att offerten '
  'utgår från rätt utrustning — det enklaste är att alltid ange registreringsnumret i stället '
  'för att välja modell i en rullista.',
 'jamfor':
  'Mot Mercedes E-klass och BMW 5-serie ligger S90 lägre i premie men också lägre i '
  'andrahandsvärde. För dig som försäkringstagare är det andra som betyder mest: det är '
  'marknadsvärdet, inte prestigen, som avgör vad vagnskadedelen kan betala ut vid en '
  'totalskada.',
 'lang': ('Är Volvo S90 dyr att försäkra?',
  'Mindre än storleken antyder. Premien beräknas på marknadsvärdet, och S90 tappar snabbt i '
  'värde de första åren. En begagnad S90 hamnar därför ofta i samma premieläge som en nyare '
  'bil i en mindre klass.'),
},

'ex30': {
 'direktsvar':
  'Volvo EX30 kostar mer att försäkra än en bensindriven bil i samma storlek. Batteriet utgör '
  'en stor andel av bilens värde, arbete på högvoltssystemet kräver certifierad verkstad, och '
  'delstillgången har varit ojämn under de första åren. Kontrollera hyrbilsmomentet före allt '
  'annat.',
 'agare':
  'EX30 köps av två ganska olika grupper: hushåll som byter ned från en större bil till en '
  'andrabil, och förstagångsköpare av elbil som lockas av prisläget. Den senare gruppen är '
  'yngre än Volvos genomsnittskund, vilket påverkar premien uppåt. Bilen används mest i stad '
  'och pendling, med korta körsträckor och laddning hemma. Har du laddbox på väggen är det '
  'värt att veta att den normalt hör till villa- eller hemförsäkringen, inte till '
  'bilförsäkringen — medan laddkabeln som följer bilen oftast gör det.',
 'jamfor':
  'Mot en Volvo XC40 med bensinmotor ligger EX30 högre i premie trots att bilen är mindre. Det '
  'är drivlinan, inte storleken, som avgör. Mot andra elbilar i klassen — Smart #1, som delar '
  'plattform, eller en MG4 — är EX30 konkurrenskraftig, men samtliga har samma grundproblem: '
  'kort marknadshistorik gör restvärdet svårbedömt, och några bolag prissätter den osäkerheten.',
 'lang': ('Täcks batteriet i Volvo EX30 av försäkringen?',
  'Batteriet omfattas normalt av samma skydd som resten av bilen, men villkoren skiljer sig '
  'mellan bolagen. Läs särskilt hur kapacitetsförlust behandlas — den räknas ofta som slitage '
  'och inte som skada, och hanteras då av garantin i stället för av försäkringen.'),
},

'ex40': {
 'direktsvar':
  'Volvo EX40 är den eldrivna XC40 och hette tidigare XC40 Recharge. Premien ligger högre än '
  'för bensinversionen, eftersom batteriet utgör en stor del av ersättningsvärdet och '
  'reparationer kräver verkstad med högvoltsbehörighet.',
 'agare':
  'EX40 har till stor del gått som förmånsbil, vilket har gett ett stort begagnatutbud med '
  'relativt låga mil. Den vanligaste fällan vid tecknandet är namnbytet: bilen finns i '
  'bolagens system under både XC40 Recharge och EX40, och en offert kan hamna på fel variant. '
  'Det säkraste är alltid registreringsnumret. Många ägare kommer direkt från en '
  'bensindriven XC40 och blir överraskade av premieskillnaden — den beror inte på att bilen '
  'är sämre utan på att en högvoltsdrivlina kostar mer att laga.',
 'jamfor':
  'Mot XC40 med bensinmotor ligger EX40 högre. Mot en Tesla Model Y eller Hyundai IONIQ 5 är '
  'bilden mer nyanserad: Volvo har fler verkstäder, men Tesla och Hyundai har byggt ut sina '
  'nät snabbt. Det som skiljer mest är hur många dagar hyrbil som ingår, eftersom väntetiden '
  'på delar är den verkliga risken med en elbil på verkstad.',
 'lang': ('Är EX40 och XC40 Recharge samma bil?',
  'Ja. Volvo bytte namn på sina eldrivna modeller, och EX40 är det nya namnet på XC40 '
  'Recharge. Bilen är densamma. Vid tecknandet bör du utgå från registreringsnumret så att '
  'offerten säkert hamnar på rätt variant.'),
},

'v70': {
 'direktsvar':
  'En helförsäkring till Volvo V70 kostar enligt publicerade uppgifter typiskt mellan 350 och '
  '900 kr i månaden beroende på årsmodell, förarens ålder och bostadsort. På de flesta '
  'exemplar är dock halvförsäkring rätt val, eftersom vagnskadedelen sällan kan betala ut mer '
  'än den kostar.',
 'agare':
  'V70 är Sveriges mest sålda bil genom tiderna och fortfarande en av de vanligaste på '
  'vägarna. Ägarna är i dag en blandad grupp: hantverkare som behöver lastutrymme, familjer '
  'som vill ha en billig andrabil och ungdomar som köper sin första bil. Just den sista '
  'gruppen förklarar varför premien på V70 kan se märkligt hög ut i vissa jämförelser — det är '
  'inte bilen som är dyr, det är att en del av beståndet körs av unga förare utan bonus. Är du '
  'över 30 med full bonus får du normalt ett pris långt under de publicerade exemplen.',
 'jamfor':
  'Mot en jämngammal Passat eller Ford Mondeo står sig V70 väl. Delstillgången är utmärkt, '
  'verkstäderna kan bilen och arbetstiden blir därefter. Det som skiljer V70 från nyare bilar '
  'är att den saknar de sensorsystem som gör moderna rutbyten dyra — ett stenskott på en V70 '
  'är fortfarande bara ett stenskott, utan kalibrering efteråt.',
 'lang': ('Lönar sig helförsäkring på en Volvo V70?',
  'Sällan. Vagnskadedelen ersätter marknadsvärdet minus självrisken, och de flesta V70 är i '
  'dag värda mellan 30 000 och 90 000 kr. Med 4 000 kr i självrisk är utrymmet litet i '
  'förhållande till vad vagnskadedelen kostar i premie. Halvförsäkring behåller stöld, brand, '
  'glas och räddning.'),
},
}

# ─── Korta klausuler till metabeskrivningen ────────────────────────
# Max cirka 60 tecken. Skrivna för att rymmas, inte kapas.
META = {
 'xc60': 'Sveriges mest sålda SUV',
 'xc40': 'kompakt SUV med yngre ägarprofil',
 'v60':  'familjekombin med låg skadefrekvens',
 'v90':  'stor kombi, ofta före detta tjänstebil',
 'xc90': 'sjusitsig SUV med krav på stöldskydd',
 's60':  'sedanversionen av V60',
 's90':  'stor sedan med snabb värdeminskning',
 'ex30': 'Volvos minsta elbil',
 'ex40': 'eldrivna XC40, tidigare XC40 Recharge',
 'v70':  'Sveriges mest sålda bil genom tiderna',
}
