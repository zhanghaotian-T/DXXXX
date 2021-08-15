#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :config.py
# @Time      :2021/8/15 12:33
# @Author    :Haotian

import sys
from UI.Call_Systerm_Auto_Config import Ui_Call_systerm
from PySide2.QtWidgets import QDialog, QApplication, QWidget, QMainWindow


class SystermCall(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Call_systerm()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = SystermCall()
    my_window.show()
    sys.exit(app.exec_())
