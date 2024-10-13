# game_2/galgje.py

import random

def welkom():
    naam = input("Wat is je naam: ")
    print(f"Hallo {naam}, welkom bij galgje. Je hebt totaal 10 kansen ongeacht het moeilijkheid van het woordje")

def spel():
    welkom()
    with open('galgjewoorden.txt', 'r') as woordenlijst:
        woorden = woordenlijst.readlines()
        gekozenwoord = random.choice(woorden).strip().lower()

    kansen = 10
    geraaddeletters = ''

    while kansen > 0:
        status = ''
        for letter in gekozenwoord:
            if letter in geraaddeletters:
                status += letter
            else:
                status += '_'
        print(status)
        if status == gekozenwoord:
            print(f"Je hebt gewonnen! Je hebt het woordje: {gekozenwoord} geraden!")
            break

        invoer = input("Raad een letter: ").lower()

        if invoer in geraaddeletters:
            print("Deze letter heb je al geprobeerd")
            continue

        geraaddeletters += invoer

        if invoer not in gekozenwoord:
            kansen -= 1
            print(f"Het letter {invoer} is fout, je hebt nog {kansen} kansen over.")

    if kansen == 0:
            print(f"Helaas, je hebt verloren, het juiste woord was: {gekozenwoord}")