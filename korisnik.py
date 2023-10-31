# fajl korisnik
# koristi se za logovane korisnike, prodavce i menadzere
# sve njihove funkcionalnosti ce biti u ovoj klasi

# funkcija za prijavu korisnika
def prijava(korisnici, korisnicko_ime, lozinka):
    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka']==lozinka:
            return korisnik
        

