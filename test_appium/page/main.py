#首页的page
from selenium.webdriver.common.by import By

from test_appium.page.addresslist import AddressList
from test_appium.page.base_page import BasePage


class Main(BasePage):

    def goto_message(self):
        pass
    def goto_address(self):
        #返回添加成员
        self.find(By.XPATH, "//*[@text = '通讯录']").click()
        return AddressList(self._driver)

    def goto_work(self):
        pass

    def goto_profile(self):
        pass


