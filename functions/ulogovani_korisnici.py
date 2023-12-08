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
                
            termin.slobodna_sedista(sifra_termina.upper(), None)

            sediste = input('Unesite vrednost sedista (; da se vratite na pocetak): ')
            if sediste == ';': continue

            while not bioskopske_karte.provera_slobodnog_mesta(sifra_termina.upper(), sediste.upper()):
                sediste = input('Sediste se ne moze rezervisati. Rezervisite drugo (; za izlazak): ')
                if sediste == ';': return

            bioskopske_karte.rezervisi_kartu(ime, sifra_termina.upper(), sediste.upper())

            ponovo = input('Da li zelite jos da rezerviste (Y/N): ')
            if ponovo.upper() == 'N':return

