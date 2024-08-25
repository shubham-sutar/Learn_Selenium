from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import allure
import time


@pytest.mark.positive
@allure.title("SVG Tutorial")
def test_ind_map():
    serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)

    select_state = driver.find_elements(By.XPATH, "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*["
                                                  "name()='path']")
    for states in select_state:
        if "Maharashtra" in states.get_attribute('aria-label'):
            states.click()
            break

    time.sleep(15)
    driver.close()
