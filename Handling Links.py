from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org')
driver.maximize_window()
driver.implicitly_wait(10)
options = driver.find_elements(by=By.TAG_NAME,value='a')
for option in options:
    print('Text is :'+option.text,'And URL is:',option.get_attribute('href'))

