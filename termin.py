from datetime import datetime

termini = []
def ucitaj_termine():
    with open('data/termini_projekcije.txt') as termini_fajl:
        lines = termini_fajl.readlines()
        for line in lines:
            data = line.split(';')
            termini.append({
                'sifra':data[0],
                'datum':data[1].replace('\n',''),
            })

def dan_projekcije(dan):
    if dan.upper() == 'PONEDELJAK': return 0
    elif dan.upper() == 'UTORAK': return 1
    elif dan.upper() == 'SREDA': return 2
    elif dan.upper() == 'CETVRTAK': return 3
    elif dan.upper() == 'PETAK': return 4
    elif dan.upper() == 'SUBOTA': return 5
    elif dan.upper() == 'NEDELJA': return 6

from projekcija import projekcije
def pretrazi_termine(filter, vrednost):
    for projekcija in projekcije:
        if filter == 'datum': 
            for termin in termini:
                if termin['datum'] == vrednost and projekcija['sifra'] in termin['sifra']:
                    print('Naziv: ' + projekcija['film'])
                    print('Sala: '+projekcija['sala'])
                    print('Pocetak termina: '+projekcija['pocetak'])
                    print('Kraj termina: '+projekcija['kraj'])
                    print('Datum: '+ termin['datum'])
                    print('////////////////////////////')
        elif vrednost.upper() in projekcija[filter].upper():
            for termin in termini:
                datum_str = termin['datum'].split('.')
                for dan in projekcija['dani'].split(' '):
                    if (datetime(int(datum_str[2]),int(datum_str[1]),int(datum_str[0])).weekday() 
                        == dan_projekcije(dan)):  
                        print('Naziv: ' + projekcija['film'])
                        print('Sala: '+projekcija['sala'])
                        print('Pocetak termina: '+projekcija['pocetak'])
                        print('Kraj termina: '+projekcija['kraj'])
                        print('Datum: '+ termin['datum'])
                        print('////////////////////////////')

def pretraga_vreme(filter, sati, minuti):
    if filter=='pocetak' or filter=='kraj':
        for projekcija in projekcije:
            if (projekcija[filter] == (sati+':'+ minuti) or
                (projekcija[filter].split(':')[0] == sati and minuti=='')):      
                for termin in termini:
                    datum_str = termin['datum'].split('.')
                    for dan in projekcija['dani'].split(' '):
                        if (datetime(int(datum_str[2]),int(datum_str[1]),int(datum_str[0])).weekday() 
                            == dan_projekcije(dan)):  
                            print('Naziv: ' + projekcija['film'])
                            print('Sala: '+projekcija['sala'])
                            print('Pocetak termina: '+projekcija['pocetak'])
                            print('Kraj termina: '+projekcija['kraj'])
                            print('Datum: '+ termin['datum'])
                            print('////////////////////////////')
    else: print('Doslo je do greske')

