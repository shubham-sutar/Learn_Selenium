from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.google.com/")
driver.maximize_window()
# time.sleep(4)
# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

# for SearchBox
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()
# time.sleep(3)

search_link = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()

# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
# time.sleep(3)

driver.close()
