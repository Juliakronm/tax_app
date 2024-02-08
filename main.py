# Importera de bibliotek vi behöver
import pandas as pd
import matplotlib.pyplot as plt

# Läs in CSV-filen med statistik
df = pd.read_csv('miljo.csv')

# Skapa funktion för att se diagram med samtliga år
def show_all():
    # Skapa ett linjediagram där jag definierar x-axeln som år och y-axeln som skatt.
    # Jag väljer att visa det som ett linjediagram med cirklar som markerar värdena.
    df.plot(x='Year', y=' Tax', kind='line', marker='o')
    # Väljer en beskrivande diagramtitel
    plt.title(f'Miljöskatt för privatkonsumtion')
    # Kallar x-axeln för 'År'
    plt.xlabel('År')
    # Kallar y-axeln för 'Miljoner'
    plt.ylabel('Miljoner')
    # Visa diagrammet
    plt.show()

# Skapa funktion som låter användaren välja ett årtal som vi kan använda senare i koden.
def get_year():
    # Drar igång en while-loop för att kunna felhantera.
    while True:
        # Gör input för att få värdet (året) från användaren
        year = input('Skriv ett år du vill se på (2011-2021): ')
        # Kolla att input är ett nummer i en if-sats.
        if year.isnumeric():
            # Omvandla input till int
            year = int(year)
            # Plocka ut minsta året ur vår statistik.
            small = df['Year'].nsmallest(1)
            # Plocka ut högsta året ur vår statistik.
            big = df['Year'].nlargest(1)
            # Få ut endast värdet på året vi hämtade från vår statistik, och inget annat krimskrams.
            small = int(small.iloc[0])
            big = int(big.iloc[0])
            # Kolla att året finns i vår statistik med en if-sats.
            if year < small or year > big:
                # Meddelande som syns om användaren valt ett år som inte finns.
                print('Felaktigt årtal')
            else:
                # Hoppar ur loopen och sparar input som varit korrekt enligt föregående parametrar.
                return year
        # Om input inte är ett nummer kickar 'else' in med ett felmeddelande och loopen fortsätter.
        else:
            # Svar som ges om användaren skrivit annat än nummer.
            print('Felaktigt svar, vänligen ange ett årtal.')

# Skapa funktion som låter användaren välja ett årtal som vi kan använda senare i koden.
def get_another_year():
    # Drar igång en while-loop för att kunna felhantera.
    while True:
        # Gör input för att få värdet (året) från användaren
        year = input('Skriv ytterligare ett år du vill se på (2011-2021): ')
        # Kolla att input är ett nummer i en if-sats.
        if year.isnumeric():
            # Omvandla input till int
            year = int(year)
            # Plocka ut minsta året ur vår statistik.
            small = df['Year'].nsmallest(1)
            # Plocka ut högsta året ur vår statistik.
            big = df['Year'].nlargest(1)
            # Få ut endast värdet på året vi hämtade från vår statistik, och inget annat krimskrams.
            small = int(small.iloc[0])
            big = int(big.iloc[0])
            # Kolla att året finns i vår statistik med en if-sats.
            if year < small or year > big:
                # Meddelande som syns om användaren valt ett år som inte finns.
                print('Felaktigt årtal')
            else:
                # Hoppar ur loopen och sparar input som varit korrekt enligt föregående parametrar.
                return year
        # Om input inte är ett nummer kickar 'else' in med ett felmeddelande och loopen fortsätter.
        else:
            # Svar som ges om användaren skrivit annat än nummer.
            print('Felaktigt svar, vänligen ange ett årtal.')

# Skapa funktion för att jämföra två år.
def compare_two():
    # Skapa variabler som kallar på funktioner, så vi kan spara år från
    # funktionernas inputs i dessa variabler.
    get_year1 = get_year()
    get_year2 = get_another_year()
    # Filtrera DataFrame för att få endast de två åren användaren matat in.
    selected_years = df[df['Year'].isin([get_year1, get_year2])]

    # Skapa ett stapeldiagram med plot. Tar bort legenden i diagrammet.
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Väljer en beskrivande diagramtitel
    plt.title(f'Jämförelse av miljöskatt mellan {get_year1} och {get_year2}')
    # Kallar x-axeln för 'År'
    plt.xlabel('År')
    # Kallar y-axeln för 'Miljoner'
    plt.ylabel('Miljoner')

    # Visa diagrammet
    plt.show()

# Skapa funktion som jämför tre årtal.
def compare_three():
    # Skapa variabler som kallar på funktioner, så vi kan spara år från
    # funktionernas inputs i dessa variabler.
    get_year1 = get_year()
    get_year2 = get_another_year()
    get_year3 = get_another_year()

    # Filtrerar DataFrame för att få endast de tre åren
    selected_years = df[df['Year'].isin([get_year1, get_year2, get_year3])]

    # Skapar ett stapeldiagram
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Väljer en beskrivande diagramtitel
    plt.title(f'Jämförelse av miljöskatt mellan {get_year1}, {get_year2} och {get_year3}')
    # Döper x-axeln till 'År'
    plt.xlabel('År')
    # Döper y-axeln till 'Miljoner'
    plt.ylabel('Miljoner')

    # Visa diagrammet
    plt.show()

# Skapa funktion
def show_as_list():
    # Skriv ut CSV-filen
    print(df)
