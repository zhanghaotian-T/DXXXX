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


class SlackQueueHandler(QueueHandler):
    def __int__(self, queue=None):
        QueueHandler.__init__(self, queue)

    def prepare(self, record):
        record.msg = self.format(record)
        record.args = None
        record.exc_info = None


class SlackQueueListener(QueueListener, Handler):
    def __int__(self, queue=None):
        QueueListener.__init__(self, queue)
        Handler.__init__(self)

    def handle(self, record):
        Handler.handle(self, record)

    def emit(self, record):
        self.emit(record)


config = \
    {
    "handlers": [
        {"sink": SlackQueueHandler, "format": "{time} - {message}"},
        {"sink": "file.log", "serialize": True},
    ],
    "extra": {"user": "someone"}
    }

logger.configure(**config)
logger.info('plesa')


class TestLog(object):
    def __init__(self):
        self.handler = None
        self.mylogger = None
        self.creat_handler()
        self.creat_logger()
        logger.info('load message')

    def creat_handler(self):
        pass

    def creat_logger(self):
        self.mylogger = logging.getLogger()

    def log(self, msg):
        self.mylogger.info(msg)


if __name__ == 'main':
    logger.info('aaaaaa')
    print('hello')

