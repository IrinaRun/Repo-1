numar = input('introd un nr: \n')
descrescator=False
crescator=False
cifra_anter = int(numar[0])
lung= len(numar)
for i in range(1,lung):
    cifra_curenta = int(numar[i])
    if cifra_anter>=cifra_curenta:
        cifra_anter=cifra_curenta
        descrescator=True
    else:
        descrescator=False
for i in range(1,lung):
    cifra_curenta= int(numar[i])
    if cifra_anter<=cifra_curenta:
        cifra_anter+=1
        crescator=True
    else:
        crescator=False
if crescator:
    print(f'Nr este crescator :da')
else:
    print(f'Nr este crescator :nu')





