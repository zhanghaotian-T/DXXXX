#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Publish_Thread.py
# @Time      :2021/9/23 23:22
# @Author    :Haotian
import json

from kombu import Connection, Exchange, Producer, Queue
from Config.Name_File import *


class PublishThread(object):
    def __init__(self, amqp_url='amqp://localhost:5672/', exchange_name='example-exchange', route_key='BOB',):
        self.amqp_url = amqp_url
        self.exchange_name = exchange_name
        self.route_key = route_key
        self.connection = None
        self.puducer = None
        self.queue = None
        self.exchange = None
        self._connect()

    def _connect(self):
        if not self.puducer:
            self.connection = Connection(self.amqp_url)
            channel = self.connection.channel()
            self.exchange = Exchange(self.exchange_name, type='direct')
            self.puducer = Producer(exchange=self.exchange, channel=channel, routing_key=self.route_key)

    def send_message(self, queue_name, message):
        self.queue = Queue(name=queue_name, exchange=self.exchange, routing_key=self.route_key)
        self.queue.maybe_bind(self.connection)
        self.queue.declare()
        self.puducer.publish(message)
        print(message)


if __name__ == "__main__":
    a = PublishThread()
    a.send_message(RRU_QUEUE, 'a')
    a.send_message(RRU_QUEUE, 'b')
    a.send_message(RRU_QUEUE, 'c')
    a.send_message(RRU_QUEUE, 'd')
    a.send_message(RRU_QUEUE, 'e')
