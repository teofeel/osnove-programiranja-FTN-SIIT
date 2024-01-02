# klasa za film
from prettytable import PrettyTable
filmovi = []
def ucitaj_filmove():
    global filmovi
    with open('data/filmovi.txt') as filmovi_fajl:
        lines = filmovi_fajl.readlines()
        for line in lines:
            data = line.split(';')
            filmovi.append({
                "naziv": data[0],
                "zanr": data[1],
                "trajanje":data[2],
                "reziser":data[3],
                "uloge":data[4],
                "zemlja porekla":data[5],
                "godina":data[6],
                "opis":data[7].replace('\n','')
            })

def pretraga_filmova_(filteri, vrednosti):
    if filmovi == []: return 0
    t = PrettyTable(['Naziv', 'Zanr','Trajanje','Reziser','Uloge','Zemlja porekla','Godina', 'Opis'])
    for film in filmovi:
        uslovi = 0
        for i in range(0, len(filteri)):
            if filteri[i] == 3:
                if vrednosti[i]['izbor']==1:
                    if int(film['trajanje'])<vrednosti[i]['vrednost'][0]:
                        uslovi+=1

                elif vrednosti[i]['izbor']==2:
                    if int(film['trajanje'])>vrednosti[i]['vrednost'][0]:
                        uslovi+=1

                elif vrednosti[i]['izbor']==3:
                    if (int(film['trajanje'])>vrednosti[i]['vrednost'][0]
                        and int(film['trajanje'])<vrednosti[i]['vrednost'][1]):
                        uslovi+=1
                continue

            elif filteri[i]==7:
                if int(film['godina'])==vrednosti[i]: 
                    uslovi+=1
                continue
             
            if filteri[i]==1: filteri[i]='naziv'
            elif filteri[i]==2: filteri[i]='zanr'
            elif filteri[i]==4: filteri[i]='reziser'
            elif filteri[i]==5: filteri[i]='uloge'
            elif filteri[i]==6: filteri[i]='zemlja porekla'
            
            if vrednosti[i].upper() in film[filteri[i]].upper(): #filter prevesti u vrednost
                uslovi+=1

        if uslovi == len(filteri):
            t.add_row([film['naziv'],film['zanr'],film['trajanje'],film['reziser'],film['uloge'],film['zemlja porekla'], film['godina'], film['opis']])
            
    print(t)
    return 

def dodaj_film(naziv, zanr, trajanje, reziser, uloge, zemlja_porekla, godina, opis):
    for film in filmovi:
        if film['naziv'].lower()==naziv.lower():
            return False
    filmovi.append({
        "naziv": naziv,
        "zanr": zanr,
        "trajanje":trajanje,
        "reziser":reziser,
        "uloge":uloge,
        "zemlja porekla":zemlja_porekla,
        "godina":godina,
        "opis":opis
    })
    upisi_filmove()
    return True

def upisi_filmove():
    fajl = open('data/filmovi.txt','w')
    for f in filmovi:
        fajl.write(f['naziv']+';'+f['zanr']+';'+f['trajanje']+';'+f['reziser']+';'+f['uloge']+';'+f['zemlja porekla']+';'+f['godina']+';'+f['opis']+'\n')

import projekcija
from bioskopske_karte import karte

def obrisi_film(naziv):
    for film in filmovi:
        print(film['naziv'] == naziv)
        if film['naziv'].upper() == naziv.upper():
            projekcija.obrisi_projekciju(naziv.upper())
            filmovi.remove(film)
    upisi_filmove()   
                
def izmeni_film(naziv, filteri, vrednosti):
    for film in filmovi:
        if film['naziv'].lower()==naziv.lower():
            for i in range(len(filteri)):
                film[filteri[i]]=vrednosti[i]
    upisi_filmove()