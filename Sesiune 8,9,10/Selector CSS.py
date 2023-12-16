from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/scroll')

#Selectorul CSS
# cautarea in pag web pt CSS Selector se poate face asa:
# Selectare dupa ID  #myId
# Selectarea dupa clasa .myClass
# Selectarea dupa tipul de element = denumire element(input)
# Cautarea primului copil al unui elem se face cu caracterul '>' sau cu sintaxa 'first-of-type'
# Cautarea ultimului copil al unui elem se face cu sintaxa 'last of type'
# Cautarea unui copil care nu e nici primul nici ultimul, se folosete 'nth-of-type'

chrome.find_element(By.CSS_SELECTOR,'input#name').send_keys('Cristina')
sleep(3)

chrome.find_element(By.CSS_SELECTOR,'input.form-control').send_keys(' Dumitru')
sleep(2)
chrome.find_element(By.CSS_SELECTOR,"input[placeholder='MM/DD/YYYY']").send_keys('14/12/2023')
sleep(2)
chrome.find_element(By.ID,'logo').click()
sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT,'Web Form').click()
sleep(2)
chrome.find_element(By.CSS_SELECTOR,'div input[placeholder*="first name"]').send_keys('Cristina')
sleep(2)
# fol *= pt a nu scrie tot continutul folderului
# *= inseamna 'contine'

chrome.find_element(By.CSS_SELECTOR,'div input[placeholder*="last name"]').send_keys('Dumitru')
sleep(2)

#ex. am facut navigare din parinte in copil combinata cu cautare dupa tip atribut-valoare
text_label_name =chrome.find_element(By.CSS_SELECTOR,'strong >label[for="last-name"]').text
text_afisat = text_label_name
textul_asteptat = 'Last name'

try:
    assert text_afisat==textul_asteptat
    print('Titlul este corect: "{}" '.format(text_afisat))
except AssertionError:
    print('Mesajul este gresit. Asteptat {}. Actual {}'.format(textul_asteptat,text_afisat))
