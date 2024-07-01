from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
print("This is a current url of webpage:", driver.current_url)
print("This is a title of webpage:", driver.title)
print("page source:", driver.page_source)

driver.quit()
