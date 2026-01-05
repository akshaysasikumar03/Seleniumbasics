from BasicSelenium.Basic import Basic


class BrowserCommands(Basic):
    def verify_commands(self):
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        print(self.driver.page_source)
commands = BrowserCommands()
commands.initialize_browser()
commands.verify_commands()