#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :SSH_Connect.py
# @Time      :2021/12/22 23:13
# @Author    :Haotian

import paramiko
from loguru import logger


class RemoteConnect(object):
    def __init__(self, ip='169.169.20.160', name='root', password='111111'):
        self.ip = ip
        self.name = name
        self.password = password
        self.p_sftp = None
        self.sftp = None
        self.ssh = None

    def run(self):
        self.sftp_connect()
        self.ssh_connect()

    def sftp_connect(self):
        if not self.p_sftp:
            try:
                self.p_sftp = paramiko.Transport((self.ip, 22))
                self.p_sftp.banner_timeout = 20
                self.p_sftp.connect(username=self.name, password=self.password)
                self.sftp = paramiko.SFTPClient.from_transport(self.p_sftp)
            except Exception as error:
                logger.info(f'Can not connect remote compute {error}')

    def ssh_connect(self):
        if not self.ssh:
            try:
                self.ssh = paramiko.SSHClient()
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(hostname=self.ip, port=22, username=self.name, password=self.password)
            except Exception as error:
                logger.error(f'Can not connect remote server; The error is : {error}')

    def ssh_close(self):
        pass

    def ssh_set_command_signal(self, command):
        try:
            stdin, stdout, stdrr = self.ssh.exec_command(command)
            return stdout.read().decode()
        except Exception as error:
            logger.error(f'one error: {error} append in set command: {command}, ')

    def sftp_download(self, remote_path, local_path):
        try:
            self.sftp.get(remote_path, local_path)
        except Exception as error:
            logger.info(f'can not download file, {error}')

    def sftp_upload(self, remote_path, local_path):
        try:
            self.sftp.put(local_path, remote_path)
        except Exception as error:
            logger.info(f'can not upload file, {error}')

    def sftp_close(self):
        pass


if __name__ == "__main__":
    a = RemoteConnect()
    a.run()
    a.sftp_download('/home/gnb/confdb.xml', r'D:\python\DXXXX\BBU_Config\BBUconfdb\confdb.xml')
    # b = a.ssh_set_command_signal('ls')
    # print(b)
