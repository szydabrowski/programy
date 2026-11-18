import json

# Próbujemy wczytać ekwipunek z pliku tekstowego
try:
    with open("ekwipunek.json", "r", encoding="utf-8") as plik:
        ekwipunek = json.load(plik)
        print("Wczytano zapisany ekwipunek z pliku!")
except FileNotFoundError:
    # Jeśli pliku jeszcze nie ma, tworzymy domyślny słownik
    ekwipunek = {
        "miecz": 50,
        "tarcza": 30,
        "eliksir": 15,
        "luk": 40
    }
    print("Brak pliku zapisu – utworzono domyślny ekwipunek.")


ekwipunek = {
    "miecz": 50,
    "tarcza": 30,
    "eliksir": 15,
    "luk": 40
}









szukany_przedmiot = ""


while szukany_przedmiot != "koniec" :
    szukany_przedmiot = input("jaki chcesz sprawdzic przedmiot? Możesz także dodać nowy, wystarczy wpisac dodaj! mozesz takze zobaczyc aktulny stan! jesli chcesz zakonczyc wpisz koniec ").strip().lower()
    if szukany_przedmiot == "koniec" :
        print("OK,Dozobacznia!!!")
    elif szukany_przedmiot == "pokaz" :
        print("ok, rzeczy w ekwipunku :", ekwipunek)
    elif szukany_przedmiot == "usun" :
        usuwany_przedmiot = input("co chcesz usunac?").strip().lower()
        if usuwany_przedmiot in ekwipunek :
            del ekwipunek[usuwany_przedmiot]
            print(f"usunieto przedmiot {usuwany_przedmiot} z ekwipunku!")
        else :
            print(f"nie ma takiego przedmiotu jak {usuwany_przedmiot} wiec nie moge go usunac!")
    elif szukany_przedmiot in ekwipunek :
        print(f"twoj przedmiot {szukany_przedmiot} ma {ekwipunek[szukany_przedmiot]} punktow!")
    elif szukany_przedmiot == "dodaj" :
        nazwa_nowego_przedmiotu = input("jak sie nazywa?").strip().lower()
        punkty_nowego_przedmiotu = int(input("ile ma punktow"))
        ekwipunek[nazwa_nowego_przedmiotu] = punkty_nowego_przedmiotu
        print(f"okej, twoj przedmiot o nazwie {nazwa_nowego_przedmiotu} o punktach {punkty_nowego_przedmiotu} zostal dodany!!!")





        
    else :
        print("nie mamy tego")





