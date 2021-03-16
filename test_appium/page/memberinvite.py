from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class MemberInvite(BasePage):

    def add_member_manul(self):
        from test_appium.page.contacadd import ContacAdd
        self.find(By.XPATH, "//*[@text = '手动输入添加']").click()
        return ContacAdd(self._driver)

    def goto_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text
        #return "toast"