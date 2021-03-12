from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_wexin_main.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        sleep(3)
        self.find(By.ID,'username').send_keys("bbbb")
        self.find(By.ID, 'memberAdd_acctid').send_keys("bbbb")
        self.find(By.ID, 'memberAdd_phone').send_keys("15234586621")

        #self._driver.find_element_by_id("username").send_keys("bbbb")
        #self._driver.find_element_by_id("memberAdd_acctid").send_keys("bbbb")
        #self._driver.find_element_by_id("memberAdd_phone").send_keys("15234586621")
        sleep(3)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        #self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(5)
        # self._driver.quit()
        return True
    #断言 检查新建的成员是否成功   思路：成员名称是否在所有成员列表中
    def get_member(self):
        #elements返回多个元素,所有成员名存在一个变量中
        #elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

        #检查多选框按钮是否可被点击
        self.wait_for_click(By.CSS_SELECTOR, '.ww_checkbox')

        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        #取出某个元素的title属性,追加到列表中,并且返回整个列表，这样可以拿到所有的名称
        # list = []
        # for element in elements:
        #     list.append(element.get_attribute("title"))
        #
        # return list

        #直接生成list,叫做列表推导式
        return [element.get_attribute("title") for element in elements]

