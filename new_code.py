from selenium import webdriver
import time


def test_open_new():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(10)


# new_start()
