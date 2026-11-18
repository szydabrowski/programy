class dronFSM:
    def __init__(self):
        self.stan = "na ziemi"
        print(f"dron wystartowal aktulany stan :{self.stan}")
    def obsluz_zdarzenie(self) :
        if self.stan == "na ziemi":
            print("dron sobie odpoczywa")
        elif self.stan == "lot" :
            print("dron jest w powietrzu")
        elif self.stan == "powrot na ziemie":
            print("dron wraca na ziemie")
        else:
            print("dron ma awarie!!")
    def sprawdz_stan(self):
        print(f"stan drona {self.dronFSM} to {self.stan}")
    def zmien_stan(self):
        
dron_x = dronFSM()

dron_x.obsluz_zdarzenie()


