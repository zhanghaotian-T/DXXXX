#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RRU_Thread.py
# @Time      :2021/9/23 23:36
# @Author    :Haotian

import threading
import pika, sys, os
from Config.Name_File import *
import yaml
from loguru import logger
from Driver.bci import Bci


class RruThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='Threading' + threadname)
        self.rru = None

    def run(self):
        self.rru_type_config()
        self.rru_queue_deal()
        pass

    def rru_type_config(self):
        if not self.rru:
            config_file = open(r'../Config/Type_Config.yaml')
            rru_type = yaml.load(config_file, Loader=yaml.FullLoader)
            if rru_type[RRU_TYPE][TYPE] == 'O-RAN':
                pass
            elif rru_type[RRU_TYPE][TYPE] == '玄铁':
                self.rru = Bci(host=rru_type[RRU_TYPE][IP], user='dg', password='passw0rd')
            else:
                logger.warning('Please Input right RRU Type')

    def rru_queue_deal(self):

        pass


if __name__ == "__main__":
    pass