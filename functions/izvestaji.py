def izvestaji_main():
    while True:
        print('1. Po datumu')
        print('2. Po terminu bioskopske projekcije')
        print('3. Po datumu i prodavcu')
        print('4. Ukupan broj i ukupna cena prodatih karata za izabran dan u nedelji prodaje')
        print('5. Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije')
        print('6. Ukupna cena prodatih karata za zadati film u svim projekcijama')
        print('7. Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca')
        print('8. Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakogprodavca) u poslednjih 30 dana')

        unos = input('Odaberite: ')
        if unos==';':return
        if not unos.isdigit(): continue
        unos = int(unos)

        if unos==1:
            izvestaji_datum_prodaje()
        elif unos==3: 
            izvestaji_datum_prodavac()
        elif unos==4: 
            broj_cena_dan_prodaje()
        elif unos==7:
            ukupno_dan_prodavac()

from datetime import datetime
from bioskopske_karte import karte
from prettytable import PrettyTable
from projekcija import projekcije
import projekcija
from termin import dan_projekcije

def izvestaji_datum_prodaje():
    while True:
        datum = input('Unesite zeljeni datum: ')
        if datum==';': return

        while not proveri_datum(datum):
            datum = input('Unesite zeljeni datum: ')
            if datum==';': return

        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        for karta in karte:
            if karta['datum_prodaje']==datum and karta['status']=='kupljena':
                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
        print(t)

def izvestaji_datum_prodavac():
    while True:
        ime_prodavca = input('Unesite ime prodavca: ')
        if ime_prodavca==';':return

        datum = input('Unesite zeljeni datum: ')
        if datum==';': return

        while not proveri_datum(datum):
            datum = input('Unesite zeljeni datum: ')
            if datum==';': return
        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])

        for karta in karte:
            if karta['datum_prodaje']==datum and karta['prodavac'].lower() == ime_prodavca.lower() and karta['status']=='kupljena':
                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
        print(t)

def broj_cena_dan_prodaje():
    while True:
        dan = input('Unesite zeljeni dan u nedelji: ')
        if dan==';': return

        dan_prodaje = dan_projekcije(dan)
        
        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])

        broj_prodatih_karata = 0 
        ukupna_cena = 0
        for karta in karte:
            karta_dan_prodaje = karta['datum_prodaje'].split('.')

            if (dan_prodaje == datetime(int(karta_dan_prodaje[2]),int(karta_dan_prodaje[1]),int(karta_dan_prodaje[0])).weekday()
                and karta['status']=='kupljena'):
                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])

                broj_prodatih_karata+=1
                for p in projekcije:
                    if p['sifra']==izvuci_broj_stringa(karta['termin']):
                        ukupna_cena+=int(p['cena'])

        if dan_prodaje==1:
            ukupna_cena-=broj_prodatih_karata*50

        print(t)
        print('Ukupno prodatih karata: ',broj_prodatih_karata)
        print('Ukupna vrednost prodatih karata: ',ukupna_cena)

def broj_cena_dan_projekcije():
    while True:
        projekcija.ispisi_projekcije()
        sifra_projekcije = input('Unesite sifru projekcije: ')
        while not sifra_projekcije.isdigit(): 
            sifra_projekcije = input('Unesite sifru projekcije: ')

        dan = input('Unesite zeljeni dan u nedelji: ')
        if dan==';':return

        dan= dan_projekcije(dan)

        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        broj_prodatih_karata = 0 
        ukupna_cena = 0

        for p in projekcije:
            if p['sifra'] == sifra_projekcije:
                dani_projekcije = p['dani'].split(' ')
                   # ovo nije zavrseno do kraja 
                    
        print(t)
        print('Ukupno prodatih karata: ',broj_prodatih_karata)
        print('Ukupna vrednost prodatih karata: ',ukupna_cena)

def ukupno_dan_prodavac():
    while True:
        ime_prodavca = input('Unesite ime prodavca: ')
        if ime_prodavca==';':return

        dan = input('Unesite zeljeni dan u nedelji: ')
        if dan==';':return

        dan= dan_projekcije(dan)
        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        broj_prodatih_karata = 0 
        ukupna_cena = 0

        for karta in karte:
            karta_dan_prodaje = karta['datum_prodaje'].split('.')
            if ((dan == datetime(int(karta_dan_prodaje[2]),int(karta_dan_prodaje[1]),int(karta_dan_prodaje[0])).weekday()) 
                and karta['prodavac'].lower() == ime_prodavca.lower() and karta['status']=='kupljena'):

                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
                broj_prodatih_karata+=1

                for p in projekcije:
                    if p['sifra']==izvuci_broj_stringa(karta['termin']):
                        ukupna_cena+=int(p['cena'])
        if dan==1:
            ukupna_cena-=broj_prodatih_karata*50
            
        print(t)
        print('Ukupno prodatih karata: ',broj_prodatih_karata)
        print('Ukupna vrednost prodatih karata: ',ukupna_cena)    

def izvuci_broj_stringa(str):
    res = ''
    for c in str:
        if c.isdigit():
            res+=c
    return res
def proveri_datum(datum):
        try:
            datetime.strptime(datum, '%d.%m.%Y.')
            return True
        except:
            return False

