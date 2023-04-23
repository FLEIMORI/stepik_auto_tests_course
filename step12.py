import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import os 


try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    prompt = browser.switch_to.alert
    prompt.accept()
    
    x = int(browser.find_element(By.ID, "input_value").text)
    code = math.log(abs(12*math.sin(x)))
    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(code)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()