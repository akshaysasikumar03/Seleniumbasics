import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from BasicSelenium.Basic import Basic


class Multipleelements(Basic):
    def verify_dropdowns(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        dropdown=self.driver.find_element(By.XPATH,"//select[@id='dropdowm-menu-1']")
        select=Select(dropdown)
        select.select_by_index(1)
        select.select_by_value("python")
        select.select_by_visible_text("JAVA")
        time.sleep(5)
    def verify_checkboxes(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        checkbox=self.driver.find_element(By.XPATH,"//input[@value='option-1']")
        checkbox.click()
        print(checkbox.is_displayed())
        print(checkbox.is_selected())
        time.sleep(5)
    def verify_radiobutton(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        self.driver.find_element(By.XPATH,"//input[@value='blue']").click()
        time.sleep(5)
verifydropdowns=Multipleelements()
verifydropdowns.initialize_browser()
#verifydropdowns.verify_dropdowns()
#verifydropdowns.verify_checkboxes()
verifydropdowns.verify_radiobutton()

