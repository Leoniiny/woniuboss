# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 下午10:18
# @Author  : Leoniiy
# @FileName: user_management.py
# @Software: PyCharm
# @Blog    ：
from urllib.parse import urlencode
from BusinessLogicLayer.login import Login


class UserManagement(Login):
    def __init__(self):
        super().__init__()

    def get_user_list(self, pageSize=10, pageIndex=1, userName='', empName=''):
        url = self.host + "user/queryUser"
        payload = urlencode(
            {
                "pageSize": pageSize,
                "pageIndex": pageIndex,
                "userName": userName,
                "empName": empName
            }
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post( url, headers=headers, data=payload)
        return response


if __name__ == '__main__':
    obj = UserManagement()
    obj.get_user_list()
