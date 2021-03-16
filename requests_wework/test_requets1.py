import requests


def test_get_token():
    #获取token
    corpid = "ww4e41b16d7392269c"
    corpsecret = "SPGUcm_ojlmcDLVG5NIliMt95F7ijqZ0pA88uSB_ZL0"
    #res可以拿到返回结果
    #参数使用变量
    res =   requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    #只提取返回结果里access_token的值
    return res.json()["access_token"]

def test_get():
    #查询成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token()}&userid=zhangsan")
    print(res.json())

def test_create():
    #添加成员
    data = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "+86 13800000000",
        "department": [1]
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token()}",
                  json=data
                  )
    print(res.json())

def test_update():
    #更新成员
    data = {
        "userid": "zhangsan",
        "name": "李四"
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_token()}",
                  json=data
                  )
    print(res.json())

def test_delete():
    #删除成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_token()}&userid=zhangsan")
    print(res.json())