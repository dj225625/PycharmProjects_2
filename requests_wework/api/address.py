import requests

from requests_wework.api.base_api import BaseApi
from requests_wework.api.wework import WeWork


class Address(BaseApi):

    def __init__(self):
        secrete = "SPGUcm_ojlmcDLVG5NIliMt95F7ijqZ0pA88uSB_ZL0"
        self.token = WeWork().get_token(secrete)

    # 添加成员
    def create(self, userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]
            }
        }
        return self.send(**data)

    # 更新成员
    def update(self, userid, name, mobile):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile
            }
        }
        return self.send(**data)

    # 删除成员
    def delete(self, userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        return self.send(**data)
