# game_2/galgje.py

# Importeer module random
import random

def welkom():
    # Vraag de naam van de speler en verwelkom ze
    naam = input("Wat is je naam: ")
    print(f"Hallo {naam}, welkom bij galgje")

def spel():
    welkom() # Roep de functie welkom aan
    # Bestand openen en willekeurig woordje selecteren
    with open('galgjewoorden.txt', 'r') as woordenlijst:
        woorden = woordenlijst.readlines()
        gekozenwoord = random.choice(woorden).strip().lower()

    kansen = 10 # Speler heeft 10 kansen
    geraaddeletters = '' # Hier wordt bijgehouden welke letters geraden zijn

    while kansen > 0: # Speler blijft spelen totdat er 0 kansen over zijn
        status = '' # Voortgang van het geraden woord
        for letter in gekozenwoord:
            if letter in geraaddeletters:
                status += letter # Geraadden letters toe voegen aan voortgang
            else:
                status += '_' # Laag streepjes toevoegen voor de niet geraden letters
        print(status)

        # Controle of het woordje is geraden
        if status == gekozenwoord:
            print(f"Je hebt gewonnen! Je hebt het woordje: {gekozenwoord} geraden!")
            break

        # Gebruiker vragen om een letter te raden.
        invoer = input("Raad een letter: ").lower()

        # Controle om te checken of een letter al is geraden.
        if invoer in geraaddeletters:
            print("Deze letter heb je al geprobeerd")
            continue

        # Nieuwe letter toevoegen aan de geraaddeletters
        geraaddeletters += invoer

        # Verminder kansen bij 1 als speler een verkeerd letter invoert
        if invoer not in gekozenwoord:
            kansen -= 1
            print(f"Je hebt nog {kansen} over.")

    # Speler verliest als er 0 kansen over zijn
    if kansen == 0:
            print(f"Helaas, je hebt verloren, het juiste woord was: {gekozenwoord}")