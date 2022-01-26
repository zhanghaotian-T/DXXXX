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
from CoreNet_Thread import CoreNetworkThread
from BBU_Thread import BBUThread


class ControlMessage(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name='Threading' + thread_name)
        self.corenetwork = None
        self.bbu = None
        self.hub = None
        self.rru = None
        self.nr_core = None

    def run(self):
        self._connection()

    def thread_init(self):
        self.bbu = BBUThread()
        pass

    def _connection(self):
        self.connection = Connection('amqp://localhost:5672/')
        self.queue = Queue(BBU_CONFIG_QUEUE, exchange='example-exchange', route_key='BOB')
        with self.connection.Consumer([self.queue], callbacks=[self.message_kind]) as self.consumer:
            while True:
                self.connection.drain_events()

    def message_kind(self, body_message, message):
        # print(body_message)
        if body_message[TARGET_Thread] == '5GC':
            core_thread = CoreNetworkThread('core_network')
            core_thread.thread_monitor()
        print(body_message, message)
        message.ack()


if __name__ == '__main__':
    a = ControlMessage('message_control')
    a.run()
    print('Python')
