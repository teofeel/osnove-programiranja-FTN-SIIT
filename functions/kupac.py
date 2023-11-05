from korisnik import korisnici
from functions import svi_korisnici
#funckija za ispisivanje mogucnosti kao registrovan korisnik
def main():
    print('///////////////////')
    unos = 0
    while unos!=3:
        print('Ulogovani korisnik')
        print('1. Pregled filmova')
        print('2. Pretraga filmova')
        print('3. Visekriterijumska pretraga filmova')
        print('4. Pretraga termina')
        print('5. Odjava')
        print('6. Izlazak iz aplikacije')
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
            return
        elif unos==6:
            izlazak()

      
# funkcija koja zatvara aplikaciju
def izlazak():
    exit()