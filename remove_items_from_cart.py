from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"
username = "problem_user"
password = "secret_sauce"

driver.get(url)
username_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")

username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

time.sleep(2)

try:
    add_item = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    add_item.click()

    time.sleep(2)

    remove_item = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
    remove_item.click()

    wait = WebDriverWait(driver, 1)
    element = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
    
except Exception as e:
    print(f" Item cannot be remove: Test failed: \n {e}")
    
finally:
    driver.quit()