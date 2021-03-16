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
        desired_caps['browserName'] = 'Browser'
        desired_caps['noReset'] = "true"
        #desired_caps['chromedriverExcutable'] = "D:\Study\chromedriver_52.0.2743"

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com/")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")

        #使用显式等待判断一下 百度一下元素是否可见
        search = (By.ID, "index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search))
        self.driver.find_element(*search).click()
        sleep(5)