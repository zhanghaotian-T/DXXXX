#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :xml_edit.py
# @Time      :2021/12/11 21:02
# @Author    :Haotian

import yaml
import xml.dom.minidom


class BbuconfdbReconfig(object):

    def __init__(self, file_path):
        self.config_message = None
        self.conf_path = file_path
        self.dom = None
        self.root = None

    def run(self):
        self.conf_get()
        self.conf_replace('services:band', '41')
        self.save_xml()

    def message_get(self):
        self.config_message = yaml.load(open('../BBUconfig.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    def conf_get(self):
        if not self.dom:
            self.dom = xml.dom.minidom.parse(self.conf_path)
            self.root = self.dom.documentElement

    def conf_replace(self, key_name, replaced_string):
        key_node_list = self.root.getElementsByTagName(key_name)
        for node in key_node_list:
            node.childNodes[0].data = str(replaced_string)

    def save_xml(self):
        with open(self.conf_path, 'w', encoding='utf-8') as file:
            self.dom.writexml(file, encoding='utf-8')


if __name__ == "__main__":
    BBU_reconfig = BbuconfdbReconfig('../BBUconfdb/confdb.xml')
    BBU_reconfig.run()
