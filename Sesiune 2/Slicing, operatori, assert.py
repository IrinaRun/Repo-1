#String Index = un sir de caractere este ordonat in sensul in care orice caracter din acel sir are o pozitie specifica
#numita index. In orice string, indexul porneste de la pozitia 0.
list = [1,2,3,4]
# elementul cu valoarea 1 are index 0
# elementul cu valoarea 2 are index 1
# elementul cu valoarea 3 are index 2

element = list[2] # accesarea elementului cu index 2 va returna cifra 3
print(f'Elementul cu index 2 este : {element}')

# Indexarea negativa = se foloseste pt a accesa elemente in sens invers, incepand de la -1 care reprezinta ultimul
# element din sir, -2 care inseamna penultiumul element, etc...
last_element = list[-1] # accesam ultimul elem din lista si va returna valoarea 4
print(f'Ultimul element din lista este: {last_element}')

# String lenght = il fol daca vrem sa aflam cate caractere are un string. Ne folosim de functia length (len)
my_text = 'Hello world!'
# lungime = len(my_text)
# print(f'Variabila mea are lungimea de: {lungime} caractere')
print(f'Variabila mea are {len(my_text)} caractere') # prin metoda folosirii functiilor direct in print se face economie
                                                    # de cod
print(f'Lista mea are o lungime de {len(list)} caractere') # la extragerea lungimii din liste sau dictionare nu va
                                                           # numara virgula si spatiile, asa cum face la stringuri

# String slicing = este o modalitate prin care putem extrage doar o parte dintr-un string
# Putem sa extragem atat intregul sir de caractere, cat si portiuni ori de la inceput pana la o anumita pozitie,
# de la o anumita pozitie pana la sfarsit sau un set de caractere din interior.
# Structura unui slicing este de forma: [pozitie_de_start:pozitie_de_end:steps]
# ATENTIE!!! Pozitia_de_end nu se ia in considerare ca si limita finala. De ex daca ne intereseaza sa extragem
# caracterele de la poz 3 la poz 8 , vom scrie slicingul [3:9:1]
# pozitie_de_start = poz de inceput a slicingului(in mod implicit index 0)
# pozitie_de_end = poz de final(nu e luat in considerare la calcul)
# step = pasul de parcurs ( fiecare al catelea caracter este luat in considerare)
# ':' = este separator de elemente
# In mod implicit, pozitia_de_inceput este 0,poz_de_final este ultimul caracter si pasul este 1

str_exemplu = 'Ana are mere'
print(f'Primele 3 caractere din variabila noastra sunt: "{str_exemplu[0:3]}"')
print(f'Ultimul caracter din variabila noastra este: "{str_exemplu[-1]}"')
print(f'Ultimele 3 caractere din variabila sunt: "{str_exemplu[-3:]}"')# pt a obtine ultimele 3 caractere ne fol de" -3:"
                                                                        #pt a incepe sa citeasca de la final 3 caractere

poezie = 'Ana are mere si este fericita cu ele si vrea sa mearga acasa.'
#ex 1: Extrageti toate caracterle de la incep pana la sf cu mentionarea pasului
print(poezie[0:len(poezie):1]) #folosim functia len(poezie) pt a determina lungimea sirului si apoi utilizam aceasta
                              # lungime pt a accesa toate caracterele din sir si sa facem sliceing

#ex 2: Extragem toate caracterele de la inceput pana la sfarsit, folosind pozitia de inceput si sf implicita
print(poezie[:])#va returna acelasi lucru ca mai sus, doar ca nu specificam nici pasul, nici startul, nici end-ul

#ex 3: Extrage toate caracterele de la inceput pana la sfarsit, dar sa imi afiseze caracterele din 2 in 2
print(poezie[::2])

#ex 4: Extragem toate caracterele de la poz 5 pana la poz 10
print(poezie[5:10])

#ex 5: extrage ultimele 3 caractere
print(poezie[-3:])

#ex 6: printeaza stringul in ordine inversa
print(poezie[::-1])

# Metoda STRING = metoda care poate fi folosita pt interactiunea cu stringurile
print(poezie.lower())#va transforma toate caracterle in litere mici
print(poezie.upper())#va transforma toate caracterele in litere mari
print(poezie.count('si'))
print(poezie.count('e'))#numaram de cate ori apare litera"e"
print(poezie.islower())#verif ca toate caracterele sunt mici - raspuns de tip boolean

# Metoda SPLIT = este folosita pt a desparti un string intr-o lista de sub-siruri
# Sintaxa este string_subsir = string.split(delimiter)
    #string este stringul initial pe care ne dorim sa-l impartim
    #delimiter = caracterul sau sirul de caractere pe baza caruia facem impartirea
    #string_subsir = este stringul care va rezulta
# In mod implicit se va face split dupa spatii in cazul in care nu dam nici un argument

text = 'Ana are pere si mere'
print(f'Asa impartim sirul de caractere dupa spatii {text.split()}')
data = '22-11-2023'
print(f'Asa facem split cu argument {data.split("-")}')

# Metoda REPLACE = este fol pt a inlocui toate caracterele unui subsir cu alt subsir de caractere
# Sintaxa_noua = string_initial.replace(subsir_vechi,subsir_nou, nr_inlocuiri)
    # string_intial= sir initial de caractere in care facem inlocuirea
    #subsir_vechi = caracterele pe care dorim sa le inlocuim
    #subsir_nou = caracterele cu care vom inlocui subsirul vechi
    #nr_inlocuiri (optional)= specifica nr max de inlocuiri

original = 'Ana are mere. Ana este fericita'
nou = original.replace('Ana','Maria')
print(original)
print(nou)

# Metodele isDeciaml, isNumeric, isDigit = au rezultat de tip boolean (true/false)
# a) isDecimal = verif daca toate caracterele sunt cifre zecimale(0-9)
numar = '123456'
print(f'Este un nr zecimal? "{numar.isdecimal()}"')

# b) isNumeric = verif daca toarte caracterele din sir sunt caractere numerice inclusiv cele care sunt cifre speciale
numar1 = '2.5v10'
print(f'Este de tip numeric "{numar1.isnumeric()}"')

# c) isDigit = verif daca toate caracterele din sir sunt cifre de la 0-9, dar include si alte caractere numerice de tip
#binar,octal
numar2 = '123456'
print(f'Este de tip digit "{numar2.isdigit()}"')

# OPERATORI ARITMETICI = sunt utilizati pt a efectua operatii matematice asupra numerelor
# 1. Operatorul de adunare '+' = adauga 2 sau mai multe nr
a = 5+3 # variabila a va primi valoarea 8

# 2. Operatori de scadere '-' = scade un nr din altul
b = 7-2 # variabila va primi valoarea 5

# 3. Operatorul de inmultire '*'
c = 4*6 # variabila va primi valoarea 24

# 4. Operatorul de impartire '/' = returneaza o val de tip float ( cu virgula)
d = 10/3 # variabila va primi valoarea 3.3333(un nr float)

# 5. Operatorul de impartire intreaga '//' = returneaza partea intreaga a rezultatului
e = 10//3 # variabila va primi valoarea 3

# 6. Operatorul de rest '%'
f = 10%3 # variabila va primi valoarea 1 deoarece restul impartirii lui 10 la 3 este 1

# 7. Operatorul de putere '**' - ridica un nr la putere
g = 2**3 # variabila va primi valoarea 8 deoarece 2 la puterea 3 este 8

# OPERATORI DE ATRIBUIRE - sunt utilizati pt a atribui o valoarea unei variabile
# 1.Operatori de atribuire simplu '=' - atribuie o val unei variabile
x = 5 #variabilei 'x' i se atribuie val 5
# 2. Operator de atribuire cu adaugare '+=' adauga o valoarea la variabila existenta si actualizeaza variabila cu
 # noul rezultat
a = 10
a+= 5 # este echivalent a=a+5
print(a)
# 3. Operatorul de atribuire cu scadere '-='
b=8
b-=5 # este echivalent b=b-5 = 3
print(b)
# 4. Operatorul de atribuire cu inmultire '*='
c = 4
c*=2  # echivalent c=c*2
print(c)
# 5. Operatorul de atribuire cu impartire '/=' imparte o var existenta la o val si actualiz var cu rezult(vom avea un
 #rezult de tip float)
d=20
d/=4 # echivalent d = d/4
d//=4 #vom avea rezult fara zecimale
print(d)
# 6. Operator de atribuire cu rest '%=' calculeaza restul impartirii variabilei la o anumita val si actualiz variabila
 #cu rezultatul
e = 17
e%= 5
print(e)

# OPERATORII DE COMPARARE = fol pt a compara 2 val si a determina rel dintre ele, rezultatele sunt de tip boolean
# 1. Operatorul egal '==' verifica daca 2 valori sunt egale
a = 5
b = 7
rezultat = (a==b)
print(rezultat)
# 2. Operatorul diferit '!=' verif daca 2 valori nu sunt egale
x = 10
y = 1
rezultat = (x!=y)
print(rezultat)
# 3. Operatorul mai mic decat '<' verif daca o val este mai mica decat alta
p = 3
q = 6
rezultat = (p<q)
print(rezultat)
# 4. Operatorul mai mare '>'
# 5. Operatorul de mai mic sau egal '<='
# 6. Operatorul de mai mare sau egal '>='

# OPERATORI LOGICI
# Prioritatea operatorilor logici este NOT, AND, OR
# 1. Operatorul AND = returneaza TRUE daca ambele expresii/valori sunt adevarate
numar = 10
if numar > 15 and numar <=20 :
    print('Numarul este mai mare decat 15 si mai mic sau egal cu 20 ')
else :
    print('Numarul nu satisface conditia')

x = 10
rezultat_and = x>3 and x<13
print(rezultat_and)

# 2. Operatorul OR = returneaza TRUE daca cel putin una din expresii/valori este adevarata
x = 9
rezultat_or = x>5 or x<8
print(rezultat_or)

# 3. Operatorul NOT = returneaza inversul valorii Boolean a unei variabile
x = True
rezultat_not = not x
print(rezultat_not)

#ASSERT - este fol pt a verifica daca o anumita conditie este adevarata. Genereaza o exceptie de tip Assertion Error
#in cazul in care conditia nu este adevarata.
#Assertul este f des utilizat in testarea automata deoarece verifica daca conditiile sunt indeplinite .
#Assertul are urmatoarele componente: pe prima pozitie valoarea pe care o comparam
                                    # pe a doua poz val cu care comparam, cele 2 valori sunt separate de operatorul de
                                    #comparare '=='
                                    # (optional) pe ultima poz un mesaj care sa fie returnat in cazul in care cele 2 valori sunt
                                    #egale
x = 5
assert x>1,'Valoarea lui x trebuie sa fie mai mare decat 1'
print('x este mai mare decat 1!')

# STRUCTURI ALTERNATIVE IF, ELSE, ELIF
#Sunt utilizate pentru a crea ramificatii in cod in functie de conditii. Aceste structuri sunt varianta automata a
#metodei de testare manuala Decision Coverage
x=1
if x>5:
    print('x este mai mare decat 5')
else:
    print('x nu este mai mare decat 5')

nota = 75
if nota>=90:
    print('Nota este A')
elif 80<=nota<90:
    print('Nota este B')
elif 70<=nota<80:
    print('Nota este C')
else:
    print('Nota este sub C')

numar =int(input('Introduceti un numar: \n'))
if numar >0:
    rezultat = 'Numarul este pozitiv'
elif numar< 0:
    rezultat = 'Numarul este negativ'
else:
    rezultat = 'Numar este zero'
assert rezultat == 'Numarul este pozitiv' or rezultat == 'Numarul este negativ' or rezultat =='Numarul este zero'
print(rezultat)

numar1 = int(input('Va rugam sa introduceti nr: \n'))
if numar1 % 2 == 0:
    print('nr par')
else:
    print('nr impar')








