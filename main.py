## UCITAVANJE PODATAKA IZ FAJLOVA ##

# liste za podatke iz .json fajlova
korisnici   = []
filmovi     = []
sale        = []
projekcije  = []
termini     = []
karte       = []

import json
# funckija za ucitavanje podataka iz json fajlova
def ucitaj_podatke():
    # iz svih fajlova se podaci ucitavaju u prethodno navedene liste
    # lste su globalne funkcija ne vraca nista
    # liste su globalne
    global korisnici
    global filmovi
    global sale
    global projekcije
    global termini
    global karte

    # ucitavanje podataka iz fajlova
    with open('data/korisnik.json') as korisnici_fajl:
        korisnici = json.load(korisnici_fajl)
    with open('data/film.json') as filmovi_fajl:
        filmovi = json.load(filmovi_fajl)
    with open('data/sala.json') as sale_fajl:
        sale = json.load(sale_fajl)
    with open('data/projekcija.json') as projekcije_fajl:
        projekcije = json.load(projekcije_fajl)
    with open('data/termin_projekcije.json') as termin_fajl:
        termini = json.load(termin_fajl)
    with open('data/karta.json') as karte_fajl:
        karte = json.load(karte_fajl)

##########################################################################

## FUNCKIJE ZA SVE KORISNIKE ##

def registracija():
    # funckija za registraciju korisnika
    # u telu funkcije treba da idu osnovni podaci o korisniku
    # nakon sto se kreira objekat, on je ubacen u listu objekata kupaca
    # jedinstveno korisnicko ime
    # jedinstvena lozinka preko 6 karakyera sa jednom cifrom

    return 0

##########################################################################

import korisnik

def main():
    ucitaj_podatke()  
    i = 0
    while i!=3:
        print('/////////////////////')
        print('1. Prijava na sistem')
        print('2. Registracija na sistem')
        print('3. Izlazak iz aplikacije')
        print('/////////////////////')

        i = int(input('Izaberite: '))
        if i==1:
            korisnik.prijava(korisnici)
        elif i==2: 
            registracija()
        

main()
