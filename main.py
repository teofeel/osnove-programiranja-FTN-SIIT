# liste za podatke iz fajlova
from korisnik import korisnici
import korisnik
from film import filmovi
import film

def ucitaj_podatke():
    # iz svih fajlova se podaci ucitavaju u prethodno navedene liste
    korisnik.ucitaj_korisnike()    
    film.ucitaj_filmove()

##########################################################################

## FUNCKIJE ZA SVE KORISNIKE ##

from functions import svi_korisnici

##########################################################################

from functions import kupac
def main():
    ucitaj_podatke()  
    
    i = 0
    while i!=7:
        print('/////////////////////')
        print('1. Prijava na sistem')
        print('2. Registracija na sistem')
        print('3. Pregledaj dostupne filmove')
        print('4. Pretraga filmova')
        print('5. Visekriterijumska pretraga')
        print('6. Pretraga termina bioskopskih projekcija')
        print('7. Izlazak iz aplikacije')
        print('/////////////////////')

        i = int(input('Izaberite: '))
        if i==1:
            if not svi_korisnici.prijava():
                print('Prijava nije uspesna. Probajte opet')
        elif i==2: 
            svi_korisnici.registracija()
        elif i==3:
            svi_korisnici.pregled_filmova()
        elif i==4:
            svi_korisnici.pretraga_filmova()
        
main()
