from functions import svi_korisnici, ulogovani_korisnici
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
        print('7. Izmeni licne podatke')
        print('8. Odjava')
        print('9. Izlazak iz aplikacije ')

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
            continue
        elif unos==6:
            continue
        elif unos==7:
            ulogovani_korisnici.izmena_licnih_podataka(_id)
        elif unos==8:
            _id=''
            return
        elif unos==9:
            exit()
