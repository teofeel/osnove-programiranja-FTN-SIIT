from korisnik import korisnici
from korisnik import novi_korisnik
from functions import kupac
from film import filmovi

# funkcija za prijavu korisnika
def prijava():
    tryagn='y'
    while tryagn!='n':
        korisnicko_ime = input('Unesite korisnicko ime: ')
        lozinka = input('Unesite lozinku: ')

        for korisnik in korisnici:
            postoji = korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka']==lozinka
            if postoji and korisnik['uloga']=='registrovani kupac':
                return kupac.main()
            elif postoji and korisnik['uloga']=='prodavac':
                return
            elif postoji and korisnik['uloga']=='menadzer':
                return
            
        tryagn = input('Korisnicko ime ili lozinka je pogresna. Da li hocete opet da probate (y/n): ')
    if(tryagn=='n'):
        return 1
    return 0

def registracija():
    # funckija za registraciju korisnika
    # nakon sto se kreira objekat, on je ubacen u listu objekata korisnika
    # jedinstveno korisnicko ime
    # jedinstvena lozinka preko 6 karaktera sa jednom cifrom
    # zabranjeni karakter ;

    korisnicko_ime = input('Unesite korisnicko ime (; nije dozvoljen u imenu): ')
    # provera da li je korisnicko ime vec registrovano
    for korisnik in korisnici:
        while korisnicko_ime == korisnik["korisnicko_ime"]:
            korisnicko_ime = input('Korisnicko ime je vec registrovano. Unesite opet korisnicko ime: ')
    while ';'in korisnicko_ime:
        korisnicko_ime = input('Ime sadrzi nedozvoljeni karakter ; . Unesite opet korisnicko ime: ')

    ime = input('Unesite ime: ')
    while ';'in ime:
        ime = input('Unesite opet ime: ')

    prezime = input('Unesite prezime: ')
    while ';'in prezime:
        prezime = input('Unesite opet prezime: ')

    lozinka = input('Lozinka: ')
    while ';'in lozinka or lozinka.isdigit() or len(lozinka)<6:
        lozinka = input('Lozinka mora biti duza od 6 karaktera, ne sme da sadrzi ; i mora sadrzati barem jednu cifru. Unesite opet lozinku. : ')

    korisnik={
        "korisnicko_ime":korisnicko_ime, 
        "lozinka":lozinka,
        "ime":ime,
        "prezime":prezime,
        "uloga":"registrovani kupac"
    }

    novi_korisnik(korisnik)

    kupac.main()

#######################################
# Funkcije za sve (ne)ulogovane korisnike bilo kada

from film import pregled_filmova
def pregled_filmova_main():
    if pregled_filmova()==0:
        print('Trenutno nema dostupnih filmova')
    

def pretraga_filmova():
    print('Dostupni filteri: Naziv Filma | Zanr | Trajanje | Reziser | Uloge | Zemlja Porekla | Godina Proizvodnje')
    print('Ako odustajete unesite ;')

    i = 0
    while i==0:
        filter = input('Unesite filter: ')
        if filter == ';':
            return 
        elif filter == '':
            pregled_filmova_main()
            i=1

        elif filter.upper() == 'TRAJANJE':
            # ovo treba zavrsiti
            i=0
            
        elif filter == 'godina':
            vrednost = int(input('Unesite vrednost: '))
        else:
            vrednost = input('Unesite vrednost: ')
