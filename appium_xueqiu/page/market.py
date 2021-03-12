from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):
    #进入搜索页
    def goto_search(self):
        #点击搜索
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)
