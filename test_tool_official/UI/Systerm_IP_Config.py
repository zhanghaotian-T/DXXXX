# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Systerm_IP_Config.ui'
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


class Ui_Systermipconfig(object):
    def setupUi(self, Systermipconfig):
        if not Systermipconfig.objectName():
            Systermipconfig.setObjectName(u"Systermipconfig")
        Systermipconfig.resize(204, 379)
        self.verticalLayout_5 = QVBoxLayout(Systermipconfig)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(Systermipconfig)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Systermipconfig)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_2.addWidget(self.comboBox_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Systermipconfig)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_3.addWidget(self.comboBox_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Systermipconfig)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_4 = QComboBox(self.groupBox_4)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_4.addWidget(self.comboBox_4)

        self.lineEdit_4 = QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(Systermipconfig)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Systermipconfig)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(Systermipconfig)

        QMetaObject.connectSlotsByName(Systermipconfig)
    # setupUi

    def retranslateUi(self, Systermipconfig):
        Systermipconfig.setWindowTitle(QCoreApplication.translate("Systermipconfig", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Systermipconfig", u"5GC", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Systermipconfig", u"BBU", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Systermipconfig", u"HUB", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Systermipconfig", u"RRU", None))
        self.pushButton_2.setText(QCoreApplication.translate("Systermipconfig", u"OK", None))
        self.pushButton.setText(QCoreApplication.translate("Systermipconfig", u"Cancel", None))
    # retranslateUi

