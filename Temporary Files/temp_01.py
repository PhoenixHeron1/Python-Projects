import random
from threading import Timer

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mode = int(input("Choisissez le mode de jeux. 1 = facile, 2 = difficile: "))


if mode == 1:
    while True:
        x = random.randint(1, 26)
        r = int(input(f"Quel est le rang alphabetique de {letters[x]}: "))
        if r == x+1:
            print("Correct")
        else:
            print("Faux,", letters[x], "est de rang", x+1)
elif mode == 2:
    while True:
        limite = int(input("Quel limite de temps voulez vous pour repondre? (en s): "))
        t = Timer(Timer, print, [''])
        x = random.randint(1, 26)
        t.start()
        question = f"Quel est le rang alphabetique de {letters[x]}" + ": " % Timer
        r = int(input(question))
        t.cancel()
        if r == x+1:
            print("Correct")
        else:
            print("Faux,", letters[x], "est de rang", x+1)