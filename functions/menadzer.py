from functions import ulogovani_korisnici
import korisnik
from functions import izvestaji
from film import filmovi
def main(korisnicko_ime):
    _id = korisnicko_ime

    while True:
        print('Ulogovani Menadzer')
        print('1. Dodaj novog prodavca')
        print('2. Dodaj novog menadzera')
        print('3. Izvestaji')
        print('4. Izmena filma')
        print('5. Izmena bioskopske projekcije')
        print('6. Izmena licnih podataka')
        print('7. Odjava')
        print('8. Izlazak iz aplikacije')

        unos = input('Izaberite: ')
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==1:
            dodaj_zaposlenog()
        elif unos==2:
            dodaj_zaposlenog('menadzer')
        elif unos==3: 
            izvestaji.izvestaji_main()
        elif unos==4: 
            izmena_filma()
        elif unos==5: 
            izmena_projekcije()
        elif unos==6:
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==7:
            return
        elif unos==8:
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
        
import projekcija    
def izmena_projekcije():
    while True:
        print('1. Dodaj bioskopsku projekciju | 2. Izmeni bioskopsku projekciju | 3. Obrisi bioskopsku projekciju')
        unos = input('Odaberite: ')
        if unos==';':return
        if not unos.isdigit(): continue
        unos= int(unos)

        if unos==1:
            print('Vec postojece projekcije')
            projekcija.ispisi_projekcije()
            dodaj_projekciju()
        elif unos==2:
            print('Postojece projekcije')
            projekcija.ispisi_projekcije()

            sifra = input('Unesite sifru projekcije: ')
            if sifra==';': return
            while not sifra.isdigit(): sifra = input('Unesite sifru projekcije: ')
            izmeni_polja_projekcije(sifra)
        elif unos==3:
            print('1. Direktan unos | 2. Pregled filmova')
            unos = input('Unesite: ')
            if unos==';':return
            if not unos.isdigit(): continue
            unos=int(unos)
            if unos==2: svi_korisnici.pregled_filmova_main()

            naziv = input('Unesite naziv filma: ')
            if naziv==';':return
            projekcija.obrisi_projekciju(naziv)

import re
from datetime import datetime,timedelta
import termin
def dodaj_projekciju():
    svi_korisnici.pregled_filmova_main()
    naziv_filma = input('Unesite naziv filma: ')
    if naziv_filma ==';': return

    sifra = input('Unesite sifru: ')
    if sifra==';': return
    while not sifra.isdigit(): sifra = input('Unesite sifru: ')

    sala = input('Unesite salu: ')
    if sala==';':return

    pocetak = unos_vremena('pocetak')
    if pocetak ==';':return
    kraj = dodaj_vreme_filma(naziv_filma.upper(), pocetak)

    dani = unos_dana()
    if dani==';':return
    
    cena = input('Unesite cenu: ')
    if cena==';':return
    while not cena.isdigit(): cena = input('Unesite cenu: ')

    if not projekcija.dodaj_projekciju(sifra, sala.upper(), pocetak, kraj, dani, naziv_filma, cena):
        print('Nije moguce dodati projekciju')



def dodaj_vreme_filma(naziv_filma, pocetak):
    for film in filmovi:
        if film['naziv'].upper() == naziv_filma.upper():
            pocetak_data = pocetak.split(':')
            pocetak_dt = datetime.strptime(pocetak, '%H:%M')
            kraj = pocetak_dt + timedelta(minutes = int(film['trajanje']))
            return str(datetime.strftime(kraj,'%H:%M'))

def unos_vremena(koji):
    while True:
        vreme = input('Unesite '+ koji + ' (S:M format): ')
        if vreme==';':return vreme
        try:
            datetime.strptime(vreme, '%H:%M')
            return vreme
        except ValueError:
            continue

def unos_dana():
    while True:
        dani = input('Unesite dane (razdavajnje sa ` `): ')
        if dani==';':return dani

        dani_lista = dani.split(' ')

        br=1
        for d in range(len(dani_lista)):
            if not (dani_lista[d].lower()=='ponedeljak' or dani_lista[d].lower()=='utorak' or dani_lista[d].lower()=='sreda' or 
                    dani_lista[d].lower()=='cetvrtak' or dani_lista[d].lower()=='petak' or dani_lista[d].lower()=='subota' or dani_lista[d].lower()=='nedelja'):
                br=0
            
            dani_lista[d] = dani_lista[d].capitalize()

        dani = ' '.join(dani_lista)
       
        if br==0: continue
        return dani
    

def izmeni_polja_projekcije(sifra):
    while True:
        print('1. Film | 2. Cena | 3. Vreme | 4. Dani | 5. Sala')
        unos = input('Odaberite: ')
        if unos==';': return
        if not unos.isdigit(): continue
        unos=int(unos)

        if unos==1: izmeni_projekciju_film(sifra)

        elif unos==2:
            cena = input('Unesi novu cenu: ')
            if cena==';':return
            while not cena.isdigit(): cena = input('Unesi novu cenu: ')
            projekcija.izmeni_polje(sifra,'cena',cena)

        elif unos==3: izmeni_projekciju_vreme(sifra)
        elif unos==4: izmeni_projekciju_dani(sifra)
        elif unos==5: izmeni_projekciju_sala(sifra)
        
        opet = input('Da li ocete jos nesta da izmenite (y/n): ')
        if opet.lower()=='n': return

def izmeni_projekciju_film(sifra):
    svi_korisnici.pregled_filmova_main()
    naziv = input('Unesite novi naziv filma: ')
    if naziv==';':return

    projekcija.izmeni_polje(sifra,'film',naziv)

def izmeni_projekciju_dani(sifra):
    dani = input('Unesite dane projekcije (razdavajati sa ` `): ')
    if dani ==';': return

    dani_projekcije=dani.split(' ')

    for i in range(len(dani_projekcije)):
        while not (dani_projekcije[i].lower()=='ponedeljak' or dani_projekcije[i].lower()=='utorak' or dani_projekcije[i].lower()=='sreda' or 
                   dani_projekcije[i].lower()=='cetvrtak' or dani_projekcije[i].lower()=='petak' or dani_projekcije[i].lower()=='subota' 
                   or dani_projekcije[i].lower()=='nedelja'):
            
            dani_projekcije[i] = input('Dan `{0}` nije postojeci. Unesite opet: '.format(dani_projekcije[i]))

        dani_projekcije[i] = dani_projekcije[i].capitalize()

    projekcija.izmeni_polje(sifra,'dani', ' '.join(dani_projekcije))


def izmeni_projekciju_sala(sifra):
    sala = input('Unesite naziv sale: ')
    if sala ==';':return

    projekcija.izmeni_polje(sifra, 'sala', sala)

def izmeni_projekciju_vreme(sifra):
    pocetak = unos_vremena('pocetak')
    if pocetak ==';':return

    kraj = unos_vremena('kraj')
    if kraj == ';':return

    projekcija.izmeni_polje(sifra,'vreme', [pocetak,kraj])
