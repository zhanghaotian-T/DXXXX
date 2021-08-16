#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :config.py
# @Time      :2021/8/15 12:33
# @Author    :Haotian
import os
import sys
from UI.Call_Systerm_Auto_Config import Ui_Call_systerm
from PySide2.QtWidgets import QDialog, QApplication, QWidget, QMainWindow


class SystermCall(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Call_systerm()
        self.ui.setupUi(self)
        self.run()

    def run(self):
        rru_name_list = self.config_file_name_get(r'SystermConfigOrder/RRU_Config')
        bbu_name_list = self.config_file_name_get(r'SystermConfigOrder/BBU_Config')
        _5gc_name_list = self.config_file_name_get(r'SystermConfigOrder/5GC_Config')
        self.ui.comboBox.addItems(_5gc_name_list)
        self.ui.comboBox_2.addItems(bbu_name_list)
        self.ui.comboBox_3.addItems(rru_name_list)

    def config_file_name_get(self, path):
        file_name_list = list()
        for root, _dir, file_name in os.walk(path):
            file_name_list = file_name
        if len(file_name_list) == 0:
            file_name_list.append('None')
        return file_name_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = SystermCall()
    my_window.show()
    sys.exit(app.exec_())
