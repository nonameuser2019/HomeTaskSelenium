from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

main_url = 'https://demoqa.com/webtables'
users_row_selector = '.rt-tr-group'
change_users_btn_selector = 'span[title="Edit"]'
delete_users_btn_selector = 'span[title="Delete"]'
users_data_row_selector = '.rt-td'
search_input_selector = '#searchBox'

#selectors for user card
first_name_selector = '#firstName'
age_selector = '#age'
submit_btn_selector = '#submit'


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser


def test_change_user_data(browser:webdriver.Chrome):
    # test data
    new_name = 'Test'
    new_age = 21

    # change name and age task 5
    browser.get(main_url)

    change_btn = browser.find_elements(By.CSS_SELECTOR, change_users_btn_selector)[0]
    change_btn.click()

    first_name_field = browser.find_element(By.CSS_SELECTOR, first_name_selector)
    first_name_field.clear()
    first_name_field.send_keys(new_name)

    age_field = browser.find_element(By.CSS_SELECTOR, age_selector)
    age_field.clear()
    age_field.send_keys(new_age)

    submit_btn = browser.find_element(By.CSS_SELECTOR, submit_btn_selector)
    submit_btn.click()

    # get first name after changing
    current_name = browser.find_elements(By.CSS_SELECTOR, users_data_row_selector)[0].text
    current_age = browser.find_elements(By.CSS_SELECTOR, users_data_row_selector)[2].text
    assert new_name == current_name
    assert new_age == int(current_age)
    browser.quit()


def test_check_user_search(browser: webdriver.Chrome):
    #task 6 find user by name
    browser.get(main_url)
    search_field = browser.find_element(By.CSS_SELECTOR, search_input_selector)
    search_field.clear()
    search_field.send_keys('Kie')
    current_name = browser.find_elements(By.CSS_SELECTOR, users_data_row_selector)[0].text
    assert current_name == 'Kierra'
    browser.quit()


def test_check_delete_user(browser: webdriver.Chrome):
    #task 7 delete first user
    browser.get(main_url)
    #find delete button
    delete_btn = browser.find_elements(By.CSS_SELECTOR, delete_users_btn_selector)[0]
    #use button
    delete_btn.click()
    #check that first user is Alden
    current_name = browser.find_elements(By.CSS_SELECTOR, users_data_row_selector)[0].text
    assert current_name == 'Alden'



