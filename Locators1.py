from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.nopcommerce.com/en/demo")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Get started")
driver.find_element(By.PARTIAL_LINK_TEXT, "Get")
links = driver.find_elements(By.CLASS_NAME, "navigation-top-menu-item")
print(len(links))
Tags = driver.find_elements(By.TAG_NAME, "a")
print(len(Tags))
driver.close()
