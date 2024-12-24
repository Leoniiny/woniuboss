# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 下午9:27
# @Author  : Leoniiy
# @FileName: path.py
# @Software: PyCharm
# @Blog    ：
import os
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT_PATH, 'ConfigurationLayer')
REPORT_PATH = os.path.join(ROOT_PATH, "ReportingLayer")


if __name__ == '__main__':
    print(CONFIG_PATH)