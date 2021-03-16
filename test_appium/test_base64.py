import json

import requests
import base64

class ApiRequests:
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def send(self,data:dict):
        res = requests.request(data["method"],data["url"],headers=data["headers"])
        if data["encoding"]  == "base64":
            return json.loads(base64.b64decode(res.content))
        elif data["encoding"] == "base128":
            return requests.post("url",data = res.content)