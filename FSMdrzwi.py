class drzwiFSM() :
    def __init__(self):
        self.stan = "zamkniete"
    def zmien_stan_zablokowania_drzwi(self):
        if self.stan == "zablokowane":
            self.stan = "zamkniete"
            print("drzwi zostaly odblokowane")
        elif self.stan == "zamkniete":
            self.stan = "zablokowane"
            print("drzwi zostaly zablokowane")
        elif self.stan == "otwarte":
            print("co ty robisz? przeciez drzwi sa otwarte!")






    def zmien_stan(self):
        if self.stan == "zamkniete":
            self.stan = "otwarte"
        elif self.stan == "otwarte":
            self.stan = "zamkniete"
        elif self.stan == "zablokowane":
            print("drzwi sa zablokowane nie da sie ich ruszyc")

drzwi_czarne = drzwiFSM()
drzwi_czarne.zmien_stan_zablokowania_drzwi()