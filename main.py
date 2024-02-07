import pandas as pd
import matplotlib.pyplot as plt

# Läs in CSV-filen
df = pd.read_csv('miljo.csv')

def show_all():
    # Skapa ett linjediagram
    df.plot(x='Year', y=' Tax', kind='line', marker='o')

    # Visa diagrammet
    plt.show()

def compare_two():
    # Välj de två år du vill jämföra
    år1 = input('Skriv ett år du vill kolla på (2011-2021): ')
    år2 = input('Skriv året du vill jämföra det med (2011-2021): ')
    print(f'{år1} och {år2}')

    # Filtrera DataFrame för att få endast de två åren
    selected_years = df[df['Year'].isin([int(år1), int(år2)])]

    # Skapa ett stapeldiagram
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Ange diagramtitel och etiketter
    plt.title(f'Jämförelse av miljöskatt mellan {år1} och {år2}')
    plt.xlabel('År')
    plt.ylabel('Miljöskatt')

    # Visa diagrammet
    plt.show()


def compare_three():
    # Välj de två år du vill jämföra
    år1 = input('Skriv ett år du vill kolla på (2011-2021): ')
    år2 = input('Skriv andra året du vill jämföra det med (2011-2021): ')
    år3 = input('Skriv tredje året du vill jämföra det med (2011-2021): ')

    # Filtrera DataFrame för att få endast de tre åren
    selected_years = df[df['Year'].isin([int(år1), int(år2), int(år3)])]

    # Skapa ett stapeldiagram
    selected_years.plot(x='Year', y=' Tax', kind='bar', legend=False)

    # Ange diagramtitel och etiketter
    plt.title(f'Jämförelse av miljöskatt mellan {år1}, {år2} och {år3}')
    plt.xlabel('År')
    plt.ylabel('Miljöskatt')

    # Visa diagrammet
    plt.show()

