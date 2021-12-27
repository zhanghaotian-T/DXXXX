#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :xml_edit_1.py
# @Time      :2021/12/11 21:02
# @Author    :Haotian
import os
import re
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import yaml
from loguru import logger


class BbuconfdbReconfig(object):

    def __init__(self, file_path):
        self.config_message = None
        self.conf_path = file_path
        self.tree = None
        self.root = None

    def run(self):
        self.conf_get()
        self.conf_replace('band', '41')
        self.save_xml()

    def message_get(self):
        self.config_message = yaml.load(open('../BBUconfig.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    def conf_get(self):
        if not self.tree:
            try:
                self.tree = ET.parse(self.conf_path)
                self.root = self.tree.getroot()
            except Exception as e:
               logger.info('Please Input right file')

    def conf_replace(self, key_name, replaced_string):
        for element in self.root.iter():
            element_tag = element.tag.split('}')[1]
            if key_name == element_tag:
                element.text = replaced_string
                logger.info('The text {} change to {}'.format(element.text, replaced_string))
            else:
                logger.info('there is no message need replace')

    def save_xml(self):
        self.tree.write(self.conf_path, 'utf-8')


if __name__ == "__main__":
    BBU_reconfig = BbuconfdbReconfig('../BBUconfdb/confdb.xml')
    BBU_reconfig.run()

