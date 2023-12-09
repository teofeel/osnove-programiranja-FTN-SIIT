
karte = []
def ucitaj_karte():
    global karte
    with open('data/bioskopske_karte.txt') as karte_fajl:
        lines = karte_fajl.readlines()
        for line in lines:
            data  = line.split(';')
            karte.append({
                'ime':data[0],
                'termin':data[1],
                'sediste':data[2],
                'datum_prodaje':data[3],
                'status':data[4].replace('\n','')
            })

def pisi_fajl():
    karte_fajl = open('data/bioskopske_karte.txt', 'w')
    for k in karte:
        karte_fajl.write(k['ime']+';'+k['termin']+';'+k['sediste']+';'+k['datum_prodaje']+';'+k['status']+'\n')

import re
import termin
def provera_slobodnog_mesta(sifra_termina, sediste):
    for karta in karte:
        if karta['termin']==sifra_termina:
            if karta['sediste']==sediste:
                return False
            
    return termin.slobodna_sedista(sifra_termina, sediste)

from datetime import datetime
def rezervisi_kartu(ime, sifra_termina, sediste):
    nova_rezervcaija = {
        'ime':ime,
        'termin':sifra_termina,
        'sediste':sediste,
        'datum_prodaje':str(datetime.now().day)+'.'+str(datetime.now().month)+'.'+str(datetime.now().year)+'.',      # izmeniti datum
        'status':'rezervisana'
    }

    karte.append(nova_rezervcaija)
    pisi_fajl()

from projekcija import projekcije
from termin import termini
def pregled_rezervacija(ime, pregled_svih, prodavac):
    print('////////////////////////')
    for karta in karte:
        if pregled_svih or (karta['ime'].upper() == ime.upper() and karta['status']=='rezervisana'):
            oznaka_termina = karta['termin']

            for termin in termini:
                if termin['sifra'] == karta['termin']:
                    datum = termin['datum']

            for projekcija in projekcije:

                if projekcija['sifra']==karta['termin'][0:4]:
                    naziv_filma = projekcija['film']
                    vreme_pocetka = projekcija['pocetak']
                    vreme_kraja = projekcija['kraj']
            
            print('Termin bioskopske projekcije: '+oznaka_termina)
            if prodavac:
                print('Ime kupca: '+karta['ime'])
            print('Naziv filma: '+ naziv_filma)
            print('Datum: '+datum)
            print('Vreme pocetka: '+vreme_pocetka)
            print('Vreme kraja: '+vreme_kraja)
            print('Sediste: '+karta['sediste'])
            print('////////////////////////')
        print(end='\n')

    return

def ponisti_rezervaciju_kupovinu(ime, termin, sediste, status):
    for karta in karte:
        if karta['ime'].upper()==ime.upper() and karta['termin']==termin and karta['sediste']==sediste and karta['status']==status:
            karte.remove(karta)
            pisi_fajl()
            return True 
    return False

def pronadji_karte(termin, ime, datum, status):
    def ispisi_kartu(karta):
        print('Termin: ' + karta['termin'])
        print('Ime: ' + karta['ime'])
        print('Datum: ' + karta['datum_prodaje'])
        print('Status: ' + karta['status'])
        print('\n')

    if termin:
        for karta in karte:
            if karta['termin'] == termin:
                ispisi_kartu(karta)
        print('//////////////')

    elif ime:
        for karta in karte:
            if karta['ime'].upper() == ime.upper():
                ispisi_kartu(karta)
        print('//////////////')
    
    elif datum:
        for karta in karte:
            if karta['datum_prodaje']==datum:
                ispisi_kartu(karta)
        print('/////////////')

    elif status:
        for karta in karte:
            if karta['status']==status:
                ispisi_kartu(karta)
        print('/////////////')
        
def prodaj_kartu(ime, termin, sediste):
    karta = {
        'ime':ime,
        'termin':termin,
        'sediste':sediste,
        'datum_prodaje':str(datetime.now().day)+'.'+str(datetime.now().month)+'.'+str(datetime.now().year)+'.',
        'status':'kupljena'
    }
    karte.append(karta)
    pisi_fajl()