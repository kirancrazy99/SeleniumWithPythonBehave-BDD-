from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

# from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

#Example1
# driver.get('https://echoecho.com/htmlforms11.htm')
# driver.maximize_window()
# # printing all drop down values
# tag_values = driver.find_element(by=By.TAG_NAME,value='select')
# print(tag_values.text)
#
# # selecting a particular drop down value
# # driver.find_element(by=By.XPATH,value='/html/body/div[2]/table[9]/tbody/tr/td[4]/table/tbody/tr/td/div/span/form/table[1]/tbody/tr/td/table/tbody/tr[2]/td[3]/select/option[2]').click()
#
# driver.find_element(by=By.XPATH,value='/html/body/div[2]/table[9]/tbody/tr/td[4]/table/tbody/tr/td/div/span/form/table[1]/tbody/tr/td/table/tbody/tr[2]/td[3]/select/option[3]').click()
# time.sleep(5)
# driver.close()


# Example2

driver.get('https://www.wikipedia.org/')
driver.maximize_window()
# dropdown = driver.find_element(by=By.ID,value='searchLanguage')
# select = Select(dropdown)
# select.select_by_visible_text('Dansk')
# select.select_by_value('hi')
options = driver.find_elements(by=By.TAG_NAME,value='option')
for option in options:
    print('Text is: '+option.text, 'Lang is :'+option.get_attribute('lang'))

print('Total no of elements is :',len(options))
driver.close()
