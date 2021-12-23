#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :BBU_Confdb_edit.py
# @Time      :2021/12/11 21:02
# @Author    :Haotian
import os
import xml.etree.ElementTree as ET
import yaml
from bs4 import BeautifulSoup


class BbuconfdbReconfig(object):

    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.soup = None


    def run(self):
        pass

    def conf_open(self, file_path):
        if not self.soup:
            self.soup = BeautifulSoup(file_path, 'xml')

    def key_worlds_replace(self, key_world, replace_worl):
        self.soup.findall(key_world)

    # def message_get(self):
    #     self.config_message = yaml.load(open('BBUconfig.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    #
    # def bbu_confdb_analyse(self):
    #     file_name = [os.path.join(root, files[0]) for root, dirs, files in os.walk(r'BBUconfdb', topdown=False) if len(files) == 1 ]
    #     soup = BeautifulSoup(file_name[0], 'xml')


if __name__ == "__main__":
    BBU_reconfig = BbuconfdbReconfig('D:\python\DXXXX\BBU_Config\BBUconfdb\confdb.xml')
    BBU_reconfig.run()

