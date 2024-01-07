from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"
username = "performance_glitch_user"
password = "secret_sauce"

start_time = time.time()

driver.get(url)
username_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")

username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

end_time = time.time()
elapsed_time = end_time - start_time

total_time_message = f"Total Time: {elapsed_time} seconds"
print(total_time_message)

with open("login_report.txt", "w") as file:
    file.write(total_time_message)

if elapsed_time > 2:
    print("Test failed: Login time exceeded 2 seconds")
else:
    print("Test passed: Login time within 2 seconds")

driver.quit()
