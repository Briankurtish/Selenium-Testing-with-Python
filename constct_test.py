from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time



service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.emu.edu.tr/en")


programs_element = driver.find_element(By.XPATH, "//*[@id='mgmenu1']/ul/li[4]/a")
programs_element.click()
time.sleep(2)

department_input_element = driver.find_element(By.XPATH, "//*[@id='contentskip']/div/div/form/div[1]/div[1]/div/div/ul[1]/li/input")
department_input_element.clear()
department_input_element.send_keys("School of Computing and Technology" + Keys.ENTER)
time.sleep(2)

language_input_element = driver.find_element(By.XPATH, "//*[@id='contentskip']/div/div/form/div[1]/div[3]/div/div/ul[1]/li/input")
language_input_element.clear()
language_input_element.send_keys("English" + Keys.ENTER)
time.sleep(2)

list_button_element = driver.find_element(By.XPATH, "//*[@id='contentskip']/div/div/form/div[2]/div/div/button")
list_button_element.click()
time.sleep(2)

IT_element = driver.find_element(By.XPATH, "//*[@id='contentskip']/div/div/div[2]/table/tbody/tr[3]/td[1]/a")
IT_element.click()
time.sleep(5)



print("SUCCESS: Test Successful!!")
# Quit the driver
driver.quit()
