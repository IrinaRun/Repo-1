# punem comentarii pe o singura linie
"""
- intre aceste ghilimele se pot pune comentarii pe mai multe linii, iar editorul de cod le va ignora
variabila = 10 # am declarat o variabila
"""
#linia acesta va fi comentata
# - cu combinatia tastelor CTRL +? putem comenta o linie selectata

# VARIABILELE sunt adrese de memorie care stocheaza diverse valori, valori care se pot modifica pe parcursul
# executiei codului
# numar_intreg = 15
# print(numar_intreg)
#CamelCase - consta in a incepe un cuvant cu majuscula, fara sa folosim spatii sau caractere cu subliere
#intre cuvinte
#NumeVariabila = 15
#SnakeCase - consta in folosirea de litere mici si adaugarea de caractere de subliniere intre cuvinte
#nume_variabila = 15
numar_intreg = 15 #(int)
numar_cu_virgula = 3.14 #(floot)
text = "salut, buna seara!" #(string)
lista = [1,2,3,4] # (lista)

# TIPURI DE DATE - proprietati ale adreselor de memorie care definesc ce fel de informatii pot fi stocate
# la acea adresa de memorie. tipul de date poate varia in functie de valoarea salvata la acea adresa de memorie
# si se poate schimba pe parcusul executiei codului
#Tipuri de date cele mai cunoscute:
 #Numeric: int (integer)
   #myvar=15
#Float (nr cu virgula)
    #myvar=3.14
# Sir de caractere: str (string)
    #myvar = "Buna ziua!"
#Valori logice
    #bool(boolean) : True, False
    #myvar=True
#Structuri de date secventiale"
    #list(lista) = [1,2,3]
    #tupla =(1,2,3)
#Structuri de date mapping:
    #dict(dictionar) = {cheie:valoare}
#Structuri de date set:
    #set(seturi) = {1,2,3}

ani = 5 #am initializat o variabila cu valoare 5 reprezentata de tipul de date int
ani1 = "cinci " # am initializat var cu val cinci de tipul de date string

#print = fctie csare ne ajuta sa printam
#print(lista)
#printare cu formatare - modalit prin care putem integra o variabila in interiorul unui string
#pt tip de date string '+' este fol pt a concatena 2 siruri de caractere
#pt tip date int semnul '+' va face adunarea
#print("Ana are " +12 + "ani" ) - aici am incercat sa concatenam date de tip str cu int si a dat err
#print("Ana are " + str(12) + "ani") -# aici am fol type casting, adica am fortat cifra 12 sa fie de tip str
                                #nu am primit err dar codul este incarcat si greu de citit
#print(f"Ana are {12} ani")
varsta = 12
print(f"Ana are {varsta} ani") #am concatenat cu variabila definita mai sus

#CONSTANTELE - sunt o adresa de memorie care stocheaza o valoare
# de obicei, constantele sunt denumite cu litere majuscule si cu subliniere intre cuvinte
# PI = 3.14159
# MAX = 100
# print(PI)
# varsta = 15 #am modif valoarea variabilei varsta
# print(f"Ana are {varsta} ani") # am printat noua valoare

#FUNCTIA TYPE()
# FUNCTIA - o logica de cod predefinita
#Functia TYPE returneaza tipul de date ale unei variabile si nu numai

# x = 5
# print(type(x))
# y = "Hello"
# print(type(y))
# z = [1,3,9]
# print(type(z))

#TYPE CASTING - transforma o valoare dintr-un tip de date in altul
#TYPE CASTING este adesea necesar cand se lucreaza cu diferite tipuri de date sau atunci cand se doreste
#sa ne asiguram ca o valoare este de un anumit tip de date.
#Castingul trebuie sa fie compatibil. Nu se poate face conversie din sttring in int pt ca va returna ERR
#mai jos incercam sa facem type casting dintr-o val string in tip int
# nume = 'cinci'
# int_nume = int(nume)
# print(int_nume)

#mai jos incercam sa facem type casting dintr-o val boolean in int. True devine 1, False devine 0
# x = True
# y = int(x)
# print(f"Am fortat variabila sa fie in {y}")
# d = 4.5678
# f= int(d)
# print(f"Valoare fara zecimale este valoarea {f}")
#
# nume1 = "Ioana"
# an = 1990
# salariu = 9999.99
# angajat = True
#
# print(f"Ma numesc {nume1} sunt nascuta in anul {an} si sunt angajata {angajat}"
#       f" si am salariul {salariu}")
#
#
# numele_meu = 'Cristina'
# print('Numele meu este', numele_meu)
#
# nume10 = 'Ana'
# ani=25
# print('Nume', nume10, 'Varsta', ani)

# Functia INPUT
# Functia Input este folosita pt a citi o linie de intrare de la tastatura/utilizator si ea returneaza o vcaloare
# citita sub forma de sir de caractere. o folosim pt a interactiona cu utilizatorii pt a obtine date de intrare
# in timpul executarii codului
# nume_utilizator = input("Va rugam introduceti numele dvs: ")
# print(f"Salut {nume_utilizator} ")

prenume= input('Va rugam sa va introduceti prenumele dvs: \n') #\n pt a cobori o linie
nume = input('Va rugam sa va introduceti numele dvs: \n')
print(f"Buna! Numele tau complet este: {prenume} {nume}")

