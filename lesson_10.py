from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    browser.find_element(By.NAME, 'firstname').send_keys('Vasia')
    browser.find_element(By.NAME, 'lastname').send_keys('Pupkin')
    browser.find_element(By.NAME, 'email').send_keys('VP')
    browser.find_element(By.ID, 'file').send_keys(r'C:\Users\123\Downloads\beegeek.txt')
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(9)
    browser.quit()
