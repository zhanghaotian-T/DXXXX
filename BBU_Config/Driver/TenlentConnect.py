#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: TenlentConnect.py
@time: 2021/08/04
"""
import time
from telnetlib import Telnet
from loguru import logger


class TelnetConnection(object):
    def __init__(self, host, user, password, port=23):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.telnet_obj = None

    def __del__(self):
        self.close()

    def _connect(self, prompt=b'>', timeout=5):
        try:
            tn = Telnet(self.host)
            logger.info('Start connect client')
            tn.read_until(b'User login: ', timeout=timeout)
            tn.write(bytes(self.user.encode()) + b'\n')
            tn.read_until(b'Password: ', timeout=timeout)
            tn.write(bytes(self.password.encode()) + b'\n')
            tn.read_until(prompt, timeout=timeout)
            logger.info("Success to connect")
        except Exception as e:
            logger.info(e)
        else:
            return tn

    def connect(self):
        """建立Telnet连接"""
        if not self.telnet_obj:
            self.telnet_obj = self._connect()

    def close(self):
        """关闭telnet"""
        if self.telnet_obj:
            self.telnet_obj.close()
            self.telnet_obj = None
            logger.info(f"disconnected to remote host({self.host}:{self.port})")

    def send_common(self, command, prompt='>', wait_time=0.2):
        try:
            time.sleep(wait_time)
            self.telnet_obj.write(bytes(command.encode()) + b'\n')
            ret = self.telnet_obj.read_until(prompt.encode('utf8'), timeout=wait_time).decode('utf-8')
            ret = ret.splitlines()
            logger.info(f'Success to execute {command}')
        except Exception as e:
            logger.info(e)
        else:
            return ret

    def query_common(self, command, prompt='>', wait_time=5, waitting_time=0.2):
        try:
            if type(command) == list:
                command = command[0]
            time.sleep(waitting_time)
            self.telnet_obj.write(bytes(command.encode()) + b'\n')
            ret = self.telnet_obj.read_until(prompt.encode('utf-8'), timeout=wait_time).decode('utf-8')
            logger.info(f'After write {command} Telnet Return {ret}')
            ret = ret.splitlines()
            ret = self.query_list_extract(ret)
            logger.info(f'Success to execute {command}, return value {ret}')
        except Exception as e:
            logger.info(e)
        else:
            return ret

    def query_list_extract(self, query_list):
        for index, element in enumerate(query_list):
            if 'command:CLI_OK' in element:
                return query_list[index-1]


if __name__ == '__main__':
    ssh_tn = TelnetConnection(host='192.168.255.11', user='dg', password='passw0rd')
    ssh_tn.connect()
    b = ssh_tn.query_common('/pltf/bsp/read 2 0x33c0')


