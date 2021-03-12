from time import sleep

from test_wexin_main.page.main import Main


class TestAddMemeber:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        # assert self.main.goto_add_member().add_member()
        add_memeber = self.main.goto_add_member()
        add_memeber.add_member()
        # 断言新创建的名称是否在list列表中
        assert "aaaa" in add_memeber.get_member()
