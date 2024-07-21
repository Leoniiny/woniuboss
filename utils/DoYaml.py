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

    def read_yaml(self):
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
            # return yaml.safe_load(f)


if __name__ == '__main__':
    do_yaml = DoYaml()
    print(do_yaml.read_yaml())