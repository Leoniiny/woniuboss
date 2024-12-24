# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 下午11:05
# @Author  : Leoniiy
# @FileName: DoYaml.py
# @Software: PyCharm
# @Blog    ：
import yaml

class DoYaml:
    def __init__(self, yaml_path="../ConfigurationLayer/env_config.yaml"):
        self.yaml_path = yaml_path
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            self.content = yaml.load(f, Loader=yaml.FullLoader)

    def read_yaml(self,nodename=None):
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            try:
                return self.content[nodename]
            except:
                raise Exception("没有找到节点")
            finally:
                print("读取完毕，没有输入节点名，默认读取全部数据")
                return self.content
    def write_yaml(self,file, write_content,mode="w"):
        with open(file, mode=mode, encoding="utf8") as f:
            try:
                yaml.dump_all(documents=write_content,stream=f,allow_unicode=True, default_flow_style=False)
            except:
                raise Exception("输入内容有误，请检查后重新输入")




if __name__ == '__main__':
    obj = DoYaml(yaml_path="../DataLayer/testcases/get_user_datacase.yaml")
    print(obj.read_yaml())