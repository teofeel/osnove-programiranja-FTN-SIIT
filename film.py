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

def pregled_filmova():
    if filmovi == []:
        return 0
    
    for film in filmovi:
        for i in film:
            print(str(i).upper()+":", end=" ")
            print(film[i], end="\n")
        print('//////////////////////',end="\n")

def pretraga_filmova_filter(filter, vrednost):
    if filter == 3:
        if vrednost['izbor']==1:
            for film in filmovi:
                if int(film['trajanje'])<vrednost['vrednost'][0]:
                    for i in film:
                        print(str(i).upper()+":", end=" ")
                        print(film[i], end="\n")
                    print('//////////////////////',end="\n")
        
        elif vrednost['izbor']==2:
            for film in filmovi:
                if int(film['trajanje'])>vrednost['vrednost'][0]:
                    for i in film:
                        print(str(i).upper()+":", end=" ")
                        print(film[i], end="\n")
                    print('//////////////////////',end="\n")
        
        elif vrednost['izbor']==3:
            for film in filmovi:
                if (int(film['trajanje'])>vrednost['vrednost'][0]
                    and int(film['trajanje'])<vrednost['vrednost'][1]):
                    
                    for i in film:
                        print(str(i).upper()+":", end=" ")
                        print(film[i], end="\n")
                    print('//////////////////////',end="\n")
        return
    if filter == 7:
        for film in filmovi:
            if int(film['godina'])==vrednost: #filter prevesti u vrednost
                print('//////////////////////', end='\n')
                for i in film:
                    print(str(i).upper()+":", end=" ")
                    print(film[i], end="\n")
                print('//////////////////////',end="\n")
        return

    if filter==1: filter='naziv'
    elif filter==2: filter='zanr'
    elif filter==3: filter='trajanje'
    elif filter==4: filter='reziser'
    elif filter==5: filter='uloge'
    elif filter==6: filter='zemlja porekla'
    elif filter==7: filter='godina'

    for film in filmovi:
        if vrednost.upper() in film[filter].upper(): #filter prevesti u vrednost
            for i in film:
                print(str(i).upper()+":", end=" ")
                print(film[i], end="\n")
            print('//////////////////////',end="\n")

    