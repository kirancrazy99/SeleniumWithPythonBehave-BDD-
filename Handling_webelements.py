from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://gmail.com')
driver.maximize_window()
driver.implicitly_wait(20)
username = driver.find_element(by='id',value='identifierId')
username.send_keys('Kirankumar.tangi@gmail.com')
driver.find_element(by='xpath',value='//*[@id="identifierNext"]/div/button/span').click()
# driver.close()
