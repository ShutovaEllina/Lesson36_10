from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pytest
import unittest

def test_button_add_to_cart_exist(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    def is_element_on_page(webdriver, by, value):
        try:
            webdriver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

        assert is_element_on_page(browser, By.CSS_SELECTOR, '#add_to_basket_form > button'), \
            'The Add to Cart button does not exist on the page.'

if __name__ == "__main__":
    unittest.main()
