from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")

driver.maximize_window()
time.sleep(4)

# find Element() - returns single web element
# 1) Locator matching with single web element

# text vs get_attribute('value')

email_box = driver.find_element(By.XPATH, "//*[@id='Email']")
email_box.clear()
email_box.send_keys("abc@123")

print("result of text:", email_box.text)
print("result of get_attribute():", email_box.get_attribute('value'))


# driver.close()
driver.quit()


