# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
# import allure
# import time
#
#
# @pytest.mark.positive
# @allure.title("Testing")
# def test_browser():
#     driver = webdriver.Firefox()
#     driver.get("https://www.joshmarathi.com")
#     driver.maximize_window()
#     time.sleep(2)
#     driver.quit()

import itertools
import string
import time

print("Hello INDIAN CYBER CLUB ARMY. I AM PASSWORD BABA CODED BY THE CYBER BABA")
chars = string.printable

password = input("Enter Password to find: ")

max_length = 10

start_time = time.time()

for length in range(1, max_length + 1):
    for combination in itertools.product(chars, repeat=length):
        candidate = "".join(combination)
        print("Trying password:", candidate)
        if candidate == password:
            end_time = time.time()
            print("HEY ICC ARMY YOUR I Password found:", candidate)
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            raise SystemExit
