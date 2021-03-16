from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW():
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
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text= '阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    @pytest.mark.skip
    def test_attr(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # enabled是方法 text和location的元素的属性
        search = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search == True:
            element.click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        element1 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text= '阿里巴巴']")
        # get_attrubute方法
        element2 = element1.get_attribute("displayed")
        if element2 == 'true':
            print("搜索成功")
        else:
            print("搜索失败")

    # 页面滑动操作
    def test_touchaction1(self):
        action = TouchAction(self.driver)
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    #元素定位打印股票价格
    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text= '阿里巴巴']").click()
        #显式等待
        locator = (By.XPATH, '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        current = self.driver.find_element(*locator).text
        assert float(current) > 200

    def test_uiautomator(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new Uiselector().resourceId("com.xueqiu.android:id/login_account")').send_keys("username")
        self.driver.find_element_by_android_uiautomator('new Uiselector().resourceId("com.xueqiu.android:id/login_password")').send_keys("username")
        self.driver.find_element_by_android_uiautomator('new Uiselector().resourceId("com.xueqiu.android:id/button_next")').click()
     #   self.driver.find_element_by_android_uiautomator('new Uiselector().resourceId("com.xueqiu.android:id/tab_name").text("我的')'




if __name__ == '__main__':
    pytest.main()
