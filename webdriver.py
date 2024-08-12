from selenium import webdriver
import time


def test_myweb():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge()
    driver.get("https://joshmarathi.com")
    driver.maximize_window()
    time.sleep(5)
    driver.close()
