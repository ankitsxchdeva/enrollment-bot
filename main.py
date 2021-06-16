import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv()
PATH = './geckodriver'

driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://my.ucsc.edu/")
time.sleep(2) # wait for redirect to login page

driver.find_element_by_id("username").send_keys(os.environ.get("user"))
driver.find_element_by_id("password").send_keys(os.environ.get("pass"))
driver.find_element_by_xpath('//button[text()="Log in"]').click()
time.sleep(4) # wait for redirect
#driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[2]/div/label/input').click()
driver.find_element_by_xpath('//fieldset/div[1]/button')

time.sleep(5) # wait for user to approve 2fa

#driver.quit()
