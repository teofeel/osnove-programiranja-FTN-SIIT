# klasa za kartu
class Karta:
    def __init__(self, ime, termin_projekcije, oznaka_sedista,
                datum_prodaje, rezervisana_kupljena):
        # korisnicko ime za registrovane kupce, za neregistrovane ime+prezime
        # ime i prezime za ne registrovane
        # termin projekcije je klasa Termin_projekcije iz termin_projekcije.py
        # oznaka sedista = broj reda + oznaka_sedista iz klase Sala iz sala.py
        # karta moze biti ili rezervicana (samo za registrovane) ili kupljena

        self.ime                    = ime
        self.termin_projekcije      = termin_projekcije
        self.sediste                = oznaka_sedista
        self.datum_prodaje          = datum_prodaje
        self.rezervisana_kupljena   = rezervisana_kupljena