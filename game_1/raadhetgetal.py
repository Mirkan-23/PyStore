# game_1/raadhetgeral.py

# Importeer module random
import random

def raadhetgetalgame():

    # Verwelkom speler
    print("Welkom bij raad het getal, geef twee getallen op, het juiste getal ligt ertussen en dat ga je raden.\nLet op! Je mag zelf kiezen hoe hoog het maximale getal is, maar de kansen blijven op 5!")

    # Vraag speler om getal tussen eerste en tweede invoer te geven (Incl getal2 daarom + 1)
    Getal1 = int(input('Voer het 1e getal in: '))
    Getal2 = int(input('Voer het 2e getal in: '))

    # Antwoord is willekeurig getal tussen die 2 door de speler ingevoerde getallen en speler heeft 5 kansen
    WillekeurigeGok = random.randrange(Getal1, Getal2 + 1)
    kansen = 5

    # Loop voor de aantal kansen dat de speler heeft
    for A in range(1, kansen + 1):
        Gok = int(input("Raad het getal: "))
    # Controleren of de gok binnen de range van de speler invoer ligt
        if Gok < Getal1 or Gok > Getal2:
            print(F"Het getal moet tussen de {Getal1} en {Getal2} liggen!")
            continue # Vragen om een nieuw gok

        # Speler in de juiste richting sturen per gok
        if Gok > WillekeurigeGok:
            print("Het getal is te hoog, probeer het opnieuw")
        elif Gok < WillekeurigeGok:
            print("Het getal is te laag, probeer het opnieuw")
        else:
            print("Netjes! Je hebt het getal geraden! Het getal was: " + str(WillekeurigeGok))
            break # Spel stoppen wanneer speler het juiste getal heeft geraden.
    else:
        # Toon dit bericht als speler geen kansen heeft, speler heeft dus verloren.
        print("Helaas, je hebt geen kansen meer en hebt verloren. Het juiste getal was: " + str(WillekeurigeGok))