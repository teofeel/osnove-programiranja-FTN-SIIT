from korisnik import korisnici
from korisnik import novi_korisnik
from functions import kupac
from film import filmovi
from projekcija import projekcije
from sala import sale

# funkcija za prijavu korisnika
def prijava():
    tryagn='y'
    while tryagn!='n':
        print('Za prekidanje prijave unesite ; bilo kad')
        korisnicko_ime = input('Unesite korisnicko ime: ')
        if korisnicko_ime == ';': return
        lozinka = input('Unesite lozinku: ')
        if lozinka == ';': return

        for korisnik in korisnici:
            postoji = korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka']==lozinka
            if postoji and korisnik['uloga']=='registrovani kupac':
                return kupac.main(korisnik['korisnicko_ime'])
            elif postoji and korisnik['uloga']=='prodavac':
                return
            elif postoji and korisnik['uloga']=='menadzer':
                return
            
        tryagn = input('Korisnicko ime ili lozinka je pogresna. Da li hocete opet da probate (y/n): ')
        if tryagn ==';': return 1
    if(tryagn=='n'):
        return 1
    return 0

def registracija():
    # funckija za registraciju korisnika
    # nakon sto se kreira objekat, on je ubacen u listu objekata korisnika
    # jedinstveno korisnicko ime
    # jedinstvena lozinka preko 6 karaktera sa jednom cifrom
    # zabranjeni karakter ;
    print('Za prekidanje registracije unesite ;')
    korisnicko_ime = input('Unesite korisnicko ime (; nije dozvoljen u imenu): ')
    # provera da li je korisnicko ime vec registrovano
    if korisnicko_ime == ';': return
    for korisnik in korisnici:
        while korisnicko_ime == korisnik["korisnicko_ime"]:
            korisnicko_ime = input('Korisnicko ime je vec registrovano. Unesite opet korisnicko ime: ')
    while ';'in korisnicko_ime:
        korisnicko_ime = input('Ime sadrzi nedozvoljeni karakter ; . Unesite opet korisnicko ime: ')

    ime = input('Unesite ime: ')
    if ime == ';': return
    while ';'in ime:
        ime = input('Unesite opet ime (; nije dozvoljeno u imenu): ')

    prezime = input('Unesite prezime: ')
    if prezime == ';': return
    while ';'in prezime:
        prezime = input('Unesite opet prezime (; nije dozvoljeno u prezimenu): ')

    lozinka = input('Lozinka: ')
    if lozinka == ';': return
    while ';'in lozinka or (not any(i.isdigit() for i in lozinka)) or len(lozinka)<6:
        lozinka = input('Lozinka mora biti duza od 6 karaktera, ne sme da sadrzi ; i mora sadrzati barem jednu cifru. Unesite opet lozinku. : ')

    korisnik={
        "korisnicko_ime":korisnicko_ime, 
        "lozinka":lozinka,
        "ime":ime,
        "prezime":prezime,
        "uloga":"registrovani kupac"
    }

    novi_korisnik(korisnik)

    kupac.main(korisnicko_ime)

#######################################
# Funkcije za sve (ne)ulogovane korisnike bilo kada

from film import pretraga_filmova_
def pregled_filmova_main():
    if pretraga_filmova_([],[])==0:
        print('Trenutno nema dostupnih filmova')
    
def pretraga_filmova(vise_krit):
    filteri = []
    vrednosti = []

    while True:
        print('Dostupni filteri: 1.) Naziv Filma | 2.) Zanr | 3.) Trajanje | 4.) Reziser | 5.) Uloge | 6.) Zemlja Porekla | 7.) Godina Proizvodnje')
        print('Ako odustajete unesite bilo koje slovo')

        filter = input('Unesite filter: ')
        if filter=='':
            return pregled_filmova_main()
        elif not filter.isdigit():
            return
            
        filter = int(filter)
        
        if filter > 7 or filter < 1:
            pregled_filmova_main()
            return

        elif filter == 3:
            j=0
            while j==0:
                print('Izaberite po da li ocete maks, min ili granicno trajanje')
                print('1.) Maksimalno trajanje | 2.) Minimalno trajanje | 3.) Granicno trajanje')

                izbor = input('Unesite vrednost: ')
                if izbor==';': return
                if not izbor.isdigit(): continue
                izbor = int(izbor)
                if izbor<1 or izbor>3: continue
                j=1
            

            if izbor==1:
                j=0
                while j==0:
                    min_vrednost = input('Maksimalno trajanje filma: ')
                    if min_vrednost==';': return
                    if not min_vrednost.isdigit(): continue
                    min_vrednost = int(min_vrednost)

                    vrednost = {"izbor":izbor, "vrednost":[min_vrednost]}
                    j=1

            elif izbor==2:
                j=0
                while j==0:
                    max_vrednost = input('Minimalno trajanje filma: ')
                    if max_vrednost==';': return
                    if not max_vrednost.isdigit(): continue
                    max_vrednost = int(max_vrednost)
                    
                    vrednost = {"izbor":izbor, "vrednost":[max_vrednost]}
                    j=1

            elif izbor==3:
                j=0
                while j==0:
                    min_vrednost = input('Minimalno trajanje filma: ')
                    if min_vrednost==';': return
                    if not min_vrednost.isdigit(): continue

                    max_vrednost = input('Maksimalno trajanje filma: ')
                    if max_vrednost==';': return
                    if not max_vrednost.isdigit(): continue

                    min_vrednost = int(min_vrednost)
                    max_vrednost = int(max_vrednost)

                    vrednost = {"izbor":izbor, "vrednost":[min_vrednost, max_vrednost]}
                    j=1
            
            #return pretraga_filmova_filter(filter, vrednost)
            
        elif filter == 7:
            j=0
            while j==0:
                vrednost = input('Unesite godinu: ')
                if vrednost==';': return
                elif not vrednost.isdigit(): continue
                vrednost = int(vrednost)
                j=1
                
            #return pretraga_filmova_filter(filter, vrednost)
        
        else:
            vrednost = input('Unesite vrednost: ')
            #return pretraga_filmova_filter(filter, vrednost)

        if vise_krit:
            filteri.append(filter)
            vrednosti.append(vrednost)
            nastavi=input('Da li ocete jos kriterijuma da dodate y/n: ')
            if nastavi=='n': break
        else:
            filteri.append(filter)
            vrednosti.append(vrednost) 
            break

    print('//////////////////////////////////')
    return pretraga_filmova_(filteri,vrednosti)


import termin
def pretraga_termina():
    def unos_vreme():
        while True:
            sati = input('Unesite vreme u satima: ')
            if sati==';': return ';',';'
            if not sati.isdigit(): continue
                    
            minuti = input('Unesite vreme u minutima: ')
            if minuti==';': return ';',';'
            elif not (minuti.isdigit() or minuti==''): continue

            return sati, minuti

    while True:
        print('1) Film | 2) Sala projekcije | 3) Datum odrzavanje | 4) Vreme pocetka | 5) Vreme kraja')
        print('Da odustanete unesite ; bilo kada')
        izbor = input('Izaberite: ')
        if izbor==';': return
        elif not izbor.isdigit(): continue
        izbor=int(izbor)

        if izbor == 1:
            for film in filmovi:
                print(film['naziv'], end=' | ')
            print('\n')
            while True:
                vrednost = input('Unesite naziv filma: ')
                if vrednost==';': return
                termin.pretrazi_termine('film', vrednost)
                yn = input('Da li zelite da nastavite sa pretragom po filmovima y/n: ')
                if yn == 'y':continue
                else: break
        
        elif izbor == 2:
            while True:
                vrednost = input('Unesite sifru ili naziv sale: ')
                if vrednost == ';': return
                termin.pretrazi_termine('sala', vrednost)
                yn = input('Da li zelite da nastavite sa pretragom po salama y/n: ')
                if yn == 'y':continue
                else: break
        
        elif izbor==3: 
            while True:
                vrednost = input('Unesite datum odrzavanja: ')
                if vrednost==';': return
                termin.pretrazi_termine('datum', vrednost)
                yn = input('Da li zelite da nastavite sa pretragom po datumu y/n: ')
                if yn == 'y':continue
                else: break

        elif izbor==4:
            while True:
                sati, minuti = unos_vreme()
                if sati==';': return
                termin.pretraga_vreme('pocetak', sati,minuti)
                yn = input('Da li zelite da nastavite sa pretragom po pocetku y/n: ')
                if yn == 'y': continue
                else: break

        elif izbor==5:
             while True:
                sati, minuti = unos_vreme()
                if sati==';': return
                termin.pretraga_vreme('kraj', sati,minuti)
                yn = input('Da li zelite da nastavite sa pretragom po kraju y/n: ')
                if yn == 'y': continue
                else: break