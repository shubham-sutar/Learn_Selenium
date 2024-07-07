from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()
driver.implicitly_wait(10)

# select_op = driver.find_element(By.XPATH, "//select[@id='testingDropdown']")
country = Select(driver.find_element(By.XPATH, "//select[@id='testingDropdown']"))

# select option from dropdown
country.select_by_visible_text("Database Testing")

time.sleep(5)

driver.close()
