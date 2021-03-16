from requests_wework.api.address import Address

class TestAddress:
    def setup(self):
        self.address = Address()

    # def test_token(self):
    #     print(self.address.get_token())

    def test_cteate(self):
        print(self.address.create("zhangsan12345678","dongjuan","12345685588"))

    def test_update(self):
        print(self.address.update("zhangsan12345678", "dongjuan123", "12345685588"))

    def test_delete(self):
        print(self.address.delete(("zhangsan12345678")))