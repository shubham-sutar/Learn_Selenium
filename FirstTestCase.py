# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
#
# driver = webdriver.Chrome(service=serv_obj)
# # driver = webdriver.Chrome()
#
# driver.get("https://www.orangehrm.com/")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")

driver = webdriver.Chrome(service=Service_obj)
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.NAME, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "submit").click()

act_title = driver.title
exp_title = "Test Login | Practice Test Automation"

if act_title == exp_title:
    print("Login Test Passed.")
else:
    print("Login Failed.")

driver.close()
