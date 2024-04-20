from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.emu.edu.tr/en")


academics_element = driver.find_element(By.XPATH, "//*[@id='mgmenu1']/ul/li[3]/a")
academics_element.click()
time.sleep(2)

card_element = driver.find_element(By.XPATH, "//*[@id='contentskip']/div[4]/div/div/div[2]/a")
card_element.click()
time.sleep(2)

department_name_element =  driver.find_element(By.XPATH, "//*[@id='contentskip']/div[1]/div/div/table/tbody/tr[18]/td[1]/a")
department_name_element.click()
time.sleep(2)

curriculum_element = driver.find_element(By.XPATH, "//*[@id='sticky_nav']/li[2]/a")
curriculum_element.click()
time.sleep(5)  


print("SUCCESS: Test Successful!!")
# Quit the driver
driver.quit()
