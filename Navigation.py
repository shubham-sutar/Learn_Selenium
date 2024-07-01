from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")

driver.maximize_window()
time.sleep(4)

driver.back()
driver.forward()
driver.refresh()

# driver.close()
driver.quit()


