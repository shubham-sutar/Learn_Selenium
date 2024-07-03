from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.google.com/")
driver.maximize_window()
# time.sleep(4)
driver.implicitly_wait(10)

# for SearchBox
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()
# time.sleep(3)

driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
# time.sleep(3)

driver.close()
