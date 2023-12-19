from datetime import datetime
from prettytable import PrettyTable
from projekcija import projekcije
from datetime import datetime, timedelta

termini = []
def ucitaj_termine():
    #with open('data/termini_projekcije.txt') as termini_fajl:
        #lines = termini_fajl.readlines()
        #for line in lines:
            #data = line.split(';')
            #termini.append({
             #   'sifra':data[0],
              #  'datum':data[1].replace('\n',''),
            #})
    def incr_chr(c):
        return chr(ord(c) + 1) if c != 'Z' else 'A'
    def incr_str(s):
        lpart = s.rstrip('Z')
        num_replacements = len(s) - len(lpart)
        new_s = lpart[:-1] + incr_chr(lpart[-1]) if lpart else 'A'
        new_s += 'A' * num_replacements
        return new_s

    for projekcija in projekcije:
        pocetna_sifra='AA'
        dani_projekcije = projekcija['dani'].split(' ')

        for d in dani_projekcije:
            dan = dan_projekcije(d.upper())
            dve_nedelje = datetime.now()

            pocetak_projekcije_min = int(projekcija['pocetak'].split(':')[1])
            pocetak_projekcije_sati = int(projekcija['pocetak'].split(':')[0])

            if (dan == dve_nedelje.weekday() and (dve_nedelje.time().hour < pocetak_projekcije_sati or 
                (dve_nedelje.time().hour==pocetak_projekcije_sati and dve_nedelje.time().minute<pocetak_projekcije_min))):
                datum = str(dve_nedelje.date().day)+'.'+str(dve_nedelje.date().month)+'.'+str(dve_nedelje.date().year)+'.'
                termini.append({
                    'sifra':projekcija['sifra']+pocetna_sifra,
                    'datum':datum+'\n'
                })
                pocetna_sifra = incr_str(pocetna_sifra)



            for i in range(13):
                dve_nedelje = dve_nedelje + timedelta(days=1)
                datum = str(dve_nedelje.date().day)+'.'+str(dve_nedelje.date().month)+'.'+str(dve_nedelje.date().year)+'.'
                if dan == dve_nedelje.weekday():
                    termini.append({
                        'sifra': projekcija['sifra']+pocetna_sifra,
                        'datum':datum+'\n'
                    })
                    pocetna_sifra = incr_str(pocetna_sifra) 
    upisi_termine() 

def upisi_termine():
    fajl = open('data/termini_projekcije.txt', 'w')
    for t in termini:
        fajl.write(t['sifra']+';'+t['datum'])

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
    t = PrettyTable(['Naziv','Sala','Pocetak termina','Kraj Termina','Datum','Sifra termina'])
    for projekcija in projekcije:
        if filter == 'datum': 
            for termin in termini:
                if termin['datum'] == vrednost and projekcija['sifra'] in termin['sifra']:
                    t.add_row([projekcija['film'], projekcija['sala'], projekcija['pocetak'], 
                               projekcija['kraj'], termin['datum'], termin['sifra']])
                    
        elif vrednost.upper() in projekcija[filter].upper():
            for termin in termini:
                datum_str = termin['datum'].split('.')
                for dan in projekcija['dani'].split(' '):
                    if (datetime(int(datum_str[2]),int(datum_str[1]),int(datum_str[0])).weekday() 
                        == dan_projekcije(dan)):  
                        t.add_row([projekcija['film'], projekcija['sala'], projekcija['pocetak'], 
                               projekcija['kraj'], termin['datum'], termin['sifra']])
                        
    print(t)



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
                            print('Sifra termina: '+ termin['sifra'])
                            print('////////////////////////////')
    else: print('Doslo je do greske')


from bioskopske_karte import karte
from sala import sale
import sala
def slobodna_sedista(sifra_termina, sediste):
    for termin in termini:
        br=0
        if termin['sifra']==sifra_termina:
            sifra_projekcije = termin['sifra'][0:4]
            br=1
            break

    if not br: return False

    for projekcija in projekcije:
        if projekcija['sifra']==sifra_projekcije:
            for sala_l in sale:
                if sala_l['naziv']==projekcija['sala']:
                    sifra_sale = sala_l['sifra']
                    break
    
    rezervisana_sedista = []
    for karta in karte:
        if karta['termin']==sifra_termina:
            rezervisana_sedista.append(karta['sediste'])

    if not sediste == None:
        return sala.postoji_sediste(sifra_sale,sediste)
        
    else: 
        sala.sedista_sale(sifra_sale,rezervisana_sedista)
        return True

def postojeci_termin(sifra_termina):
    for termin in termini:
        if termin['sifra'].upper()==sifra_termina:
            return True
    return False

def obrisi_termin(sifra):
    obrisani = []
    for t in termini:
        if sifra in t['sifra']:
            obrisani.append(t)

    for o in obrisani:
        termini.remove(o)
    print(termini)
    upisi_termine()
    