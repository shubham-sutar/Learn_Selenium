from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.relative_locator import locate_with
import pytest
import allure
import time


@pytest.mark.positive
@allure.title("Learning the Exception")
def test_exception():
    # serv_object = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome()

    driver.get("https://www.google.com")
    driver.maximize_window()
    time.sleep(3)

    try:
        search_box = driver.find_element(By.NAME, "qp")
        search_box.send_keys("joshmarathi")
    except NoSuchElementException as Ne:
        print(f"Exception Occurs {Ne}")
    time.sleep(2)

    driver.quit()
