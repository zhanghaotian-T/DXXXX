#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :config.py
# @Time      :2021/8/15 12:33
# @Author    :Haotian
import os
import sys

import yaml
from loguru import logger
from UI.Call_Systerm_Auto_Config import Ui_Call_systerm
from PySide2.QtWidgets import QDialog, QApplication
from bci import Bci



class SystermCall(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Call_systerm()
        self.ui.setupUi(self)
        self.ui_set_up()

    def ui_set_up(self):
        rru_name_list = self.config_file_name_get(r'SystermConfigOrder/RRU_Config')
        bbu_name_list = self.config_file_name_get(r'SystermConfigOrder/BBU_Config')
        _5gc_name_list = self.config_file_name_get(r'SystermConfigOrder/5GC_Config')
        hub_name_list = self.config_file_name_get(r'SystermConfigOrder/HUB_Config')
        self.ui.comboBox.addItems(_5gc_name_list)
        self.ui.comboBox_2.addItems(bbu_name_list)
        self.ui.comboBox_3.addItems(rru_name_list)
        self.ui.comboBox_4.addItems(hub_name_list)
        self.ui.comboBox_5.addItems(['O-RAN', '玄铁'])
        self.ui.pushButton.clicked.connect(self.hub_config)

    def config_file_name_get(self, path):
        file_name_list = list()
        for root, _dir, file_name in os.walk(path):
            file_name_list = file_name
        if len(file_name_list) == 0:
            file_name_list.append('None')
        return file_name_list

    def rru_config_set(self):
        if self.ui.comboBox_5.currentText() == 'O-RAN':
            file_root = './SystermConfigOrder/RRU_Config/'
            rru = Bci(host='192.168.255.1', user='dg', password='passw0rd')
            rru.connect()
            logger.info('RRU Connect Finish')
            file_path = file_root + self.ui.comboBox_3.currentText()
            with open(file_path) as rru_config:
                command_rru = rru_config.readline()
                rru.send_common(command_rru)
            logger.info('RRU Config Finish')
        elif self.ui.comboBox_5.currentText() == '玄铁':
            file_root = './SystermConfigOrder/RRU_Config/'
            rru = Bci(host='192.168.255.11', user='dg', password='pssw0rd')
            rru.connect()
            logger.info('RRU Connect Finish')
            file_path = file_root + self.ui.comboBox_3.currentText()
            with open(file_path) as rru_config:
                command_rru = rru_config.readline()
                rru.send_common(command_rru)
            logger.info('RRU Config Finish')

    def hub_config(self):
        file_root = './SystermConfigOrder/HUB_Config/'
        hub = Bci(host='192.168.255.11', user='dg', password='passw0rd')
        hub.connect()
        file_path = file_root + self.ui.comboBox_4.currentText()
        hub_config = yaml.load(open(file_path))
        for hub_config_command in hub_config['write']:
            hub.send_common(hub_config_command)

    def hub_statue_query(self):
        file_root = './SystermConfigOrder/HUB_Config/'
        hub = Bci(host='192.168.255.11', user='dg', password='passw0rd')
        hub.connect()
        file_path = file_root + self.ui.comboBox_4.currentText()
        hub_config = yaml.load(open(file_path))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = SystermCall()
    my_window.show()
    sys.exit(app.exec_())
