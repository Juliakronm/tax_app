# Miljöskatteanalys med Python
Denna Python-kod använder biblioteken pandas och matplotlib för att analysera och visualisera miljöskattedata från en CSV-fil. Koden ger användaren möjlighet att utforska och jämföra miljöskatter för olika år. Här är en översikt över koden och dess funktionalitet:

#### Steg 1: Importera bibliotek
Först importerar koden de nödvändiga biblioteken, pandas för att hantera data och matplotlib för att skapa diagram.

#### Steg 2: Läs in CSV-fil
Därefter läses en CSV-fil in och omvandlas till en pandas DataFrame, vilket gör det möjligt att enkelt arbeta med och analysera datan.

#### Steg 3: Visa diagram för alla år
En funktion show_all() har skapats för att generera ett linjediagram som visar miljöskatten över alla tillgängliga år. Användaren får en tydlig överblick över hur skatten har utvecklats över tid.

#### Steg 4: Välj ett specifikt år
För att undersöka miljöskatten för ett specifikt år har en funktion get_year() implementerats. Användaren uppmanas att ange ett år mellan 2011 och 2021, och koden hanterar inmatningsfel för att säkerställa korrekta värden.

#### Steg 5: Jämför två eller tre år
För att göra jämförelser mellan olika år har två funktioner compare_two() och compare_three() skapats. Användaren kan välja två eller tre år för att visualisera och jämföra miljöskatten i ett stapeldiagram.

#### Steg 6: Visa hela datamängden som lista
Slutligen, för de som vill se hela datamängden, finns en funktion show_as_list() som skriver ut hela DataFrame som en tabell.

### Vidareutveckling och Användningsmöjligheter
Denna kod kan vidareutvecklas genom att lägga till fler analytiska funktioner eller förbättra användargränssnittet. Möjliga förbättringar inkluderar:
Tidsperiodanalyser: Lägg till funktioner för att analysera miljöskatten över specifika tidsperioder.
Felhantering: Utveckla felhantering ytterligare för att göra användarupplevelsen robustare.
Interaktivitet: Implementera interaktivitet i diagrammen för att möjliggöra djupare undersökningar och dynamiska jämförelser.
Denna kod utgör en grund för att utforska och förstå miljöskattedata, och dess flexibilitet möjliggör enkel utökning och anpassning för olika analysbehov.

### Hjälpmedel under arbetet
De hjälpmedel som använts under arbetet har varit ChatGPT, Youtube, tidigare kod från kursen, StackOverflow och respektive biblioteks dokumentation. Jag fick även bra tips under redovisningen.
