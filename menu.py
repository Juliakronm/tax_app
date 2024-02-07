#Importera min fil med funktioner
import main

#Boolean som avgör om programmet körs
run = True

#Loop för att programmet ska vara aktivt enligt föregående variabel.
while run:
    answer = input('Välkommen till denna enkla applikation där du får möjlighet att titta på miljöskatt för privatkonsumption mellan åren 2011-2021. Välj ett av nedan val.'
                    "\n\nMeny:"
                   '\n1. Se miljöskatten som diagram med samtliga år'
                   '\n2. Jämför två år'
                   '\n3. Jämför tre år'
                   '\n4. tbc'
                   '\n5. tbc'
                   '\n6. tbc'
                   '\nQ. Avsluta program'
                   '\n -> ').strip()
    match answer.lower():
        case '1':
            main.show_all()
        case  '2':
            main.compare_two()
        case '3':
            print('Oj, här var det tomt. Återkom senare igen.')
        case '4':
            print('Oj, här var det tomt. Återkom senare igen.')
        case '5':
            print('Oj, här var det tomt. Återkom senare igen.')
        case '6':
            print('Oj, här var det tomt. Återkom senare igen.')
        case 'q':
            run = False
        case _:
            print(f'{answer} är inte ett alternativ, gör om gör rätt.')