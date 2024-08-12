from selenium import webdriver
import time


def test_open_vwo():
    driver = webdriver.Chrome()

    print(driver.session_id)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    time.sleep(5)

    assert driver.title == "Login - VWO"
    time.sleep(3)
