import time
import pyautogui
import pytest
from config import WEBDRIVER, LOG
from loging import loging

def test_img_recog():

    username = "visual_user"
    loging.loging(username)

    time.sleep(3)

    try:
        res = pyautogui.locateOnScreen("bag.png")
        LOG.info("Image found at location:", res)
        
    except pyautogui.ImageNotFoundException:
        LOG.info("The image is not found")

    WEBDRIVER.quit()


