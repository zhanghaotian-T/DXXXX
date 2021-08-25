#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: config.py
@time: 2021/08/24
"""
import os
import sys

import yaml
from loguru import logger
from bci import Bci
import threading
from PySide2.QtWidgets import QErrorMessage


class SystermCall(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='Threading' + threadname)

    def run(self):
        self.systerm_config_get()
        pass

    def systerm_config_get(self):
        config_yaml_path = r'./Config/Type_Config.yaml'
        config_yaml = yaml.load(config_yaml_path)
        

    def config_save_yaml(self):

        pass


if __name__ == "__main__":
    print('线程运行')

