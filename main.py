## UCITAVANJE PODATAKA IZ FAJLOVA ##

# liste za podatke iz .json fajlova
korisnici   = []
filmovi     = []
sale        = []
projekcije  = []
termini     = []
karte       = []

import json
from korisnik import Korisnik
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
    with open('data/korisnici.txt') as korisnici_fajl:
        lines = korisnici_fajl.readlines()
        for line in lines:
            data = line.split(';')
            korisnici.append(Korisnik(data[0],data[1],data[2],data[3],data[4])) 
    #with open('data/film.json') as filmovi_fajl:
        #filmovi = json.load(filmovi_fajl)
    #with open('data/sala.json') as sale_fajl:
        #sale = json.load(sale_fajl)
    #with open('data/projekcija.json') as projekcije_fajl:
        #projekcije = json.load(projekcije_fajl)
    #with open('data/termin_projekcije.json') as termin_fajl:
        #termini = json.load(termin_fajl)
    #with open('data/karta.json') as karte_fajl:
        #karte = json.load(karte_fajl)

##########################################################################

## FUNCKIJE ZA SVE KORISNIKE ##

def registracija():
    # funckija za registraciju korisnika
    # nakon sto se kreira objekat, on je ubacen u listu objekata korisnika
    # jedinstveno korisnicko ime
    # jedinstvena lozinka preko 6 karaktera sa jednom cifrom
    # zabranjeni karakter ;

    korisnicko_ime = input('Unesite korisnicko ime (; nije dozvoljen u imenu): ')
    # provera da li je korisnicko ime vec registrovano
    for korisnik in korisnici:
        while korisnicko_ime == korisnik.getKorisnickoIme():
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

    return 0

##########################################################################

from functions import ulogovani_korisnik

def main():
    ucitaj_podatke()  
    
    i = 0
    while i!=3:
        print('/////////////////////')
        print('1. Prijava na sistem')
        print('2. Registracija na sistem')
        #
        #
        #
        #
        print('3. Izlazak iz aplikacije')
        print('/////////////////////')

        i = int(input('Izaberite: '))
        if i==1:
            ulogovani_korisnik.prijava(korisnici)
        elif i==2: 
            registracija()
        
main()
