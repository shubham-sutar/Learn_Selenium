from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_web_options():

    # create an instance of ChromeOptions
    chrome_option = Options()
    chrome_option.add_argument("--windows-size=500*1000")
    chrome_option.add_argument("--non-headless")
    chrome_option.add_argument("--incognito")
    chrome_option.add_extension("C:\\Users\\Admin\\Downloads\\screenShot.crx")

    driver = webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com")
    time.sleep(5)
