# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ProjectEditor(object):
    def __init__(self,parent):
        super(ProjectEditor, self).__init__()
        self.started = False
        self.parent = parent
        self.widget = QWidget()
        self.setupUi(self.widget)
    
    def ClickedA(self):
        print("Clicked A | 1")
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Project Editor")
        Form.resize(1291, 540)
        self.tabWidgetInfo = QTabWidget(Form)
        self.tabWidgetInfo.setObjectName(u"tabWidgetInfo")
        self.tabWidgetInfo.setGeometry(QRect(20, 70, 1241, 391))
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.layoutWidget_17 = QWidget(self.tab_9)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(10, 40, 341, 43))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget_17)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_16.addWidget(self.label_21)

        self.lineEditGroupName_5 = QLineEdit(self.layoutWidget_17)
        self.lineEditGroupName_5.setObjectName(u"lineEditGroupName_5")

        self.verticalLayout_16.addWidget(self.lineEditGroupName_5)

        self.layoutWidget_18 = QWidget(self.tab_9)
        self.layoutWidget_18.setObjectName(u"layoutWidget_18")
        self.layoutWidget_18.setGeometry(QRect(380, 40, 411, 311))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget_18)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_17.addWidget(self.label_22)

        self.textEditDescription_3 = QTextEdit(self.layoutWidget_18)
        self.textEditDescription_3.setObjectName(u"textEditDescription_3")

        self.verticalLayout_17.addWidget(self.textEditDescription_3)

        self.label_idText_3 = QLabel(self.tab_9)
        self.label_idText_3.setObjectName(u"label_idText_3")
        self.label_idText_3.setGeometry(QRect(10, 10, 339, 21))
        self.layoutWidget_20 = QWidget(self.tab_9)
        self.layoutWidget_20.setObjectName(u"layoutWidget_20")
        self.layoutWidget_20.setGeometry(QRect(10, 100, 341, 43))
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget_20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.layoutWidget_20)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_18.addWidget(self.label_24)

        self.comboBox = QComboBox(self.layoutWidget_20)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_18.addWidget(self.comboBox)

        self.tabWidgetInfo.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.layoutWidget_22 = QWidget(self.tab_10)
        self.layoutWidget_22.setObjectName(u"layoutWidget_22")
        self.layoutWidget_22.setGeometry(QRect(10, 30, 1185, 111))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget_22)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_26 = QLabel(self.layoutWidget_22)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_13.addWidget(self.label_26)

        self.pushButtonUserAdd_6 = QPushButton(self.layoutWidget_22)
        self.pushButtonUserAdd_6.setObjectName(u"pushButtonUserAdd_6")

        self.horizontalLayout_13.addWidget(self.pushButtonUserAdd_6)


        self.verticalLayout_20.addLayout(self.horizontalLayout_13)

        self.tableViewClient = QTableView(self.layoutWidget_22)
        self.tableViewClient.setObjectName(u"tableViewClient")

        self.verticalLayout_20.addWidget(self.tableViewClient)

        self.tabWidgetInfo.addTab(self.tab_10, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.layoutWidget_25 = QWidget(self.tab_13)
        self.layoutWidget_25.setObjectName(u"layoutWidget_25")
        self.layoutWidget_25.setGeometry(QRect(10, 30, 1185, 257))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget_25)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_29 = QLabel(self.layoutWidget_25)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_16.addWidget(self.label_29)

        self.pushButtonClientsAdd_7 = QPushButton(self.layoutWidget_25)
        self.pushButtonClientsAdd_7.setObjectName(u"pushButtonClientsAdd_7")

        self.horizontalLayout_16.addWidget(self.pushButtonClientsAdd_7)

        self.pushButtonClientsMinus_7 = QPushButton(self.layoutWidget_25)
        self.pushButtonClientsMinus_7.setObjectName(u"pushButtonClientsMinus_7")

        self.horizontalLayout_16.addWidget(self.pushButtonClientsMinus_7)


        self.verticalLayout_23.addLayout(self.horizontalLayout_16)

        self.tableViewScenes = QTableView(self.layoutWidget_25)
        self.tableViewScenes.setObjectName(u"tableViewScenes")

        self.verticalLayout_23.addWidget(self.tableViewScenes)

        self.tabWidgetInfo.addTab(self.tab_13, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.layoutWidget_24 = QWidget(self.tab_12)
        self.layoutWidget_24.setObjectName(u"layoutWidget_24")
        self.layoutWidget_24.setGeometry(QRect(10, 30, 1185, 257))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget_24)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_28 = QLabel(self.layoutWidget_24)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_15.addWidget(self.label_28)

        self.pushButtonClientsAdd_6 = QPushButton(self.layoutWidget_24)
        self.pushButtonClientsAdd_6.setObjectName(u"pushButtonClientsAdd_6")

        self.horizontalLayout_15.addWidget(self.pushButtonClientsAdd_6)

        self.pushButtonClientsMinus_6 = QPushButton(self.layoutWidget_24)
        self.pushButtonClientsMinus_6.setObjectName(u"pushButtonClientsMinus_6")

        self.horizontalLayout_15.addWidget(self.pushButtonClientsMinus_6)


        self.verticalLayout_22.addLayout(self.horizontalLayout_15)

        self.tableViewExports = QTableView(self.layoutWidget_24)
        self.tableViewExports.setObjectName(u"tableViewExports")

        self.verticalLayout_22.addWidget(self.tableViewExports)

        self.tabWidgetInfo.addTab(self.tab_12, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget_26 = QWidget(self.tab)
        self.layoutWidget_26.setObjectName(u"layoutWidget_26")
        self.layoutWidget_26.setGeometry(QRect(10, 30, 1185, 257))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget_26)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_30 = QLabel(self.layoutWidget_26)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_17.addWidget(self.label_30)

        self.pushButtonClientsAdd_8 = QPushButton(self.layoutWidget_26)
        self.pushButtonClientsAdd_8.setObjectName(u"pushButtonClientsAdd_8")

        self.horizontalLayout_17.addWidget(self.pushButtonClientsAdd_8)

        self.pushButtonClientsMinus_8 = QPushButton(self.layoutWidget_26)
        self.pushButtonClientsMinus_8.setObjectName(u"pushButtonClientsMinus_8")

        self.horizontalLayout_17.addWidget(self.pushButtonClientsMinus_8)


        self.verticalLayout_24.addLayout(self.horizontalLayout_17)

        self.tableViewClients_8 = QTableView(self.layoutWidget_26)
        self.tableViewClients_8.setObjectName(u"tableViewClients_8")

        self.verticalLayout_24.addWidget(self.tableViewClients_8)

        self.tabWidgetInfo.addTab(self.tab, "")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 1187, 61))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.retranslateUi(Form)

        self.tabWidgetInfo.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Project Editor", u"Project Editor", None))
        self.label_21.setText(QCoreApplication.translate("Project Editor", u"Project Name", None))
        self.label_22.setText(QCoreApplication.translate("Project Editor", u"Description", None))
        self.label_idText_3.setText(QCoreApplication.translate("Project Editor", u"Id : 2", None))
        self.label_24.setText(QCoreApplication.translate("Project Editor", u"Project Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Project Editor", u"Edit", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Project Editor", u"Video Game", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Project Editor", u"VFX", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Project Editor", u"Sculpt", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Project Editor", u"Sketch", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Project Editor", u"WIP", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Project Editor", u"Code", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Project Editor", u"Sandbox", None))

        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab_9), QCoreApplication.translate("Project Editor", u"Info", None))
        self.label_26.setText(QCoreApplication.translate("Project Editor", u"Client", None))
        self.pushButtonUserAdd_6.setText(QCoreApplication.translate("Project Editor", u"Open", None))
        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab_10), QCoreApplication.translate("Project Editor", u"Client", None))
        self.label_29.setText(QCoreApplication.translate("Project Editor", u"Scenes", None))
        self.pushButtonClientsAdd_7.setText(QCoreApplication.translate("Project Editor", u"+", None))
        self.pushButtonClientsMinus_7.setText(QCoreApplication.translate("Project Editor", u"-", None))
        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab_13), QCoreApplication.translate("Project Editor", u"Scenes", None))
        self.label_28.setText(QCoreApplication.translate("Project Editor", u"Exports", None))
        self.pushButtonClientsAdd_6.setText(QCoreApplication.translate("Project Editor", u"+", None))
        self.pushButtonClientsMinus_6.setText(QCoreApplication.translate("Project Editor", u"-", None))
        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab_12), QCoreApplication.translate("Project Editor", u"Exports", None))
        self.label_30.setText(QCoreApplication.translate("Project Editor", u"Delivery", None))
        self.pushButtonClientsAdd_8.setText(QCoreApplication.translate("Project Editor", u"+", None))
        self.pushButtonClientsMinus_8.setText(QCoreApplication.translate("Project Editor", u"-", None))
        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab), QCoreApplication.translate("Project Editor", u"Delivery", None))
        self.label.setText(QCoreApplication.translate("Project Editor", u"Project Editor", None))
    # retranslateUi

