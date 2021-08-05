#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: TenlentConnect.py
@time: 2021/08/04
"""
import time
from telnetlib import Telnet
import logging

logger = logging.getLogger(__name__)


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
            tn = Telnet(bytes(self.host))
            logger.info('Start connect client')
            tn.read_until(b'login: ', timeout=timeout)
            tn.write(bytes(self.user) + b'\n')
            tn.read_until(b'Password: ', timeout=timeout)
            tn.write(bytes(self.password) + b'\n')
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

    def send_common(self, command, prompt=b'>', wait_time=5):
        try:
            time.sleep(0.5)
            self.telnet_obj.write(bytes(command) + b'\n')
            ret = self.telnet_obj.read_until(prompt, timeout=wait_time).decode('utf-8')
            ret = ret.splitlines()
            logger.info('Success to execute command({0})'.format(command))
        except Exception as e:
            logger.info(e)
        else:
            return ret


if __name__ == '__main__':
    print('Python')
    ssh_tn = TelnetConnection(host=b'192.168.255.11', user=b'dg', password=b'passw0rd')
    ssh_tn.connect()
    ssh_tn.send_common(b'bci')

