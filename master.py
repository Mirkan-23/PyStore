from game_1.raadhetgetal import raadhetgetalgame
from game_2.galgje import spel

while True:
    try:
        print("Welkom bij PyStore van. Er zijn 2 games beschikbaar:\n1: Raad het getal\n2: Galgje\n3: Afsluiten\nVoer je keuze in")
        keuze = int(input("Welke spel wil je spelen: "))

        if keuze == 1:
            raadhetgetalgame()
        elif keuze == 2:
            spel()
        elif keuze == 3:
            print("Tot ziens!")
            break
        else:
            print("Oneldige keuze. Er zijn momenteel 2 games beschikbaar!")
    except ValueError:
        print("Ongeldige invoer, voer een getal in.")