from datetime import datetime
projekcije = []
def ucitaj_projekcije():
    global projekcije
    with open('data/projekcije.txt') as projekcije_fajl:
        lines = projekcije_fajl.readlines()
        for line in lines:
            data = line.split(';')
            projekcije.append({
                'sifra':data[0],
                'sala': data[1],
                'pocetak': data[2],
                'kraj': data[3],
                'dani':data[4],
                'film':data[5],
                'cena':data[6].replace('\n','')
            })

import termin
def vreme_do_projeckije(sifra_termina):
    for t in termin.termini:
        if t['sifra'].upper() == sifra_termina.upper():
            datum_str = t['datum'].split('.')
    
    for projekcija in projekcije:
        for dan in projekcija['dani'].split(' '):
            
            if (datetime(int(datum_str[2]),int(datum_str[1]),int(datum_str[0])).date()
                == datetime.now().date()):
                
                pocetak = projekcija['pocetak'].split(':')
                
                sati = (int(pocetak[0])-datetime.now().hour)*60
                if sati<0: return 0

                minuti = int(pocetak[1])-datetime.now().minute
                
                return sati+minuti

def upisi_projekcije():
    fajl = open('data/projekcije.txt', 'w')
    for p in projekcije:
        fajl.write(p['sifra']+';'+p['sala']+';'+p['pocetak']+';'+p['kraj']+';'+p['dani']+';'+p['film']+';'+p['cena']+'\n')


def obrisi_projekciju(naziv_filma):
    for projekcija in projekcije:
        if projekcija['film'].upper() == naziv_filma.upper():
            termin.obrisi_termin(projekcija['sifra'])
            projekcije.remove(projekcija)
    termin.ucitaj_termine()
    upisi_projekcije()

from prettytable import PrettyTable
def ispisi_projekcije():
    t = PrettyTable(['Sifra','Sala', 'Pocetak', 'Kraj', 'Dani','Film','Cena'])
    for p in projekcije:
        t.add_row([p['sifra'],p['sala'],p['pocetak'],p['kraj'],p['dani'],p['film'],p['cena']])
    print(t)

from sala import sale
from film import filmovi
def dodaj_projekciju(sifra, sala, pocetak, kraj, dani, film, cena):
    for projekcija in projekcije:
        if projekcija['sifra']==sifra:
            print('Sifra problem')
            return False
        
        s_br=0
        for s in sale:
            if s['naziv']==sala.upper(): s_br+=1
        if s_br==0: 
            print('Sala problem')
            return False

        f_br=0
        for f in filmovi:
            if f['naziv'].upper()==film.upper(): f_br+=1
        if f_br==0: 
            print('Naziv problem')
            return False

        vreme_pocetka_projekcija = projekcija['pocetak'].split(':')
        sati_pocetka_projekcija = int(vreme_pocetka_projekcija[0])
        minuti_pocetka_projekcija = int(vreme_pocetka_projekcija[1])

        vreme_pocetka = pocetak.split(':') 
        sati_pocetka = int(vreme_pocetka[0])
        minuti_pocetka = int(vreme_pocetka[1])

        vreme_kraja_projekcija = projekcija['kraj'].split(':')
        sati_kraja_projekcija = int(vreme_kraja_projekcija[0])
        minuti_kraja_projekcija = int(vreme_kraja_projekcija[1])

        vreme_kraja = kraj.split(':')
        sati_kraja = int(vreme_kraja[0])
        minuti_kraja = int(vreme_kraja[1])

        pocetak_dok_traje = ((sati_pocetka>sati_pocetka_projekcija and sati_pocetka<sati_kraja_projekcija) or
                             (sati_pocetka==sati_pocetka_projekcija and minuti_pocetka>minuti_pocetka_projekcija and sati_pocetka<sati_kraja_projekcija) or 
                             (sati_pocetka==sati_pocetka_projekcija and minuti_pocetka>minuti_pocetka_projekcija and 
                              sati_pocetka==sati_kraja_projekcija and minuti_pocetka<minuti_kraja_projekcija))

        kraj_dok_traje = ((sati_kraja>sati_pocetka_projekcija and sati_kraja<sati_kraja_projekcija) or 
                          (sati_kraja==sati_pocetka_projekcija and minuti_kraja>minuti_pocetka_projekcija and sati_kraja<sati_kraja_projekcija) or
                          (sati_kraja==sati_pocetka_projekcija and minuti_kraja>minuti_pocetka_projekcija and 
                           sati_kraja==sati_kraja_projekcija and minuti_kraja<minuti_kraja_projekcija))
        
        dani_projekcije_postojece = projekcija['dani'].split(' ')
        dani_projekcije = dani.split(' ')

        dan_postoji=False
        for d in dani_projekcije_postojece:
            for d1 in dani_projekcije:
                if d.upper()==d1.upper(): dan_postoji=True

        if projekcija['sala'].upper() == sala.upper() and (pocetak_dok_traje or kraj_dok_traje) and dan_postoji:
            print('Vreme problem')
            return False
        
    projekcije.append({
        'sifra':sifra,
        'sala':sala.upper(),
        'pocetak':pocetak,
        'kraj':kraj,
        'dani':dani,
        'film':film,
        'cena':cena
    })
    upisi_projekcije()
    termin.ucitaj_termine()
    return True

def izmeni_polje(sifra_projekcije, polje, vrednost):
    try:
        if polje=='film':
            br=0
            for f in filmovi:
                if f['naziv'].lower()==vrednost.lower():
                    br+=1
            if br==0: raise Exception('Film ne postoji')
        
        elif polje=='sala':
            br=0
            for s in sale:
                if s['naziv'].lower()==vrednost.lower(): err = False
                br+=1
            if br==0: raise Exception('Sala ne postoji')

        
        
        for p in projekcije:
            if p['sifra']==sifra_projekcije and not polje=='vreme':
                p[polje]=vrednost
                upisi_projekcije()
                return
            elif p['sifra']==sifra_projekcije and polje=='vreme':
                p['pocetak']=vrednost[0]
                p['kraj']=vrednost[1]
                upisi_projekcije()
                return  
        raise Exception('Projekcija je nepostojeca')        
    except Exception as e:
        print(e)
        return
