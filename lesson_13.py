from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    wait = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.TAG_NAME, 'button').click()
    val = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(math.log(abs(12 * math.sin(val))))
    browser.find_element(By.ID, 'solve').click()
finally:
    sleep(90)
    browser.quit()
