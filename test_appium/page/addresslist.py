from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage
from test_appium.page.memberinvite import MemberInvite


class AddressList(BasePage):


    def add_member(self):
        self.find(By.XPATH, "//*[@text = '添加成员']").click()
        return MemberInvite(self._driver)