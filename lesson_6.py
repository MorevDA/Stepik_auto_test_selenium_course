from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep



link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)
sleep(10)

try:
    people_radio = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    people_checked = people_radio.get_attribute('disabled')
    print("submit: ", people_checked)
    #assert people_checked == "true", "People radio is not selected by default"
finally:
    sleep(10)
    browser.quit()