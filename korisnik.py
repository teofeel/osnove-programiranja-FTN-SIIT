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

def pisi_fajl():
    korisnici_fajl = open('data/korisnici.txt', 'w')
    for k in korisnici:
        korisnici_fajl.write(k['korisnicko_ime']+';'+k['lozinka']+';'+k['ime']+';'+k['prezime']+';'+k['uloga']+'\n')
        
def novi_korisnik(korisnik):
    global korisnici
    korisnici.append(korisnik)
    pisi_fajl()
        



def izmeni_podatke(id,podatak,vrednost):
    for korisnik in korisnici:
        if podatak=='lozinka' and korisnik['korisnicko_ime'] == id:
            if not korisnik['lozinka'] == vrednost[0]: return 0
            korisnik['lozinka'] = vrednost[1]
            pisi_fajl()
        elif korisnik['korisnicko_ime'] == id:
            korisnik[podatak]=vrednost 
            pisi_fajl()


     

