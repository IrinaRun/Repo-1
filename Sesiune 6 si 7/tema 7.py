#  ex.1 ABSTRACTIZARE

from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    PI = 3.14
    print(f'Valoarea lui PI este:  {PI}')

    def descrie(self):
        print(f'Cel mai probabil am colturi')
class FormaGeometrica1(FormaGeometrica):

    @abstractmethod
    def aria(self):
        pass
geometrica= FormaGeometrica()
geometrica.descrie()

#ex.2
# MOSTENIRE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.latura= latura

latura = 6
print(f'latura are valoarea : {latura}')
patrat=Patrat(latura)
patrat.descrie()

#ex.3
# ENCAPSULARE
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
class Patrat(FormaGeometrica):
    def __init__(self):
        self.__latura = 6
    @property
    def privat(self):
        pass
    @privat.getter
    def privat(self):
        return self.__latura
    @privat.setter
    def privat(self,latura_noua):
        self.__latura+=latura_noua
    @privat.deleter
    def privat(self):
        self.__latura = 0

patrat=Patrat(latura)
print(patrat.latura)
