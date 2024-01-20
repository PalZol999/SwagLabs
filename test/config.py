from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

WEB_URL = "https://www.saucedemo.com/"
ADMIN_PW = "secret_sauce"

WEBDRIVER = webdriver.Chrome()

def find_element(locator):
    return WEBDRIVER.find_element(*locator)

selenium_logger = logging.getLogger('selenium')
selenium_logger.setLevel(logging.INFO)
LOG = selenium_logger

ITEMS_TO_ADD = [
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-onesie",
    "add-to-cart-test.allthethings()-t-shirt-(red)"
]

__all__ = ['WEBDRIVER', 'LOG']
