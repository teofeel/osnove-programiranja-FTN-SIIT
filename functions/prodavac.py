from functions import svi_korisnici, ulogovani_korisnici
import bioskopske_karte, termin

_id=''
def main(korisnicko_ime):
    global _id
    _id = korisnicko_ime
    while True:
        print('Meni - Ulogovani Prodavac')
        print('1. Pregled dostupnih filmova')
        print('2. Pretraga filmova')
        print('3. Visekriterijumska pretraga filmova')
        print('4. Pretraga termina')
        print('5. Rezervacija karata')
        print('6. Pregled rezervacija')
        print('7. Ponistite rezervaciju / kupljenu kartu')
        print('8. Pretraga karata')
        print('9. Prodaj kartu')
        print('10. Izmeni licne podatke')
        print('11. Odjava')
        print('12. Izlazak iz aplikacije ')

        unos = input('Vas izbor: ')
        if not unos.isdigit(): continue

        unos = int(unos)

        if unos==1:
            svi_korisnici.pregled_filmova_main()
        elif unos==2:
            svi_korisnici.pretraga_filmova(0)
        elif unos==3:
            svi_korisnici.pretraga_filmova(1)
        elif unos==4:
            svi_korisnici.pretraga_termina()
        elif unos==5:
            ulogovani_korisnici.rezervisi_kartu(None,1)
        elif unos==6:
            ulogovani_korisnici.pregled_rezervacija(None,1)
        elif unos==7:
            ime, rezervacija = ponistavanje_rezervacija_kupvoina()
            ulogovani_korisnici.ponisti_rezervaciju_prodaju(ime, rezervacija)
        elif unos==8:
            pretraga_karata()
        elif unos==9:
            direktna_prodaja_karte()
        elif unos==10:
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==11:
            _id=''
            return
        elif unos==12:
            exit()


def ponistavanje_rezervacija_kupvoina():
    ime = input('Unesite ime ')
    rezervacija = input('Da li je rezervacija y/n: ')

    while not (rezervacija.upper()=='Y' or rezervacija.upper()=='N'):
        rezervacija = input('Da li je rezervacija y/n: ')
    if rezervacija.upper()=='Y': rezervacija=True
    else: rezervacija=False

    return ime, rezervacija

def pretraga_karata():
    while True:
        print('1. Sifra projekcije | 2. Imenu (i prezimenu) kupca | 3. Datumu | 4. Status karte')

        unos = input('Odaberite neku od opcija za pretragu (; za nazad): ')
        if unos==';':return
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==1:
            odabir = input('1. Direktan unos termina | 2. Pregled termina projekcija: ')
            if odabir == ';':return 
            if not odabir.isdigit(): return
            if int(odabir) ==2:
                svi_korisnici.pretraga_termina()

            termin = input('Unesite termin: ')
            print('/////////////')
            bioskopske_karte.pronadji_karte(termin, None, None, None)
            return
        
        elif unos==2:
            ime = input('Unesite ime i prezime neregistrovanog, odnosno samo ime registrovanog kupca: ')
            bioskopske_karte.pronadji_karte(None, ime, None, None)

        elif unos==3:
            godina = input('Unesite godinu: ')
            while not godina.isdigit():
                godina = input('Unesite opet godinu: ')

            mesec = input('Unesite mesec (brojem): ')
            while (not mesec.isdigit()) or int(mesec)>12:
                mesec = input('Unesite opet mesec (brojem): ')

            dan = input('Unesite dan: ')
            while (not dan.isdigit()) or int(dan)>31:
                dan = input('Unesite opet dan: ')

            bioskopske_karte.pronadji_karte(None, None, (dan+'.'+mesec+'.'+godina+'.'), None)

        elif unos==4:
            rezervacija = input('Da li je karta rezervisana ili kupljena (r/k): ')
            while not (rezervacija=='r' or rezervacija=='k'):
                rezervacija = input('Da li je karta rezervisana ili kupljena (r/k): ')
            
            if rezervacija=='k': rezervacija='kupljena'
            else: rezervacija='rezervisana'

            bioskopske_karte.pronadji_karte(None,None,None, rezervacija)
    

def direktna_prodaja_karte():
    while True:
        print('1. Direktan unos termina | 2. Pretraga termina projekcije')
        unos = input('Odaberite opciju (; za nazad): ')
        
        if unos==';':return
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==2: svi_korisnici.pretraga_termina()

        sifra_termina=input('Unesite termin: ')
        if sifra_termina==';': return

        ime = input('Unesite ime i prezime za neregistrovanog, odnosno samo me za registrovanog korisnika: ')
        if ime==';':return

        while not termin.slobodna_sedista(sifra_termina.upper(), None):
            sifra_termina=input('Termin ne postoji. Unesite opet termin: ')
            if sifra_termina==';': return


        sediste = input('Unesite sediste: ')
        if sediste==';':return
        while not termin.slobodna_sedista(sifra_termina.upper(), sediste.upper()):
            sediste = input('Unesite sediste: ')
            if sediste==';':return
        
        bioskopske_karte.prodaj_kartu(ime.upper(), sifra_termina.upper(), sediste.upper())

        ponovo = input('Da li zelite jos da prodate (Y/N): ')
        if ponovo.upper() == 'N':return

        





        