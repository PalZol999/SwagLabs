from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import WEBDRIVER, LOG
from loging import loging

def test_locked_user():

    username = "locked_out_user"
    
    try:
        loging.loging(username)

        WebDriverWait(WEBDRIVER, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")))

        LOG.info("Login successful!")

    except Exception as e:
        LOG.info(f"Login failed: \n {e}")
    
    finally:
        WEBDRIVER.quit()