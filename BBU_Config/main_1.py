#!usr/bin/env python
# -*- coding:utf-8 -*
"""
@author:Haotian
@file: main_1.py
@time: 2022/02/04
"""
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui
from UI.ThrouputTest import Ui_MainWindow
import sys


class EmittingStream(QtCore.QObject):
    def __init__(self, config_sinal):
        QtCore.QObject.__init__(self)
        self.textWrite = config_sinal
        self.textWrite = QtCore.Signal(str)

    def write(self, text):
        self.textWrite.emit(str(text))


class BbuUi(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.run()
        self.ui.retranslateUi(self)

    def run(self):
        sys.stdout = EmittingStream(config_sinal=self.outputwriten)
        sys.stderr = EmittingStream(config_sinal=self.outputwriten)

    def outputwriten(self, text):
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textEdit.setTextCursor(cursor)
        self.ui.textEdit.ensureCursorVisible()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = BbuUi()
    # widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec_())
