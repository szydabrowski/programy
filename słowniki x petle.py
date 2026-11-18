ekwipunek = {
    "miecz": 50,
    "tarcza": 30,
    "eliksir": 15,
    "luk": 40
}
szukany_przedmiot = ""


while szukany_przedmiot != "koniec" :
    szukany_przedmiot = input("jaki chcesz sprawdzic przedmiot?").strip().lower()
    if szukany_przedmiot == "koniec" :
        print("OK,Dozobacznia!!!")


    elif szukany_przedmiot in ekwipunek :
        szukany_przedmiot = input(f"twoj przedmiot {szukany_przedmiot} ma {ekwipunek[szukany_przedmiot]} punktow!")

    else :
        print("nie mamy tego")

