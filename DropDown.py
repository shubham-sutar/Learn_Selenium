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
testing = Select(driver.find_element(By.XPATH, "//select[@id='testingDropdown']"))

# select option from dropdown
# testing.select_by_visible_text("Database Testing")
# testing.select_by_value("1")  # value
# testing.select_by_index(2)  # index

# capture all the options

all_menu = testing.options
print("total ops", len(all_menu))

for menus in all_menu:
    print(menus.text)


time.sleep(5)

driver.close()
