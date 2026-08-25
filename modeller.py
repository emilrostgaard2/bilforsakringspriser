# -*- coding: utf-8 -*-
"""Modelldata — underlaget till sidorna på /bilmarken/<märke>/<modell>/.

HUR DEN HÄR FILEN ÄR TÄNKT ATT ANVÄNDAS
Generatorn i modellsidor.py skriver ramverket: rubriker, tabeller,
sektionsordning och de delar som gäller alla bilar. Det som gör varje
sida unik står här — och det är avsiktligt en hel del per modell.

Fyller ni på med fler märken: skriv aldrig av ett fält från en annan
modell. Ett 'vinkel'-stycke som återanvänds mellan två modeller gör
båda sidorna sämre, och två nästan identiska sidor är det enda som
gör riktig skada i det här upplägget.

FÄLT PER MODELL
  slug      URL-del, t.ex. 'xc60' → /bilmarken/volvo/xc60/
  namn      Modellnamnet utan märke, 'XC60'
  typ       Karosstyp, används i rubriker och text
  ar        Generationens år på svenska marknaden
  drivlina  Vad som finns att välja på
  kort      En mening som beskriver bilen — går in i metabeskrivningen
  vinkel    Två till tre meningar om just den här modellens premie
  punkter   Tre korta punkter, syns som lista
  skada     Den skadetyp modellen oftast drabbas av, med förklaring
  varde     Hur bilen står sig i värde — avgör valet av skyddsnivå
  niva      Vilken nivå som brukar vara rimlig, med motivering
  fraga     En modellspecifik fråga och ett svar till FAQ
"""

MODELLER = {

# ═══ VOLVO ═════════════════════════════════════════════════════════
'volvo': [
{
 'slug': 'xc60', 'namn': 'XC60', 'typ': 'mellanstor SUV', 'ar': '2017–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Sveriges mest sålda SUV och en av de vanligaste bilarna i '
         'försäkringsbolagens statistik.',
 'vinkel': 'XC60 ligger i ett gynnsamt läge: beståndet är så stort att varje bolag har '
           'gedigen skadestatistik på just den här modellen, och delarna finns hos alla '
           'verkstäder. Det håller nere premien i förhållande till nypriset. '
           'Laddhybridversionerna T6 och T8 ligger däremot högre, både för att '
           'ersättningsvärdet är högre och för att drivlinan innehåller fler dyra '
           'komponenter.',
 'punkter': ['Stort bestånd ger välunderbyggd skadestatistik',
             'Laddhybrid kostar mer att försäkra än bensinversionen',
             'Förarassistansen bakom vindrutan måste kalibreras vid rutbyte'],
 'skada': 'Parkeringsskador dominerar. XC60 är bred nog att bli trång i äldre '
          'parkeringshus, och de flesta ärenden gäller repor och skador på stötfångare '
          'utan känd motpart — vilket bara vagnskadedelen täcker.',
 'varde': 'Värdet håller sig väl de första fem åren, vilket gör helförsäkring motiverad '
          'längre än på många konkurrenter i samma klass.',
 'niva': 'Helförsäkring på bilar upp till åtta år. Därefter är det värt att räkna på '
         'halvförsäkring, särskilt om bilen står i garage.',
 'fraga': ('Är Volvo XC60 dyr att försäkra?',
           'Nej, sett till nypriset ligger XC60 rimligt. Det stora beståndet och den goda '
           'delstillgången väger upp bilens storlek. Laddhybriderna T6 och T8 ligger dock '
           'märkbart högre än bensinversionerna.'),
},
{
 'slug': 'xc40', 'namn': 'XC40', 'typ': 'kompakt SUV', 'ar': '2018–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Volvos minsta SUV och märkets vanligaste förstabil bland yngre förare.',
 'vinkel': 'XC40 hamnar ofta hos förare som är yngre än den typiska Volvokunden, och det '
           'syns i statistiken. Bilen i sig är inte dyr att reparera, men förarprofilen '
           'drar upp genomsnittspremien. Är du över 30 och har full bonus får du därför '
           'ofta ett bättre pris än vad generella prisjämförelser antyder.',
 'punkter': ['Yngre förarprofil än övriga Volvomodeller',
             'Kompakt format ger färre parkeringsskador än XC60',
             'Laddhybriden har högre ersättningsvärde än mildhybriden'],
 'skada': 'Glasskador är överrepresenterade. XC40 används mycket i pendling, och '
          'kilometer på motorväg är det som ger stenskott — inte körstil.',
 'varde': 'Andrahandsvärdet är starkt, delvis för att modellen är eftertraktad på '
          'privatleasingmarknaden.',
 'niva': 'Helförsäkring så länge bilen är under sju år. Vagnskadegarantin täcker de '
         'första tre.',
 'fraga': ('Varför är XC40 dyrare att försäkra än XC60 för unga förare?',
           'Skillnaden ligger inte i bilen utan i vem som kör den. XC40 har en yngre '
           'ägarprofil, och åldern på föraren väger tyngre i premieberäkningen än '
           'skillnaden i bilarnas storlek.'),
},
{
 'slug': 'v60', 'namn': 'V60', 'typ': 'kombi', 'ar': '2018–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Kombin som ersatte V70 i Volvos utbud och tog över dess plats i svenska '
         'garage.',
 'vinkel': 'V60 har den lägsta genomsnittliga skadefrekvensen i Volvos moderna utbud. '
           'Ägarprofilen är äldre, körsträckorna är förutsägbara och en stor del av '
           'beståndet står på villauppfarter i stället för på gatan. Kombinationen ger '
           'ofta en lägre premie än en XC60 med samma motor och årsmodell.',
 'punkter': ['Lägre skadefrekvens än märkets SUV-modeller',
             'Cross Country-versionen kostar något mer att försäkra',
             'Tjänstebilsbeståndet gör begagnatutbudet stort och delarna billiga'],
 'skada': 'Viltolyckor sticker ut. V60 används mycket på landsväg, och '
          'djurkollisioner är den skada som oftast leder till ett större belopp — '
          'kontrollera om självrisken reduceras vid viltolycka.',
 'varde': 'Värdeminskningen är brantare än på SUV-modellerna, vilket flyttar gränsen för '
          'när helförsäkring slutar löna sig nedåt i ålder.',
 'niva': 'Helförsäkring till omkring sex eller sju år, sedan är halvförsäkring ofta '
         'rimligare än på en jämngammal XC60.',
 'fraga': ('Är V60 billigare att försäkra än XC60?',
           'Ofta ja, med samma förare och motor. Kombin har lägre skadefrekvens och lägre '
           'marknadsvärde, och båda drar premien nedåt.'),
},
{
 'slug': 'v90', 'namn': 'V90', 'typ': 'stor kombi', 'ar': '2016–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Volvos största kombi, i stor utsträckning en före detta tjänstebil.',
 'vinkel': 'Det mesta av V90-beståndet har gått som tjänstebil de första tre åren, vilket '
           'betyder höga körsträckor tidigt och sedan en tvär övergång till privatägande. '
           'Köper du en begagnad V90 ska du vara noga med att ange din egen körsträcka och '
           'inte utgå från vad bilen kört tidigare — det är en av de vanligaste '
           'felkällorna i offerten på just den här modellen.',
 'punkter': ['Stort utbud av begagnade exemplar med hög körsträcka',
             'Cross Country-versionen har högre markfrigång och något högre premie',
             'Laddhybriden T8 hamnar i en högre effektklass'],
 'skada': 'Skador i samband med backning och trånga utrymmen är vanliga. V90 är nästan fem '
          'meter lång, och parkeringsgarage byggda på sjuttiotalet är det inte.',
 'varde': 'Värdeminskningen är kraftig de första fyra åren och planar sedan ut, vilket gör '
          'begagnatköp prisvärt men helförsäkring mindre motiverad på äldre exemplar.',
 'niva': 'Helförsäkring på exemplar under sex år. På en tio år gammal V90 är '
         'halvförsäkring nästan alltid rätt.',
 'fraga': ('Vad kostar det att försäkra en begagnad V90?',
           'Premien beräknas på bilens marknadsvärde och på din förarprofil, inte på '
           'nypriset. En äldre V90 kostar därför betydligt mindre att försäkra än siffrorna '
           'för nya exemplar antyder.'),
},
{
 'slug': 'xc90', 'namn': 'XC90', 'typ': 'stor SUV med sju säten', 'ar': '2015–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Volvos flaggskepp och en av få sjusitsiga bilar som säljs i volym i Sverige.',
 'vinkel': 'XC90 är den Volvomodell som oftast omfattas av särskilda stöldkrav. Stora SUV:ar '
           'i premiumsegmentet är eftertraktade, och flera bolag kräver godkänt stöldskydd '
           'eller spårsändare i vissa postnummerområden. Kravet står i villkoren och är en '
           'förutsättning för ersättning — inte ett råd.',
 'punkter': ['Kan omfattas av krav på spårsändare beroende på var du bor',
             'Sju säten betyder fler passagerare och därmed högre exponering',
             'Luftfjädringen är dyr att laga och täcks inte av alla maskinskadevillkor'],
 'skada': 'Stöldförsök och inbrott väger tyngre här än på övriga modeller. Bilens värde och '
          'utrustningsnivå gör den intressant, särskilt i storstadsområdena.',
 'varde': 'Höga ersättningsvärden även på äldre exemplar, vilket håller vagnskadedelen '
          'motiverad längre än på mindre modeller.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde, i '
         'praktiken tio år eller mer.',
 'fraga': ('Krävs spårsändare på Volvo XC90?',
           'Vissa bolag ställer krav på godkänt stöldskydd eller spårsändare för större '
           'SUV-modeller, ofta kopplat till postnummer. Kontrollera villkoren innan du '
           'tecknar — uppfylls inte kravet kan ersättningen sättas ned vid stöld.'),
},
{
 'slug': 's60', 'namn': 'S60', 'typ': 'sedan', 'ar': '2018–',
 'drivlina': 'bensin och laddhybrid',
 'kort': 'Sedanversionen av V60, ovanligare på svenska vägar än kombin.',
 'vinkel': 'S60 delar teknik och delkatalog med V60, men beståndet är betydligt mindre '
           'eftersom svenskar köper kombi. Det påverkar inte premien nämnvärt — delarna är '
           'desamma — men det gör att modellen sällan dyker upp i prisjämförelser. Begär '
           'offert på ditt eget registreringsnummer i stället för att utgå från listor.',
 'punkter': ['Delar delkatalog och verkstadsnät med V60',
             'Litet bestånd gör att modellen sällan finns i prisexempel',
             'Polestar Engineered-versionen hamnar i en högre effektklass'],
 'skada': 'Skadebilden liknar V60:s, men med färre viltolyckor eftersom S60 i högre grad '
          'är en stadsbil.',
 'varde': 'Lägre efterfrågan på begagnatmarknaden än kombin, vilket ger snabbare '
          'värdeminskning.',
 'niva': 'Helförsäkring till omkring sex år, därefter en fråga om marknadsvärdet.',
 'fraga': ('Skiljer sig försäkringen mellan Volvo S60 och V60?',
           'Marginellt. Bilarna delar teknik och reservdelar, så skillnaden ligger främst i '
           'marknadsvärdet — och där ligger kombin ofta något högre.'),
},
{
 'slug': 's90', 'namn': 'S90', 'typ': 'stor sedan', 'ar': '2016–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Volvos största sedan, vanligast som tidigare tjänste- eller representationsbil.',
 'vinkel': 'S90 har det minsta beståndet av Volvos storbilar, och en stor andel av bilarna '
           'har gått i tjänstebilsflottor. Det gör att skadestatistiken bygger på ett smalare '
           'underlag än för V90, och att premien kan skilja mer mellan bolagen än den gör på '
           'vanligare modeller. Här lönar det sig särskilt att begära flera offerter.',
 'punkter': ['Smalt bestånd ger större spridning mellan bolagens priser',
             'Höga körsträckor i tidigare tjänstebilar',
             'Utrustningsnivån varierar kraftigt mellan exemplar'],
 'skada': 'Låg skadefrekvens totalt, men de skador som sker blir dyra eftersom '
          'karossdelarna är stora och lacken ofta metallic.',
 'varde': 'Kraftig värdeminskning de första åren gör begagnade exemplar prisvärda och '
          'ersättningsvärdet lägre än nypriset antyder.',
 'niva': 'Helförsäkring på nyare exemplar, halvförsäkring blir aktuellt tidigare än på XC90.',
 'fraga': ('Är Volvo S90 dyr i försäkring?',
           'Premien styrs av marknadsvärdet, och det faller snabbt på den här modellen. En '
           'begagnad S90 är därför ofta billigare att försäkra än man tror sett till '
           'bilens storlek och nypris.'),
},
{
 'slug': 'ex30', 'namn': 'EX30', 'typ': 'liten eldriven SUV', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'Volvos minsta elbil och den modell som drog in märket i lågprissegmentet för el.',
 'vinkel': 'EX30 är byggd på en plattform som Volvo delar med Smart och Zeekr inom '
           'Geelysfären, och tillverkas utanför Europa. Delstillgången har varit den stora '
           'frågan under de första åren, och väntetid på delar påverkar dig direkt genom '
           'hyrbilsmomentet. Kontrollera hur många dagar hyrbil som ingår — det är den '
           'viktigaste villkorsfrågan på just den här bilen.',
 'punkter': ['Kontrollera hyrbilsdagar — delstillgången har varit ojämn',
             'Batteriet utgör en stor andel av bilens värde',
             'Prestandaversionen Twin Motor hamnar i en högre effektklass'],
 'skada': 'Skador på det främre stötfångarpartiet är vanliga eftersom sensorer och radar '
          'sitter där — en till synes liten smäll blir ett dyrt ärende med kalibrering.',
 'varde': 'Kort marknadshistorik gör restvärdet svårbedömt, vilket några bolag prissätter '
          'som en osäkerhet.',
 'niva': 'Helförsäkring. Bilen är för ny för att något annat ska vara aktuellt, och '
         'vagnskadegarantin täcker de första åren.',
 'fraga': ('Vad kostar försäkring till Volvo EX30?',
           'Premien ligger högre än för en bensindriven bil i samma storlek, framför allt på '
           'grund av batteriets värde och reparationskostnaderna. Skillnaden krymper i takt '
           'med att beståndet växer.'),
},
{
 'slug': 'ex40', 'namn': 'EX40', 'typ': 'eldriven kompakt SUV', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna XC40, omdöpt till EX40 när Volvo lade om sin modellbenämning.',
 'vinkel': 'EX40 hette tidigare XC40 Recharge, och namnbytet gör att bilen kan dyka upp '
           'under båda namnen hos bolagen. Kontrollera att offerten avser rätt bil — det '
           'enklaste sättet är att alltid utgå från registreringsnumret i stället för att '
           'välja modell i en rullista.',
 'punkter': ['Hette XC40 Recharge före namnbytet — kan förekomma under båda namnen',
             'Delar kaross och delkatalog med bensindrivna XC40',
             'Tvåmotorsversionen ligger i en högre effektklass'],
 'skada': 'Samma skadebild som XC40 i övrigt, men med den skillnaden att arbete nära '
          'högvoltssystemet kräver certifierad verkstad och därmed längre transport.',
 'varde': 'Restvärdet följer elbilsmarknaden i stort och har varit rörligare än för '
          'bensinversionen.',
 'niva': 'Helförsäkring, och kontrollera att batteriet omfattas av vagnskadedelen.',
 'fraga': ('Är EX40 samma bil som XC40 Recharge?',
           'Ja. Volvo bytte namn på sina eldrivna modeller, och EX40 är den eldrivna XC40. '
           'Vid tecknandet är det säkrast att utgå från registreringsnumret så att offerten '
           'hamnar på rätt bil.'),
},
{
 'slug': 'v70', 'namn': 'V70', 'typ': 'kombi', 'ar': '2007–2016',
 'drivlina': 'bensin och diesel',
 'kort': 'Den mest sålda kombin i svensk bilhistoria och fortfarande vanlig på vägarna.',
 'vinkel': 'V70 är den modell där valet av skyddsnivå spelar störst roll. Marknadsvärdet '
           'ligger på nivåer där vagnskadedelen ofta kostar mer i premie under några år än '
           'den någonsin kan betala ut. Samtidigt är delarna billiga och verkstäderna många, '
           'vilket gör att en reparation sällan blir så dyr att den motiverar helförsäkring.',
 'punkter': ['Marknadsvärdet gör halvförsäkring rätt för de flesta exemplar',
             'Utmärkt delstillgång och konkurrens mellan verkstäderna',
             'Maskinskademomentet har oftast upphört på grund av ålder'],
 'skada': 'Rost och slitage är de vanligaste bekymren — och inget av dem ersätts av någon '
          'nivå, eftersom de räknas som förslitning och inte som skada.',
 'varde': 'Låga och stabila värden. Skillnaden mellan ett välskött och ett slitet exemplar '
          'är större än skillnaden mellan årsmodellerna.',
 'niva': 'Halvförsäkring på i princip alla exemplar. Trafikförsäkring om bilen är värd '
         'mindre än självrisken plus några tusenlappar.',
 'fraga': ('Behöver jag helförsäkring på en Volvo V70?',
           'Sällan. Vagnskadedelen ersätter marknadsvärdet minus självrisken, och på en V70 '
           'är det utrymmet litet. Halvförsäkring behåller stöld, brand, glas och räddning '
           'till en betydligt lägre premie.'),
},
],
}
