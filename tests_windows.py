from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


main_url = 'https://demoqa.com/browser-windows'
new_tab_btn_locator = '#tabButton'
new_page_title_locator = '#sampleHeading'
new_window_btn_locator = '#windowButton'
new_window_msg_selector = '#messageWindowButton'
main_header_locator = '.main-header'
button_list_selector = '#browserWindows'



@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser


def test_task8(browser):
    browser.get(main_url)
    main_window = browser.current_window_handle
    new_tab_btn = browser.find_element(By.CSS_SELECTOR, new_tab_btn_locator)
    new_tab_btn.click()
    # use handle with index 1
    browser.switch_to.window(browser.window_handles[1])
    title = browser.find_element(By.CSS_SELECTOR, new_page_title_locator).text
    assert title == 'This is a sample page'
    #close tab
    browser.close()
    # switch to main window because browser changed context
    browser.switch_to.window(main_window)
    # get page title
    main_page_h1 = browser.find_element(By.CSS_SELECTOR, main_header_locator).text
    assert main_page_h1 == 'Browser Windows'
    new_window_btn = browser.find_element(By.CSS_SELECTOR, new_window_btn_locator)
    new_window_msg_btn = browser.find_element(By.CSS_SELECTOR, new_window_msg_selector)
    #print all button names
    print(f'\nnew_tab_btn: {new_tab_btn.text}, new_window_btn: {new_window_btn.text},'
          f' new_window_msg_btn: {new_window_msg_btn.text}')





