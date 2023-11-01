from korisnik import korisnici
from korisnik import novi_korisnik
from functions import kupac
from film import filmovi

# funkcija za prijavu korisnika
def prijava():
    tryagn='y'
    while tryagn!='n':
        print('Za prekidanje prijave unesite ;')
        korisnicko_ime = input('Unesite korisnicko ime: ')
        if korisnicko_ime == ';': return
        lozinka = input('Unesite lozinku: ')
        if lozinka == ';': return

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
    print('Za prekidanje registracije unesite ;')
    korisnicko_ime = input('Unesite korisnicko ime (; nije dozvoljen u imenu): ')
    # provera da li je korisnicko ime vec registrovano
    if korisnicko_ime == ';': return
    for korisnik in korisnici:
        while korisnicko_ime == korisnik["korisnicko_ime"]:
            korisnicko_ime = input('Korisnicko ime je vec registrovano. Unesite opet korisnicko ime: ')
    while ';'in korisnicko_ime:
        korisnicko_ime = input('Ime sadrzi nedozvoljeni karakter ; . Unesite opet korisnicko ime: ')

    ime = input('Unesite ime: ')
    if ime == ';': return
    while ';'in ime:
        ime = input('Unesite opet ime: ')

    prezime = input('Unesite prezime: ')
    if prezime == ';': return
    while ';'in prezime:
        prezime = input('Unesite opet prezime: ')

    lozinka = input('Lozinka: ')
    if lozinka == ';': return
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
    
from film import pretraga_filmova_filter
def pretraga_filmova():
    print('Dostupni filteri: 1.) Naziv Filma | 2.) Zanr | 3.) Trajanje | 4.) Reziser | 5.) Uloge | 6.) Zemlja Porekla | 7.) Godina Proizvodnje')
    print('Ako odustajete unesite bilo koje slovo')

    i = 0
    while True:
        filter = input('Unesite filter: ')
        if filter=='':
            return pregled_filmova_main()
        elif not filter.isdigit():
            return
            
        filter = int(filter)
        
        if filter > 7 or filter < 1:
            pregled_filmova_main()
            return

        elif filter == 3:
            j=0
            while j==0:
                print('Izaberite po da li ocete maks, min ili granicno trajanje')
                print('1.) Maksimalno trajanje | 2.) Minimalno trajanje | 3.) Granicno trajanje')

                izbor = input('Unesite vrednost: ')
                if not izbor.isdigit(): continue
                izbor = int(izbor)
                if izbor<1 or izbor>3: continue
                j=1

            if izbor==1:
                j=0
                while j==0:
                    min_vrednost = input('Maksimalno trajanje filma: ')
                    if not min_vrednost.isdigit(): continue
                    min_vrednost = int(min_vrednost)

                    vrednost = {"izbor":izbor, "vrednost":[min_vrednost]}
                    j=1

            elif izbor==2:
                j=0
                while j==0:
                    max_vrednost = input('Minimalno trajanje filma: ')
                    if not max_vrednost.isdigit(): continue
                    max_vrednost = int(max_vrednost)
                    
                    vrednost = {"izbor":izbor, "vrednost":[max_vrednost]}
                    j=1

            elif izbor==3:
                j=0
                while j==0:
                    min_vrednost = input('Minimalno trajanje filma: ')
                    if not min_vrednost.isdigit(): continue
                    max_vrednost = input('Maksimalno trajanje filma: ')
                    if not max_vrednost.isdigit(): continue
                    min_vrednost = int(min_vrednost)
                    max_vrednost = int(max_vrednost)

                    vrednost = {"izbor":izbor, "vrednost":[min_vrednost, max_vrednost]}
                    j=1
            
            return pretraga_filmova_filter(filter, vrednost)
            
        elif filter == 7:
            j=0
            while j==0:
                vrednost = input('Unesite godinu: ')
                if vrednost==';': return
                elif not vrednost.isdigit(): continue
                vrednost = int(vrednost)
                j=1
                
            return pretraga_filmova_filter(filter, vrednost)
        
        else:
            vrednost = input('Unesite vrednost: ')
            return pretraga_filmova_filter(filter, vrednost)