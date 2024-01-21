from selenium.webdriver.common.by import By
import time

def add_items_to_cart(webdriver, items_to_add):
    for item_id in items_to_add:
        add_item = webdriver.find_element(By.ID, item_id)
        add_item.click()
        time.sleep(2)

    total_item = webdriver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")
    actual_count = int(total_item.text)
    expected_count = len(items_to_add)

    return actual_count, expected_count
