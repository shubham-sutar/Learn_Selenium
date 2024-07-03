from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://programiz.pro/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, "Get Started").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='inputEmailAddress2']").send_keys("kigajap536@mposhop.com")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

driver.find_element(By.ID, "exampleInputfullName1").send_keys("kingajapa")
driver.find_element(By.NAME, "password").send_keys("&gXZ:0+W*x^b")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='sign-up-with-email']").click()
time.sleep(5)

driver.close()



