import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.implicitly_wait(10)

AllLinks = driver.find_elements(By.TAG_NAME, 'aS')

counter = 0
for links in AllLinks:
    url = links.get_attribute('href')
    try:
        res = requests.head(url, timeout=10)
    except requests.RequestException:
        None
        raise

    if res.status_code >= 400:
        print(url, "  is Broken link")
        counter += 1
    else:
        print(url, " is valid link")

print("total number of Broken links:", counter)
