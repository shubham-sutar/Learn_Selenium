from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)

# is_displayed()

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Search Box Displayed:", search_box.is_displayed())
print("Search Box Enabled:", search_box.is_enabled())

# is_selected()
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

rd_male.click()

print(rd_male.is_selected())

driver.quit()

