from appium import webdriver

from test_appium.page.base_page import BasePage

from test_ui.page.main import Main


class App(BasePage):
    def start(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = "com.xueqiu.android"
        desired_caps['appActivity'] = ".view.WelcomeActivityAlias"
        desired_caps['noReset'] = "true"

        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待 是全局的动态的  每次查到元素  每0.5秒查找1次  最多查找5秒
        self._driver.implicitly_wait(5)

        #返回自身
        return self

    def main(self) -> Main:
        return Main(self._driver)