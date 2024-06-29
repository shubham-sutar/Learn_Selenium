from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(5)

# tag and id combination (CSS Selector)
"""
tagName#value_of_id ---  input#email
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("Admin")
"""
# tag and class combination (CSS Selector)
"""
tagName.value_of_class ---  input.inputtext
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("Admin")
"""
# tag and attribute combination (CSS Selector)
"""
tagName[attribute = value] ---  input[name=pass]
driver.find_element(By.CSS_SELECTOR, "input[name=pass]").send_keys("Admin")

"""
# tag and class attribute combination (CSS Selector)
"""
tagName.valueofclass[attribute = value] ---  input.inputtext[name=pass]
driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]").send_keys("admin123")
"""

driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[name=pass]").send_keys("admin123")
time.sleep(5)




