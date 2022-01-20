#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: Control_Thread.py
@time: 2022/01/13
"""

import threading
import pika
from kombu import Connection, Queue
from Common_name import *


class ControlMessage(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name='Threading' + thread_name)

    def run(self):
        self._connection()

    def _connection(self):
        self.connection = Connection('amqp://localhost:5672/')
        self.queue = Queue(BBU_CONFIG_QUEUE, exchange='example-exchange', route_key='BOB')
        with self.connection.Consumer([self.queue], callbacks=[self.message_kind]) as self.consumer:
            while True:
                self.connection.drain_events()

    def message_kind(self, body_message, message):




        print(body_message, message)


if __name__ == '__main__':
    a = ControlMessage('message_control')
    a.start()
    print('Python')
