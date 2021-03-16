from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestWeixin():
    def setup(self):
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

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        # 隐式等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_addcontact(self):
        self.driver.find_element(By.XPATH, "//*[@text = '通讯录']").click()
        self.driver.find_element(By.XPATH, "//*[@text = '添加成员']").click()
        self.driver.find_element(By.XPATH, "//*[@text = '手动输入添加']").click()
        name_element = self.driver.find_element(By.XPATH,"//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        name_element.send_keys("dongjuan4")

        self.driver.find_element(By.XPATH,"//*[@text='性别']/..//*[contains(@class,'TextView') and @text='男']").click()
        self.driver.find_element(By.XPATH, "//*[@text = '男']").click()
        self.driver.find_element(By.ID,"com.tencent.wework:id/esg").click()
        phone_element = self.driver.find_element(By.XPATH, "//*[@text='手机　']/..//*[contains(@class,'EditText')]")
        phone_element.send_keys("15258345652")
        self.driver.find_element(By.ID,"com.tencent.wework:id/aj_").click()

        sleep(3)
        #print(self.driver.page_source)
        #self.driver.find_element(By.XPATH, "//*[@text='添加成功']")


