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
                'cena':data[6]
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
    


