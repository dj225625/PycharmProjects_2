import random

import pytest
import requests


# 获取token
@pytest.fixture(scope="session")
def test_get_token():
    res = None
    corpid = "ww4e41b16d7392269c"
    corpsecret = "SPGUcm_ojlmcDLVG5NIliMt95F7ijqZ0pA88uSB_ZL0"
    # res可以拿到返回结果
    # 参数使用变量
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    # 只提取返回结果里access_token的值
    return res.json()["access_token"]


# 查询成员
def test_get(userid, test_get_token):
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token}&userid={userid}")
    return res.json()


# 添加成员
# 添加多个成员
def test_create(userid, name, mobile, test_get_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token}",
                        json=data
                        )
    return res.json()


# 更新成员
def test_update(userid, name, mobile, test_get_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_token}",
                        json=data
                        )
    return res.json()


# 删除成员
def test_delete(userid, test_get_token):
    res = requests.get(
        f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_token}&userid={userid}")
    return res.json()


# 随机生成多个用户,用来进行数据驱动
def test_create_data():
    data = [(str(random.randint(0, 9999999)),
             "zhangsan",
             str(random.randint(15250000000, 15260000000))) for x in range(10)]
    return  data

#使用pytest进行参数化传递
@pytest.mark.parametrize("userid,name,mobile", test_create_data())
def test_123(userid, name, mobile, test_get_token):
    assert "created" == test_create(userid, name, mobile, test_get_token)["errmsg"]
    assert name == test_get(userid, test_get_token)["name"]

    assert "updated" == test_update(userid, "lisi", mobile, test_get_token)["errmsg"]
    assert "lisi" == test_get(userid, test_get_token)["name"]

    assert "deleted" == test_delete(userid, test_get_token)["errmsg"]
    assert 60111 == test_get(userid, test_get_token)['errcode']
