# Importeren van de games vanuit de desbetreffende mappen
from game_1.raadhetgetal import raadhetgetalgame
from game_2.galgje import spel

# Keuze menu blijven draaien totdat een keuze is gemaakt
while True:
    try: # Welkomst bericht bij op het main menu
        print("Welkom bij PyStore van. Er zijn 2 games beschikbaar:\n1: Raad het getal\n2: Galgje\n3: Afsluiten\nVoer je keuze in")
        # Gebruiker maakt een keuze
        keuze = int(input("Welke spel wil je spelen: "))

        if keuze == 1: # Bij keuze 1 wordt game raad het getal gestart
            raadhetgetalgame()
        elif keuze == 2: # Bij keuze 2 wordt het game galgje gestart
            spel()
        elif keuze == 3: # Bij keuze 3 wordt PyStore afgesloten met een bericht "Tot ziens!"
            print("Tot ziens!")
            break
        else:
            print("Oneldige keuze. Er zijn momenteel 2 games beschikbaar!") # Er kan alleen 1, 2 of 3 als keuze worden gemaakt
    except ValueError:
        print("Ongeldige invoer, voer een getal in.") # Error als er een ongeldig invoer is



