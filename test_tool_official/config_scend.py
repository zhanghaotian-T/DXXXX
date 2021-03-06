#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: config_scend.py
@time: 2021/10/08
"""
from Thread.Publish_Thread import PublishThread
from Config.Name_File import *


class SystermCall(object):
    def __init__(self):
        self.publish = None

    def run(self):
        self.publish = PublishThread()
        self.publish.send_message(RRU_QUEUE, {RRU_ACtion: 'WriteSinge',
                                              RRU_Action_Type: None,
                                              RRU_Action_Message: ['/pltf/bsp/read 2 0x3068']})
        self.publish.send_message(RRU_QUEUE, {RRU_ACtion: 'WriteModel',
                                              RRU_Action_Type: ['SPF', 'ecppri'],
                                              RRU_Action_Message: None})
        self.publish.send_message(RRU_QUEUE, {RRU_ACtion: 'WriteALL',
                                              RRU_Action_Type: ['ALL'],
                                              RRU_Action_Message: None})
        # self.publish.send_message(RRU_QUEUE, {RRU_ACtion: 'Read',
        #                                       RRU_Action_Type: ['SFP', 'TBM', 'CPPRI'],
        #                                       RRU_Action_Message: None})


if __name__ == '__main__':
    a = SystermCall()
    a.run()
