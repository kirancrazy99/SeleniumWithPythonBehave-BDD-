from selenium import  webdriver
from time import  sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('https://gmail.com')
driver.maximize_window()



def find_element(who,what):
    try:
        driver.find_element(by=who,value=what)
        return True
    except NoSuchElementException:
        return False


# print(driver.find_element(by=By.ID,value='identifierId222').is_enabled())
print(find_element(By.TAG_NAME,'input'))
sleep(2)
driver.close()