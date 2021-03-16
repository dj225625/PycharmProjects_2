# 对driver 或者元素查找封装
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 实例变量  子类可以使用
    _driver: WebDriver = None
    #黑名单
    _black_list=[(By.ID,"iv_close")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

#对find进行封装 实现异常捕获
    def find(self, locator, value):
        try:
            #没有黑名单 就正常返回
            element = self._driver.find_element(locator, value)
            return  element
        #遍历黑名单
        except:
            # 遍历黑名单
            for black in self._black_list:
                #若发现了黑名单
               elements = self._driver.find_elements(*black)
                #若长度大于0  代表找到了黑名单
               if len(elements) > 0:
                   #默认取出第一个元素 进行点击
                    elements[0].click()
                    break
            #再次去查元素
            return self.find(locator, value)


    def steps(self, path):
        #打开路径下的yaml文件
        with open(path) as f:
            #读取yaml文件的内容
            steps = yaml.safe_load(f)
            print(steps)
            #[{'by': 'id', 'locator': 'tv_search', 'action': 'click'}]

        element = None
        #循环遍历yaml文件里的内容
        for  step in steps:
            if "by" in step.keys():
                #step["by"]代表提取by的值
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                #提取action
                action = step["action"]
                #如果action等于click，就点击
                if action == "click":
                    element.click()


