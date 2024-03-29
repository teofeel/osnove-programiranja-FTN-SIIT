from prettytable import PrettyTable

sale = []
def ucitaj_sale():
    global sale
    with open('data/sale.txt') as sale_fajl:
        lines = sale_fajl.readlines()
        for line in lines:
            data = line.split(';')
            sale.append({
                'sifra':data[0],
                'naziv':data[1],
                'redovi':data[2],
                'sedista':data[3]
            })

def sala_ispis_po(filteri, vrednosti):
    for sala in sale:
        for i in range(0, len(filteri)):
            if vrednosti[i].upper() == sala[filteri[i]].upper():
                
                for j in sala:
                    print(str(j).upper()+': ', end=' ')
                    print(sala[j], end='\n')
                print('//////////////////////',end="\n")
                
def sedista_sale(sifra_sale, rezervisana_sedista):
    print('Slobodna sedista: ')
    t = PrettyTable()
    for sala in sale:
        if sala['sifra']==str(sifra_sale):
            for i in range(1,int(sala['sedista'])):
                sedista_arr=[]
                for j in range(int(sala['redovi'])):
                    pocetno = 'A'
                    sediste = chr(ord(pocetno)+j)+str(i)
                    x_na_to = False

                    for sedista in rezervisana_sedista:
                        if sedista == sediste:
                            x_na_to = True
                            break
                    if x_na_to:
                        sedista_arr.append('X')
                    else:
                        sedista_arr.append(sediste)
                t.add_column('Red '+str(i),sedista_arr)
    print(t)

def postoji_sediste(sifra_sale, sediste_provera):
    for sala in sale:
        if sala['sifra'] == str(sifra_sale):
            for i in range(int(sala['redovi'])+1):
                for j in range(1,int(sala['sedista'])):
                    pocetno = 'A'
                    sediste = chr(ord(pocetno)+i)+str(j)
                    if sediste == sediste_provera:
                        return True
    return False
                    
