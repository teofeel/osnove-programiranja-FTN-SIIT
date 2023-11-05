from korisnik import korisnici
import korisnik

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