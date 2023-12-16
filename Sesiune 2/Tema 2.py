#VARIABILE
#Ex.1 Variabila este o adresa de memorie care stocheaza valori, aceste valori putand fi modificate pe parcussul executiei
#Ex.2
import numbers

variabila1 = 'Hello World!' #variabila de tip string
variabila2 = 5 #variabila de tip integer
variabila3 = 23.45 #variabila de tip float
variabila4 = False # variabila de tip boolean
#ex.3
print(type(variabila1))
print(type(variabila2))
print(type(variabila3))
print(type(variabila4))
#ex.4
print(round(variabila3))
variabila3 = round(variabila3)
print(type(variabila3))
#ex5
# int_variabila1 = int(variabila1)
# print(int_variabila1) # err deoarece nu se poate converti string in int
#ex.6
bool_variabila4 = int(variabila4)
print(bool_variabila4) # primeste val 0
#ex.7
variabila4 = True
bool_variabila4 = int(variabila4)
print(bool_variabila4)

#PRINT
#ex.1
print(variabila1)
print(f'Valoarea variabilei de tip int este: {variabila2}')
print(f'Valoarea variabilei de tip float este: {variabila3}')
print(f'Valoarea variabilei de tip boolean este: {variabila4}')
#ex.2
# nume = input('Va rugam introduceti numele dvs: \n')
# prenume = input('Va rugam introduceti prenumele dvs: \n')
# print(f'Numele complet are {len(nume + prenume)} caractere')
#ex.3
# lungime = int(input('Va rugam introduceti lungimea dreptunghiului: \n'))
# latime = int(input('Va rugam introduceti latimea dreptunghiului: \n'))
# print(f'Aria dreptunghiului este: {lungime*latime}')
#ex.4
text = 'Coral is either the stupidest animal or the smartest rock'
print(text.count('the'))
#ex.5
print(text.replace('the','THE'))
#ex.6
print(text.isnumeric())


#Exercitii de dificultate medie
#ex.1
# text = input(str('Introduceti un sir de caractere de tip string cu lungime impara \n'))
# print(text[len(text)//2])
#ex.3
# text1 = input(str('Introduceti un string \n'))
# print(text1.split(' '))
#ex.4
text1 = input(str('Introduceti un string \n'))
print(text1[0])
print(text1.replace('a','A'))
print(text1.index(sub[start[end]]))

#ex.5
user = input('Va rugam introduceti user-ul dvs:\n')
parola = input('Va rugam introduceti parola dvs: \n')
print(f'Parola pt user {user} este {parola} si are {len(parola)} caractere')

