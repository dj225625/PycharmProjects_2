import pytest
import yaml

from test_ui.page.app import App
from test_ui.test_case.test_case import TestBase


class TestMain(TestBase):
    #使用pytest的参数化方式  声明2个变量 value1和value2
    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self, value1, value2):
        # print(value1)
        # print(value2)
        #app = App()
        self.app.start().main().goto_search()

    def test_windows(self):
        #app = App()
        self.app.start().main().goto_windows()