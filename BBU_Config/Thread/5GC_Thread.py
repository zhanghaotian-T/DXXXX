#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: 5GC_Thread.py
@time: 2022/01/13
"""
import threading


class CoreNetwork(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name='Threading' + thread_name)

    def thread_monitor(self):
        pass


if __name__ == '__main__':
    print('Python')
