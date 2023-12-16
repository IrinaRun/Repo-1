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
chrome.get('https://the-internet.herokuapp.com/redirector')

#Selector Link Text
# In codul HTML se gaseste de forma aceasta:
# <a href = 'link de redirectionare'> textul care este pus peste link </a>
# a = prescurtare de la ancora si este o legatura catre alt link
# href = prescurtare de la hypertext reference si reprez pag catre care se va naviga at cand se va da click pe acel
#link

# clic_on_me=chrome.find_element(By.LINK_TEXT,'here')
# sleep(2)
# clic_on_me.click()
# sleep(2)
# chrome.find_element(By.LINK_TEXT,'200').click()
# sleep(2)

# Ex.1
# chrome.find_element(By.LINK_TEXT,'here').click()
# assert chrome.current_url=='https://the-internet.herokuapp.com/status_codes','Err, url nu este corect'

# Selector Partial Link Text - este o alternativa pentru Selectorul Link Text atunci cand textul este prea lung
#sau se schimba frecvent

# link_partial= chrome.find_element(By.PARTIAL_LINK_TEXT,'Elemental')
# sleep(2)
# link_partial.click()
# sleep(2)

#ex.
try:
    chrome.find_element(By.PARTIAL_LINK_TEXT,'he').click()
    assert chrome.current_url=='https://the-internet.herokuapp.com/status_codes', 'Err, url is not correct'
    print('Current url is correct')
except AssertionError as e:
    print(e)


