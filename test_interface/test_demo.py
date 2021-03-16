import requests
from jsonpath import jsonpath
from requests.auth import HTTPBasicAuth

class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r)
        print(r.text)
        print(r.json())
        print(r.headers)
        print(r.status_code)
        assert r.status_code == 200
    def test_query(self):
        payload={
            "a": 1,
            "name": "zhangsan"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "a": 1,
            "name": "zhangsan"
        }
        r = requests.post('http://httpbin.testing-studio.com/post',data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_header(self):
        r = requests.get('http://httpbin.testing-studio.com/get',headers={"a": "header"})
        print(r.json())
        assert r.json()['headers']["A"] == "header"

    def test_post_json(self):
        payload = {
            "a": 1,
            "name": "zhangsan"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200

    def test_hogwards_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        assert jsonpath(r.json(),'$..name')[0] == '开源项目'

    def test_header(self):
        url = 'http://httpbin.testing-studio.com/cookies'
        header = {'User-Agent': 'python-requests/2.23.0'}
        cookie_data = {"a":"b"}
        r = requests.get(url= url,headers = header,cookies = cookie_data)
        print(r.request.headers)

    def test_auth(self):
        r = requests.get("http://httpbin.testing-studio.com/basic-auth/user/passwd",
                     auth =HTTPBasicAuth("user", "passwd"))
        print(r)


