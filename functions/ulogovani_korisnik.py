#funckija za ispisivanje mogucnosti kao registrovan korisnik
def ulogovan_main():
    print('Ulogovani ste!!!!!!')
    unos = 0
    while unos!=3:
        print('Ulogovani korisnik')
        unos = int(input('Izaberite: '))

    izlazak()

# funkcija za prijavu korisnika
def prijava(korisnici):
    korisnicko_ime = input('Unesite korisnicko ime: ')
    lozinka = input('Unesite lozinku: ')

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka']==lozinka:
            ulogovan_main()
    return 0
        
def izlazak():
    exit()