from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class ContacAdd(BasePage):

    def input_name(self):
        name_element = self.find(By.XPATH, "//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        name_element.send_keys("dongjuan5")
        return self

    def set_gender(self):
        self.find(By.XPATH, "//*[@text='性别']/..//*[contains(@class,'TextView') and @text='男']").click()
        self.find(By.XPATH, "//*[@text = '男']").click()
        self.find(By.ID,"com.tencent.wework:id/esg").click()
        return self

    def input_phone(self):
        phone_element = self.find(By.XPATH, "//*[@text='手机　']/..//*[contains(@class,'EditText')]")
        phone_element.send_keys("15258345662")
        return self

    def click_save(self):
        from test_appium.page.memberinvite import MemberInvite
        self.find(By.ID, "com.tencent.wework:id/aj_").click()
        return MemberInvite(self._driver)
