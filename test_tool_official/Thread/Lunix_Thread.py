#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: Lunix_Thread.py
@time: 2021/10/05
"""
import threading


class RruThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='Threading' + threadname)
        self.threadname = threadname

    def run(self):
        pass

    def _connect(self):
        pass


if __name__ == '__main__':
    print('Python')
