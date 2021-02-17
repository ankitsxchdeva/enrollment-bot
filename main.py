import time
from selenium import webdriver
driver = webdriver.Firefox(executable_path='/Users/ankitsachdeva/PycharmProjects/autoEnrollUCSC/geckodriver') #this path must point to where geckdriver is installed
driver.get('https://google.com')
