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
                
def getSala_naziv_sifra(sifra):
    # treba popraviti
    for s in sale:
        if sifra.isdigit():
            if s['sifra']==sifra:
                return s
        else:
            if s['naziv'].upper()==sifra.upper():
                return s