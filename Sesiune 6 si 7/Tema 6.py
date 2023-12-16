class Cinema:
    nume_sala =None
    nr_locuri = 50
    bilete_vandute = 0
    filme = []
    produse_vandute =['popcorn','bauturi','dulciuri']
    popcorn_vandut = 0
    total_vanzari = 0
    tip_filme = ['drama','comedie','desene','horror']
    tip_audienta = ['AG','interzis minori']
    bauturi_vandute = 0
    def __init__(self,adresa,capacitate,):
        self.capacitate=capacitate
        self.adresa= adresa


    def adauga_film(self,film):
        self.filme.append(film)
    def remove_film(self,film):
        self.filme.remove(film)
    def audienta(self,tip_audienta):
        self.tip_audienta.append(tip_audienta)
    def bilete(self,bilete_vandute):
        self.bilete_vandute+=bilete_vandute
    def vanzari(self,bauturi_vandute):
        self.bauturi_vandute=56+bauturi_vandute
    def informatii(self):
        print(f'cinema are adresa {cinema1.adresa} si o capacitate de {cinema1.capacitate}')


cinema1 = Cinema('Coresi nr.25', 501)
cinema1.bilete(50)
cinema1.adauga_film('Godzilla')
cinema1.adauga_film("007")
cinema1.audienta('sub12')
cinema1.vanzari(10)
cinema1.bilete(30)
cinema1.informatii()
print(f'Filmele care ruleaza sunt: {cinema1.filme}')
print(f'Nr bilete vandute este: {cinema1.bilete_vandute}')
print(f'ruleaza urmatoarele tipuri de filme: {cinema1.tip_filme}')
print(f'in cinema sunt urmatoarele tipuri de audienta: {cinema1.tip_audienta}')
print(f'in cinema se comercializeaza: {cinema1.produse_vandute}')
print(f'in cinema s-au vandut: {cinema1.bauturi_vandute} bauturi')
while cinema1.capacitate <=310:
    print(f'cinema are {cinema1.capacitate}')
    cinema1.capacitate+=1
else:
    print('nu mai sunt locuri')
if cinema1.capacitate>500:
    print('err')








