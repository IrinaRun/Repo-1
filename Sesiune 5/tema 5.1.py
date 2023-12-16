nr=input(f'intr un nr\n')
lung=len(nr)
nr_cifre_impare=0
i=0
for i in range(0,lung):
    if nr[i].isnumeric():
        cifra= int(nr[i])
        if not (cifra%2==0):
            nr_cifre_impare+=1
if nr_cifre_impare>0:
    print(f'are cifre impare{nr_cifre_impare}')
else:
    print(f'nu are ')





