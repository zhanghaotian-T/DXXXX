#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main_window.py
# @Time      :2022/4/5 21:39
# @Author    :Haotian
import sys

from PySide6.QtWidgets import QApplication, QTextBrowser, QMainWindow
from ui.test_ui import Ui_MainWindow
from loguru import logger
import logging


class LogPrint(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QTextBrowser(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.append(msg)


class RRUConfig(QMainWindow, LogPrint):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.run()

    def run(self):
        self.logger_hander_transfer()

    def logger_hander_transfer(self):
        _logger_text_broswer = LogPrint(self)
        logger.add(_logger_text_broswer)
        self.ui.verticalLayout.addWidget(_logger_text_broswer.widget)


    def ui_reconfig(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RRUConfig()
    main_window.show()
    sys.exit(app.exec())
