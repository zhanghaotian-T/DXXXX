#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :LoggerPrint.py
# @Time      :2021/9/5 11:19
# @Author    :Haotian
import threading
import os


class LogThreading(threading.Thread):

    def __init__(self, threadname):
        threading.Thread.__init__(self, name='Threading' + threadname)
        pass

    def run(self):
        pass

    def getlogger(self):
        pass


if __name__ == "__main__":
    run_code = 0
