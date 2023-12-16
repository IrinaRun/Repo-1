# MOSTENIREA - este un concept in POO care permite unei clase copil (numita clasa derivata sau subclasa) sa preia
# atribute si metode de la una sau mai multe clase parinte (numite si clase de baza sau superclase)
# Clasa copil preia atributele si metodele clasei parinte si poate adauga sau modifca comportamentul acesteia.
# Avantajul mostenirii este acela ca nu mai este nevoie sa scriem acelasi cod de mai multe ori.
# O clasa copil poate sa mosteneasca un nr nelimitat de clase parinte

# Ex de defnire clasa parinte si copil

class Animal:
    def __init__(self, nume):
        self.nume = nume # aceasta este clasa de baza (parinte) in ierarhia de mostenire

    def sunet(self):    #metoda cu implementare implicita
        return 'Sunet necunoscut'

class Caine(Animal):    #clasa copil care mosteneste clasa parinte "Animal"
    def sunet(self):    #aceasta metoda va suprascrie metoda din clasa parinte
        return "Ham ham"

class Pisica(Animal):
    def sunet(self):
        return "Miau miau"

rex = Caine(nume='Rex')
tom = Pisica(nume= 'Tom')
print(rex.nume)
print(tom.nume)
print(rex.sunet())
print(tom.sunet())

# Ex. mostenire multipla
class AnimalTerestru:
    def deplasare(self):
        return "Se deplaseaza pe uscat"

class AnimalAerian:
    def deplasare(self):
        return "Se deplaseaza in aer"

class Pasare(AnimalTerestru,AnimalAerian):
    pass

papagal = Pasare()
print(papagal.deplasare())




