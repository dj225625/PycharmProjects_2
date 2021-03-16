# 第一个page页面，主要针对app的基本操作
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:

            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'

            # 不会清除登陆的缓存信息
            desired_caps['noReset'] = "true"

            # 不需要每次运行脚本  都要先关闭应用程序 再打开；页面在哪个页面 就继续操作；但是执行完以后不会关闭页面
            desired_caps['dontStopAppOnReset'] = 'true'

            # 跳过设置等
            desired_caps['skipDeviceInitialization'] = 'true'

            # 支持中文输入
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            #appium提供的方法 直接启动应用
            self._driver.launch_app()
        # 隐式等待
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    #  -> Main指定返回的类型
    def main(self) -> Main:
        #传递driver
        return Main(self._driver)
