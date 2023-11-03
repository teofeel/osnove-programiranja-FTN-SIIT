# klasa projekcija
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

from sala import getSala_naziv_sifra
def ispisi_uslov(filter,uslov):
    br=0
    for projekcija in projekcije:
        if filter=='sala':
            if getSala_naziv_sifra(uslov)['naziv'] in projekcija[filter]:
                print('Sala: '+projekcija['sala'])
                print('Pocetak termina: '+projekcija['pocetak'])
                print('Kraj termina: '+projekcija['kraj'])
                print('Dani: '+projekcija['dani'])
                print('Film: '+projekcija['film'])
                print('Sala: '+projekcija['cena'])
                return 1

        if uslov in projekcija[filter]:
            print('Sala: '+projekcija['sala'])
            print('Pocetak termina: '+projekcija['pocetak'])
            print('Kraj termina: '+projekcija['kraj'])
            print('Dani: '+projekcija['dani'])
            print('Film: '+projekcija['film'])
            print('Sala: '+projekcija['cena'])
            br+=1    
    if br==0: return 0