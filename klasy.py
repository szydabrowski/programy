class samochod:
    def __init__(self, marka, model, silnik, typ,):
        self.marka = marka
        self.model = model
        self.silnik = silnik
        self.typ = typ
        self.predkosc = 0
        self._paliwo = 50
        self.predkosc_maksymalna = 200
        self.uruchomiony = False


        
    def opisz_auto(self):
        print(f"to jest {self.marka} {self.model} z silnikiem {self.silnik} o typie nadwozia {self.typ}")


        
    def przyspiesz(self, o_ile):
        if not self.uruchomiony :
            print(f" uruchom najpierw samochod {self.marka} {self.model}")
            return
        if self._paliwo <= 0 :
            self._paliwo = 0
            print(f"pojazd {self.marka} {self.model} ma pusty bak! zatankuj aby jechac")
            return
        self.predkosc += o_ile
        self._paliwo -= 5
        if self.predkosc > self.predkosc_maksymalna :
            self.predkosc = 200
            print(f"pojazd {self.marka} {self.model} osiagnal limit konstrukcyjny predkosci ! szybciej sie jechac nie da!")
        print(f"{self.marka} {self.model} przyspieszyl o {o_ile} km/h! aktualna predkosc to {self.predkosc} a stan paliwa to {self._paliwo} litrów")



        
    def hamuj(self, o_ile):
        self.predkosc -= o_ile
        if self.predkosc < 0 :
            self.predkosc = 0
        print(f"{self.marka} {self.model} zwolnił o {o_ile} km/h aktualna predkosc to {self.predkosc}")


        
    def zatankuj(self, ile_litrow):
        if self.predkosc != 0 :
            print("nie mozesz tankowac podczas jazdy")
            return
        self._paliwo += ile_litrow
        if self._paliwo > 60 :
            self._paliwo = 60
            print("zbiornik moze pomiescic tylko 60 litrow")
        print(f"{self.marka} {self.model} zostal zatankowany, paliwo wynosi {self._paliwo}")


        
    def wlacz(self):
        self.uruchomiony = True
        print(f"samochod {self.marka} {self.model} zostal uruchomiony")

    def wylacz(self):
        self.uruchomiony = False
        print(f"samochod {self.marka} {self.model} zostal wylaczony")


class SamochodSportowy(samochod):
    def __init__ (self, marka, model, silnik, typ,):
        super().__init__(marka, model, silnik, typ,)
        self.predkosc_maksymalna = 350




            
    def przyspiesz(self, o_ile):
        if not self.uruchomiony :
            print(f" uruchom najpierw samochod {self.marka} {self.model}")
            return
        if self._paliwo < 0 :
            self._paliwo = 0
            print(f"pojazd {self.marka} {self.model} ma pusty bak! zatankuj aby jechac")
            return
        self.predkosc += o_ile
        self._paliwo -= 5
        if self.predkosc > self.predkosc_maksymalna :
            self.predkosc = 350
            print(f"pojazd {self.marka} {self.model} osiagnal limit konstrukcyjny predkosci ! szybciej sie jechac nie da!")
        print(f"{self.marka} {self.model} przyspieszyl o {o_ile} km/h! aktualna predkosc to {self.predkosc} a stan paliwa to {self._paliwo} litrów")



        
    def turbo(self):
        if self.uruchomiony == False :
            print("uruchom najpierw silnik")
            return
        if self._paliwo <= 0 :
            self.paliwo = 0
            print("masz za malo paliwa")
            return
            
        self.predkosc += 150
        if self.predkosc > 350 :
            self.predkosc = 350
        self._paliwo -= 10
        print(f" samochod {self.marka} {self.model} wlaczyl turbo, jego predkosc to teraz {self.predkosc} a paliwo to {self._paliwo} litrow")
        




flota = [

    samochod("bmw", "X5", "2.0V", "sedan"),
    samochod("opel", "vectra", "1.6V", "combi"),
    SamochodSportowy("ferrari", "la ferrari", "6.5V", "sedan")
]
for pojazd in flota :
    pojazd.opisz_auto()
    pojazd.wlacz()
    pojazd.przyspiesz(50)
    if isinstance(pojazd, SamochodSportowy):
        pojazd.turbo()
    pojazd.wylacz()
