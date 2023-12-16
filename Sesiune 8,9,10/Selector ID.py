from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

#initializare Chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# In cazul in care folositi o versiune mai veche de Pycharm, va trebui sa va setati descarcarea driverului corect in mod
#dinamic si puteti face asta prin comanda de mai jos:
#chrome=webdriver.Chrome(executable_patch=ChromeDriverManager().install())

#navigam catre un url:
chrome.get('https://formy-project.herokuapp.com/')

#maximizare fereastra
chrome.maximize_window()
sleep(3)

#inchiderea instantei de Chrome ! se va folosi dupa ce am inserat toate testele dorite
# chrome.quit()
#inchiderea unui tab din Chrome
# chrome.close()

# Selector ID
#cautarea in web se poate face folosind: [id='val ID']
chrome.get('https://formy-project.herokuapp.com/')

# first_name=chrome.find_element(By.ID,'first-name')
# sleep(2)
# first_name.send_keys("Lidia")
# sleep(3)
# last_name= chrome.find_element(By.ID,'last-name')
# sleep(1)
# last_name.send_keys('Popa')
# sleep(2)

#metoda recomandata pt economisire cod
# chrome.find_element(By.ID,'last-name').send_keys('Popa')
# sleep(2)

#Modelul pe care il veti folosi in testare
try:
    first_name= chrome.find_element(By.ID,"first-name")
    first_name.send_keys("Lid")
except:
    print('ID-ul nu este corect')
print('Am reusit cu succes')
