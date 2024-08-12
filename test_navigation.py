from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    time.sleep(3)

    driver.refresh()
    driver.back()
    driver.forward()

    driver.close()
