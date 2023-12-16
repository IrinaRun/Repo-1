# Structurile de date reprez adrese de memorie care pot stoca mai multe valori
# exista 4 struct de date: liste,seturi, tupluri, dictionare

#1. LISTELE - sunt structuri care permit stocarea si manipularea unui nr variabil de elemente. Listele sunt ordonate si
#indexate (indexarea incepe de la 0). listele sunt mutabile, ceea ce inseamna ca pot fi modificate(se pot adauga,
#sterge si modifica elementele) dupa ce au fost create. Listele sunt definite prin incadrarea elementelor intre
#paranteze drepte
#lista permite elemente duplicate
#Adaugarea elementelor se poate face la finalul listei cu functia Append(), dar se poate face adaugare si in interioruk
#listei cu functia Insert().Stergera elementelor din lista se face atat prin metoda Pop(se sterge ultimul element din
# lista) cat si prin functia Del(sterge un element de la un index precizat)

lista = [1,2,3,'patru',5.1,True]
print(f'Aceasta este lista mea {lista}')
print(f'Tipul listei este : {type(lista)}')

# Indexarea listelor
primul_element = lista[0]
print(primul_element)
al2lea_element = lista[1]
print(al2lea_element)

#Sliceing lista = permite extragerea unei portiuni din lista
print(f'Portiunea din lista este {lista[1:3]}')
print(f'A doua portiune din lista este {lista[3:5]}')

#Adaugare de elemente
lista.append(3)
print(f'Am adaugat un nou element, lista arata asa {lista}')
lista.insert(1,9)
print(lista)

#Stergere de elemente
lista.pop()
print(f'am sters un element prin metoda pop. elementul sters este  {lista.pop()}')
lista.append(10)
print(lista)
del lista[4]
print(f'asa arata lista dupa ce am fol functia del {lista}')
lista.append(True)
lista.append(3)
print(lista)
lista.remove(5.1)
print(f'asa arata lista cu metoda remove {lista}')

#Concatenare de doua liste = se face cu operatorul '+'
lista1 = [1,2,3]
lista2 = [4,5,6]
lista_concatenata = lista1+lista2
print(f'lista concatenata este: {lista_concatenata}')

#Extindere de lista = se fol metoda extend()
lista1.extend(lista2)
print(f'Am extins lista1 cu elem din lista2. Lista arata asa: {lista1}')

#Metode si functii pt liste
print(f'Am folosit functia len. Lista are lungimea de: {len(lista)} elemente')
print(lista)
print(f'De cate ori apare cifra 3 in lista? {lista.count(3)}')
print(f'Lista sortata este urmatoarea: {sorted(lista)}')#sortare ascendenta
lista.sort(reverse=True)#sortare descendenta
print(F'Lista sortata descendent este: {lista}')
print(f'Indexul primei cifre 3 gasite in lista este: {lista.index(3)}')
print(f'Cifra cea mai mare din lista este: {max(lista)}')
print(f'Cifra cea mai mica din lista este: {max(lista)}')

# SETURI - sunt colectii de date neordonate si permit doar date unice. Sunt asemanatoare cu listele, diferenta este ca
#seturile nu sunt ordonate adica indexate si nu permit elemente duplicate. Faptul ca nu sunt ordonate, nu ne permite sa
#accesam elemente pe baza de index. Nu putem adauga elemente la o anumita pozitie si nu ne lasa sa extragem un singur
#element din set. Acesta poate fi gestionat doar in intregime. Seturile sunt definite de paranteze "{}".
# Pentru ca seturile nu pot contine duplicate, orice incercare de a adauga elemente duplicate va fi ignorata (nu va
#returna eroare, dar nici nu va adauga element). Permit toate tipurile de date.
set1 = {1,'sapte',2,9,3.23,True}
print(set1)#le printeaza aleatoriu

#existenta unui element in set
exista =3 in set1
print(exista)
print(f'Exista elem 3 in set? {3 in set1}')

#adaugare element nou
set1.add(47)
print(set1)
print(f'asa arata setul meu cu adaugare {set1}')

#stergere de element
set1.remove(47)
print(f'setul meu dupa stergere element arata asa: {set1}')

#unire de seturi
set2 = {1,2,3}
set3 = {3,4,5}
unire = set2.union(set3)
print(f'nou set de unire va fi: {unire}')

#Intersectia seturilor
intersectie= set2.intersection(set3)
print(f'Intersectia celor 2 seturi este: {intersectie}')

#Diferenta seturilor
diferenta = set2.difference(set3)
print(f'diferenta seturilor este: {diferenta}')

# TUPLE
# Sunt structuri de date asemanatoare cu listele, diferenta este ca tuplele sunt imutabile, adica nu pot fi modificate
# dupa ce au fost create. Asta inseamna ca putem face orice operatie de accesare a elementelor, dar nu putem face
# operatii de adaugare, stergere sau modificare. Tuplele sunt definite utilizand paranteze rotunde '()', sau daca
#contin un sg element, tb sa punem virgula ',' dupa acel element deoarece sistemul ar vedea tupla ca o variabila
# cu valoare de tip integer.

#tupla cu mai multe elemente
tupla1 = (1,2,3,'patru')
print(tupla1)
# tupla cu un sg element
tupla2 = (5,)
print(type(tupla2))
#tupla fara paranteze(tupla packing)
tupla3 = 1,2,3
print(tupla3)
#tupla goala
tupla_goala = ()
print(tupla_goala)

# Indexarea tuplelor
primul_element = tupla1[0]
print(primul_element)
print(f'Primul element din tupla este: {tupla1[0]}') # metoda recomandata pt economisire de cod

# Sliceing tupla
print(f'Aceasta este o portiune din tupla: {tupla1[0:3]}')

# Iterare tuple = se refera la procesul de parcurgere a elementelor dintr-o lista/tupla/si de caractere si prelucrarrea
#fiecarui element intr-un mod specific. Iterarea este realizata cu ajutorul buclelor, de ex bucla 'FOR'
for x in tupla1:
    print(x) # x este o variabila care ia valoarea fiec element dim tupla in timpul iterarii

# Despachetare tuple (Tuple Unpacking) - este procesul de asignare a valorilor dintr-o tupla unor variabile individuale
# Acest proces ajuta la lucrul cu tuplele in diferite contexte. Pentru a despacheta se fol o tupla pe partea dreapta a
# unei instructiuni de atribuire si de a asigna valorile la variabila individuala pe partea stanga.

a,b,c,d = tupla1 # a=1, b=2, c=3, d=patru
print(f'Variabila "d"  are urmatoarea valoare : "{d}"')
print(f'Variabila "c"  are urmatoarea valoare : "{c}"')

# DICTIONARE
# Dictionarele sunt structuri de date flexibile si ordonate care asociaza chei unice cu valorile corespunzatoare
# Dictionarele sunt mutabile, adica putem adauga, sterge sau modifica valori din interiorul unui dictionar. Cheile unui
#dictionar trebuie sa fie unice, dar valorile se pot repeta.
# Dictionarele sunt definite utilizand acolade '{}' si au format cheie:valoare
dictionar1 = {"cheie1":10,
              "cheie2":"Cristina",
              "cheie3":3.14}
print(dictionar1)
print(type(dictionar1))

# Dictionar gol
dictionar_gol = {}
print(dictionar_gol)

#Adaugare elemente in dictionar
dictionar1["cheie4"] = "John"
print(dictionar1)
#Accesare valori prin intermediul unei chei
print(f'Aceasta este valoarea cheii doi din dictionar: {dictionar1["cheie2"]} ')

#Iterare prin dictionare
for cheie,valoare in dictionar1.items():
    print(f'Cheia este: {cheie}, Valoarea este: {valoare}')

#apeland metoda items() asupra dictionarului, se returneaza o secventa de tupluri de genul:(("cheie1",10),
# ("cheie2",Cristina))

# Verificare existenteoi unei chei
print(f'Exista "cheia3" in dictionar? {"cheie3" in dictionar1}')

#Stergera unui element prin intermediul cheii
# del dictionar1["cheie1"] #stergere prin metoda del
# print(dictionar1)
# dictionar1.pop("cheie4") #stergere prin metoda pop
# print(dictionar1)

#actualizarea valorilor unei chei
dictionar1["cheie2"] = "valoare_noua" #actualizare fol operatorul de atribuire "="
print(dictionar1)
dictionar1.update({"cheie3":"valoare_cu_update"}) #actualizare cu metoda update
print(dictionar1)
dictionar1.update({"cheia3":"adaugare_element_prin_update"}) # se va face adaugare de cheie noua pt ca in dictionar
                                                # nu exista nici o cheie cu denumirea"cheia3"
print(dictionar1)

# Dictionare imbricate = dictionar in dictionar, mai sunt cunoscute si ca dictionare embedde - 2D - nested
jucatori_de_fotbal ={
    "Ducadam":{"varsta":70,"numar_tricou":10,"numar_meciuri":50},
    "Nicolita" :{"varsta":45,"numar_tricou":7,
                  "titluri_campion":{"balon_aur":2016,"jucatorul_anului":2010, "an_castig":[2016,2010,2020]},
                    "numar_meciuri":30}
}
print(f'Nicolita a fost jucatorul anului in:{jucatori_de_fotbal["Nicolita"]["titluri_campion"]["jucatorul_anului"]}')
print(f'Al 2lea an in care a castigat Nicolita este in anul: {jucatori_de_fotbal["Nicolita"]["titluri_campion"]["an_castig"][1]}')
