from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"
username = "locked_out_user"
password = "secret_sauce"

try:
    driver.get(url)
    username_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")

    username_field.send_keys(username)
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")))

    print("Login successful!")

except Exception as e:
    print(f"Login failed: \n {e}")
 
finally:
    driver.quit()