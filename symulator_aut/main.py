from pojazdy import samochod, SamochodSportowy


BMW_X5 = samochod("bmw", "X5", "2.0V", "sedan")
opel_vectra = samochod("opel", "vectra", "1.6V", "combi")
ferrari_la_ferrari = SamochodSportowy("ferrari", "la ferrari", "6.5V", "sedan")

BMW_X5.wlacz()
BMW_X5.przyspiesz(50)
BMW_X5.przyspiesz(100)
ferrari_la_ferrari.wlacz()
ferrari_la_ferrari.przyspiesz(100)
ferrari_la_ferrari.turbo()
ferrari_la_ferrari.hamuj(250)
ferrari_la_ferrari.zatankuj(30)
ferrari_la_ferrari.wylacz()
