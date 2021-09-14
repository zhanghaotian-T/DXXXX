#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: bci.py
@time: 2021/08/05
"""

import re
import logging
from Driver.TenlentConnect import TelnetConnection
logger = logging.getLogger(__name__)


class Bci(TelnetConnection):
    """
    BCI基础类
    """
    def __init__(self, host, user, password, port=23):
        """初始化函数"""
        TelnetConnection.__init__(self, host, user, password, port)
        self.connect()
        self.get_into_bci()

    def _get_int0_bci(self):
        try:
            self.send_common(command='bci', prompt='')
            self.send_common(command='dg', prompt='User login: ')
            self.send_common(command='passw0rd', prompt='Password: ')
        except Exception as e:
            logger.info(e)


    def get_into_bci(self):
        self._get_int0_bci()

    def set_command_list(self, command_list):
        for command in command_list:
            self.send_common(command)


if __name__ == '__main__':
    a = Bci(host='192.168.255.11', user='dg', password='passw0rd')
    b = a.query_common('/pltf/bsp/read 2 0x3068')
    print('b')
