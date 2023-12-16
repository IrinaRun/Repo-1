#LISTE
#ex.1
lista1 = [1,"doi",3.14,'Maria',True]
print(lista1)
#ex.2
lista_goala = []
print(lista_goala)
#ex.3
print(f'Al doilea element din lista este: "{lista1[1]}"')
print(f'Primul element din lista este: "{lista1[0]}"')
print(f'Al doilea element din lista este: "{lista1[1]}"')
print(len(lista1))
print(f'Ultimul element din lista este: "{lista1[4]}"')
#ex.4
print(f'Indexul cifrei "1" din lista este: {lista1.index(1)}')
print(f'Indexul elementului  "Maria" din lista este: {lista1.index("Maria")}')
#ex.5
lista1.append("Ioana")
print(f'Lista cu elementul adaugat cu append este: {lista1}')# elementul adaugat este la sf listei
lista1.insert(2,"Dan")
print(f'Lista cu elementul adaugat cu insert este: {lista1}')# elementul se adauga la ce poz ii spunem noi
#ex.6
lista1.pop(2)
print(f'Lista cu elementul sters cu pop este: {lista1}')#sterge elem de la ce index ii spunem noi
lista1.remove('Ioana')
print(f'Lista cu elementul sters cu Remove este: {lista1}')#sterge elem a carei valoare i-o spunem noi
#ex.7
print(f'Lista mea are: {len(lista1)} elemente')
#ex.8
lista1.append("Maria")
lista1.append(1)
lista1.append(1)
print(lista1)
print(f'Elementul "1" apare de : {lista1.count(1)} ori')
#ex.9
lista2 = [5,9,12]
lista1.extend(lista2)
print(f'Cele doua liste unite sunt: {lista1}')
#ex.10
print(F'Lista sortata ascendent este: {sorted(lista2)}')
#ex.11
lista2.sort(reverse=True)
print(F'Lista sortata descendent este: {lista2}')
#ex.12
# lista2.clear()
# print(f'Lista stearsa este: {lista2}')

#TUPLURI
#Ex.1
tupla1 = (4,6,"Dana",1,4,22,6,6,19)
print(F'Tupla mea este: {tupla1}')
print(type(tupla1))
#ex.2
tupla_goala = ()
print(F'Tupla mea goala este: {tupla_goala}')
#ex.3
print(f'Primul eleemnt din tupla este: {tupla1[0]}')
print(f'Ultimul element din tupla este: {tupla1[3]}')
#ex.4
print(f'Elementul "Dana" este la pozitia {tupla1.index("Dana")} in tupla')
#ex.5
print(f'Elementul "6" apare de: {tupla1.count(6)} ori in tupla')
#ex.6
print(f'Elementul Dana se afla la pozitia: {tupla1.index("Dana")}')
#ex.7
#nu se pot modifica tuplele

#SETURI
#ex.1
set1 = {1,3,5,2,9,2,2,1,}
print(f'Setul meu este: {set1}')#nu permite elemente duplicate si va ordona el automat elementele din set
#ex.2
set_gol = {}
print(f'Setul meu gol este: {set_gol}')
#ex.3
set1.add(7)
print(f'Setul cu noul element adaugat este: {set1}')
#ex.4
# set1.pop()
# print(f'Setul sters cu pop este: {set1}')#sterge primul element din set
# set1.remove(5)
# print(f'Setul sters cu remove este: {set1}')#sterge elementul pe care il precizam noi
#ex.5
set2 = {2,3,5}
print(set2.issubset(set1))
#ex.6
print(set2.issuperset(set1))
#ex.7
set3 = {2,3,8,10,1}
print(set3)
intersectie = set1.intersection(set3)
print(f'Intersectia celor 2 seturi este: {intersectie}')
#ex.8
diferenta = set1.difference(set3)
print(f'Diferenta celor 2 seturi este: {diferenta}')# elem pe care le are in plus setul1 fata de setul3
#ex.9
set_sters = set3.clear()
print(f'Setul sters este: {set_sters}')

#DICTIONARE
#ex.1
patinatori = {"Trusova":"RUS",
              "Hendrix":"BEL",
              "Medvedeva":"RUS",
              "Bell":"USA"}
print(patinatori)
#ex.2
dictionar_gol = {}
print(dictionar_gol)
#ex.3
patinatori.update({"Valieva":"RUS"})#fol functia update
patinatori["Bonali"] = "FRA" #pe baza de cheie-valoare
print(patinatori)
#ex.4
patinatori.get("FRA")
print(f'Este "Bonali" in dictionar: {patinatori}')#cu functia get
print(f'Ce valoare are "Bell" in dictionar: {patinatori["Bell"]}')#pe baza de valoare
#ex.5
patinatori.pop("Hendrix")
print(f"Dictionar dupa ce am sters 'Hendrix': {patinatori}")#sterge elem pe care il specificam noi
patinatori.popitem()#sterge ultimul element din dictionar
print(f'Dictionarul sters cu pop.item este: {patinatori}')
#ex.6
print(f'Asa se extrag toate elem unul cate unul: {patinatori.items()}')
print(f'Asa se extrag toate cheile din dictionar: {patinatori.keys()}')
print(f'Asa se extrag toate valorile din dictionar: {patinatori.values()}')
#ex.7
patinatori.clear()
# print(f'Asa arata dictionarul dupa ce am fol met clear: {patinatori}')
