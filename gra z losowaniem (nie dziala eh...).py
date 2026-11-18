import random

haslo = random.randint(0, 10)

strzal = int(input("strzelaj!"))


while strzal != haslo :
    if strzal == haslo :
        print("wygrales!!")
else :
    print("dawaj jescze raz!")
    strzal = int(input("strzelaj ponownie!"))
