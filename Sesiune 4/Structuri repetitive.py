#STRUCTURI REPOETITIVE
#Structurile repetitive sunt: while, for, for each(cele mai utilizate sunt while si for)
#Structurile repetitive sunt utilizate pt a executa aceeasi secventa de instructiuni de mai multe ori, pana cand o
#anumita conditie nu mai este indeplinita

# 1. WHILE
# este o structura repetitiva care executa un set de instructiuni atata timp cat o conditie este adevarata.
# Se fol atunci cand nu stim exact momentul in care conditita nu mai este adevarata.
# Componentele unui while sunt:
#a) o variabila de control (nu este obligatoriu)
#b)inceputul while-ului marcat prin cuvantul WHILE
#c)conditia de evaluare(cea pe baza careia se decide daca se mai trece o data prin while sau nu)
#d)separatorul intre cond de evaluare si corpul while-ului ":"
#e)corpul while-ului (o serie de instructiuni care se vor repeta)

#ex.1
suma = 0
i = 1 # o variabila de iteratie

while i>=1 and i<=10:
    suma = suma+i
    print(f'Am adunat numarul {i}')
    i+=1

#ex.2
# numar = 1
# while numar<=5:
#     print(numar)
#     numar+=1

#ex.3 Vreau sa ii printez pe cei 101 dalmatieni
# nr_dalmatieni = 1
# while nr_dalmatieni<=101:
#     print(f'Dalmatianul curent are numarul {nr_dalmatieni}')
#     nr_dalmatieni+=1

# 2. FOR
# este o structura repetitiva care executa un set de instructiuni pe baza unui range si care se fol atunci cand stim
#exact de cate ori vrem sa parcurgem un anumit set de instructiuni. Se bazeaza pe o variabila de iteratie care va stoca
#rand pe rand valoarea din range
# Componentele unui FOR:
#a)Inceputul For-ului marcat de cuvantul "FOR"
#b)variabila de iteratie care va stoca indexul in range
#c)range-ul sau structura repetitiva care este parcursa
#d) separatorul de range ":"
#e)corpul For-ului adica o serie de instructiuni

#Ex.1 = sa calculez suma nr de la 1 la 10
suma = 0
for i in range(1,11):
    suma+=i
print(f'Valoarea curenta a sumei este: {suma}')

#Iterare printr-o lista
fructe = ['mar','banana','cirese']
for fruct in fructe:
    print(fruct)

#ex.3 Vreau sa ii printez pe cei 101 dalmatieni
nr_dalmatieni = 1
for i in range(1,102):
    print(f'Dalmatianul curent are nr {i}')

# 3. FOR EACH
# diferenta intre For si For each este aceea ca in cazul for-ului variabila de iteratie stocheaza indexul curent al
#elementului din lista, in timp ce la For each variabila de iteratie stocheaza valoarea curenta a elementului aflat la
#un anumit index

#ex.1
# lista = [1,2,3,4]
# for element in lista:
#     print(element)

# In concluzie, For este mai util atunci cand vrem sa modificam o valoare din lista pt ca se acceseaza pe baza de index.
#Fo reach este mai util atunci cand vrems a scoatem un element din lista, pt a nu se calcula lungimea listei.

#METODE DE CONTROL AL STRUCTURILOR REPETITIVE
# Exista cateva metode de control al struct repetitive(bucle), cum ar fi: BREAK, CONTINUE si ELSE in buclele For si
#Wile

# a) BREAK = incheie executia tuturor iteratiilor curente si viitoare in bucla

#ex.
for i in range(1,11):
    if i==5:
        break
    print(i)

#b) CONTINUE = sare peste iteratia curenta, dar executa iteratia viitoare

#ex.
for i in range(1,11):
    if i==5:
        continue
    print(i)

#c) ELSE in bucle For =  este executata atunci cand bucla se termina normal(fara a fi intrerupta de Break)

# ex.
for i in range(1,6):
    print(i)
else:
    print(f'Bucla a fost parcursa complet')

#d) ELSE in bucla While = este executata atunci cand conditia din bucla devine falsa

# ex.
i = 1
while i <=5:
    print(i)
    i+=1
else:
    print(f'Conditia nu mai este adevarata')

#ex Vrem sa parcurgem o lista de masini si sa alegem din lista doar daca este mercedes
lista_masini = ['audi','skoda','ferrari','mercedes','trabant','dacia','mustang','tesla']
i = 0
while i<len(lista_masini):
    if lista_masini[i] =='mercedes':
        print(f'Am gasit masina dvs ')
        break
    i+=1
