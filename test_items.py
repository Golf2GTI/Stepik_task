from selenium.webdriver.common.by import By
import time

def test_add_to_cart_button_exists(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    x = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert x, 'NoSuchElementException'

