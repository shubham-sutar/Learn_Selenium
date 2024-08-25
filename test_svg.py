from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
import time


@pytest.mark.positive
@allure.title("Testing the svg image")
def test_svg():
    serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    select_box = driver.find_element(By.XPATH, "//input[@name='q']")
    select_box.send_keys("cycle")

    # click_btn = driver.find_element(By.XPATH, "//*[local-name()='svg']/*[contains(text(),'Search Icon')]")
    # click_btn.click()

    svg_list = driver.find_elements(By.XPATH, "//*[local-name()='svg']")
    svg_list[0].click()

    time.sleep(3)
    # WebDriverWait(driver=driver, timeout=5).until()
    driver.close()
