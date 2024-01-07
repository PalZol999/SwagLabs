from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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

print(f"Login Time: {elapsed_time} seconds")

with open("login_report.txt", "w") as file:
    file.write(f"Login Time: {elapsed_time} seconds")

driver.quit()
