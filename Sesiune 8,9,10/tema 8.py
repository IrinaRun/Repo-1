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

#test 1
# chrome.get('https://www.elefant.ro/')

#test2
chrome.get('https://www.elefant.ro/search?SearchTerm=iphone+14')
sleep(1)
lista_prod=chrome.find_elements(By.CLASS_NAME,'current-price')
sleep(2)




