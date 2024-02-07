# Importera min fil med funktioner
import main

# Boolean som avgör om programmet körs
run = True

# Loop för att programmet ska vara aktivt enligt föregående variabel.
while run:
    answer = input('Välkommen till denna enkla applikation där du får möjlighet att titta på miljöskatt för privatkonsumption mellan åren 2011-2021. Välj ett av nedan val.'
                    "\n\nMeny:"
                   '\n1. Se miljöskatten som diagram med samtliga år'
                   '\n2. Jämför två år'
                   '\n3. Jämför tre år'
                   '\n4. Visa samtliga år i en tabell'
                   '\n5. tbc'
                   '\n6. tbc'
                   '\nQ. Avsluta program'
                   '\n -> ').strip()
    # Se till att rätt svar leder till rätt funktion
    match answer.lower():
        # Startar funktion 1 enligt användarens val.
        case '1':
            main.show_all()
        # Startar funktion 2 enligt användarens val.
        case  '2':
            main.compare_two()
        # Startar funktion 3 enligt användarens val.
        case '3':
            main.compare_three()
        # Startar funktion 4 enligt användarens val.
        case '4':
            main.show_as_list()
        # Startar funktion 5 enligt användarens val.
        case '5':
            print('Oj, här var det tomt. Återkom senare igen.')
        # Startar funktion 6 enligt användarens val.
        case '6':
            print('Oj, här var det tomt. Återkom senare igen.')
        # För att avsluta programmet
        case 'q':
            run = False
        # Om man skriver något som inte finns:
        case _:
            print(f'{answer} är inte ett alternativ, gör om gör rätt.')