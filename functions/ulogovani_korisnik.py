from korisnik import korisnici
from functions import svi_korisnici
#funckija za ispisivanje mogucnosti kao registrovan korisnik
def ulogovan_main():
    print('///////////////////')
    unos = 0
    while unos!=3:
        print('Ulogovani korisnik')
        print('1. Pregled filmova')
        print('2. Odjava')
        print('3. Izlazak iz aplikacije')
        unos = int(input('Izaberite: '))
        
        if unos==1:
            svi_korisnici.pregled_filmova()
        elif unos==2:
            return
    izlazak()

# funkcija za prijavu korisnika
def prijava():
    tryagn='y'
    while tryagn!='n':
        korisnicko_ime = input('Unesite korisnicko ime: ')
        lozinka = input('Unesite lozinku: ')

        for korisnik in korisnici:
            if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka']==lozinka:
                return ulogovan_main()
        
        tryagn = input('Korisnicko ime ili lozinka je pogresna. Da li hocete opet da probate (y/n): ')
    if(tryagn=='n'):
        return 1
    return 0
      
def izlazak():
    exit()