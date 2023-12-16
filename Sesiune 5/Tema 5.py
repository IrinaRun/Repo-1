
import datetime
import math


#Ex.1
def suma():
    a=int(input(f'Introduceti nr a: \n'))
    b =int(input(f'Introduceti nr b: \n'))
    rezultat= a+b
    print(f'Suma este: {rezultat}')
suma()


#ex.2
def verificare(a):
    rezultat=a%2
    return rezultat
rezultat=verificare(5)
if rezultat==0:
    print(f'TRUE')
else:
    print(f'FALSE')

#ex.3
def numaratoare(a):
    numar_caractere=len(a)
    return numar_caractere
nr_caractere= numaratoare('Runcanu Irina')
print(f'Numarul total de caractere al numelui este: {nr_caractere}')

#ex.4
def aria(a,b):
    rezultat = a*b
    return rezultat
aria_dreptunghi= aria(4,6)
print(f'Aria dreptunghiului este {aria_dreptunghi}')

#ex.5
def aria(a):
    return math.pi*a**2
rezultat = aria(5)
print(f'aria cercului este {rezultat}')

#ex.6
def verificare_caracter(s):
        print(f'Textul este', s)
        litera= input('Introduceti o litera:\n')
        if litera in s:
            print("TRUE")
        else:
            print('False')
verificare_caracter("Mama merge la piata")

#ex.7
def numarare(a):
    dictionar = {"Upper_case":0,"Lower_case":0}
    for litera in a:
        if litera.islower():
            dictionar["Lower_case"]+=1
        elif litera.isupper():
            dictionar["Upper_case"]+=1
        else:
            pass
    print(f'Textul este:',a)
    print(f'Nr litere mari:' ,dictionar["Upper_case"])
    print(f'Nr litere mici:' ,dictionar["Lower_case"])
numarare("Maria Mirabela")

#Ex.8
def verif_numere(nr,lista):
    if nr==len(lista):
        return
    if lista[nr]>=0:
        print(lista[nr],end = ' ')
    verif_numere(nr+1,lista)

lista =[1,-5,3,-2,5]
verif_numere(0,lista)


#Ex.9
def comparare(a,b):
    if a>b:
        print(f'Primul nr este mai mare decat al 2 lea nr')
    elif a<b:
        print(f'Primul nr este mai mic decat al 2 lea nr')
    else:
        print(f'Cele 2 nr sunt egale')

rezult =comparare(5,5)
print(rezult)

#Ex.10
def adaugare_nr(a,nr):
    a=int()
    if a in nr:
        print(f'nu am adaugat numărul în set. Acesta există deja')
        print(f'FALSE')
        return
    else:
        nr.add(a)
        print(f'am adaugat numărul nou în set')
        print(f'TRUE')
        return
    a+=1

adaugare_nr(2,{5,9,3})

#ex.11
from calendar import monthrange

def nr_zile_luna(an,luna):
    return monthrange(an,luna)[1]

print(f'Nr de zile ale lunii este: ',nr_zile_luna(2023,6))

#Ex.12
def calculator(x,y):
    adunare =x+y
    print(f'Suma este:',adunare)
    scadere = x-y
    print(f'Diferenta este:' ,scadere)
    produs = x*y
    print(f'Produsul este:' ,produs)
    impartire = x/y
    print(f'Rezult impartirii este:', impartire)

rezul= calculator(10,3)
print(rezul)

#Ex.13
def dictionar_nr(nr_aparitii):
    cifra =len(nr_aparitii)
    dictionar=dict()
    k=0
    for i in range(0,cifra):
        aparitii =1
        for j in range(0, cifra):
            if (i != j) and (nr_aparitii[i] == nr_aparitii[j]):
                aparitii += 1
        dictionar[k]=(nr_aparitii[i],aparitii)
        k+=1
    return dictionar

rezul=dictionar_nr((1,4,1,7,9,7))
print(rezul)

#Ex.14
def nr_max(a,b,c):
    rezul= max(a,b,c)
    return rezul
nr_mare = nr_max(7,10,5)
print(f'Nr cel mai mare este:', nr_mare)

#Ex.15
def suma_Gauss(n):
    rezultat = n*(n+1)/2
    return rezultat
suma=suma_Gauss(3)
print(suma)

#Ex.16.
def lista_comuna(lista1,lista2):
    i =lista1.intersection(lista2)
    return i
rez=lista_comuna({1,2,2,4,5,6},{2,2,5,6})
print(rez)


#Ex.17
def reduceri(pret,reducere):
    if reducere<pret:
        rezultat=pret-(pret*reducere/100)
        return rezultat
    else:
        print(f'Reducere invalida')
calcul= reduceri(100,110)
print(calcul)










