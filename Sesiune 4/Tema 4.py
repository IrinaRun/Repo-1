#ex.1
#ciclul For
lista_prezenta = ["Ivan Cristina","Dogaru Valentin","Runcanu Irina","Moraru Alexandru","Borbey Robert","Raduleanu Serban"]
nr_persoane = len(lista_prezenta)
i = 0
for i in range(0,nr_persoane):
    print(lista_prezenta[i])
#ciclul While
while i < nr_persoane :
    print(f"{lista_prezenta[i]}")
    i += 1
#ciclul For each
for element in lista_prezenta:
    print(element)


#DICTIONARE
#ex.1
fotbalisti_pe_echipe={
				"Barcelona":{
							"Dica":{"Nume complet":"Nicolae Dica",
									 "Varsta":45,
								 	"Numar Tricou":10
								},
							"Banel":{"Nume complet":"Banel Nicolita",
								 	"Varsta":47,
									 "Numar Tricou":3
								},
							"Dukadam":{"Nume complet":"Helmut Dukadam",
									"Varsta":65,
									"Numar Tricou":7
								}
					    }
		       }
print(fotbalisti_pe_echipe)
print(f'Numarul de pe tricoul lui "Banel" este: {fotbalisti_pe_echipe["Barcelona"]["Banel"]["Numar Tricou"]}')
#ex.2
# fotbalisti_pe_echipe.pop("Dukadam")
# print(f'Am scos jucatorul"Dukadam" din dictionar. Noul dictionar va arata asa: {fotbalisti_pe_echipe}')

#ALTE EXERCITII
#ex.1
text = str(input("Va rugam introduceti un cuvant/o propozitie \n"))
vocale = {'a','A','e','E','i','I','o','O','u','U'},
lungime =len(text)
#for
text_rezultat = '*'
for i in range(0,lungime):
	if text[i] in vocale:
		text_rezultat+='*'
	else:
		text_rezultat+=text[i]
print(text_rezultat)


#ex.2
# numar = 5
# for i in range(2,numar//2):
# 	if (numar%i)==0:
# 		print(f'numarul nu este prim')
# 		break
# 	else:
# 		print(f'nr este prim')
#
# val_infer= int(input('introd val de inceput interval'))
# val_super = int(input('introd val de final interval'))
# for i in range(val_infer, val_super+1):
# 	if


#ex. 3
# numar={'a':6,'b':9,'c':5}
# par=0
# impar=0
# for i in numar:
# 	if numar[i]%2==0:
# 		par+=1
# 	else:
# 		impar+=1
#
# print(f'nr cifre pare ', par)
# print(f'nr cifre impare ', impar)

#ex,4
# numar=input('Introd un nr: \n')
# for i in numar:
# 	print(f'introd un nr {numar}')
# 	print(f'nr total cifre ale nr este {len(numar)}')
# 	break

# numar= input('nr:')
# nr_cifre = 0
# i=0
# lungime = len(numar)
# for i in range(0,lungime):
#     if numar[i].isnumeric():
#         cifra = int(numar[i])
#         nr_cifre+=1
# if nr_cifre>0:
#     print(f'Numarul {numar} are {nr_cifre} cifre')
# else:
#     print(f'Numaru;l {numar} nu are{nr_cifre} cifre')
#ex.5

#ex.6
# numar=input('introd un nr')
# lung= len(numar)
# for i in range(0,lung):
#     print(f'cea mai mare cifra este {max(numar)}')
#     print(f'cea mai mica cifra este {min(numar)}')
#     break

#ex.7
numar = input('introd un nr: \n')
crescator= False
descrescatos=True
lung= len(numar)
for i in range (0,lung):
	if cifra ==sorted(numar[i]):
		crescator=True
	return crescator









