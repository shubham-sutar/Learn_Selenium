from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time


@pytest.mark.positive
@allure.title("Finding the Xpath absolute and relative")
@allure.description("Explore more about Relative Xpath")
def test_xpath_proj():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(3)

    # find absolute Xpath
    full_btn_xpath = driver.find_element(By.XPATH, "/html/body/header/div/a")
    full_btn_xpath.click()
    time.sleep(2)

    # find relative Xpath
    relative_xpath = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    relative_xpath.click()
    time.sleep(2)

    # Verify the current url
    actual_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    assert driver.current_url == actual_url

    # Xpath Function
    # 1) full visible Text - //a[text()="Make Appointment"]
    # 2) partial visible Text - //a[contains(text()="Make")]



    driver.close()
