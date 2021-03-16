from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestAttribute():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = "true"
        # 不需要每次运行脚本  都要先关闭应用程序 再打开；页面在哪个页面 就继续操作；但是执行完以后不会关闭页面
        desired_caps['dontStopAppOnReset'] = 'true'
        # 跳过设置等
        desired_caps['skipDeviceInitialization'] = 'true'
        # 支持中文输入
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        pass
    @pytest.mark.parametrize('key,type,price',[
        ('alibaba','BABA',251),
        ('xiaomi','01810',28)])
    def test_search(self,key,type,price):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(key)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.xueqiu.android:id/name']").click()
        sleep(3)
        current_price = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current = float(current_price.text)

        #expeted_price = 251
        assert_that(current, close_to(price, price * 0.1))

