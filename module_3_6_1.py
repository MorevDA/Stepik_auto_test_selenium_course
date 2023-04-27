import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
import math

login = ''
password = ''


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('page', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, page, login, password):
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)
    sleep(4)
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(login)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
    sleep(9)
    browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    sleep(9)
    assert browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text == 'Correct!'
    print(browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text)
