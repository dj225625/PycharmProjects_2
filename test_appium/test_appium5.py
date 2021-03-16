from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
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
        self.driver.quit()

    def test_touchaction(self):
        action = TouchAction(self.driver)
        action.press(x=118, y=174).wait(200).move_to(x=365 ,y=174).wait(200).move_to(x=592, y=174).wait(200).move_to(x=600, y=416).wait(200).move_to(x=598, y=657).release().perform()