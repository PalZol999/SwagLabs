from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from config import WEBDRIVER, LOG
from loging import loging

def test_user_login():

    username = "performance_glitch_user"
    
    start_time = time.time()
    loging.loging(username)
    end_time = time.time()
    
    elapsed_time = end_time - start_time

    total_time_message = f"Total Time: {elapsed_time} seconds"
    LOG.info(total_time_message)

    if elapsed_time > 2:
         LOG.info("Test failed: Login time exceeded 2 seconds")
    else:
         LOG.info("Test passed: Login time within 2 seconds")

    WEBDRIVER.quit()
