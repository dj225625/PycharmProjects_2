from test_appium.page.app import App


class TestWeixin:
    def setup(self):
        #初始化app
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        element = self.main.goto_address().add_member().add_member_manul().input_name().input_phone().set_gender().click_save()
        assert '成功' in element.goto_toast()