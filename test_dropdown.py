from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select


@pytest.mark.positive
def test_dropdown():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "dropdown"))  # visibility_of_element
    )

    select_element = driver.find_element(By.ID, "dropdown")
    select = Select(select_element)
    select.select_by_visible_text("Option 2")
    allure.attach(driver.get_screenshot_as_png(), name='dropdown', attachment_type=AttachmentType.PNG)

    driver.close()
