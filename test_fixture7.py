import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895"])#, "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    area = browser.find_element_by_css_selector("#ember78")
    area.send_keys(str(answer))
    browser.find_element_by_class_name(".submit-submission")
    browser.click()
    time.sleep(10)