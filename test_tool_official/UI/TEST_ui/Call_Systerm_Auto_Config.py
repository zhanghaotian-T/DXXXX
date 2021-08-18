# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Call_Systerm_Auto_Config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Call_systerm(object):
    def setupUi(self, Call_systerm):
        if not Call_systerm.objectName():
            Call_systerm.setObjectName(u"Call_systerm")
        Call_systerm.resize(560, 436)
        self.gridLayout_8 = QGridLayout(Call_systerm)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Call_systerm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Call_systerm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Call_systerm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_3.addWidget(self.comboBox_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(Call_systerm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.tabWidget.addTab(self.widget, "")
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.textBrowser_2 = QTextBrowser(self.widget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_5.addWidget(self.textBrowser_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.widget_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.textBrowser_3 = QTextBrowser(self.tab)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.gridLayout_6.addWidget(self.textBrowser_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textBrowser_4 = QTextBrowser(self.tab_2)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.gridLayout_7.addWidget(self.textBrowser_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Call_systerm)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Call_systerm)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Call_systerm)
    # setupUi

    def retranslateUi(self, Call_systerm):
        Call_systerm.setWindowTitle(QCoreApplication.translate("Call_systerm", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Call_systerm", u"BBU_Type", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Call_systerm", u"5GC_Type", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Call_systerm", u"RRU_Type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("Call_systerm", u"\u6838\u5fc3\u7f51", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_2), QCoreApplication.translate("Call_systerm", u"BBU", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Call_systerm", u"RRU\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Call_systerm", u"RRUconfig", None))
        self.pushButton.setText(QCoreApplication.translate("Call_systerm", u"Config", None))
    # retranslateUi

