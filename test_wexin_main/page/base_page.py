from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 初始化封装
        if driver is None:

            options = Options()
            options.debugger_address = "127.0.0.1:9222"

            self._driver = webdriver.Chrome(options=options)

            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        # 地址封装
        if self._base_url != "":
            self._driver.get(self._base_url)

    # 定位元素封装
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    # 定位元素封装
    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 显式等待封装
    def wait_for_click(self, locator, time = 10):
        WebDriverWait(self._driver,time).until(expected_conditions.element_to_be_clickable(locator))


