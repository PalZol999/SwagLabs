from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"
username = "error_user"
password = "secret_sauce"

driver.get(url)
username_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")

username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

time.sleep(2)

try:
    items_to_add = ["add-to-cart-sauce-labs-bike-light", 
                    "add-to-cart-sauce-labs-backpack", 
                    "add-to-cart-sauce-labs-bolt-t-shirt", 
                    "add-to-cart-sauce-labs-fleece-jacket",
                    "add-to-cart-sauce-labs-onesie",
                    "add-to-cart-test.allthethings()-t-shirt-(red)"]

    for item_id in items_to_add:
        add_item = driver.find_element(By.ID, item_id)
        add_item.click()
        time.sleep(1)  

    total_item = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")

    actual_count = int(total_item.text)
    expected_count = len(items_to_add)

    if actual_count == expected_count:
        print(f"Test successful! Total items: {actual_count}")
    else:
        print(f"Test failed! Expected items: {expected_count}, Actual items: {actual_count}")

except Exception as e:
    print(f"Test failed: \n {e}")

finally:
    driver.quit()
