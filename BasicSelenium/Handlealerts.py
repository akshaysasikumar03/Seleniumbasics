import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from BasicSelenium.Basic import Basic

class Handlealerts(Basic):
    def verify_simplealerts(self):
        self.driver.get("https://demoqa.com/alerts")
        simpleclick=self.driver.find_element(By.XPATH,"//button[@id='alertButton']")
        time.sleep(2)
        simpleclick.click()
        simplealert=self.driver.switch_to.alert
        print(simplealert.text)
        simplealert.accept()

    def confirm_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
        confirmalert = self.driver.switch_to.alert
        #confirmalert.accept()
        confirmalert.dismiss()
        time.sleep(2)
    def prompt_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
        promptalert = self.driver.switch_to.alert
        promptalert.send_keys("Akshay")   #sendkeys to add text to prompt
        promptalert.accept()
        time.sleep(2)
alerthandle=Handlealerts()
alerthandle.initialize_browser()
#simplealert.verify_simplealerts()
#alerthandle.confirm_alert()
alerthandle.prompt_alert()










