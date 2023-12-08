
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

import datetime
def rezervisi_kartu(ime, sifra_termina, sediste):
    nova_rezervcaija = {
        'ime':ime,
        'termin':sifra_termina,
        'sediste':sediste,
        'datum_prodaje':'08.12.2023.',
        'status':'rezervisana'
    }

    karte.append(nova_rezervcaija)
    pisi_fajl()
