from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
time.sleep(3)

driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
time.sleep(5)

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
    print("User login Successfully. ✔")
else:
    print("User failed to login. ❌")

print("❤❤❤ Happy Coding ❤❤❤")
driver.close()



