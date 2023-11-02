from korisnik import korisnici
from functions import svi_korisnici
#funckija za ispisivanje mogucnosti kao registrovan korisnik
def main():
    print('///////////////////')
    unos = 0
    while unos!=3:
        print('Ulogovani korisnik')
        print('1. Pregled filmova')
        print('2. Odjava')
        print('3. Izlazak iz aplikacije')
        unos = input('Izaberite: ')
        if not unos.isdigit(): continue
        unos = int(unos)
        if unos==1:
            svi_korisnici.pregled_filmova_main()
        elif unos==2:
            return
    izlazak()

      
# funkcija koja zatvara aplikaciju
def izlazak():
    exit()