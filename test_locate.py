from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time
import pytest
import allure


@pytest.mark.positive
@allure.title("Locate with Tutorial")
def test_locators():
    servo = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=servo)
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    time.sleep(5)

    year_exp = driver.find_element(By.XPATH, "//span[text()='Years of Experience']")
    rdo_btn3 = driver.find_element(locate_with(By.ID, 'exp-3').to_right_of(year_exp))
    rdo_btn3.click()

    time.sleep(4)
    driver.close()
