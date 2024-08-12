from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import time


def test_page_load():
    web_options = Options()
    # web_options.page_load_strategy = 'none'
    # web_options.page_load_strategy = 'eager'
    web_options.page_load_strategy = 'normal'
    # web_options.add_argument("--page-load-strategy=none")

    driver = webdriver.Chrome(web_options)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
