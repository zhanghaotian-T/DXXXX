#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Publish_Thread.py
# @Time      :2021/9/23 23:22
# @Author    :Haotian
import json
import pika


class PublishThread(object):
    def __init__(self):
        self.connection = None
        self.channel = None
        self._connect()

    def _connect(self):
        if not self.connection:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            self.channel = self.connection.channel()

    def sender(self, queue_name, sende_message=dict):
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(sende_message)
        )


if __name__ == "__main__":
    run_code = 0
