import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.way2automation.com')
driver.maximize_window()

menu = driver.find_element(by=By.XPATH,value="""//*[@id="menu-item-27597"]/a/span[2]""")
action = ActionChains(driver)
action.move_to_element(menu).perform()
driver.find_element(by=By.XPATH,value="""//*[@id="menu-item-27600"]""").click()