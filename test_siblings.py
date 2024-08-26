from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import pytest
import allure
import time


@pytest.mark.positive
@allure.title("Tutorial of locators")
def test_allocators():
    serv_obj = Service("C:\\Drivers\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://www.aqi.in/in/real-time-most-polluted-city-ranking")
    driver.maximize_window()
    time.sleep(10)

    search_city = driver.find_element(By.ID, "search_city")
    search_city.send_keys("India")
    time.sleep(5)

    select_state = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")
    print("\n")
    print(" Rank " + " | " + " Name " + " | " + " AQI ")
    for state in select_state:
        if "India" in state.text:
            s1 = driver.find_element(locate_with(By.TAG_NAME, "p").to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(state)).text
            s3 = driver.find_element(locate_with(By.TAG_NAME, "p").below(state)).text
            s4 = driver.find_element(locate_with(By.TAG_NAME, "p").above(state)).text
            print(s2 + " | " + state.text + " | " + s1)
            print(s3 + " | " + state.text + " | " + s4)
        else:
            # You can add a default or error handling case here if needed
            print("City not found for state: ", state.text)

    driver.quit()
