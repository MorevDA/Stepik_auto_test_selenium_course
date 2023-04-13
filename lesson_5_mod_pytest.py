from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pytest


def registration(url: str) -> str:
    browser = wd.Chrome()
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "input.first:required").send_keys('Vasia')
    browser.find_element(By.CSS_SELECTOR, "input.second:required").send_keys("Pupkin")
    browser.find_element(By.CSS_SELECTOR, "input.third:required").send_keys("VP@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    return browser.find_element(By.TAG_NAME, "h1").text


link_test_1 = 'http://suninjuly.github.io/registration1.html'
link_test_2 = 'http://suninjuly.github.io/registration2.html'


def test_1():
    result = registration(link_test_1)
    assert result == "Congratulations! You have successfully registered!"


def test_2():
    assert registration(link_test_2) == "Congratulations! You have successfully registered!"


if __name__ == "__main__":
    pytest.main()
