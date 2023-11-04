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
