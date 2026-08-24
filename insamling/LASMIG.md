# Prisinsamling — så gör du

Fyll i `prisunderlag.csv` och kör `python3 importera.py`. Skriptet
validerar och skriver `insamlat.py`, som `data.py` plockar upp
automatiskt. Kör sedan `python3 build.py` från rotmappen.

## Ordning — börja med det som inte kräver offert

**Steg 1: självrisker (ingen offert behövs).**
Beloppen står i respektive bolags villkor, som ligger öppet på deras
sajter. De gäller oavsett bil och är därför jämförbara rakt av.
Fyll i kolumnerna `sjalvrisk_*`. Ungefär två timmar för alla 16 bolag,
och du får en tabell ingen konkurrent har.

**Steg 2: Trustpilot.**
Betyg och antal omdömen, hämtade samma dag. Notera datumet — betyg
rör sig.

**Steg 3: priser (kräver offert).**
Samma bil, samma personnummer, samma uppgifter hos varje bolag.
Profilen står i `data.PROFIL` och publiceras på /redaktionell-metod/.
Ändrar du profilen: ändra den där, inte bara i huvudet.

## Regler som gör siffrorna jämförbara

- Alltid **kronor per år**, aldrig månad. Skriptet stoppar dig annars.
- **Utan nykundsrabatt.** Rabatten gäller normalt bara år ett och gör
  jämförelsen falsk. Finns den bara som paketpris: notera det i
  `notering` och använd priset utan.
- **Samma självrisk** i alla offerter, den som står i profilen.
- **Samma tillägg**, eller inga alls. Ett bolag som paketerar in hyrbil
  ser dyrare ut än ett som inte gör det — notera skillnaden.
- **Datum och källa obligatoriskt.** Skriptet vägrar spara ett pris
  utan dem. Det är den viktigaste E-E-A-T-signalen på hela sajten.

## När räcker underlaget?

Topplistan publicerar placeringssiffror först när minst tre av fyra
kriterier finns för merparten av bolagen. Fram till dess visas en
sammanställning utan placering. Skriptet säger till när tröskeln nås.

## Kom ihåg efteråt

Höj `UPPDATERAD` i `data.py` till dagens datum. Den styr "Senast
kontrollerad" på varje sida, `dateModified` i schema.org och `lastmod`
i sitemap.xml.
