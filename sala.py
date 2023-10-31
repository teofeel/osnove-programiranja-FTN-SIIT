# klasa za salu projekcije

class Sala:
    def __init__(self, sifra, naziv, broj_redova, oznaka_sedista):
        # naziv nije obavezan
        # broj redova 1,2,3,4,.....
        # oznaka sedista A,B,C,....
        self.sifra           = sifra
        self.naziv           = naziv
        self.broj_redova     = broj_redova
        self.oznaka_sedista  = oznaka_sedista
        