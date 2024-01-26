from selenium.webdriver.common.by import By
import pytest
from config import WEBDRIVER, LOG, ITEMS_TO_ADD 
from loging import loging
from items.items import add_items_to_cart

def test_all_items_to_cart():
    
    username = "error_user"
    loging.loging(username)

    try:
        actual_count, expected_count = add_items_to_cart(WEBDRIVER, ITEMS_TO_ADD)

        if actual_count == expected_count:
            LOG.info(f"Test successful! Total items: {actual_count}")
        else:
            LOG.info(f"Test failed! Expected items: {expected_count}, Actual items: {actual_count}")

    except Exception as e:
        LOG.info(f"Test failed: \n {e}")

    finally:
        WEBDRIVER.quit()
