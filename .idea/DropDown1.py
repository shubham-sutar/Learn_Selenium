from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
driver.implicitly_wait(10)

drp_sec_country = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

drp_sec_country.select_by_visible_text("India")

time.sleep(5)

driver.close()

