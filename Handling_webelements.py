from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://gmail.com')
driver.maximize_window()
sleep(5)
username = driver.find_element(by='id',value='identifierId')
username.send_keys('Kirankumar.tangi@gmail.com')
sleep(5)
driver.find_element(by='xpath',value='//*[@id="identifierNext"]/div/button/span').click()
driver.close()
