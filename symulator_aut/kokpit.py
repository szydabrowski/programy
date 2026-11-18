import tkinter as tk
from pojazdy import samochod, SamochodSportowy
okno =tk.Tk()

BMW_X5 = samochod("bmw", "X5", "2.0V", "sedan")
opel_vectra = samochod("opel", "vectra", "1.6V", "combi")
ferrari_la_ferrari = SamochodSportowy("ferrari", "la ferrari", "6.5V", "sedan")




licznik_BMW_X5 = tk.Label(okno,text= f"predkosc to {BMW_X5.predkosc} km/h")
licznik_BMW_X5.pack()
przyspiesz_BMW_X5 = tk.Button(okno, text="przyspiesz", command=BMW_X5.przyspiesz)
def przyspiesz_bmw():
    
przyspiesz_BMW_X5.pack()

tk.mainloop()



