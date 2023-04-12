from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)
    print(x + y)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    print(x + y)
    select.select_by_value(str(x +y))
    button = browser.find_element(By.TAG_NAME, 'button').click()
    print(x+y)

finally:
    sleep(13)
    browser.quit()
