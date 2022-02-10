#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: lunix_set.py
@time: 2022/02/10
"""
from SSH_Connect import RemoteConnect


class LinuxRemote(RemoteConnect):
    def __init__(self, ip='169.169.20.160', name='root', password='111111'):
        RemoteConnect.__init__(self, ip=ip, name=name, password=password)

    def set_command(self, command):

        pass


if __name__ == '__main__':
    print('Python')
