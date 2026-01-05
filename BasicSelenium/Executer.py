import time

from selenium.webdriver.common.by import By

from BasicSelenium.Basic import Basic

class Executer(Basic):
    def verify_javascript_executor(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        # Locate the button with XPath
        show_message_button = self.driver.find_element(By.XPATH, "//button[@id='button-one']")

        # JavaScript Executor for clicking the button
        self.driver.execute_script("arguments[0].click();", show_message_button)

        # Scroll down by 200px
        self.driver.execute_script("window.scrollBy(0, 200);")


        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
execute=Executer()
execute.initialize_browser()
execute.verify_javascript_executor()