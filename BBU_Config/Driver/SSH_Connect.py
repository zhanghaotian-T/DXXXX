#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :SSH_Connect.py
# @Time      :2021/12/22 23:13
# @Author    :Haotian
import socket
import time

import paramiko
from loguru import logger
import re


class RemoteConnect(object):
    def __init__(self, ip='169.169.20.160', name='root', password='111111'):
        self.ip = ip
        self.name = name
        self.password = password
        self.p_sftp = None
        self.sftp = None
        self.ssh = None
        self.__channel = None

        self.__ansi_escape = re.compile(r'''
                        \x1B  # ESC
                        (?:   # 7-bit C1 Fe (except CSI)
                        [@-Z\\-_]
                        |     # or [ for CSI, followed by a control sequence
                        \[
                        [0-?]*  # Parameter bytes
                        [ -/]*  # Intermediate bytes
                        [@-~]   # Final byte
                    )
                ''', re.VERBOSE)

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

    def __match(self, out_str: str, end_str: list):
        result = self.__ansi_escape.sub('', out_str)
        for it in end_str:
            if result.endswith(it):
                return True, result
        return False, result

    def __recv(self, channel, end_str, timeout):
        result = ''
        out_str = ''
        max_wait_time = timeout * 1000
        channel.settimeout(0.05)
        while max_wait_time > 0:
            try:
                out = channel.recv(1024 * 1024).decode()
                if not out or out == '':
                    continue
                out_str = out_str + out
                match, result = self.__match(out_str, end_str)
                if match is True:
                    return result.strip()
                else:
                    max_wait_time -=50
            except socket.timeout:
                max_wait_time -= 50
        raise Exception('recv data timeout')

    def exec(self, cmd: str, end_str=('# ', '$ ', '? ', '% ',), timeout=30) -> str:
        if not self.__channel:
            self.__channel = self.ssh.invoke_shell(term='xterm', width=4096, height=48)
            time.sleep(0.02)
            self.__channel.recv(4096).decode()

        if cmd.endswith('\n'):
            self.__channel.send(cmd)
        else:
            self.__channel.send(cmd + '\n')
        result = self.__recv(self.__channel, end_str, timeout)
        begin_pos = result.find('\r\n')
        end_pos = result.rfind('\r\n')
        logger.info(result[begin_pos + 2:end_pos])
        if begin_pos == end_pos:
            return ''
        return result[begin_pos + 2:end_pos]

        # try:
        #     stdin, stdout, stdrr = self.ssh.exec_command(command)
        #     result = stdout.read().decode('utf-8')
        #     logger.info(result)
        #     # for line in stdrr.readlines():
        #     #     logger.info(line + ' ')
        #     # return True
        #     # return stdout.read().decode()
        # except Exception as error:
        #     logger.error(f'one error: {error} append in set command: {command}, ')

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

    def __del__(self):
        self.__close()

    def __close(self):
        if not self.ssh:
            return
        self.ssh.close()
        self.ssh = None


if __name__ == "__main__":
    a = RemoteConnect()
    a.run()
    a.sftp_download('/home/gnb/confdb.xml', r'D:\python\DXXXX\BBU_Config\BBUconfdb\confdb.xml')
    # b = a.ssh_set_command_signal('ls')
    # print(b)
