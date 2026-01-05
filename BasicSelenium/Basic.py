import time

from selenium import webdriver


class Basic:
    def __init__(self):
        self.driver = None
    def initialize_browser(self):
        self.driver = webdriver.Chrome() #Webdriver syncing with chrome
        #self.driver = webdriver.Edge()
        #self.driver.get("https://selenium.qabible.in/")
        #self.driver.maximize_window()
        time.sleep(10)

    def close_browser(self):
        self.driver.quit()
        # self.driver.close()
#basicconfigration = Basic()
#basicconfigration.initialize_browser()
#basicconfigration.close_browser()