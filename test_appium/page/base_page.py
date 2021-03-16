# 存放公共的方法，比如init方法 在每个page里都有 就把init方法单独拿出来
# 其他类可以继承父类
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 弹框的基本类型
    _black_list = [
        (By.XPATH, "//*[text='确认']"),
        (By.XPATH, "//*[text='下次再说']"),
        (By.XPATH, "//*[text='确定']")
    ]

    __max_num = 3
    _error_num = 0

    # 指定类型  定义driver的默认值是None
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # find方法进行封装 如果是元祖 直接解包
    def find(self, locator, value: str = None):
        ele: WebElement
        try:
            if isinstance(locator, tuple):
                ele = self._driver.find_element(*locator)
            else:
                ele = self._driver.find_element(locator, value)
                self._error_num = 0
                self._driver.implicitly_wait(10)
                return ele
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self.__max_num:
                raise e
            self._error_num += 1

            # 遍历弹框
            for ele1 in self._black_list:
                elelist = self._driver.find_elements(*ele1)
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.find(locator, value)
            raise e
