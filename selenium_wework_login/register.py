from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        # send content
        self.driver.find_element_by_id('corp_name').send_keys("hello")
        sleep(3)
        self.driver.quit()
        return True
