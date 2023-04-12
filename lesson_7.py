from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calck(x):
    return math.log(abs(12 * math.sin(x)))


link ="http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    val = browser.find_element(By.ID, "treasure").get_attribute('valuex')
    print(val)

    inp_value = browser.find_element(By.ID, 'answer')
    inp_value.send_keys(calck(int(val)))
    button = browser.find_element(By.ID, 'robotCheckbox')
    button.click()
    button_1 = browser.find_element(By.ID, 'robotsRule')
    button_1.click()
    button_3 = browser.find_element(By.TAG_NAME, 'button')
    button_3.click()
finally:
    sleep(15)
    browser.quit()
