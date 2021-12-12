#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :BBU_Confdb_edit.py
# @Time      :2021/12/11 21:02
# @Author    :Haotian
import os
import xml.etree.ElementTree as ET
import yaml


class BbuconfdbReconfig(object):

    def __init__(self):
        self.config_message = None
        self.tree = None
        self.root = None
        pass

    def run(self):
        self.message_get()
        self.bbu_confdb_analyse()

    def message_get(self):
        self.config_message = yaml.load(open('BBUconfig.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    def bbu_confdb_analyse(self):
        file_name = [os.path.join(root, files[0]) for root, dirs, files in os.walk(r'BBUconfdb', topdown=False) if len(files) == 1 ]
        if not self.tree:
            self.tree = ET.parse(file_name[0])
            self.root = self.tree.getroot()
        self.confdb_service_frequency_edit()

    def confdb_service_frequency_edit(self):
        print(self.root.tag)
        # service_band = self.root.findall(r'.//services:band')
        service_frequency1 = self.root.findall(r'.//services')
        service_frequency = self.root.findall(r'.//ssb-frequency')
        pass


if __name__ == "__main__":
    BBU_reconfig = BbuconfdbReconfig()
    BBU_reconfig.run()

