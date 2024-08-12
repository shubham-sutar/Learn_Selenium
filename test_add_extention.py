from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_option_ss():
    web_options = Options()
    # web_options.add_argument("--incognito")  # dont use incognito while performing add ext.
    web_options.add_extension("C:\\Users\\Admin\\Downloads\\screenShot.crx")

    driver = webdriver.Chrome(web_options)
    driver.get("https://app.vwo.com")
    time.sleep(5)

    driver.close()
