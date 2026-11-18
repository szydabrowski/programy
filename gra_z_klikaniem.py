import tkinter as tk
okno = tk.Tk()
okno.title("kliker")
okno.geometry("300x200")
wynik = 0
aktualny_wynik = tk.Label(okno, text= f"wynik to {wynik}punktow")
aktualny_wynik.pack()
def dodaj_punkt():
    global wynik
    wynik += 1
    aktualny_wynik.config(text= f"aktualny wynik to {wynik} punktow")

zdobadz_punkt = tk.Button(okno, text="kliknij, aby zdobyc punkt", command=dodaj_punkt)
zdobadz_punkt.pack()



okno.mainloop()




