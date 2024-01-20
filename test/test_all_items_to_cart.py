from selenium.webdriver.common.by import By
import time
import pytest
from config import WEBDRIVER, LOG, ITEMS_TO_ADD 
from loging import loging

def test_all_items_to_cart():
    
    username = "error_user"
    loging.loging(username)

    try:
        for item_id in ITEMS_TO_ADD:
            add_item = WEBDRIVER.find_element(By.ID, item_id)
            add_item.click()
            time.sleep(2)  

        total_item = WEBDRIVER.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")

        actual_count = int(total_item.text)
        expected_count = len(ITEMS_TO_ADD)

        if actual_count == expected_count:
            LOG.info(f"Test successful! Total items: {actual_count}")
        else:
            LOG.info(f"Test failed! Expected items: {expected_count}, Actual items: {actual_count}")

    except Exception as e:
        LOG.info(f"Test failed: \n {e}")

    finally:
        WEBDRIVER.quit()
