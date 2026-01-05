from selenium.webdriver.common.by import By

from BasicSelenium.Basic import Basic


class Locators(Basic):
    def verify_locators(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        self.driver.find_element(By.ID,"single-input-field")
        self.driver.find_element(By.CLASS_NAME,"form-control")
        self.driver.find_element(By.TAG_NAME,"input")
        self.driver.find_element(By.NAME,"viewport")
        self.driver.find_element(By.LINK_TEXT,"Simple Form Demo")
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Simple Form")
        self.driver.find_element(By.CSS_SELECTOR,"button[id='button-one']")
        self.driver.find_element(By.XPATH,"//button[@id='button-two']")
