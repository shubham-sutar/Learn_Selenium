from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

multiple_checks = driver.find_elements(By.XPATH, "//input[contains(@id,'day')]")

for all_checks in multiple_checks:
    all_checks.click()

time.sleep(5)

driver.close()
