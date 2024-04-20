from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.emu.edu.tr/en")

academics_element = driver.find_element(By.XPATH, "//*[@id='mgmenu1']/ul/li[3]/a")
academics_element.click()

card_element = driver.find_element()




time.sleep(10)

driver.quit()