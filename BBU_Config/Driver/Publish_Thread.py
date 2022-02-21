#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Publish_Thread.py
# @Time      :2021/9/23 23:22
# @Author    :Haotian

import os
from kombu import Connection, Exchange, Producer, Queue
from Common_name import *
from loguru import logger


class PublishThread(object):

    # amqp_url = 'amqp://localhost:5672/'
    # exchange_name = 'example-exchange'
    # route_key = 'BOB'
    #
    # connection = Connection(amqp_url)
    # channel = connection.channel()
    #
    # exchange = Exchange(exchange_name, type='direct')
    # producer = Producer(exchange=exchange, channel=channel, routing_key=route_key)
    # os.popen('rabbitmqctl purge_queue "RRU Queue"')

    def send_message(self, queue_name, message, producer=None):
        amqp_url = 'amqp://localhost:5672/'
        exchange_name = 'example-exchange'
        route_key = 'BOB'

        connection = Connection(amqp_url)
        channel = connection.channel()

        exchange = Exchange(exchange_name, type='direct')
        producer = Producer(exchange=exchange, channel=channel, routing_key=route_key)
        os.popen('rabbitmqctl purge_queue "RRU Queue"')

        queue = Queue(name=queue_name, exchange=exchange, routing_key=route_key)
        queue.maybe_bind(connection)
        queue.declare()
        producer.publish(message)
        connection.close()
        print(message)

    # def __init__(self, amqp_url='amqp://localhost:5672/', exchange_name='example-exchange', route_key='BOB',):
    #     self.amqp_url = amqp_url
    #     self.exchange_name = exchange_name
    #     self.route_key = route_key
    #     self.connection = None
    #     self.puducer = None
    #     self.queue = None
    #     self.exchange = None
    #     self._connect()
    #
    # def _connect(self):
    #     if not self.puducer:
    #         self.connection = Connection(self.amqp_url)
    #         channel = self.connection.channel()
    #         self.exchange = Exchange(self.exchange_name, type='direct')
    #         self.puducer = Producer(exchange=self.exchange, channel=channel, routing_key=self.route_key)
    #         os.popen('rabbitmqctl purge_queue "RRU Queue"')
    #
    # def send_message(self, queue_name, message):
    #     self.queue = Queue(name=queue_name, exchange=self.exchange, routing_key=self.route_key)
    #     self.queue.maybe_bind(self.connection)
    #     self.queue.declare()
    #     self.puducer.publish(message)
    #     print(message)


if __name__ == "__main__":
    # PublishThread.send_message(PublishThread, BBU_CONFIG_QUEUE,
    #                            {TARGET_Thread: 'BBU',
    #                             MESSAGE:
    #                                 {
    #                                  UNIT_ACTION: 'query',
    #                                  ACTION_MEASSAGE: {MESSAGE_NAME: 'config_modify',
    #                                                    MESSAGE_ARGS: {}}},
    #                             })
    PublishThread.send_message(PublishThread, BBU_CONFIG_QUEUE,
                               {TARGET_Thread: 'BBU',
                                MESSAGE:
                                    {
                                        UNIT_ACTION: 'write',
                                        ACTION_MEASSAGE: {MESSAGE_NAME: 'bbu_start',
                                                          MESSAGE_ARGS: {}}},
                                })
