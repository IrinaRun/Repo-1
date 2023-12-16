#Ex.1 If else= struct alternativa care este folosita pentru a crea o ramificatie in cod in functie de conditii
# prestabilite.

# Ex.2
# x = int(input('Introduceti numarul x: \n'))
# if x >0:
#     print(f'x este numar natural')
# else:
#     print('x nu este numar natural')

# Ex.3
# if x>0:
#     print(f'Numarul este pozitiv')
# elif x<0:
#     print(f'Numarul este negativ')
# else:
#     print(f'Numarul este neutru')

# Ex.4
# if -2<=x<+13:
#     print(f'Numarul este in intervalul selectat')
# else:
#     print(f'Numarul este in afara intervalului selectat')

# Ex.5
# if not 5<x<27:
#     print(f'Numarul nu este in intervalul selectat')
# else:
#     print(f'Numarul este in interval')

# Ex.6
# y = int(input('Introduceti numarul y:\n'))
# if x==y:
#     print(f'Numerele x si y sunt egale.')
# elif x>y:
#     print(f'Numarul x este mai mare decat numarul y.')
# else:
#     print(f'Numarul x este mai mic decat numarul y.')

# Ex.7
# z = int(input('Introduceti numarul z: \n'))
# if x==y==z:
#     print(f'Triunghiul este echilateral')
# elif x==y or x==z or y==z:
#     print(f'Triunghiul este isoscel')
# else:
#     print(f'Triunghiul este oarecare')

# Ex.8
# litera= str(input('Introduceti o litera: \n'))
# lista = ['a','e','i','o','u','A','E','I','O','U']
# if lista.__contains__((litera) or (litera.upper())):
#     print(f'Litera introdusa este vocala')
# else:
#     print(f'Litera introdusa este consoana')

# Exercitii dificultate medie
# Ex.1
# clasa =str(input(f'Calatoriti la clasa 1? (da/nu) \n'))
# varsta = int(input('Introduceti varsta dvs: \n'))
# copii = int(input('Introduceti nr de copii: \n'))
# luna_calatorie = str(input('Introduceti luna calatoriei: \n'))
# luna_iarna = ['decembrie','ianuarie','februarie']
# if clasa == 'da' and varsta>65 and luna_iarna.__contains__(luna_calatorie):
#     print(f'Primiti o reducere de (15% +10%) si se aplica taxa lux de 3%')
# elif varsta>65 and luna_iarna.__contains__(luna_calatorie):
#     print(f'Primiti o reducere de 15% +10% si se aplica taxa gestiune de 1%')
# elif clasa =='da'and varsta>65:
#     print(f'Primiti o reducere de 15% si se aplica taxa de lux de 3%')
# elif varsta >65:
#     print(f'Reducere 15% si se aplica taxa gestiune 1%')
# elif clasa == 'da' and copii >0 and luna_iarna.__contains__(luna_calatorie):
#     print(f'Primiti o reducere de 10%+10% si se aplica taxa lux de 3%' )
# elif copii>0 and luna_iarna.__contains__(luna_calatorie):
#     print(f'Primiti o reducere de 10%+10% si se aplica taxa gestiune de 1%')
# elif clasa == 'da' and luna_iarna.__contains__(luna_calatorie):
#     print(f'Primiti o reducere de 10% si se aplica taxa lux de 3%')
# else:
#     print(f'Reducere 10% si se aplica taxa gestiune 1%')

# Ex.2
# tip_client = str(input('Completati daca sunteti client en-gross/en-detail?  \n'))
# metoda_plata = str(input('Platiti ramburs cash? da/nu \n'))
# bucati_comandate = int(input('Introduceti nr bucati comandate \n'))
# if tip_client.lower() == 'en-gross' and metoda_plata.lower() == 'da' and bucati_comandate>50:
#     print(f'Reducere 2%+2%+2% la toate comenzile')
# elif tip_client.lower() == 'en-gross'and bucati_comandate>50:
#     print(f'Reducere 2%+2% la toate comenzile')
# elif tip_client.lower() == 'en-gross':
#     print(f'Reducere 2% la toate comenzile')
# elif metoda_plata.lower() =='da' and bucati_comandate>50:
#     print(f'Reducere 2%+2% la toate comenzile')
# elif metoda_plata.lower() =='da':
#     print(f'Reducere 2% la toate comenzile cash')
# else:
#     print(f'Nu se acorda nici o reducere')

# Ex.3
# film_preferat = str('The Ghost')
# film_ales = str(input(f'Introduceti un film care v-a placut \n'))
# if film_ales.lower() == film_preferat.lower():
#     print(f'Acesta este filmul meu preferat')
# else:
#     print(f'Din pacate nu este filmul meu preferat')

# Ex.4
database_url = str('jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC')
print(database_url.split())
