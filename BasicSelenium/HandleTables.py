from selenium.webdriver.common.by import By

from BasicSelenium.Basic import Basic


class Handletables(Basic):
    def verify_tables(self):
        self.driver.get("https://selenium.qabible.in/table-pagination.php")
        print(self.driver.find_element(By.XPATH,"//table[@id='dtBasicExample']").text)
        print(self.driver.find_element(By.XPATH,"//table[@id='dtBasicExample']/tbody/tr[3]/td[2]").text)
handletab=Handletables()
handletab.initialize_browser()
handletab.verify_tables()



