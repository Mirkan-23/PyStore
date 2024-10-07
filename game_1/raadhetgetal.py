# game_1/raadhetgeral.py

import random

def raadhetgetalgame():

    print("Welkom bij raad het getal, geef twee getallen op, het juiste getal ligt ertussen en dat ga je raden.\nLet op! Je mag zelf kiezen hoe hoog het maximale getal is, maar de kansen blijven op 5!")

    Getal1 = int(input('Voer het 1e getal in: '))
    Getal2 = int(input('Voer het 2e getal in: '))
    WillekeurigeGok = random.randrange(Getal1, Getal2 + 1)
    kansen = 5
    for A in range(1, kansen + 1):
        Gok = int(input("Raad het getal: "))

        if Gok < Getal1 or Gok > Getal2:
            print(F"Het getal moet tussen de {Getal1} en {Getal2} liggen!")
            continue

        if Gok > WillekeurigeGok:
            print("Het getal is te hoog, probeer het opnieuw")
        elif Gok < WillekeurigeGok:
            print("Het getal is te laag, probeer het opnieuw")
        else:
            print("Netjes! Je hebt het getal geraden! Het getal was: " + str(WillekeurigeGok))
            break
    else:
        print("Helaas, je hebt geen kansen meer en hebt verloren. Het juiste getal was: " + str(WillekeurigeGok))