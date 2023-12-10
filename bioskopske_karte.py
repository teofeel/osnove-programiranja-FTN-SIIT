from prettytable import PrettyTable
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
    t = PrettyTable(['Termin bioskopske projekcije','Naziv filma', 'Datum', 'Vreme pocetka', 'Vreme Kraja', 'Sediste'])
    ime_kupca_column = []
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
            
            t.add_row([oznaka_termina, naziv_filma, datum, vreme_pocetka, vreme_kraja, karta['sediste']])
            if prodavac:
                ime_kupca_column.append(karta['ime'])

    if prodavac: t.add_column('Ime Kupca', ime_kupca_column)
    print(t)
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

    t = PrettyTable(['Termin','Ime','Sediste','Datum','Status'])

    if termin:
        for karta in karte:
            if karta['termin'].upper() == termin.upper():
                t.add_row([karta['termin'],karta['ime'],karta['sediste'],karta['datum_prodaje'],karta['status']])


    elif ime:
        for karta in karte:
            if karta['ime'].upper() == ime.upper():
                t.add_row([karta['termin'],karta['ime'],karta['sediste'],karta['datum_prodaje'],karta['status']])

    
    elif datum:
        for karta in karte:
            if karta['datum_prodaje']==datum:
                t.add_row([karta['termin'],karta['ime'],karta['sediste'],karta['datum_prodaje'],karta['status']])


    elif status:
        for karta in karte:
            if karta['status']==status:
                t.add_row([karta['termin'],karta['ime'],karta['sediste'],karta['datum_prodaje'],karta['status']])


    print(t)
        
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

def prodaj_rezervisanu(sifra_termin, sediste):
    for karta in karte:
        if (karta['termin']==sifra_termin and karta['sediste']==sediste and karta['status']=='rezervisana'):

            karta['datum_prodaje'] = str(datetime.now().day)+'.'+str(datetime.now().month)+'.'+str(datetime.now().year)+'.'
            karta['status']='kupljena'
            
            pisi_fajl()

            return True
    return False