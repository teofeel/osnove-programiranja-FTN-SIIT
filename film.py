# klasa za film
class Film:
    def __init__(self,naziv_filma, zanr, trajanje, reziser, 
                 uloge, zemlja_porekla, godina_proizvodnje, opis_filma):
        self.naziv_filma        = naziv_filma 
        self.zanr               = zanr
        self.trajanje           = trajanje
        self.reziser            = reziser
        self.uloge              = uloge
        self.zemlja_porekla     = zemlja_porekla
        self.godina_proizvodnje = godina_proizvodnje
        self.opis_filma         = opis_filma