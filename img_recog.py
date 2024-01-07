from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"
username = "visual_user"
password = "secret_sauce"

driver.get(url)
username_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")

username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

driver.maximize_window()

time.sleep(3)

try:
    res = pyautogui.locateOnScreen("bag.png")
    print("Image found at location:", res)
    
except pyautogui.ImageNotFoundException:
    print("The image is not found")

driver.quit()


