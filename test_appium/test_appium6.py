from appium import webdriver
import pytest
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
        pass
    @pytest.mark.skip
    def test_attribute(self):
        ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(ele.get_attribute("resource-id"))
        print(ele.get_attribute("enabled"))
        print(ele.get_attribute("clickable"))
        assert 'search' in ele.get_attribute("resource-id")

    @pytest.mark.skip
    def test_assert(self):
        a = 10
        b = 20
        assert a < b
        assert 'h' in "hello"

    def test_hamcrest(self):
        #10是实际值  equal_to(10)是期望值
        # assert_that(10, equal_to(10), "这是一个提示信息")

        #close_to里面代表10上下幅度2
        #assert_that(10, close_to(10, 2))

        assert_that("asb string", contains_string("string"))