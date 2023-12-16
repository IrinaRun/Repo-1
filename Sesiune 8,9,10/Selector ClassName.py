from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
#initializare Chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

#navigam catre un url:
chrome.get('https://formy-project.herokuapp.com/')

#maximizare fereastra
chrome.maximize_window()
sleep(3)


#Selector ClassName- bazat pe clase
#ex.1
chrome.get('https://formy-project.herokuapp.com/')
# clasa_mea= chrome.find_element(By.CLASS_NAME , 'nav-link')
# sleep(2)
# clasa_mea.click()
# sleep(2)

#ex.2 = pt economie de cod
# chrome.find_element(By.CLASS_NAME ,'nav-link').click()
# sleep(2)

#ex.3
element_web=chrome.find_element(By.CLASS_NAME,'lead')
text_element =element_web.text
expected_text='This is a simple site that has form components that can be used for testing purposes.'

try:
    assert text_element== expected_text
    print('mesajul este corect: "{}"'.format(text_element))
except AssertionError:
    print('Mesajul este gresit .Asteptat {}.Actual {}'.format(expected_text,text_element))


