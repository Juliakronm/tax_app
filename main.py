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
    år1 = input('Skriv ett år du vill kolla på (2011-2021): ')
    år2 = input('Skriv året du vill jämföra det med (2011-2021): ')

    # Filtrera DataFrame för att få endast de två åren
    selected_years = df[df['Year'].isin([int(år1), int(år2)])]

    # Skapa ett stapeldiagram
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Välj diagramtitel och etiketter
    plt.title(f'Jämförelse av miljöskatt mellan {år1} och {år2}')
    plt.xlabel('År')
    plt.ylabel('Miljöskatt')

    # Visa diagrammet
    plt.show()

# Skapa funktion
def compare_three():
    # Spara år från inputs i variabler
    år1 = input('Skriv ett år du vill kolla på (2011-2021): ')
    år2 = input('Skriv andra året du vill jämföra det med (2011-2021): ')
    år3 = input('Skriv tredje året du vill jämföra det med (2011-2021): ')

    # Filtrerar DataFrame för att få endast de tre åren
    selected_years = df[df['Year'].isin([int(år1), int(år2), int(år3)])]

    # Skapar ett stapeldiagram
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Välj diagramtitel och etiketter
    plt.title(f'Jämförelse av miljöskatt mellan {år1}, {år2} och {år3}')
    plt.xlabel('År')
    plt.ylabel('Miljöskatt')

    # Visa diagrammet
    plt.show()

# Skapa funktion
def show_as_list():
    # Skriv ut CSV-filen
    print(df)
