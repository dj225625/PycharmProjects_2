from requests_wework.api.base_api import BaseApi


class WeWork(BaseApi):

    def get_token(self, secrete):
            corpid = "ww4e41b16d7392269c",
            corpsecret = secrete
            data = {
                "method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                "params": {
                    "corpid": corpid,
                    "corpsecret": corpsecret
                }
            }
            return self.send(**data)["access_token"]