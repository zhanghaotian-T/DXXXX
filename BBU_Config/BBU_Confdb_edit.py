#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :BBU_Confdb_edit.py
# @Time      :2021/12/11 21:02
# @Author    :Haotian
import os
import re
import xml.etree.ElementTree as ET
import yaml
from bs4 import BeautifulSoup


class BbuconfdbReconfig(object):

    def __init__(self, file_path):
        self.config_message = None
        self.conf_path = file_path
        self.soup = None

    def run(self):
        self.conf_get()
        self.conf_replace('services', '41')

    def message_get(self):
        self.config_message = yaml.load(open('BBUconfig.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    def conf_get(self):
        if not self.soup:
            self.soup = BeautifulSoup(open(self.conf_path), features="lxml-xml")
            print(self.soup.name)

    def conf_replace(self, key_name, replaced_string):
        for tag in self.soup.find_all(name=key_name):
            tag.string = replaced_string


if __name__ == "__main__":
    BBU_reconfig = BbuconfdbReconfig('C:\HomeWork\DXXXX\BBU_Config\BBUconfdb\confdb.xml_2.6')
    BBU_reconfig.run()

