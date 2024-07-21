# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 下午10:04
# @Author  : Leoniiy
# @FileName: login.py
# @Software: PyCharm
# @Blog    ：
import requests

class Login:
    def __init__(self, userName="WNCD000",userPass="woniu123",checkcode="0000",remember="Y"):
        self.session = requests.session()
        url = "http://localhost:8080/WoniuBoss/login/userLogin"
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
