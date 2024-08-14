from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure


@pytest.mark.positive
@allure.title("learn about the Locaters")
@allure.description("Verify the url changes")
def test_locators():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(3)

    select_btn = driver.find_element(By.ID, "btn-make-appointment")
    select_btn.click()

    # current_url == actual_url
    actual_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    assert driver.current_url == actual_url
    time.sleep(3)
