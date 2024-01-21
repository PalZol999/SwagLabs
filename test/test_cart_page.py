from selenium.webdriver.common.by import By
from config import WEBDRIVER, LOG, ITEMS_TO_ADD 
from loging import loging
import pytest
import time
from items.items import add_items_to_cart

def test_cart_page():
     
    username = "visual_user"
    loging.loging(username)

    try:
        actual_count, expected_count = add_items_to_cart(WEBDRIVER, ITEMS_TO_ADD)

        if actual_count == expected_count:
             LOG.info(f"Test successful! Total items: {actual_count}")
        else:
             LOG.info(f"Test failed! Expected items: {expected_count}, Actual items: {actual_count}")

    except Exception as e:
         LOG.info(f"Test failed: \n {e}")

    cart_icon = WEBDRIVER.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")   
    cart_icon.click()

    time.sleep(2)
    WEBDRIVER.quit()
