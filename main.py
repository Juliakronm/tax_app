# Importera de bibliotek vi behöver
import pandas as pd
import matplotlib.pyplot as plt

# Läs in CSV-filen
df = pd.read_csv('miljo.csv')


# Skapa funktion
def show_all():
    # Skapa ett linjediagram
    df.plot(x='Year', y=' Tax', kind='line', marker='o')
    # Visa diagrammet
    plt.show()


# Skapa funktion
def compare_two():
    # Spara år från inputs i variabler
    def year1():
        year = input('Skriv ett år du vill kolla på (2011-2021): ')
        year = int(year)
        if year < 2011 or year > 2021:
            print('Felaktigt årtal')
            year1()
        return year

    def year2():
        year = input('Skriv andra året du vill jämföra det med (2011-2021): ')
        year = int(year)
        if year < 2011 or year > 2021:
            print('Felaktigt årtal')
            year2()
        return year

    get_year1 = year1()
    get_year2 = year2()
    # Filtrera DataFrame för att få endast de två åren
    selected_years = df[df['Year'].isin([get_year1, get_year2])]

    # Skapa ett stapeldiagram
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Välj diagramtitel och etiketter
    plt.title(f'Jämförelse av miljöskatt mellan {get_year1} och {get_year2}')
    plt.xlabel('År')
    plt.ylabel('Miljoner')

    # Visa diagrammet
    plt.show()


# Skapa funktion
def compare_three():
    # Spara år från inputs i variabler
    def year1():
        year = input('Skriv ett år du vill kolla på (2011-2021): ')
        year = int(year)
        if year < 2011 or year > 2021:
            print('Felaktigt årtal')
            year1()
        return year

    def year2():
        year = input('Skriv andra året du vill jämföra det med (2011-2021): ')
        year = int(year)
        if year < 2011 or year > 2021:
            print('Felaktigt årtal')
            year2()
        return year

    def year3():
        year = input('Skriv tredje året du vill jämföra det med (2011-2021): ')
        year = int(year)
        if year < 2011 or year > 2021:
            print('Felaktigt årtal')
            year3()
        return year

    get_year1 = year1()
    get_year2 = year2()
    get_year3 = year3()

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
