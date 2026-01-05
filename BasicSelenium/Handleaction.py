import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from BasicSelenium.Basic import Basic


class Handleaction(Basic):
    def verify_rightclick(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        actionform=self.driver.find_element(By.XPATH,"//a[@class='nav-link' and @href='simple-form-demo.php']")
        actions=ActionChains(self.driver)
        actions.context_click(actionform).perform()
        time.sleep(5)
    def mousehover(self):
        actionform = self.driver.find_element(By.XPATH, "//a[@class='nav-link' and @href='simple-form-demo.php']")
        actions = ActionChains(self.driver)
        actions.move_to_element(actionform).perform()
        time.sleep(5)
    def dragdrop(self):
        self.driver.get("https://selenium.qabible.in/drag-drop.php")
        draggable=self.driver.find_element(By.XPATH,"//span[text()='Draggable n°1']")
        droppable=self.driver.find_element(By.XPATH,"//div[@id='mydropzone']")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable, droppable).perform()
        time.sleep(5)
handle=Handleaction()
handle.initialize_browser()
#handle.verify_rightclick()
#handle.mousehover()
handle.dragdrop()