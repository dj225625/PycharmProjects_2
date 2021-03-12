from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_login.register import Register


class Login:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # click register
        #self.driver.find_element_by_css_selector('login_registerBar_link').click()
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)
