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
        print('10. Prodaj rezervisanu kartu')
        print('11. Izmena karte')
        print('12. Izmeni licne podatke')
        print('13. Odjava')
        print('14. Izlazak iz aplikacije ')

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
            prodaja_rezervisane_karte()
        elif unos==11:
            izmeni_kartu()
        elif unos==12:
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==13:
            _id=''
            return
        elif unos==14:
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
            if not odabir.isdigit(): continue
            if int(odabir) ==2:
                svi_korisnici.pretraga_termina()

            termin = input('Unesite termin: ')
            bioskopske_karte.pronadji_karte(termin, None, None, None)
        
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
        while not (bioskopske_karte.provera_slobodnog_mesta(sifra_termina.upper(), sediste.upper()) and termin.slobodna_sedista(sifra_termina.upper(), sediste.upper())):
            sediste = input('Sediste se ne moze rezervisati: ')
            if sediste==';':return
        
        bioskopske_karte.prodaj_kartu(ime.upper(), sifra_termina.upper(), sediste.upper())

        ponovo = input('Da li zelite jos da prodate (Y/N): ')
        if ponovo.upper() == 'N':return

def prodaja_rezervisane_karte():
    while True:
        print('1. Direktan unos rezervacije | 2. Pregled karata')
        unos = input('Odaberite opciju (; za nazad): ')

        if unos==';':return
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==2: pretraga_karata()

        sifra_termina = input('Unesite sifru termin: ')
        if sifra_termina ==';':return
        sediste = input('Unesite oznaku sedista: ')
        if sediste ==';':return

        if not bioskopske_karte.prodaj_rezervisanu(sifra_termina.upper(), sediste.upper()):
            probaj = input('Rezervacija ne postoji, da li ocete opet da probate? (y/n) ')
            if probaj.lower()=='y':continue
            else: return

        opet = input('Karta uspesno prodata. Da li ocete jos da prodate? (y/n) ')
        if opet.lower()=='y': continue
        return

    
def izmeni_kartu():
    def izmeni_info_karte(karta):
        while True:
            print('1. Termin | 2. Ime | 3. Sedise')
            unos = input('Odaberite opciju (; za nazad): ')
            if unos==';':return
            if not unos.isdigit(): continue
            unos = int(unos)

            if unos==1:
                print('1. Direktan unos termina | 2. Pretraga termina')
                opcija = input('Odaberite opciju: ')
                if opcija==';':return
                if not opcija.isdigit(): continue
                opcija=int(opcija)

                if opcija==2: svi_korisnici.pretraga_termina()

                sifra_termina = input('Unesite sifru termina: ')
                if sifra_termina==';':return
                while not termin.postojeci_termin(sifra_termina.upper()):
                    sifra_termina=input('Termin ne postoji. Unesite opet termin: ')
                    if sifra_termina==';': return

                termin.slobodna_sedista(sifra_termina.upper(), None)
                sediste = input('Unesite sediste: ')
                if sediste==';':return
                while not (bioskopske_karte.provera_slobodnog_mesta(sifra_termina.upper(), sediste.upper()) and 
                           termin.slobodna_sedista(sifra_termina.upper(), sediste.upper())):
                    sediste = input('Sediste se ne moze rezervisati: ')
                    if sediste==';':return
                
                bioskopske_karte.izmeni_kartu(karta, sifra_termina.upper(), None, sediste.upper())

            elif unos==2:
                ime = input('Unesite ime kupca: ')
                bioskopske_karte.izmeni_kartu(karta, None, ime.upper(), None)

            elif unos==3: 
                termin.slobodna_sedista(karta['termin'].upper(), None)
                sediste = input('Unesite sediste: ')
                if sediste==';':return
                while not (bioskopske_karte.provera_slobodnog_mesta(karta['termin'].upper(), sediste.upper()) and
                                termin.slobodna_sedista(karta['termin'].upper(), sediste.upper())):
                    sediste = input('Sediste se ne moze rezervisati. Rezervisite drugo (; za izlazak): ')
                    if sediste == ';': return

                bioskopske_karte.izmeni_kartu(karta, None, None, sediste.upper())
                

            opet = input('Da li ocete jos polja da izmenite? (y/n): ')
            if opet.lower()=='n': return
            

    while True:
        print('1. Direktan unos karte | 2. Pregled karata')

        unos = input('Odaberite opciju (; za nazad): ')
        if unos==';':return
        if not unos.isdigit():continue
        unos=int(unos)

        if unos==2: pretraga_karata()

        sifra_termina = input('Unesite sifru termina: ')
        if sifra_termina==';':return

        ime = input('Unesite ime kupca: ')
        if ime==';':return

        sediste=input('Unesite sediste: ')
        if sediste==';':return

        karta = bioskopske_karte.postojeca_karta(sifra_termina.upper(), ime.upper(), sediste.upper())
        print(karta)
        if not karta:
            probaj = input('Karta ne postoji. Ocete opet? (y/n): ')
            if probaj.lower()=='n':return 
            else:continue

        izmeni_info_karte(karta)
        
        opet = input('Da li ocete jos karata da izmenite? (y/n): ')
        if opet.lower()=='n': return



        