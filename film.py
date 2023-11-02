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

def pretraga_filmova_(filteri, vrednosti):
    if filmovi == []: return 0
    if filteri==[] or vrednosti==[]:
        for film in filmovi:
            for i in film:
                print(str(i).upper()+":", end=" ")
                print(film[i], end="\n")
            print('//////////////////////',end="\n")

    filmovi_stampanje = []
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

            if filteri[i]==1: filteri[i]='naziv'
            elif filteri[i]==2: filteri[i]='zanr'
            elif filteri[i]==3: filteri[i]='trajanje'
            elif filteri[i]==4: filteri[i]='reziser'
            elif filteri[i]==5: filteri[i]='uloge'
            elif filteri[i]==6: filteri[i]='zemlja porekla'
            elif filteri[i]==7: filteri[i]='godina'
            
            
            if vrednosti[i].upper() in film[filteri[i]].upper(): #filter prevesti u vrednost
                uslovi+=1

        if uslovi == len(filteri):
            for j in film:
                print(str(j).upper()+":", end=" ")
                print(film[j], end="\n")
            print('//////////////////////',end="\n")
        
    return 