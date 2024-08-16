from selenium import webdriver
from selenium.webdriver.common.by import By


def test_implicit():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    driver.implicitly_wait(5)  # give instruction for I will wait for only 5sec.

    email_box = driver.find_element(By.ID, "login-username")
    email_box.send_keys("shubham@abc.com")

    password_box = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_box.send_keys("admin123")

    sub_btn = driver.find_element(By.ID, "js-login-btn")
    sub_btn.click()

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    assert error_msg.text == "Your email, password, IP address or location did not match"

    driver.close()
