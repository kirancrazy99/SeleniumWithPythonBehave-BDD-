from selenium import  webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.tizag.com/htmlT/htmlcheckboxes.php')
driver.maximize_window()
#select individual checkboxes
# driver.find_element(by=By.XPATH,value='//div[4]/input[1]').click()
# driver.find_element(by=By.XPATH,value='//div[4]/input[2]').click()
# driver.find_element(by=By.XPATH,value='//div[4]/input[3]').click()
# driver.find_element(by=By.XPATH,value='//div[4]/input[4]').click()

i = 1

def is_element_present(who,how):
    try:
        driver.find_element(by=who,value=how)
        return True
    except NoSuchElementException:
        return False


# Method:1
# i=1
# while is_element_present(By.XPATH,f'//div[4]/input[{str(i)}]'):
#     driver.find_element(by=By.XPATH, value=f'//div[4]/input[{str(i)}]').click()
#     i+=1

block = driver.find_element(by=By.XPATH,value='/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]')

cb = block.find_elements(by=By.NAME,value='sports')
for c in cb:
    c.click()




