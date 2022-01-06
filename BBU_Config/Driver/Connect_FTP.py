#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Connect_FTP.py
# @Time      :2021/12/22 23:13
# @Author    :Haotian

import paramiko
from loguru import logger


class FtpConnect(object):
    def __init__(self, ip='169.169.20.160', name='root', password='1111111', ):
        self.ip = ip
        self.name = name
        self.password = password
        self.p_sftp = None
        self.sftp = None

    def run(self):
        self.ftp_connect()

    def ftp_connect(self):
        if not self.p_sftp:
            try:
                self.p_sftp = paramiko.Transport((self.ip, 22))
                self.p_sftp.banner_timeout = 20
                self.p_sftp.connect(username='root', password='111111')
                self.sftp = paramiko.SFTPClient.from_transport(self.p_sftp)
            except Exception as error:
                logger.info(f'Can not connect remote compute {error}')

    def ftp_download(self, remote_path, download_path):
        try:
            self.sftp.get(remote_path, download_path)
        except Exception as error:
            logger.info(f'can not download file, {error}')


if __name__ == "__main__":
    pass
