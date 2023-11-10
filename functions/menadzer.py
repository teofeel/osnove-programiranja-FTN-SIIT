from functions import ulogovani_korisnici
import korisnik

def main(korisnicko_ime):
    _id = korisnicko_ime

    while True:
        print('Ulogovani Menadzer')
        print('1. Dodaj novog prodavca')
        print('2. Dodaj novog menadzera')
        print('3. Izmena licnih podataka')
        print('4. Odjava')
        print('5. Izlazak iz aplikacije')

        unos = input('Izaberite: ')
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==1:
            dodaj_zaposlenog()
        elif unos==2:
            dodaj_zaposlenog('menadzer')
        elif unos==3:
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==4:
            return
        elif unos==5:
            exit()

def dodaj_zaposlenog(zaposleni='prodavac'):
    while True:
        print('Da se vratite unesite ;')

        korisnicko_ime = input('Unesite korisnicko ime (karakter ; u korisnickom imenu je zabranjen): ')
        if korisnicko_ime==';':return
        for k in korisnik.korisnici:
            while korisnicko_ime == k["korisnicko_ime"]:
                korisnicko_ime = input('Korisnicko ime je vec registrovano. Unesite opet korisnicko ime: ')
        while ';'in korisnicko_ime:
            korisnicko_ime = input('Unesite opet korisnicko ime: ')

        ime = input('Unesite ime (karakter ; u imenu je zabranjen): ')
        if ime==';':return
        while ';'in ime:
            ime = input('Unesite opet ime: ')

        prezime = input('Unesite prezime (karakter ; u prezimenu je zabranjen): ')
        if korisnicko_ime==';':return
        while ';'in korisnicko_ime:
            korisnicko_ime = input('Unesite opet prezime: ')

        lozinka = input('Unesite lozinku (karakter ; u lozinci je zabranjen): ')
        if lozinka==';':return
        while ';'in lozinka or (not any(i.isdigit() for i in lozinka)) or len(lozinka)<6:
            lozinka = input('Lozinka mora biti duza od 6 karaktera, ne sme da sadrzi ; i mora sadrzati barem jednu cifru. Unesite opet lozinku: ')
            if lozinka==';':return

        novi_prodavac = {
            "korisnicko_ime":korisnicko_ime, 
            "lozinka":lozinka,
            "ime":ime,
            "prezime":prezime,
            "uloga":zaposleni
        }

        korisnik.novi_korisnik(novi_prodavac)
        return
        
