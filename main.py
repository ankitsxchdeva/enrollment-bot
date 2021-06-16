import time
import datetime
import os
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
PATH = './geckodriver'
driver = webdriver.Firefox(executable_path=PATH)
target_time = datetime.datetime(2021, 6, 16, 2, 33, 0) # year, month, day, hour, minute

print("Target time is " + target_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Current time is " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def click(id_str):
    driver.find_element_by_id(id_str).click()

# Initial
driver.get("https://my.ucsc.edu/")
time.sleep(2) 

# Login
driver.find_element_by_id("username").send_keys(os.environ.get("user"))
driver.find_element_by_id("password").send_keys(os.environ.get("pass"))
driver.find_element_by_xpath('//button[text()="Log in"]').click()
time.sleep(2)

# Handle Duo 2FA
driver.switch_to.frame("duo_iframe")
driver.find_element_by_name("dampen_choice").click()
driver.find_element_by_xpath("//*[@id='auth_methods']/fieldset/div[1]/button").click()
print("Waiting for duo 2FA")
time.sleep(5)

# Enter non-portal in normal mode
driver.switch_to.default_content()
click("shibSubmit")
time.sleep(2)
click("win0divPTNUI_LAND_REC_GROUPLET$5")
time.sleep(2)

# Wait until target time to enroll into classes
if(target_time > datetime.datetime.now()):
    time.sleep((target_time - datetime.datetime.now()).total_seconds())
print("Enrolling now! Time is " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Select the correct term
driver.get("https://my.ucsc.edu/psc/csprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=CAR&EMPLID=1829475&ENRL_REQUEST_ID=&INSTITUTION=INST&STRM=TERM")
time.sleep(1)
click("SSR_DUMMY_RECV1$sels$0$$0")
click("DERIVED_SSS_SCT_SSR_PB_GO")
time.sleep(1)
click("DERIVED_REGFRM1_LINK_ADD_ENRL$82$")
time.sleep(1)
click("DERIVED_REGFRM1_SSR_PB_SUBMIT")
print("Tried to enroll, please check for any errors.")

time.sleep(10)
driver.quit()

