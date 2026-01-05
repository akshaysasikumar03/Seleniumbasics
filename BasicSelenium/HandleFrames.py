import time

from selenium.webdriver.common.by import By

from BasicSelenium.Basic import Basic


class Handleframes(Basic):
    def verify_handleframes(self):
        self.driver.get("https://demoqa.com/frames")
        totalframes=self.driver.find_elements(By.TAG_NAME,"iframe")
        print(totalframes)
        print(len(totalframes))
        time.sleep(5)
        iframeelement=self.driver.find_element(By.XPATH,"//iframe[@id='frame1']")
        self.driver.switch_to.frame(iframeelement)
        samplehead=self.driver.find_element(By.XPATH,"//h1[@id='sampleHeading']")
        print(samplehead.text)
        time.sleep(5)
        self.driver.switch_to.default_content()
hframes=Handleframes()
hframes.initialize_browser()
hframes.verify_handleframes()