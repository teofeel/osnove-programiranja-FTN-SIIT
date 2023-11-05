# fajl korisnik
# koristi se za logovane korisnike, prodavce i menadzere
# sve njihove funkcionalnosti ce biti u ovoj klasi
korisnici = []
def ucitaj_korisnike():
    global korisnici
    with open('data/korisnici.txt') as korisnici_fajl:
        lines = korisnici_fajl.readlines()
        for line in lines:
            data = line.split(';')
            korisnici.append({
                "korisnicko_ime":data[0], 
                "lozinka":data[1],
                "ime":data[2],
                "prezime":data[3],
                "uloga":data[4].split('\n')[0]
            }) 

def novi_korisnik(korisnik):
    global korisnici
    korisnici.append(korisnik)

def izmeni_podatke(id,podatak,vrednost):
    for korisnik in korisnici:
        if podatak=='lozinka' and korisnik['korisnicko_ime'] == id:
            if not korisnik['lozinka'] == vrednost[0]: return 0
            korisnik['lozinka'] = vrednost[1]
            return 1
        elif korisnik['korisnicko_ime'] == id:
            korisnik[podatak]=vrednost 
            return 1

     

