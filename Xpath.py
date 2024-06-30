from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//input[@id='username']" or "//input[@name='username']").send_keys("student")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='password']" and "//input[@name='password']").send_keys("Password123")
time.sleep(2)
# driver.find_element(By.XPATH, "//button[@id='submit']").click()
# driver.find_element(By.XPATH, "//button[contains (@id,'submit')]").click()
# driver.find_element(By.XPATH,"//button[starts-with(@id,'sub')]").click()
driver.find_element(By.XPATH, "//button[text() = 'Submit']").click()
time.sleep(2)

act_title = driver.title
exp_title = "Logged In Successfully | Practice Test Automation"

if act_title == exp_title:
    print("User Login Successfully.")
else:
    print("User Login Failed.")
time.sleep(3)

driver.close()


