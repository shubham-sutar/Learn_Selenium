from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
# import time
import allure
import pytest


@pytest.mark.positive
@allure.title("Automation testing and report generation")
@allure.description("conduct automation testing and report generation of https://katalon-demo-cura.herokuapp.com/")
def test_project4():
    driver = webdriver.Chrome()
    # open the url
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # click on the make appointment button
    btn_click = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    btn_click.click()

    # verify that url changes - assert
    actual_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    assert driver.current_url == actual_url

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Demo account']"))
    )

    # enter the username, password
    user_box = driver.find_element(By.XPATH, "//input[@id='txt-username']")
    user_box.send_keys("John Doe")

    pass_box = driver.find_element(By.XPATH, "//input[@id='txt-password']")
    pass_box.send_keys("ThisIsNotAPassword")

    btn_click_log = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    btn_click_log.click()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.url_to_be("https://katalon-demo-cura.herokuapp.com/#appointment")
    )

    allure.attach(driver.get_screenshot_as_png(), name='PaasTest', attachment_type=AttachmentType.PNG)

    mk_appointment = driver.find_element(By.XPATH, "//h2[text()='Make Appointment']")
    assert ((driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment") and (mk_appointment.text ==
                                                                                                'Make Appointment'))
    driver.close()
