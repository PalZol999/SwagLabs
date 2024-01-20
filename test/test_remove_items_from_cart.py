from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from config import WEBDRIVER, LOG
import pytest
import time
from loging import loging

def test_remove_items_from_cart():
    username = "problem_user"
    loging.loging(username)

    try:
        add_item = WEBDRIVER.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item.click()

        time.sleep(2)

        remove_item = WEBDRIVER.find_element(By.ID, "remove-sauce-labs-bike-light")
        remove_item.click()

        wait = WebDriverWait(WEBDRIVER, 1)
        element = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
        
    except Exception as e:
         LOG.info(f" Item cannot be remove: Test failed: \n {e}")
        
    finally:
        WEBDRIVER.quit()