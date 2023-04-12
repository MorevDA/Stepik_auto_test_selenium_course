from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import math
from time import sleep

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = wd.Chrome()
    browser.get(link)
    answer = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    answer.click()
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(30)
    browser.quit()
