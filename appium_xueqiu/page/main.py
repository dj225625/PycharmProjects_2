from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    #进入行情页
    def goto_market(self):
        #先定位爷爷 再定位孙子 点击行情
        self.find(By.XPATH,"//*[@resource-id ='android:id/tabs']//*[@text='行情']").click()
        return Market(self._driver)