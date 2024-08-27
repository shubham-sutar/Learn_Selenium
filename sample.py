from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time


@pytest.mark.positive
@allure.title("Testing")
def test_browser():
    driver = webdriver.Firefox()
    driver.get("https://www.joshmarathi.com")
    driver.maximize_window()
    time.sleep(2)
    driver.quit()
