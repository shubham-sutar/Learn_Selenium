# internal links
# External links

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)


# Find Number of links
"""
links = driver.find_elements(By.TAG_NAME, 'a')
print("The Total number of links:", len(links))
time.sleep(4)
"""

# Find Number of links using XPATH
"""
links = driver.find_elements(By.XPATH, "//a")
print("total links:", len(links))
"""

# Print the all links name
"""
links = driver.find_elements(By.XPATH, "//a")

for link in links:
    print(link.text)
"""

driver.close()
