import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button2 = browser.find_element(By.ID, "book")
    xui = WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button2.click()

    x = int(browser.find_element(By.ID, "input_value").text)
    code = math.log(abs(12*math.sin(x)))
    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(code)
    
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    time.sleep(10)
    browser.quit()