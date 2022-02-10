#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: BBU_Thread.py
@time: 2022/01/13
"""

import threading
from Driver.SSH_Connect import RemoteConnect
from Driver.CETC_BBU_Conf_edit import CETCbbuEdite
from Common_name import *
from loguru import logger


class BBUThread(threading.Thread):
    def __init__(self, thread_name, bbu_type='CETC', ip='169.169.20.162'):
        threading.Thread.__init__(self, name='Threading' + thread_name)
        self.bbu_type = bbu_type
        self.ip = ip
        self.bbu_ssh_signal = None
        self.bbu_ssh_continue = None
        self.bbu_remote = None

    def run(self):
        self._connect()

    def _connect(self):
        if self.bbu_type == 'CETC':
            self.bbu_remote = RemoteConnect(ip=self.ip)
            self.bbu_remote.ssh_connect()

    def thread_monitor(self, message_args=dict):
        try:
            if message_args[UNIT_ACTION] == 'read':
                pass
            elif message_args[UNIT_ACTION] == 'write':
                self.thread_write_action(message_args[ACTION_MEASSAGE])
            elif message_args[UNIT_ACTION] == 'query':
                self.thread_query_action(message_args[ACTION_MEASSAGE])
                pass
            else:
                logger.error('the unit_action is error')
        except Exception as error:
            raise f'The queue is not convert to the thread, {error}'

    def thread_read_action(self):
        pass

    def thread_write_action(self, action_message_dict=dict):
        if action_message_dict[MESSAGE_NAME] == 'bbu_start':
            return_args = self.bbu_start(action_message_dict[MESSAGE_ARGS])
        else:
            return_args = None
        return return_args

    def thread_query_action(self, action_message_dict=dict):
        if action_message_dict[MESSAGE_NAME] == 'config_modify':
            return_args = self.bbu_thread_config_modify(action_message_dict[MESSAGE_ARGS])
        else:
            return_args = None
        return return_args

    def bbu_thread_config_modify(self, message_args=dict):
        print('进入处理程序')
        self.bbu_remote.sftp_connect()
        self.bbu_remote.sftp_download('/home/gnb/confdb.xml', r'D:\python\DXXXX\BBU_Config\BBUconfdb\confdb.xml')
        confdb_edit = CETCbbuEdite()
        confdb_edit.cetc_confdb_edit()
        # self.bbu_remote.sftp_upload()
        return True

    def bbu_start(self, message_args=dict):
        return_command = self.bbu_remote.ssh_set_command_signal('./home/gnb/x v')
        logger.info(return_command)
        return_command2 = self.bbu_remote.ssh_set_command_signal('./home/gnb/x v')
        logger.info(return_command2)
        return True


if __name__ == '__main__':
    a = BBUThread('BBU_Thread')
    a.run()
    print('Python')
