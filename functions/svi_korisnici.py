from korisnik import korisnici
from korisnik import novi_korisnik
from functions import ulogovani_korisnik
from film import filmovi
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

    ulogovani_korisnik.ulogovan_main()


def pregled_filmova():
    for film in filmovi:
        for i in film:
            print(str(i).upper()+":", end=" ")
            print(film[i], end="\n")
        print('//////////////////////',end="\n")
    return 0