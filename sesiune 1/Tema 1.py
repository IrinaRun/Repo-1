#ex.1
import datetime
from datetime import date
data_curenta = date.today() # va fi variabila
print(data_curenta)
#ex.2
print(type(data_curenta))
#ex.3
curs = 'Testare automata' # string
zi = datetime.datetime.today()
sesiune_curs = 'TA1.1' #string
print('Ziua de azi este:', zi.strftime('%A'))
#ex.4
#“Ana s-a nascut in anul 1990 si acum are 33 de ani”
nume= 'Ana'
an = 1990
varsta = 33
print(f'{nume} s-a nascut in anul {an} si acum are {varsta} de ani' ) #print cu formatare si variable
print('Ana s-a nascut in anul 1990 si acum are 33 de ani') #print cu formatare si text
print('Ana s-a nascut in anul ' + str(1990) + ' si acum are ' + str(33) + ' de ani') #print cu formatare si tip variabile
#ex.5
nume = input('Introduceti numele dvs: \n') #am declarat si citit de la tastatura variabila
prenume = input('Introduceti prenumele dvs: \n') #am declarat si citit de la tastatura variabila
varsta = int(input('Ce varsta aveti? \n')) #am declarat si citit de la tastatura variabila
print(f'Ma numesc {nume} {prenume} si am varsta de:{varsta} ani.') # am tiparit mesajul folosind variabilele declarate
