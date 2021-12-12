#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2021/10/21 22:11
# @Author    :Haotian
import yaml

from Systerm_Main_Windows import Ui_SystermMainWindow
from PySide2.QtWidgets import QDialog, QApplication
import sys


class SystermGui(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SystermMainWindow()
        self.ui.setupUi(self)
        self.main_ui_setup()

    def systerm_ui_config(self):
        pass

    def main_ui_setup(self):
        systerm_confige_message = yaml.load(open(r'../Config/Type_Config.yaml', encoding='utf-8'), Loader=yaml.FullLoader)
        for config in systerm_confige_message:
            self.ui.textBrowser_2.append(f'NETFuction: {config}\n'
                                         f"Type: {systerm_confige_message[config]['Type']}\n"
                                         f"IP: {systerm_confige_message[config]['IP']}\n")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = SystermGui()
    my_window.show()
    sys.exit(app.exec_())
