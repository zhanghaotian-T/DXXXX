#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :qttest01.py
# @Time      :2022/3/29 22:07
# @Author    :Haotian

from loguru import logger
from PySide6.QtWidgets import QPlainTextEdit, QDialog, QPushButton, QVBoxLayout, QApplication, QTextEdit, QTextBrowser
import logging


class QPlainTextEditeLoggrt(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QTextBrowser(parent)
        # self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.append(msg)
        # self.widget.appendHtml(msg)


class MyDialog(QDialog, QPlainTextEditeLoggrt):
    def __init__(self, parent=None):
        super().__init__(parent)
        _LogTextBox = QPlainTextEditeLoggrt(self)
        logger.add(_LogTextBox)

        # _LogTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        # logging.getLogger().addHandler(_LogTextBox)
        # logging.getLogger().setLevel(logging.DEBUG)

        self._button = QPushButton(self)
        self._button.setText('Test')
        logger.info('ddddd')

        layout = QVBoxLayout()
        layout.addWidget(_LogTextBox.widget)
        layout.addWidget(self._button)
        self.setLayout(layout)

        self._button.clicked.connect(self.test)
        self.ggy()

    def test(self):
        logger.info('aaaa')
        logger.info('bbbbb')
        # logging.debug('damn, a bug')
        # logging.info('something to remember')
        # logging.warning('that\'s not right')
        # logging.error('foobar')
    def ggy(self):
        logger.info('ffff')


if __name__ == "__main__":
    app = None
    logger.info('ccccc')
    if (not QApplication.instance()):
        app = QApplication([])
    dlg = MyDialog()
    dlg.show()
    dlg.raise_()
    if (app):
        app.exec()
