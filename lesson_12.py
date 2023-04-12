from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calk(x):
    return math.log(abs(12 * math.sin(x)))


link = 'http://suninjuly.github.io/redirect_accept.html'
#link = 'http://suninjuly.github.io/redirect_page.html?'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    window_new = browser.window_handles[1]
    browser.switch_to.window(window_new)
    data = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calk(data))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(9)
    browser.quit()



