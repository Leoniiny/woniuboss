# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 下午10:04
# @Author  : Leoniiy
# @FileName: login.py
# @Software: PyCharm
# @Blog    ：
# @Description:后台用户登录
import requests
from utils.DoYaml import DoYaml


class Login:

    def __init__(self, userName="WNCD000",userPass="woniu123",checkcode="0000",remember="Y"):
        env = DoYaml().read_yaml()["test"]
        self.host = env["url"]
        self.session = requests.session()
        url = self.host + "login/userLogin"
        payload = {
            "userName": userName,
            "userPass": userPass,
            "checkcode": checkcode,
            "remember": remember
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        response = self.session.post( url, headers=headers, data=payload)


if __name__ == '__main__':
    Login()
