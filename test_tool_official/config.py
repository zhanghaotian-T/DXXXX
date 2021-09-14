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
        self._5gc_config = None
        self.bbu_config = None
        self.hub_config = None
        self.rru_config = None

    def run(self):
        self.systerm_config_get()
        self.systerm_element_config()

    def systerm_config_get(self):
        config_yaml_path = r'./Config/Type_Config.yaml'
        yaml_open = open(config_yaml_path, encoding='utf-8')
        config_yaml = yaml.load(yaml_open, Loader=yaml.FullLoader)
        self._5gc_config = config_yaml['5GC_Type']
        self.bbu_config = config_yaml['BBU_Type']
        self.hub_config = config_yaml['HUB_Type']
        self.rru_config = config_yaml['RRU_Type']

    def systerm_element_config(self):
        self._5gc_config_set()
        self.bbu_config_set()
        if self.rru_config['Type'] == '玄铁':
            self.rru_query_and_set()
        elif self.rru_config['Type'] == 'O-RAN':
            self.hub_query_and_set()
            self.rru_query_and_set()
        else:
            logger.error('Please Check RRU Type, The RRU Type is Error')

    def _5gc_config_set(self):
        pass

    def bbu_config_set(self):
        pass

    def hub_query_and_set(self):
        pass

    def rru_query_and_set(self):
        if self.rru_config['Type'] == '玄铁':
            pass
        elif self.rru_config['Type'] == 'O-RAN':
            pass
        else:
            logger.error('Please Check RRU Type, The RRU Type is Error')

    def statue_query(self, file_path, agreement):
        sfp_status = False
        tbm_status = False
        cppri_status = False
        file_open = yaml.load(open(file_path, encoding='utf-8'), Loader=yaml.FullLoader)
        if agreement == 'Cppri':
            pass
        elif agreement == 'Ecppri':
            pass
        else:
            logger.error('Pleese Input Right SFP agreement')


if __name__ == "__main__":
    a = SystermCall('RRUconnect')
    a.start()
    print('线程运行')


