# klasa korisnik
# koristi se za logovane korisnike, prodavce i menadzere
# sve njihove funkcionalnosti ce biti u ovoj klasi

class Korisnik:
    def __init__(self, korisnicko_ime, lozinka, ime, prezime, uloga):
        self.korisnicko_ime =           korisnicko_ime
        self.lozinka        =           lozinka
        self.ime            =           ime
        self.prezime        =           prezime
        self.uloga          =           uloga

    