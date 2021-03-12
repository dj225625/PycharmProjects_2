from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self,name):
        #输入alibaba
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
        self.find(By.XPATH,"//*[@text='BABA']").click()
        #使用相对定位，定位到加自选 并且进行参数化
        self.find(By.XPATH,f"//*[@resource-id='com.xueqiu.android:id/ll_stock_item_container']//*[@text='{name}']/../..//*[@text='加自选']").click()

    def is_choose(self,name):
        eles = self.finds(By.XPATH,f"//*[@resource-id='com.xueqiu.android:id/ll_stock_item_container']//*[@text='{name}']/../..//*[@text='已添加']")
        return len(eles) > 0