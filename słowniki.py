
ekwipunek = {
    "miecz": 50,
    "tarcza": 30,
    "eliksir": 15,
    "luk": 40
}

szukany_przedmiot = input("Jaki przedmiot chcesz sprawdzić? ").strip().lower()

if szukany_przedmiot in ekwipunek :
    print(f"{szukany_przedmiot} daje {ekwipunek [szukany_przedmiot]} punktow!")
else :
    print("nie mamy tego")
