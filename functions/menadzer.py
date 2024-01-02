from functions import ulogovani_korisnici
import korisnik

def main(korisnicko_ime):
    _id = korisnicko_ime

    while True:
        print('Ulogovani Menadzer')
        print('1. Dodaj novog prodavca')
        print('2. Dodaj novog menadzera')
        print('3. Izmena filma')
        print('4. Izmena bioskopske projekcije')
        print('5. Izmena licnih podataka')
        print('6. Odjava')
        print('7. Izlazak iz aplikacije')

        unos = input('Izaberite: ')
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==1:
            dodaj_zaposlenog()
        elif unos==2:
            dodaj_zaposlenog('menadzer')
        elif unos==3: 
            izmena_filma()
        elif unos==4: continue
        elif unos==5:
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==6:
            return
        elif unos==7:
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

        if korisnik.novi_korisnik(novi_prodavac):
            print('Novi korisnik je dodat')
        return
    
from functions import svi_korisnici
import film
def izmena_filma():
    while True:
        print('1. Dodaj novi film | 2. Izmeni podatke o filmu | 3. Obrisi film')

        unos = input('odaberite opciju (; za nazad) ')
        if unos==';':return
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==1: dodaj_film()
        if unos==2: 
            print('1. Direktna izmena | 2. Prikaz svih filmova')
            unos = input('Odaberite: ')
            if unos==';':return
            if not unos.isdigit(): continue
            unos = int(unos)

            if unos==2: 
                svi_korisnici.pregled_filmova_main()

            naziv = input('Unesite naziv filma: ')
            if naziv==';': return
            izmena_polja_filma(naziv)
        if unos==3: 
            print('1. Direktna izmena | 2. Prikaz svih filmova')
            unos = input('Odaberite: ')
            if unos==';':return
            if not unos.isdigit(): continue
            unos = int(unos)

            if unos==2: svi_korisnici.pregled_filmova_main()

            naziv_filma = input('Unesite naziv filma: ')

            film.obrisi_film(naziv_filma)

def dodaj_film():
    naziv = input('Unesite naziv: ')
    if naziv==';': return
    zanr = input('Unesite zanr: ')
    if zanr==';':return
    
    trajanje=input('Unesite trajanje: ')
    if trajanje==';':return
    while not trajanje.isdigit():   
        trajanje=input('Unesite trajanje: ')

    reziser = input('Reziser: ')
    if reziser==';':return
    uloge = input('Glumci (Odvajajte sa zarezom i razmakom, npr. `, `): ')
    if uloge==';':return
    zemlja_porekla = input('Zemlja porekla filma: ')
    if zemlja_porekla==';':return
    
    godina = input('Godina objave filma: ')
    if godina==';':return
    while not godina.isdigit(): 
        godina = input('Godina objave filma: ')

    opis=input('Kratak opis filma: ')
    if opis==';':return

    if not film.dodaj_film(naziv,zanr,trajanje,reziser,
                           uloge,zemlja_porekla,godina,opis):
        print('Film vec postoji')

def izmena_polja_filma(naziv_original):
    filter = []
    vrednosti = []
    while True:
        print('1. Naziv | 2. Zanr | 3. Trajanje | 4. Reziser | 5. Uloge | 6. Zemlja porekla | 7. Godina | 8. Opis')
        unos = input('Izaberite: ')
        if unos==';':return
        elif not unos.isdigit():continue

        unos=int(unos)

        if unos==1:
            filter.append('naziv')
            naziv = input('Unesi naziv: ')
            if naziv==';':return

            vrednosti.append(naziv)
        elif unos==2:
            filter.append('zanr')
            naziv = input('Unesi zanr: ')
            if naziv==';':return
            
            vrednosti.append(naziv)
        elif unos==3:
            filter.append('trajanje')
            naziv = input('Unesi trajanje: ')
            if naziv==';':return
            while not naziv.isdigit(): naziv = input('Unesi trajanje')
            vrednosti.append(naziv)
        elif unos==4:
            filter.append('reziser')
            naziv = input('Unesi rezisera: ')
            if naziv==';':return
            
            vrednosti.append(naziv)
        elif unos==5:
            filter.append('uloge')
            naziv = input('Unesi uloge(Odvajaj po `, `): ')
            if naziv==';':return
            
            vrednosti.append(naziv)
        elif unos==6:
            filter.append('zemlja_porekla')
            naziv = input('Unesi zemlju porekla: ')
            if naziv==';':return
            
            vrednosti.append(naziv)
        elif unos==7:
            filter.append('godina')
            godina = input('Unesi godinu: ')
            if godina==';':return
            while not godina.isdigit(): godina = input('Unesite godinu: ')
            vrednosti.append(godina)
        elif unos==8:
            filter.append('opis')
            opis = input('Unesi opis: ')
            if opis==';':return
            
            vrednosti.append(opis)

        opet = input('Da li zelite jos nesta da promenite (y/n): ')
        if opet.lower()=='n': film.izmeni_film(naziv_original, filter, vrednosti)    
        
        