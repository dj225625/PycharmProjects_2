from appium import webdriver
from selenium.webdriver.common.by import By


class TestDW():
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'

        # 不会清除登陆的缓存信息
        desired_caps['noReset'] = "true"

        # 不需要每次运行脚本  都要先关闭应用程序 再打开；页面在哪个页面 就继续操作；但是执行完以后不会关闭页面
        desired_caps['dontStopAppOnReset'] = 'true'

        # 跳过设置等
        desired_caps['skipDeviceInitialization'] = 'true'

        # 支持中文输入
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
       pass

    def teardown(self):
        pass
        #点击取消按钮

    def test_search(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text= '阿里巴巴']").click()
        #通过父级关系来定位
        self.driver.find_element(By.XPATH, "//*[@text='加自选']").click()

