#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: RRU_Thread.py
@time: 2022/01/13
"""
import threading


class RRUThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name='Threading' + thread_name)

    def thread_monitor(self, message_args=dict):
        print('我已经执行了')
        pass

if __name__ == '__main__':
    print('Python')
