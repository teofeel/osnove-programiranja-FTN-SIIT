#klasa za termin projekcije

class Termin_Projekcije:
    def __init__(self, projekcija, datum, sifra):
        # projekcija je tipa klasa Projekcija iz projekcija.py
        # za datum treba samo datum bez vremena
        
        self.projekcija = projekcija
        self.datum = datum
        self.sifra = projekcija.sifra+sifra+'|'+datum
        return 0