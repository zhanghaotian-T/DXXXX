#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Publish_Thread.py
# @Time      :2021/9/23 23:22
# @Author    :Haotian
import json
from kombu import Connection, Exchange, Producer, Queue


class PublishThread(object):
    def __init__(self, amqp_url='amqp://localhost:5672/', exchange_name='example-exchange', route_key='BOB', queue_name='example-queue'):
        self.amqp_url = amqp_url
        self.exchange_name = exchange_name
        self.route_key = route_key
        self.queue_name = queue_name
        self.connection = None
        self.puducer = None
        self.queue = None

    def _connect(self):
        if not self.puducer:
            self.connection = Connection(self.amqp_url)
            channel = self.connection.channel()
            exchange = Exchange(self.exchange_name, type='direct')
            self.puducer = Producer(exchange=exchange, channel=channel, routing_key=self.route_key)
            self.queue = Queue(name=self.queue_name, exchange=exchange, routing_key=self.route_key)
            self.queue.maybe_bind(self.connection)
            self.queue.declare()

    def send_message(self):
        pass







if __name__ == "__main__":
    run_code = 0
