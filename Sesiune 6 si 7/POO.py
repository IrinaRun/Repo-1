'''
POO = PROGRAMARE ORINETATA PE OBIECT
POO este o modalitate prin care putem sa structuram proprietatile si comportamentul unei entitati din viata reala intr-o
structura logica ce functioneaza ca un template. Acest template va servi drept model pentru crearea unei enitati care
sa reprezinte un exemplu din viata reala.
POO se bazeaza pe clase si obiecte.
O CLASA este un sablon sau un model (ca o reteta) pentru a crea obiecte. Ea defineste atributele si modelele care vor
fi prezente in obiectele create din acea clasa.
OBIECTELE sunt instante ale claselor. Acestea contin date specifice (atribute) si pot apela metodele definite in clasa lor.
ATRIBUTELE sunt variabile definite intr-o clasa. Atributele unei clase descriu cum ar trebui sa arate entitatea (ce
proprietati sa aiba)
METODELE sunt functii definite intr-o clasa. Metodele unei clase descriu ce ar tb sa faca entitatea (cum sa se comporte)
Diferenta intre functii si metode este aceea ca functiile sunt independente, in timp ce metodele sunt create in
interiorul unei clase
'''

#ex.1

# class Masina:
#     def __init__(self,marca,model):
#         self.marca=marca
#         self.model=model
#     def afiseaza_intormatii(self):
#         print(f'Masina: {self.marca} {self.model}')
#
#
# #exemplu de obiect al clasei Masina
#
# masina_mea = Masina(marca='Toyota',model='Corolla')
# print(masina_mea.marca,masina_mea.model)
# masina_mea.afiseaza_intormatii()

#ex.2

class Caine:                            #am definit clasa Caina
    def __init__(self,nume, varsta):    #am definit metoda speciala __init__care actioneaza ca un constructor
        self.nume = nume                #atributele nume si varsta ale obiectului sunt initializate cu valorile primite
                                        # la crearea obiectului
        self.varsta = varsta
    def latra(self):                    #am definit metoda latra care afiseaza un mesaj simplu in consola
        print('ham ham')

rex = Caine(nume ='REX', varsta=3)      #am creat un obiect 'rex' si am transmis valorile atributelor nume si varsta
print(rex.nume)                         #se acceseaza si se afiseaza valorile atributului nume
print(rex.varsta)                       #se acceseaza si se afiseaza valorile atributului varsta
rex.latra()                             #am apelat metoda 'latra' a obiectului 'rex'

'''
Exista 2 tipuri de constructori
1. constructor implicit - care este incorporat in limbajul Python si el este apelat automat atunci cand nu exista un
constructor explicit
2. constructor explicit - este definit de catre un utilizator cu scopul de a controla felul in care acel obiect este
instantiat
'''
#exemplu de constructor implicit

class Masina:
    def __init__(self):
        self.model = 'Nissan'
        self.an_fabricatie = 2020
    def afisare_informatii(self):
        print(f'model: {self.model} , an fabricatie: {self.an_fabricatie}')

masina1= Masina()
masina1.afisare_informatii()


#exemplu de constructor explicit
class Masina:
    def __init__(self,model='Dacia', an_fabricatie=2020):
        self.model = model
        self.an_fabricatie = an_fabricatie
    def afisare_informatii(self):
        print(f'model: {self.model} , an fabricatie: {self.an_fabricatie}')

masina2= Masina(model='Tesla',an_fabricatie=2021)
masina2.afisare_informatii()

#exemplu de constructor explicit
class Scoala():
    #atribute pe care le poate avea Scoala:
    adresa = None            #am pus none pt ca fiecare obiect al clasei sa poata avea propria adresa
    ciclu_invatamant = 'Primar'
    capacitate_elevi = None
    numar_profesori = None
    profil = "Real"
    clase ={}                   #este un dictionar care va contine inform despre clasele scolii

    #definim un constructor explicit
    def __init__(self, adresa, ciclu_invatamant, profil):
        self.adresa = adresa
        self.ciclu_invatamant = ciclu_invatamant
        while profil.lower() not in ("real","uman"):
            profil = input("profil invalid. Va rugam sa introduceti una din optiunile 'Real' sau 'Uman' ")

    #activitati care se pot face intr-o scoala
    def adauga_clasa(self, nume_clasa,profil, ciclu,numar_elevi,numar_profesori):
        self.clase[nume_clasa] = {'profil':profil,
                                  'ciclu':ciclu,
                                  'numar_elevi':numar_elevi,
                                  'numar_profesori':numar_profesori}

    #definim o metoda prin care actualizam adresa scolilor
    def actualizare_adresa_scoala(self, adresa_noua):
        self.adresa = adresa_noua
        print(self.adresa)
        return self.adresa      #returneaza noua adresa astfel incat sa poata fi utilizata sau afisata in alta parte a codului

    #definim o met care sa extraga nr profesorilor
    def extrage_nr_de_profesori(self):
        return self.numar_profesori     #returneaza val atributului numar_profesori al obectului curent

# scoala1=Scoala() #at cand initializam un obiect dintr-o clasa cu constructor explicit, suntem obligati sa dam valori pt
                #parametri definiti in constructorul explicit
scoala1= Scoala('str.Mihai voda','primar','Real')
print(f'Adresa scolii este: {scoala1.adresa}')
print(f'Ciclul de invatamant este: {scoala1.ciclu_invatamant}')
print(f'Profilul scolii este: {scoala1.profil}')

scoala1.actualizare_adresa_scoala('str.Mircea cel Batran 23')
print(f'noua adresa este: {scoala1.adresa}')

scoala1.numar_profesori =45
print(scoala1.extrage_nr_de_profesori())
print(f'Nr de profesori este :{scoala1.numar_profesori}')

#asa printam atribute definite la nivel de obiect:
print(f'Atributele definite la nivel de obiect sunt: {scoala1.adresa} {scoala1.profil} {scoala1.numar_profesori}'
      f' {scoala1.ciclu_invatamant} {scoala1.clase}')

#sa printam atributele definite la nivel de clasa:
print(f'Atributele definite la nivel de clasa sunt: {Scoala.adresa} {Scoala.profil} {Scoala.clase}'
      f' {Scoala.numar_profesori} {Scoala.ciclu_invatamant} {Scoala.capacitate_elevi}')

#ATENTIE!! Ordinea argumentelor date la instantiere trebuie sa coincida cu ordinea parametrilor definiti in constructor
scoala3= Scoala('Str.Margelelor nr.60','Gimnazial','Real')
print(f'Atributele definite la niv de obiect "Scoala3" sunt: {scoala3.adresa} {scoala3.ciclu_invatamant}'
       f' {scoala3.profil} ')

#In POO exista 4 principii:
#1. Mostenirea (Inheritance)
#2. Abstractizarea (Abstracting)
#3. Polimorfism (Polymorphism)
#4. Incapsularea (Encapsulation)
