from time import sleep
from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeb():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['noReset'] = "true"
        desired_caps['chromedriverExcutable'] = "D:\Study\chromedriver_52.0.2743"

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_browser(self):
        # 交易控件是native页面
        self.driver.find_element(By.XPATH, '//*[@text="交易"]').click()

        # A股开户是webview页面，使用devtools进行定位
        elelocator = (By.XPATH, '//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')

        # 从native切换到webview
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])

        # 显式等待
        WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable(elelocator))
        # 定位元素 A股户
        self.driver.find_element(*elelocator).click()

        window_1 = self.driver.window_handles[-1]
        self.driver.switch_to.window(window_1)

        # 显式等待  手机号码框能够出现
        locator_phone = (By.ID, 'phone-number')
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(locator_phone))
        # 使用手机号码 验证码
        self.driver.find_element(*locator_phone).send_keys("12345678901")
        self.driver.find_element_by_id("code").send_keys("1234")
        # 点击立即开户
        self.driver.find_element(By.XPATH, '//*[@text="立即开户"]').click()
