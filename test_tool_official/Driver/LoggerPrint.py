#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :LoggerPrint.py
# @Time      :2021/9/5 11:19
# @Author    :Haotian
import logging
import threading
import os
from loguru import logger
from logging import Handler
from logging.handlers import QueueHandler
from logging.handlers import QueueListener
from queue import Queue


class SlackQueueHandler(QueueHandler):
    def __int__(self, queue=None):
        QueueHandler.__init__(self, queue)

    def prepare(self, record):
        record.msg = self.format(record)
        record.args = None
        record.exc_info = None
        return record.msg


class SlackQueueListener(QueueListener, Handler):
    def __int__(self, queue=None):
        QueueListener.__init__(self, queue)
        Handler.__init__(self)

    def handle(self, record):
        Handler.handle(self, record)

    def emit(self, record):
        self.emit(record)


class LoggerThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='Threading' + threadname)
        self.logger_queue = Queue(2000)
        self.logger_queue_listener = None

    def run(self):
        logger_handler = SlackQueueHandler(self.logger_queue)
        logger.add(logger_handler)

    def get_logger(self):
        self.logger_queue_listener = SlackQueueListener(self.logger_queue)
        logger_message = self.logger_queue_listener.queue.get()
        return logger_message


if __name__ == "__main__":
    # a = Queue(10)
    # b = SlackQueueHandler(a)
    # logger.add(b)
    # c = SlackQueueListener(a)
    # logger.info('bbbbbbb')
    # logger.info('aaaaaa')
    # d = c.queue.get()
    # print('hello')
    a = LoggerThread('LoggerCollection')
    a.start()
    logger.info('aaaaaaa')
    logger.info('bbbbbbb')
    b = a.get_logger()
    print(b)

