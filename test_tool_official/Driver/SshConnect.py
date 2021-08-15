#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: SshConnect.py
@time: 2021/08/09
"""
import paramiko


class SshConnect(object):
    def __init__(self, host_name, port, user_name, password):
        self.ssh_connect = None
        self.host_name = host_name
        self.port = port
        self.user_name = user_name
        self.password = password

    def _connect(self):
        if not self.ssh_connect:
            self.ssh_connect = paramiko.SSHClient()

    def connect(self):
        self._connect()


if __name__ == '__main__':
    print('Python')
