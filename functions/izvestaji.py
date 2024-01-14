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
        elif unos==2:
            izvestaj_po_terminu()
        elif unos==3: 
            izvestaji_datum_prodavac()
        elif unos==4: 
            broj_cena_dan_prodaje()
        elif unos==5:
            ukupno_dan_projekcija()
        elif unos==6:
            ukupno_film_projekcije()
        elif unos==7:
            ukupno_dan_prodavac()
        elif unos==8:
            ukupno_prodavac_mesec()

from datetime import datetime, timedelta, date
from dateutil import relativedelta
from bioskopske_karte import karte
from prettytable import PrettyTable
from projekcija import projekcije
import projekcija
from termin import dan_projekcije, termini
from functions import svi_korisnici

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
        with open('data/izvestaji/dan_prodaje_{0}'.format(datum), 'w') as izvestaj_txt:
            izvestaj_txt.write(str(t))

def izvestaj_po_terminu():
    while True:
        projekcija.ispisi_projekcije()
        sifra_projekcije = input('Unesite siftu projekcije: ')
        if sifra_projekcije == ';':return
        elif not sifra_projekcije.isdigit():continue

        datum = input('Unesite zeljeni datum: ')
        if datum==';': return

        while not proveri_datum(datum):
            datum = input('Unesite zeljeni datum: ')
            if datum==';': return
        datum+='\n'

        sifra_termina = ''
        for termin in termini:
            if sifra_projekcije in termin['sifra'] and termin['datum']==datum:
                sifra_termina = termin['sifra']

        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        for karta in karte:
            if karta['termin'].upper()==sifra_termina.upper() and karta['status']=='kupljena':
                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
        print(t)

        with open('data/izvestaji/projekcija_{0}_datum_prodaje_{1}'.format(sifra_projekcije,datum.replace('\n','')), 'w') as izvestaj_txt:
            izvestaj_txt.write(str(t))
        
        nazad = input('Da li zelite da se vratite nazad (y/n): ')
        if nazad==';' or nazad.lower()=='y':return

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

        with open('data/izvestaji/prodavac_{0}_datum_prodaje_{1}'.format(ime_prodavca, datum),'w') as f:
            f.write(str(t))

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
                ukupna_cena+=ukupna_vrednost_prodatih(karta['termin'],dan_prodaje)

        print(t)
        t1=PrettyTable(['Ukupno prodatih karata', 'Ukupna vrednost prodatih karata'])
        t1.add_row([broj_prodatih_karata, ukupna_cena])
        print(t1)

        with open('data/izvestaji/dan_prodaje_{0}'.format(dan), 'w') as f:
            f.write(str(t))
            f.write('\n')
            f.write(str(t1))

def ukupno_dan_projekcija():
    while True:
        prikazi_projekcije = input('Da li ocete da pretrazite projekcije (y/n): ')
        if prikazi_projekcije.lower()=='y':projekcija.ispisi_projekcije()

        sifra_projekcije = input('Unesite sifru termina: ')
        if sifra_projekcije==';':return
        if not sifra_projekcije.isdigit(): continue

        dan_projekcija = input('Unesite dan projekcije: ')
        if dan_projekcija==';': return
        dan = dan_projekcije(dan_projekcija)

        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        broj_prodatih_karata = 0 
        ukupna_cena = 0
        
        for termin in termini:
            datum_termina = termin['datum'].split('.')
            datum_termina = datetime(int(datum_termina[2]),int(datum_termina[1]),int(datum_termina[0]))

            if sifra_projekcije in termin['sifra'] and datum_termina.weekday()==dan:
                for karta in karte:
                    if karta['termin'].upper() == termin['sifra']:
                        t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
                        broj_prodatih_karata+=1
                        ukupna_cena+=ukupna_vrednost_prodatih(karta['termin'], dan)
        
        print(t)
        t1=PrettyTable(['Ukupno prodatih karata', 'Ukupna vrednost prodatih karata'])
        t1.add_row([broj_prodatih_karata, ukupna_cena])
        print(t1)

        with open('data/izvestaji/sifra_{0}_dan_{1}'.format(sifra_projekcije, dan_projekcija), 'w') as f:
            f.write(str(t))
            f.write('\n')
            f.write(str(t1))

        nazad = input('Da li ocete da se vratite na sve izvestaje (y/n): ')
        if nazad.lower()=='y' or nazad==';':return

def ukupno_film_projekcije():
    while True:
        svi_korisnici.pregled_filmova_main()
        naziv_filma = input('Unesite naziv filma: ') 
        if naziv_filma==';':return

        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        ukupna_cena = 0
        for p in projekcije:
            if naziv_filma.lower() in p['film'].lower():
                naziv_filma = p['film']
                for karta in karte:
                    if p['sifra'] in karta['termin'] and karta['status']=='kupljena':

                        t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
                        ukupna_cena+=int(p['cena'])
        print(t)
        t1 = PrettyTable(['Ukupna vrednost'])
        t1.add_row([ukupna_cena])
        print(t1)

        with open('data/izvestaji/film_{0}'.format(naziv_filma),'w') as f:
            f.write(str(t))
            f.write('\n')
            f.write(str(t1))

        opet=input('Da li ocete da se vratite na sve izvestaje (y/n): ')
        if opet.lower()=='y' or opet==';':return

def ukupno_dan_prodavac():
    while True:
        ime_prodavca = input('Unesite ime prodavca: ')
        if ime_prodavca==';':return

        dan_projekcija = input('Unesite zeljeni dan u nedelji: ')
        if dan_projekcija==';':return

        dan= dan_projekcije(dan_projekcija)
        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        broj_prodatih_karata = 0 
        ukupna_cena = 0

        for karta in karte:
            karta_dan_prodaje = karta['datum_prodaje'].split('.')
            if ((dan == datetime(int(karta_dan_prodaje[2]),int(karta_dan_prodaje[1]),int(karta_dan_prodaje[0])).weekday()) 
                and karta['prodavac'].lower() == ime_prodavca.lower() and karta['status']=='kupljena'):

                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
                broj_prodatih_karata+=1
                ukupna_cena+=ukupna_vrednost_prodatih(karta['termin'], dan)
            
        print(t)
        t1=PrettyTable(['Ukupno prodatih karata', 'Ukupna vrednost prodatih karata'])
        t1.add_row([broj_prodatih_karata, ukupna_cena])
        print(t1)

        with open('data/izvestaji/dan_prodaje_{0}_prodavac_{1}'.format(dan_projekcija, ime_prodavca), 'w') as f:
            f.write(str(t))
            f.write('\n')
            f.write(str(t1))

def ukupno_prodavac_mesec():
    while True:
        naziv_prodavca = input('Unesite naziv prodavca: ')
        if naziv_prodavca==';':return

        t = PrettyTable(['Ime', 'Termin', 'Sediste', 'Datum Prodaje', 'Status', 'Prodavac'])
        broj_prodatih_karata=0
        ukupna_cena = 0
        for karta in karte:
            datum_prodaje = karta['datum_prodaje'].split('.')

            datum_prodaje = datetime(int(datum_prodaje[2]), int(datum_prodaje[1]), int(datum_prodaje[0]))
            dani_od_prodaje = (datetime.now()-datum_prodaje).days

            if naziv_prodavca.lower() == 'svi' and karta['status']=='kupljena' and dani_od_prodaje<30:
                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
                broj_prodatih_karata+=1
                ukupna_cena += ukupna_vrednost_prodatih(karta['termin'], datum_prodaje.weekday())

            if karta['prodavac'].lower() == naziv_prodavca.lower() and karta['status']=='kupljena' and dani_od_prodaje<=30:
                t.add_row([karta['ime'],karta['termin'],karta['sediste'],karta['datum_prodaje'],karta['status'],karta['prodavac']])
                broj_prodatih_karata+=1
                ukupna_cena += ukupna_vrednost_prodatih(karta['termin'], datum_prodaje.weekday())

        print(t)
        t1 = PrettyTable(['Ukupno prodatih karata', 'Ukupna vrednost'])
        t1.add_row([broj_prodatih_karata, ukupna_cena])
        print(t1)

        danasnji_datum = datetime.now()
        mesec_dana_ranije = datetime.strftime(danasnji_datum + timedelta(days=-30), '%d.%m.%Y')
        danasnji_datum = datetime.strftime(danasnji_datum, '%d.%m.%Y')
        with open('data/izvestaji/prodavac_{0}_od_{1}_do_{2}'.format(naziv_prodavca, danasnji_datum, mesec_dana_ranije),'w') as f:
            f.write(str(t))
            f.write('\n')
            f.write(str(t1))



def izvuci_broj_stringa(str):
    res = ''
    for c in str:
        if c.isdigit():
            res+=c
    return res

def ukupna_vrednost_prodatih(termin, dan_prodaje):
        for p in projekcije:
            if p['sifra']==izvuci_broj_stringa(termin) and dan_prodaje==1:
                return (int(p['cena'])-50)
            elif p['sifra']==izvuci_broj_stringa(termin):
                return int(p['cena'])
            

def proveri_datum(datum):
        try:
            datetime.strptime(datum, '%d.%m.%Y.')
            return True
        except:
            return False

