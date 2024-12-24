# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 下午11:16
# @Author  : Leoniiy
# @FileName: repot_log.py
# @Software: PyCharm
# @Blog    ：日志
import logging
import os

from utils.path import CONFIG_PATH
import logging.config

class Loger:
    loger_path = os.path.join(CONFIG_PATH,"log.ini")
    # 读取配置文件
    logging.config.fileConfig(loger_path)

    # 获取配置文件中的记录器
    # root_logger = logging.getLogger("root")
    logger = logging.getLogger("woniuboss")

    # 写日志
    logger.debug("it is from root_logger msg !!!")
    # file_logger.debug("it is from file_logger msg !!!")


if __name__ == '__main__':
    # print(os.path.dirname(os.path.abspath(__file__)))
    Loger().logger.debug("it is from logger msg !!!")