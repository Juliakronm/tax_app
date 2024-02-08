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
    # Visa diagrammet
    plt.show()

# Skapa funktion som låter användaren välja ett årtal som vi kan använda senare i koden.
def get_year():
    while True:
        year = input('Skriv andra året du vill jämföra det med (2011-2021): ')
        # Kolla att input är ett nummer
        if year.isnumeric():
            # Omvandla input till int
            year = int(year)
            # Plocka ut minsta året
            small = df['Year'].nsmallest(1)
            # Plocka ut högsta året
            big = df['Year'].nlargest(1)
            # Få ut endast värdet på året
            small = int(small.iloc[0])
            big = int(big.iloc[0])
            # Kolla att året finns i vår statistik
            if year < small or year > big:
                # Meddelande som syns om användaren valt ett år som inte finns.
                print('Felaktigt årtal')
            else:
                #Hoppar ur loopen och sparar input som varit korrekt enligt föregående parametrar.
                return year
        else:
            # Svar som ges om användaren skrivit annat än nummer.
            print('Felaktigt svar, vänligen ange ett årtal.')

# Skapa funktion för att jämföra två år.
def compare_two():
    # Spara år från funktionernas inputs i variabler
    get_year1 = get_year()
    get_year2 = get_year()
    # Filtrera DataFrame för att få endast de två åren
    selected_years = df[df['Year'].isin([get_year1, get_year2])]

    # Skapa ett stapeldiagram med plot. Tar bort legenden i diagrammet.
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Välj diagramtitel och etiketter
    plt.title(f'Jämförelse av miljöskatt mellan {get_year1} och {get_year2}')
    plt.xlabel('År')
    plt.ylabel('Miljoner')

    # Visa diagrammet
    plt.show()

# Skapa funktion som jämför tre årtal.
def compare_three():
    # Spara år från funktionernas inputs i variabler
    get_year1 = get_year()
    get_year2 = get_year()
    get_year3 = get_year()

    # Filtrerar DataFrame för att få endast de tre åren
    selected_years = df[df['Year'].isin([get_year1, get_year2, get_year3])]

    # Skapar ett stapeldiagram
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Välj diagramtitel och etiketter
    plt.title(f'Jämförelse av miljöskatt mellan {get_year1}, {get_year2} och {get_year3}')
    plt.xlabel('År')
    plt.ylabel('Miljoner')

    # Visa diagrammet
    plt.show()

# Skapa funktion
def show_as_list():
    # Skriv ut CSV-filen
    print(df)
