from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import pytest
import allure


@pytest.mark.positive
@allure.title("Mini Project of idrive360")
@allure.description("Conduct testing and Generate Automation testing report")
def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()

    # Enter the username, password
    username_box = driver.find_element(By.XPATH, "//input[@id='username']")
    username_box.send_keys("augtest_040823@idrive.com")

    password_box = driver.find_element(By.XPATH, "//input[@id='password']")
    password_box.send_keys("123456")

    WebDriverWait(driver=driver, timeout=3).until(
        EC.visibility_of_element_located((By.ID, 'frm-btn'))
    )

    submit_btn = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    submit_btn.click()

    WebDriverWait(driver=driver, timeout=20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Your free trial has expired']"))
    )

    assert (driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true") and (
        driver.find_element(By.XPATH, "//span[text()='Your free trial has expired']"))

    allure.attach(driver.get_screenshot_as_png(), name='Mini_Project', attachment_type=AttachmentType.PNG)
    driver.close()
