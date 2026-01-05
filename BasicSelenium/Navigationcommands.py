import time

from BasicSelenium.Basic import Basic


class NavigationCommands(Basic):
    def verify_navigation(self):
        self.driver.get("https://www.amazon.in/")
        self.driver.back()
        self.driver.forward()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(5)
commandss = NavigationCommands()
commandss.initialize_browser()
commandss.verify_navigation()



