from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time


@pytest.mark.positive
@allure.title("VWO Invalid login page - test mini project")
@allure.description("Verify that invalid email, password. error msg came")
def test_proj():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    time.sleep(3)

    # find the email, password and enter the invalid value
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    email_box = driver.find_element(By.ID, "login-username")
    email_box.send_keys("shubham@abc.com")
    time.sleep(4)

    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="jobodapuxe"
    # >

    password_box = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_box.send_keys("admin123")

    # <button
    # type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica"
    # >
    # <span
    # class="icon loader hidden"
    # data-qa="zuyezasugu"></span>
    # <span
    # data-qa="ezazsuguuy">Sign in</span>
    # </button>

    sub_btn = driver.find_element(By.ID, "js-login-btn")
    sub_btn.click()
    time.sleep(4)

    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi"
    # >
    # Your email, password, IP address or location did not match
    # </div>

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    assert error_msg.text == "Your email, password, IP address or location did not match"

    driver.close()
