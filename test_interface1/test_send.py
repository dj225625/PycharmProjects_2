from test_interface1 import env_demo


class TestApi():
    data = {
        "method": "get",
        "url": "http://abc:9999/demo.txt",
        "headers": None
    }

    def test_send(self):
        api = env_demo.Api()
        print(api.send(self.data).text)