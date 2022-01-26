#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: BBU_Thread.py
@time: 2022/01/13
"""

import threading
from Common_name import *


class BBUThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name='Threading' + thread_name)

    def thread_monitor(self, message_args=dict):
        if message_args[MESSAGE_NAME] == 'config_modify':
            pass
        print('我已经执行了')
        pass


if __name__ == '__main__':
    print('Python')
