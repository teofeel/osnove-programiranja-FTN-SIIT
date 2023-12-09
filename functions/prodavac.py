from functions import svi_korisnici, ulogovani_korisnici
import bioskopske_karte

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
        print('8. Izmeni licne podatke')
        print('9. Odjava')
        print('10. Izlazak iz aplikacije ')

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
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==9:
            _id=''
            return
        elif unos==10:
            exit()


def ponistavanje_rezervacija_kupvoina():
    ime = input('Unesite ime ')
    rezervacija = input('Da li je rezervacija y/n: ')

    while not (rezervacija.upper()=='Y' or rezervacija.upper()=='N'):
        rezervacija = input('Da li je rezervacija y/n: ')
    if rezervacija.upper()=='Y': rezervacija=True
    else: rezervacija=False

    return ime, rezervacija