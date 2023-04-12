from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    data = browser.find_element(By.ID, 'input_value').text
    print(int(data))
    browser.find_element(By.ID, "answer").send_keys(calc(int(data)))
    browser.find_element(By.CLASS_NAME, 'form-check-label').click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, 'robotsRule'))
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    sleep(10)
    browser.quit()
