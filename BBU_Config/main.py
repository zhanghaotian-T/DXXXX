#!usr/bin/env python
# -*- coding:utf-8 -*
"""
@author:Haotian
@file: main_1.py
@time: 2022/02/04
"""
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui
from PySide2.QtCore import Slot
from UI.ThrouputTest import Ui_MainWindow
import sys


class EmittingStream(QtCore.QObject):
    textwriten = QtCore.Signal(str)

    def write(self, text):
        self.textwriten.emit(str(text))
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(5000, loop.quit)
        loop.exec_()
        QApplication.processEvents()


class BbuUi(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.run()
        sys.stdout = EmittingStream()
        # sys.stdout.textwriten.connect(self.outputwriten)
        # sys.stderr = EmittingStream()
        # sys.stderr.textwriten.connect(self.outputwriten)

        self.ui.textEdit.connect(sys.stdout, QtCore.SIGNAL("textwriten(QString)"), self.outputwriten)
        sys.stderr = EmittingStream()
        self.ui.textEdit.connect(sys.stderr, QtCore.SIGNAL("textwriten(QString)"), self.outputwriten)
        self.ui.retranslateUi(self)

    def run(self):
        sys.stdout = EmittingStream()
        self.ui.textEdit.connect(sys.stdout, QtCore.SIGNAL("textwriten(QString)"), self.outputwriten)
        sys.stderr = EmittingStream()
        self.ui.textEdit.connect(sys.stderr, QtCore.SIGNAL("textwriten(QString)"), self.outputwriten)

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
