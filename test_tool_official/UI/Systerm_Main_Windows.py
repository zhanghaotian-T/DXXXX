# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Systerm_Main_Windows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SystermMainWindow(object):
    def setupUi(self, SystermMainWindow):
        if not SystermMainWindow.objectName():
            SystermMainWindow.setObjectName(u"SystermMainWindow")
        SystermMainWindow.resize(498, 611)
        self.gridLayout = QGridLayout(SystermMainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(SystermMainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.textBrowser_2 = QTextBrowser(self.groupBox)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout.addWidget(self.textBrowser_2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(SystermMainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser = QTextBrowser(SystermMainWindow)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_4.addWidget(self.textBrowser)

        self.widget = QWidget(SystermMainWindow)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_4.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)


        self.retranslateUi(SystermMainWindow)

        QMetaObject.connectSlotsByName(SystermMainWindow)
    # setupUi

    def retranslateUi(self, SystermMainWindow):
        SystermMainWindow.setWindowTitle(QCoreApplication.translate("SystermMainWindow", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("SystermMainWindow", u"Systerm_message", None))
        self.pushButton.setText(QCoreApplication.translate("SystermMainWindow", u"config_systerm", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SystermMainWindow", u"Manual_Check_RRU", None))
        self.pushButton_2.setText(QCoreApplication.translate("SystermMainWindow", u"Query", None))
    # retranslateUi

