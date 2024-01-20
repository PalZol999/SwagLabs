from config import WEB_URL, ADMIN_PW, find_element, WEBDRIVER
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def loging(username):
    WEBDRIVER.get(WEB_URL)
    username_locator = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
    password_locator = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")

    username_field = find_element(username_locator)
    password_field = find_element(password_locator)

    username_field.send_keys(username)
    password_field.send_keys(ADMIN_PW)

    time.sleep(2)
    password_field.send_keys(Keys.RETURN)

 
    