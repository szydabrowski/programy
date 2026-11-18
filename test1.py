

imie = input("Siema! podaj imie")
print(" zgadnij hasło!! Masz tylko 3 próby.")

haslo = input("Próba 1: ")
proby = 1

while haslo != "grubas" and proby < 3:
    print("zle haslo, dawaj jeszcze raz!")
    proby = proby + 1
    haslo = input("Kolejna próba: ")

if haslo == "grubas":
    print(f"dobre haslo! Wygrałeś {imie}!")
else:
    print(f"Koniec prób! Przegrałeś {imie}, hasło to grubas.")





