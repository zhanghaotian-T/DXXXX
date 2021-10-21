#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RRU_Thread.py
# @Time      :2021/9/23 23:36
# @Author    :Haotian
import os.path
import threading
import yaml
from Config.Name_File import *
from kombu import Connection, Queue
from Driver.bci import Bci
from loguru import logger


class RruThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='Threading' + threadname)
        self.connection = None
        self.queue = None
        self.consumer = None
        self.rru = None
        self.rru_config = None
        self.threadname = threadname

    def run(self):
        self._rru_connect()
        self._connection()

    def _connection(self):
        self.connection = Connection('amqp://localhost:5672/')
        self.queue = Queue(RRU_QUEUE, exchange='example-exchange', route_key='BOB')
        with self.connection.Consumer([self.queue], callbacks=[self.rru_thread_kind]) as self.consumer:
            while True:
                self.connection.drain_events()

    def _rru_connect(self):
        rru_type_file_path = r'../Config/Type_Config.yaml'
        rru_type = yaml.load(open(rru_type_file_path, encoding='utf-8'), Loader=yaml.FullLoader)['RRU_Type']
        if not self.rru:
            self.rru = Bci(host=rru_type['IP'], user='dg', password='passw0rd')
        self.rru_configration_get(rru_type['Type'] + '.YAML')

    def rru_thread_kind(self, body_message, message):
        print('进入队列获取程序')
        if body_message[RRU_ACtion] == 'Read':
            self.rru_read(body_message)
        elif body_message[RRU_ACtion] == 'Write':
            self.rru_write(body_message)
        elif body_message[RRU_ACtion] == 'Monitor':
            self.rru_monitor(body_message)
        message.ack()

    def rru_configration_get(self, path_name):
        file_path = r'../SystermConfigOrder/RRU_Config/'
        file_name = os.path.join(file_path, path_name)
        self.rru_config = yaml.load(open(file_name, encoding='utf-8'), Loader=yaml.FullLoader)

    def rru_read(self, message):
        rru_read_config = self.rru_config['Read']
        try:
            if message[RRU_Action_Type] == WRITE_SINGLE:
                pass
            elif message[RRU_Action_Type] == WRITE_MODEL:
                pass
            elif message[RRU_Action_Type] == WRITE_ALL:
                pass
            else:
                logger.info(f'The input RRU action type {message[RRU_Action_Type]} is error')
        except Exception as error:
            logger.info(f'rru action filter is error {error}')


        # rru_read_config = self.rru_config['Read']
        # try:
        #     if message[RRU_Action_Type]:
        #         for read_name in message[RRU_Action_Type]:
        #             for common in rru_read_config[read_name]:
        #                 rru_read_result = self.rru.query_common(common)
        #                 logger.info('RRU Read Type{}, RRU Read {},\n Return {}'.format(read_name, common, rru_read_result))
        #     if message[RRU_Action_Message]:
        #         for message_common in message[RRU_Action_Message]:
        #             rru_read_result = self.rru.query_common(message_common)
        #             logger.info('RRU Read {},\n Return {}'.format(message_common, rru_read_result))
        # except Exception as error:
        #     logger.info('The RRU Read Common is Error : {}'.format(error))

    def rru_write(self, message):
        rru_write_config = self.rru_config['Write']
        try:
            if message[RRU_Action_Type] == 'Write':
                for read_name in message[RRU_Action_Type]:
                    for common in rru_write_config[read_name]:
                        self.rru.send_common(common)
                        logger.info('RRU Read Type{}, RRU Read {}'.format(read_name, common))
            elif message[RRU_Action_Type] == 'WriteALL':
                for common in rru_write_config.values:
                    self.rru.send_commonI(common)
                    logger.info(f'RRU Set Common {common}')
            if message[RRU_Action_Message]:
                for message_common in message[RRU_Action_Message]:
                    self.rru.send_common(message_common)
                    logger.info('RRU Read {}'.format(message_common))
        except Exception as error:
            logger.info('The RRU Read Common is Error : {}'.format(error))

    def rru_monitor(self, message):
        rru_read_config = self.rru_config['Read']
        try:
            if message[RRU_Action_Type]:
                for read_name in message[RRU_Action_Type]:
                    result_list = list()
                    for common in rru_read_config[read_name]:
                        rru_read_result = self.rru.query_common(common)
                        logger.info('RRU Read Type{}, RRU Read {},\n Return {}'.format(read_name, common, rru_read_result))
                        result_list.append(rru_read_result)
                    self.rru_query_fail_reset(read_name, result_list)
            if message[RRU_Action_Message]:
                for message_common in message[RRU_Action_Message]:
                    rru_read_result = self.rru.query_common(message_common)
                    logger.info('RRU Read {},\n Return {}'.format(message_common, rru_read_result))
        except Exception as error:
            logger.info('The RRU Read Common is Error : {}'.format(error))

    def rru_query_fail_reset(self, query_name, retun_list):
        tbm_set = {'01000001'}
        sfp_set = {'00000005'}
        if query_name == 'TBM':
            result_tbm = tbm_set - set(retun_list)
            if len(result_tbm) != 0:
                for common in self.rru_config['RESET']['TBM']:
                    self.rru.send_common(common)
        elif query_name == 'SFP':
            result_sfp = sfp_set - set(retun_list)
            if len(result_sfp) != 0:
                for common in self.rru_config['RESET']:
                    self.rru.send_common(common)
        else:
            logger.info('Please input right reset type')

    def rru_reset_query(self, query_name):
        pass


if __name__ == "__main__":
    a = RruThread(RRU_QUEUE)
    a.start()
    print('进程结束')