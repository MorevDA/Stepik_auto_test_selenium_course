from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep

link = 'http://suninjuly.github.io/registration2.html'

browser = wd.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
    input1.send_keys('Vasia')
    input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    input2.send_keys("Pupkin")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
    input3.send_keys("VP@gmail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    sleep(6)
    browser.quit()