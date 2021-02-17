import time
from selenium import webdriver
from datetime import datetime
driver = webdriver.Firefox(executable_path='/Users/ankitsachdeva/PycharmProjects/autoEnrollUCSC/geckodriver')
driver.get('https://google.com')


class TimingCheck:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    goal_time = "00:00"

    def update_time(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M")

    def get_time(self):
        self.update_time(self)
        return self.current_time

    def print_time(self):
        self.update_time(self)
        print("The current time is ", self.current_time)


timingChecker = TimingCheck
timingChecker.print_time(timingChecker)

