from korisnik import korisnici
from bioskopske_karte import karte
from functions import svi_korisnici
from functions import ulogovani_korisnici
#funckija za ispisivanje mogucnosti kao registrovan korisnik
_id = ''

def main(korisnicko_ime):
    global _id
    _id = korisnicko_ime
    print('///////////////////')
    unos = 0
    while unos!=3:
        print('Ulogovani korisnik')
        print('1. Pregled filmova')
        print('2. Pretraga filmova')
        print('3. Visekriterijumska pretraga filmova')
        print('4. Pretraga termina')
        print('5. Rezervisi sediste')
        print('6. Izmeni licne podatke')
        print('7. Odjava')
        print('8. Izlazak iz aplikacije')
        unos = input('Izaberite: ')
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
            ulogovani_korisnici.rezervisi_kartu(_id,0)
        elif unos==6:
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==7:
            _id = ''
            return
        elif unos==8:
            izlazak()

      
# funkcija koja zatvara aplikaciju
def izlazak():
    exit()