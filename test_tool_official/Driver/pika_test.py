#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: pika_test.py
@time: 2021/09/20
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='hello world')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='yes')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='no')
print('[x] sent hello world')

connection.close()

if __name__ == '__main__':
    print('Python')
