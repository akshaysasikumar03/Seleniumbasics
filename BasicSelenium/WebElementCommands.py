import time

from selenium.webdriver.common.by import By

from BasicSelenium.Basic import Basic


class Webelementcommands(Basic):
    def verify_commands(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        textbox=self.driver.find_element(By.XPATH,"//input[@id='single-input-field']")
        textbox.send_keys("Akshay")
        textmessage=self.driver.find_element(By.XPATH,"//button[@id='button-one']")
        textmessage.click()
        showmessage=self.driver.find_element(By.XPATH,"//div[@id='message-one']")
        print(showmessage.text)
        print(textmessage.is_displayed())
        print(textmessage.is_enabled())
        textbox.clear()
        time.sleep(5)
webele=Webelementcommands()
webele.initialize_browser()
webele.verify_commands()
