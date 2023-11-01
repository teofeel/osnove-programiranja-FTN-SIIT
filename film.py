# klasa za film
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
                "zemlja poerkla":data[5],
                "godina":data[6],
                "opis":data[7]
            })
