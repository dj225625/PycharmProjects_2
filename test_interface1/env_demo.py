import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))
    # 重新构造请求信息
    def send(self, data: dict):
        # 将字符串替换成ip地址,将域名替换
        data["url"] = str(data["url"]).replace("abc", self.env["default"])

        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r
