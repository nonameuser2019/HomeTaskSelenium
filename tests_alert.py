from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

main_url = 'https://demoqa.com/alerts'
alert_btn_selector = '#alertButton'
allert_btn_with_wait_selector = '#timerAlertButton'
confirm_btn_selector = '#confirmButton'
prompt_btn_selector = '#promtButton'
prompt_result_selector = '#promptResult'


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser


def test_check_alert_message(browser):
    #task 9 part 1
    browser.get(main_url)
    allert_btn = browser.find_element(By.CSS_SELECTOR, alert_btn_selector)
    allert_btn.click()
    #switch_to allert
    allert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    assert allert.text == 'You clicked a button'
    browser.quit()


def test_all_btn_click(browser):
    browser.get(main_url)
    allert_btn_with_wait = browser.find_element(By.CSS_SELECTOR, allert_btn_with_wait_selector)
    allert_btn_with_wait.click()
    #this test fail with 5 seconds wait? you need 6 seconds to success pass
    allert = WebDriverWait(browser, 6).until(EC.alert_is_present())
    assert allert.text == 'This alert appeared after 5 seconds'
    allert.accept()

    #test prompt allert
    confirm_btn = browser.find_element(By.CSS_SELECTOR, confirm_btn_selector)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(confirm_btn)).click()
    confirm = browser.switch_to.alert
    assert confirm.text == 'Do you confirm action?'
    confirm.accept()

    #test prompt allert
    prompt_btn = browser.find_element(By.CSS_SELECTOR, prompt_btn_selector)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(prompt_btn)).click()
    prompt_btn = browser.switch_to.alert
    prompt_btn.send_keys('test')
    prompt_btn.accept()
    prompt_result_test = browser.find_element(By.CSS_SELECTOR, prompt_result_selector).text
    assert prompt_result_test == 'You entered test'


