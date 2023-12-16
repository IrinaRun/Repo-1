from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
chrome= webdriver.Chrome(service=s)


# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.maximize_window()
# sleep(1)
# address=chrome.find_element(By.ID,'autocomplete')
# sleep(1)
# address.send_keys('saulescu')
# sleep(2)
# street_address = chrome.find_element(By.ID,'street_number')
# sleep(2)
# street_address.send_keys('6')
# sleep(2)
# city=chrome.find_element(By.ID,'locality')
# sleep(1)
# city.send_keys('Iasi')
# sleep(2)
#
# try:
#     address==chrome.find_element(By.ID,'address')
#     address.send_keys('saulescu')
#     street_address==chrome.find_element(By.ID,'street_address')
#     street_address.send_keys('6')
#     city=chrome.find_element(By.Id,'city')
#     city.send_keys('Iasi')
# except:
#     print('datele nu sunt corecte')
# print('Am reusit cu succes')


# chrome.get('https://formy-project.herokuapp.com/')
# chrome.maximize_window()
# sleep(1)
# # element_web=chrome.find_element(By.CLASS_NAME,'lead')
# text_element=element_web.text
# expected_text = ('This is a simple site that has form components that can be used for testing purposes.')
# try:
#     assert text_element ==expected_text
#     print('mesajul este corect :"{}"'.format(text_element))
# except AssertionError:
#     print ('mesaj gresit. actual {} .asteptat {}'.format(expected_text,text_element))

# element = chrome.find_element(By.CLASS_NAME,'display-3')
# text_element=element.text
# expected_text = ('Welcome to Formy')
# try:
#     assert text_element==expected_text
#     print('text corect "{}"'.format(text_element))
# except AssertionError:
#     print('text incorect. asteptat {}.actual {}'.format(expected_text,text_element))

# try:
#     first_name =chrome.find_element(By.ID,'first-name')
#     first_name.send_keys('iri')
#     last_name = chrome.find_element(By.ID, 'last-name')
#     last_name.send_keys('run')
#     job_title = chrome.find_element(By.ID,'job-title')
#     job_title.send_keys('director')
#     button=chrome.find_element(By.ID,'radio-button-1')
#     button.click()
# except:
#     print('date incorecte')
# print('introduse cu succes')
chrome.get('https://formy-project.herokuapp.com/form')
chrome.maximize_window()
sleep(1)
first_name=chrome.find_element(By.ID,'first-name')
sleep(2)
first_name.send_keys('iri')
sleep(2)
last_name =chrome.find_element(By.ID, 'last-name')
sleep(2)
last_name.send_keys('runc')
sleep(2)
job=chrome.find_element(By.ID,'job-title')
sleep(1)
job.send_keys('director')
sleep(2)
buton=chrome.find_element(By.ID,'radio-button-1')
sleep(1)
buton.click()
sleep(2)
buton2 = chrome.find_element(By.ID,'checkbox-2')
sleep(1)
buton2.click()
sleep(1)

