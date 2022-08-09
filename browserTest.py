from selenium import  webdriver
from time import  sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com')
title = driver.title
print(title)
driver.maximize_window()
sleep(10)
driver.close()