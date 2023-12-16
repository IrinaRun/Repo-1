import math
#FUNCTII
#Functiile sunt blocuri de cod reutilizabile care efectueaza o anumita actiune. Ele sunt definite cu scopul de a limita
#nr de linii de cod pe care le scriem si a face programul sa fie mai modular si respectiv mai usor de citit.
# Componentele unei functii sunt:
#inceputul functiei definit prin cuvantul "def"
#numele functiei care nu trebuie sa fie un cuvant rezervat si se foloseste formatul snake_case
#() care pot stoca parametri
#separatorul intre lista de parametri si corpul functiei este ":"
#corpul functiei - setul de instructiuni care se vor executa la apelarea functiei
#(optional) - instructiunea de return



#ex
def salutare():
    print("Salut!")

salutare()#Apelul functiei

#Pt a fol instructiunile salvate intr-o functie, tb sa facem ceea ce se numeste apelarea functiei. Instructiunile
#dintr-o functie se vor executa DOAR DACA APELAM FUNCTIA.
#Apelarea se face prin scrierea numelui functiei urmat de doua paranteze rotunde in interiorul carora vom pune
#(daca este cazul) unul sau mai multe argumente.

'''
EXISTA 4 TIPURI DE FUNCTII IN PYTHON:
1. Functii simple
2. Functii cu parametri
3. Functii cu return
4. Functii cu parametri si return

PARAMETRI: un parametru este o adresa de memorie temporara care se populeaza atunci cand functia este apelata. Parametrii
sunt reprezentati de un nume care este specificat intre paranteze rotunde la definirea functiei si au rolul de a stoca 
informatii venite din exterior, aceste informatii vor fi utilizate in momentu executarii instructiunilor.

PARAMETRII sunt de 2 feluri:
1. Parametri expliciti - specificati in mod direct in definirea functiei
2. Parametri impliciti - in cazul in care nu vor primi valoare la apelarea functiei se vor folosi implicit valoarea 
specifica la definirea functiei
'''

#ex parametri expliciti
def salutare_cineva(nume): #nume este parametru explicit
    print(f'Salut, {nume}!')

salutare_cineva('John') #la apelare, numele valorilor efective care sunt transmise functiilor se numesc argumente. John
                        #este un argument

#ex. parametri impliciti
def salutare_cineva(nume='Ioana'): #aceasta functie are un sg parametru explicit care are o val implicita setata 'Ioana'
    print(f'Salut, {nume}!')

salutare_cineva()# la apelare nu am furnizat argument
salutare_cineva('Cristi')# la aceast apelare am furnizat si argument, iar in acest caz val implicita(Ioana)
                    # setata la definirea functiei va fi ignorata deoarece am furnizat un argument explicit

'''
RETURN
este modalitatea prin care putem sa transmitem rezultatul functiei in exterior (adica sa o vizualizam)
Spre ex daca vrem sa calculam suma a 2 nr si sa o printam pe ecran, in momentul apelarii functiei va trebui sa avem 
instructiune de return, altfel adunarea se va executa, dar noi nu vom putea valida acest lucru pt ca nu va fi afisat 
nicaieri
'''

#Ex. Functii cu parametri si return
def adunare(a,b):
    rezultat = a+b #se realizeaza adunarea parametrilor a si b, iar rezultatul este stocat in variabila rezultat
    return rezultat #aceasta este valoarea pe care il va primi orice cod care apeleaza aceasta functie

suma = adunare(3,5)#se apeleaza functia adunare cu argumentele a=3 si b=5. Rezultatul returnat in functie(suma lui a,b)
                    #este asignat variabilei suma
print(f'Suma este: {suma}')#printam variabila suma


#FUNCTII cu nr indefinit de parametri
#in Python poti defini functii care sa accepte un nr variabil de parametri, folosindu-ne de functia Python "*args" si
#'kwargs

def functie_variabila(*args):#functia a fost definita cu un sg parametru *args, aratand ca functia accepta un nr variabil
                            #de argumente
    rezultat=0 #se initializaaza variabila rezultat la zero, care va fi utilizat pt a stoca suma argumentelor
    for numar in args: #bucla 'For' itereaza prin toate argumentele furnizate si adauga fiecare la variabila rezultat
        rezultat+=numar
    return rezultat #aceasta este valoarea pe care il va primi orice cod care apeleaza aceasta functie
rezultat1 = functie_variabila(1,2,3) #se apleaza functia cu 3 argumente, iar rezultatul va fi stocat in rezultat1
rezultat2 = functie_variabila(4,5,6,7,8,9,10)#se apleaza functia cu 7 argumente, iar rezultatul va fi stocat in rezultat2

print(f'Rezultat 1: {rezultat1}')#la rularea acestui cod, se vor afisa rezultatele sumelor pentru cele 3 arguemnte
print(f'Rezultat 2: {rezultat2}')#la rularea acestui cod, se vor afisa rezultatele sumelor pentru cele 7 arguemnte


#functii cu **kwargs

def informatii_student(**kwargs):#folosim parametrul **kwargs, aratand ca functia accepta un nr variabil de argumente keyword
    for cheie,valoare in kwargs.items():#fol bucla For pt a itera prin perechile cheie-valoare din kwargs
        print(f'{cheie} {valoare}') #fiecare pereche cheie-valoare va fi afisata in consola folosindu-ne de functie print

informatii_student(nume = "John",varsta =20)#se apeleaza functia furnizand argumente de tip cheie-val(nume=John)
informatii_student(nume = "Alice",varsta =25, nota =10, cursul = "Biologie" )

#ex. sa calculam aria unui cerc
def aria_cerc(raza):
    return math.pi *raza **2

rez = aria_cerc(3)
print(rez)

#TRATAREA EXCEPTIILOR
'''
Este o tehnica de tratare a situatiilor exceptionale care pot aparea in timpul executiei unei bucati de cod sau a codului
intreg.
Exceptiile sunt evenimente neasteptate care pot provoca intreruperea rularii codului. Sunt utile at cand nu ne dorim
oprirea codului.
Structura trratarii exceptiilor
try - inceputul blocului de exceptie
caracterul ":" - marcheaza inceputul blocului de cod care se incearca a se executa
except - inceputul blocului de tratare exceptii
caracterul ":" - marcheaza inceputul blocului de cod de tratare a exceptiilor
blocul de cod care se executa atunci cand se reproduce o exceptie
'''

#ex.1
# print(10/0)
try:
    print(10/0)
except:
    print('impartirea la 0 nu este permisa')

try:
    rezultat = 10/0 #inmcerc sa impart 10 la 0
except ZeroDivisionError: #ZeroDivisionError este denumirea erorii care apare daca vrem sa impartim 10 la 0
    print('Eroare: Impartirea la 0 nu este permisa') #blocul care se executa daca apare exceptia specifica

def impartire(a,b):
    try:
        rezultat3 = a/b
        print(f'Rezultatul impartirii este: {rezultat3}')
    except ZeroDivisionError:
        print('Nu se poate efectua impartirea')

impartire(10,0)
impartire(9,3)

#RIDICAREA UNEI EXCEPTII
#Se poate ridica o exceptie manual folosind instructiunea "raise" (ridicarea unei exceptii). Este folosta in ggeneral
#de catre programatori. Este utila atunci cand vrei sa semnalezi ceva anormal in program si sa fortezi o executie
#alternativa.

#ex.1
# nota_elev = int(input('Introduceti nota care trebuie sa fie procesata \n'))
# if nota_elev<5: #verifica conditia daca nota este mai mica de 5
#     raise Exception ('Nota cursantului este prea mica') # daca comd de mai sus este adevarata, atunci este executata
#                                                 #instructiunea de 'Raise'

# folosirea raise, programul semnaleaza explicit ca se afla intr-o situatie exceptioanla, unde nota studentului este
#considerata prea mica. Functia raise este utilizata in general doar de programatori.


##DEBUGGING
#Repreziunta procesiul de analiza a codului prin care observam cum circula datele prin intermediul caruia putem
#identifica potentialele probleme. Pt a face debugging tb sa punem un break point in locul in care vrem sa vedem cum
#circula datele.Se pot pune multiple break pointuri. Un break point este un loc in care codul se opreste inainte sa
#execute urmatoarea instructiune.
#Pt a pune un break point, dam click pe marginea din stg a fisierului intre cifre si marginea fisierului
#Dupa ce am pus break point-ul de care avem nevoie, dam click dreapta si "Debug"

#Ex.
lista_masini = ['audi','skoda','ferrari','mercedes','trabant','dacia','mustang','tesla']
i = 0
while i<len(lista_masini):
    if lista_masini[i] =='mercedes':
        print(f'Am gasit masina dvs ')
        break
    i+=1


