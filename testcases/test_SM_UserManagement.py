# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 下午11:43
# @Author  : Leoniiy
# @FileName: test_SM_UserManagement.py
# @Software: PyCharm
# @Blog    ：
# 导入pytest模块
import pytest,allure

from BusinessLogicLayer.user_management import UserManagement
from utils.DoYaml import DoYaml


@allure.epic("系统管理")
@allure.feature("用户管理模块")
class TestUserManagement:
    testdata = DoYaml(yaml_path="../DataLayer/testcases/get_user_datacase.yaml").read_yaml(nodename='case01')
    @pytest.mark.smoke
    @allure.story("获取用户列表")
    @allure.title("获取用户列表成功")
    @pytest.mark.parametrize("params",testdata)
    def test_get_user_list_success(self,params):
        with allure.step("获取用户列表"):
            rest = UserManagement().get_user_list(**params).json()
            print(f"params的值为:{params}")
        with allure.step("断言"):
            pytest.assume(len(rest.get("list"))!=0,f"获取用户列表失败,实际值为：{rest}")


if __name__ == '__main__':
    pytest.main(["-vs", "test_SM_UserManagement.py"])
