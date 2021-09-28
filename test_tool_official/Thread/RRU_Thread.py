#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RRU_Thread.py
# @Time      :2021/9/23 23:36
# @Author    :Haotian

import threading

import yaml

from Config.Name_File import *
from kombu import Connection, Queue


class RruThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='Threading' + threadname)
        self.connection = None
        self.queue = None
        self.consumer = None
        self.rru = None
        self.rru_config = None

    def run(self):
        self._connection()

    def _connection(self):

        self.connection = Connection('amqp://localhost:5672/')
        self.queue = Queue(RRU_QUEUE, exchange='example-exchange', route_key='BOB')
        with self.connection.Consumer([self.queue], callbacks=[self.rru_thread_kind]) as self.consumer:
            while True:
                self.connection.drain_events()

    def rru_thread_kind(self, body_message, message):
        print('进入队列获取程序')
        if body_message[RRU_ACtion] == 'READ':
            self.rru_read(body_message)
        elif body_message[RRU_ACtion] == 'WRITE':
            self.rru_write(body_message)
        elif body_message[RRU_ACtion] == 'Monitor':
            self.rru_monitor(body_message)
        message.ack()

    def rru_configration_get(self):
        file_path = r'../SystermConfigOrder/RRU_Config/O-RAN.YAML'
        self.rru_config = yaml.load(open(file_path))

    def rru_queue_deal(self, message):
        pass

    def rru_read(self, message):
        pass

    def rru_write(self, message):
        pass

    def rru_monitor(self, message):
        pass


if __name__ == "__main__":
    a = RruThread(RRU_QUEUE)
    a.start()