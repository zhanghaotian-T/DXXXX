#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: bci.py
@time: 2021/08/05
"""

import re
import logging
from TenlentConnect import TelnetConnection
logger = logging.getLogger(__name__)


class Bci(TelnetConnection):
    """
    BCI基础类
    """
    def __init__(self, host, user, password, port=23):
        """初始化函数"""
        TelnetConnection.__init__(self, host, user, password, port)
        self.connect()

    def _get_int0_bci(self):
        self.send_common(command='bci', prompt='login: ')

    def get_into_bci(self):
        self._get_int0_bci()


if __name__ == '__main__':
    print('Python')
