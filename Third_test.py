from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
print("script started running...")

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys("student")
print("user enters username.")
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("Password123")
print("user enters password.")
time.sleep(2)

driver.find_element(By.ID, "submit").click()
print("user clicked login button.")
time.sleep(2)

act_txt = driver.title
exp_txt = "Logged In Successfully | Practice Test Automation"

if act_txt == exp_txt:
    print("user successfully logged in")
else:
    print("user failed to logged in")

time.sleep(2)

driver.close()
