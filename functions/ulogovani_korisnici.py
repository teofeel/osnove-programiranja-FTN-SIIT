from korisnik import korisnici
import korisnik
from bioskopske_karte import karte
import bioskopske_karte
from functions import svi_korisnici

def izmena_licnih_podataka(_id):
    while True:
        for k in korisnici:
            if k['korisnicko_ime']==_id:
                print(k['ime'],' | ', k['prezime'])

        print('1) Ime | 2) Prezime | 3) Sifra')
        podatak = input('Unesite sta ocete da izmenite (za povratak unesite ;): ')
        if podatak==';': return 
        elif not podatak.isdigit(): continue
        podatak = int(podatak)

        if podatak==1:
            while True:
                ime = input('Unesite novo ime (karakter ; je zabranjen u imenu): ')
                if ime == ';': return
                elif ';'in ime: continue

                korisnik.izmeni_podatke(_id, 'ime', ime)
                break
        elif podatak==2:
             while True:
                prezime = input('Unesite novo prezime (karakter ; je zabranjen u prezimenu): ')
                if prezime == ';': return
                elif ';'in prezime: continue

                korisnik.izmeni_podatke(_id, 'prezime', prezime)
                break
        elif podatak==3:
            while True:
                stara_lozinka = input('Unesite novu staru lozinku: ')
                if stara_lozinka == ';': return

                lozinka = input('Unesite novu lozinku (karakter ; je zabranjen u lozinki): ')
                if lozinka == ';': return
                while ';'in lozinka or (not any(i.isdigit() for i in lozinka)) or len(lozinka)<6:
                    lozinka = input('Unesite novu lozinku (karakter ; je zabranjen u lozinki): ')

                if korisnik.izmeni_podatke(_id, 'lozinka', [stara_lozinka, lozinka])==0: 
                    print('Stara lozinka je pogresna, pokusajte opet')
                    continue
                break

import termin
def rezervisi_kartu(ime, prodavac):
    while True:
        print('1. Direktan unos sifre termina | 2. Pretraga termina')
        unos = input('Odaberite opciju 1 ili 2: ')

        if unos == ';': return
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==2:
            svi_korisnici.pretraga_termina()

        sifra_termina = input('Unesite sifru termina: ')
        if sifra_termina == ';': return
            
        if prodavac==1:
            ime = input('Unesite ime i prezime za neregistrovanog, odnosno korisnicko ime za registrovanog kupca: ').upper()
            if ime ==';':return
                
        while not termin.slobodna_sedista(sifra_termina.upper(), None):
            sifra_termina = input('Termin ne postoji. Unesite opet sifru termina: ')
            if sifra_termina == ';': return

        sediste = input('Unesite vrednost sedista (; da se vratite na pocetak): ')
        if sediste == ';': continue

        while not (bioskopske_karte.provera_slobodnog_mesta(sifra_termina.upper(), sediste.upper()) and
                   termin.slobodna_sedista(sifra_termina.upper(), sediste.upper())):
            sediste = input('Sediste se ne moze rezervisati. Rezervisite drugo (; za izlazak): ')
            if sediste == ';': return

        bioskopske_karte.rezervisi_kartu(ime, sifra_termina.upper(), sediste.upper())

        ponovo = input('Da li zelite jos da rezerviste (Y/N): ')
        if ponovo.upper() == 'N':return



def pregled_rezervacija(ime,prodavac):
    while True:
        if prodavac==1:
            print('1. Pregled svih rezervacija | 2. Pregled rezervacija kupca')
            unos = input('Odaberite opciju: ')
            if unos==';': return
            if not unos.isdigit(): continue

            unos=int(unos)
            if unos==1: bioskopske_karte.pregled_rezervacija(None, 1,1)
            elif unos==2:
                ime = input('Unesite ime i prezime kupca (korisnicko ime za registrovanog): ').upper()
                if ime==';':return
                bioskopske_karte.pregled_rezervacija(ime,0,1)
        else:
            bioskopske_karte.pregled_rezervacija(ime, 0,0)
            return

def ponisti_rezervaciju_prodaju(ime, rezervacija):
    while True:
        if rezervacija:
            print('1. Direktno obrisite rezervaciju unosom termina i sedista | 2. Pregled rezervacija')
        else:
            print('1. Direktno obrisite kupljenu kartu unosom termina i sedista | 2. Pregled rezervacija')
        unos = input('Odaberite opciju (; za nazad): ')

        if unos == ';':return
        elif not unos.isdigit(): continue
        unos = int(unos)

        if unos==2:
            bioskopske_karte.pregled_rezervacija(ime,0,0)
        
        termin = input('Unesite termin projekcije: ')
        if termin==';': return

        sediste = input('Unesite oznaku sedista: ')
        if sediste == ';': return

        if rezervacija:
            while not bioskopske_karte.ponisti_rezervaciju_kupovinu(ime.upper(), termin.upper(), sediste.upper(), 'rezervisana'):
                print('Nije moguce ponistiti rezervaciju (Termin ili sediste ne odgovara ni jednoj postojecoj rezervaciji)\n')
                termin = input('Unesite opet termin projekcije: ')
                if termin==';': return

                sediste = input('Unesite opet oznaku sedista: ')
                if sediste == ';': return

            opet = input('Rezervacija je ponistena. Ocete jos neku da ponistite (y/n): ')
            if opet.upper()=='Y': continue

        else:
            while not bioskopske_karte.ponisti_rezervaciju_kupovinu(ime.upper(), termin.upper(), sediste.upper(), 'kupljena'):
                print('Nije moguce ponistiti kupovinu (Termin ili sediste ne odgovara ni jednoj postojecoj rezervaciji)\n')
                termin = input('Unesite opet termin projekcije: ')
                if termin==';': return

                sediste = input('Unesite opet oznaku sedista: ')
                if sediste == ';': return

            opet = input('Kupovina je ponistena. Ocete jos neku da ponistite (y/n): ')
            if opet.upper()=='Y': continue
        
        return