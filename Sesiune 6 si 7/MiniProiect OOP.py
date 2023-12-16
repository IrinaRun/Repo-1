'''
Magazin care vinde prod alimentare si non-alimentare

'''

# 1. Mostenire
class Magazin:
    def __init__(self,nume):
        self.nume= nume

class Alimentare(Magazin):
    def categorie(self):
        return 'Magazinul comercializeaza prod alimentare'
class NonAlimentare(Magazin):
    def tip_produs(self):
        return 'Magazinul comercializeaza prod non-alimentare'

paine = Alimentare('Panificatie')
mezel = Alimentare('Mezeluri')
hartie_igienica= NonAlimentare('cosmetice')
deodorant= NonAlimentare('cosmetice')
print(paine.categorie())
print(deodorant.tip_produs())

# 2. Polimorfism
class Apa:
    def categorie(self):
        return "Produsul este din categoria Alimentare"
class Imbracaminte:
    def categorie(self):
        return 'Produsul nu este din categoria Alimentare'
def afiseaza_categorie(categ):
    print(categ.categorie())

borsec= Apa()
bluza= Imbracaminte()
afiseaza_categorie(borsec)
afiseaza_categorie(bluza)

# 3. Encapsulare

class Magazin1:
    def __init__(self,adresa,nume):
        self.adresa=adresa
        self.nume=nume
        self._cantit=0
        self.__vanzari =3000
        self.tip_produse =[]
        self.categorii =[]
    def add_tip_produse(self,tip_prod):
        self.tip_produse.append(tip_prod)
    def remove_tip_produse(self,tip_prod):
        self.tip_produse.remove(tip_prod)
    def cant_vandute(self,cant_vanz):
        self._cantit+=cant_vanz

    @property
    def vanzari(self):
        pass

    @vanzari.getter
    def vanzari(self):
        return self.__vanzari

    @vanzari.setter
    def vanzari(self,val_totala):
        self.__vanzari+=val_totala

    @vanzari.deleter
    def vanzari(self):
        self.__vanzari = 0

Braldico= Magazin1('Reconstructiei,nr.5','Braldico')
#apelare getter
print(f'vanzarile magazinului Braldico prin metoda getter sunt: {Braldico.vanzari}')
#apelare setter
Braldico.vanzari =500
print(f'vanzarile magazinului Braldico prin metoda setter sunt: {Braldico.vanzari}')
#apelare deleter
del Braldico.vanzari
print(f'vanzarile magazinului Braldico prin metoda deleter sunt: {Braldico.vanzari}')

# 4. Abstractizare
from abc import ABC, abstractmethod
class Vanzare_produse(ABC):
    @abstractmethod
    def proces_vanzare(self):
        pass
class Bauturi(Vanzare_produse):
    def proces_vanzare(self):
        print(f'Declansare proces vanzare')
fanta =Bauturi()
fanta.proces_vanzare()

class Vanzare_magazin(ABC):
    @abstractmethod
    def verificare(self):
        raise NotImplementedError
    def scanare(self):
        pass
    @abstractmethod
    def incasare(self):
        pass

class Vanzare_magazinPrivat(ABC):
    nr_produse = 0
    adresa = None
    ora_deschidere =None
    def scanare(self):
        print (f'Cod exista in baza de date')
    def incasare(self):
        print(f'Incasare realizata')

class Vanzare_magazinPublic(ABC):
    nr_produse = 0
    adresa = None
    ora_deschidere =None
    def scanare(self):
        print (f'Produs validat cu succes')
    def incasare(self):
        print(f'Produs incasat cu succes')

privata = Vanzare_magazinPrivat()
print(privata)
privata.scanare()
privata.incasare()
publica = Vanzare_magazinPublic()
print(publica)
publica.scanare()
publica.incasare()








