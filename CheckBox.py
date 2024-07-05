from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()
driver.implicitly_wait(10)
# time.sleep(5)


driver.find_element(By.CSS_SELECTOR, "input.Automation").click()
# time.sleep(5)

print("success")
driver.close()
