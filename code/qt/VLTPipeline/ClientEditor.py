# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientEdit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

class ClientEdit(QtWidgets.QWidget):
    def __init__(self,parent):
        super(ClientEdit, self).__init__()
        self.started = False
        self.parent = parent
        self.widget = QtWidgets.QWidget()
        self.setupUi(self.widget)
    
    def ClickedA(self):
        print("Clicked A | 1")
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        # self.parent.resize(1300, 679)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 1187, 61))
        self.parent = QFont()
        self.parent.setPointSize(20)
        self.parent.setBold(True)
        self.parent.setUnderline(True)
        self.parent.setWeight(75)
        # self.label.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 20, 80, 21))
        self.tabWidgetInfo = QTabWidget(Form)
        self.tabWidgetInfo.setObjectName(u"tabWidgetInfo")
        self.tabWidgetInfo.setGeometry(QRect(20, 70, 1241, 391))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.layoutWidget = QWidget(self.tab_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 341, 43))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.lineEditGroupName = QLineEdit(self.layoutWidget)
        self.lineEditGroupName.setObjectName(u"lineEditGroupName")

        self.verticalLayout_8.addWidget(self.lineEditGroupName)

        self.layoutWidget_2 = QWidget(self.tab_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 100, 341, 251))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.textEditDescription = QTextEdit(self.layoutWidget_2)
        self.textEditDescription.setObjectName(u"textEditDescription")

        self.verticalLayout_2.addWidget(self.textEditDescription)

        self.label_idText = QLabel(self.tab_4)
        self.label_idText.setObjectName(u"label_idText")
        self.label_idText.setGeometry(QRect(10, 10, 339, 21))
        self.layoutWidget_3 = QWidget(self.tab_4)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(380, 40, 431, 311))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.layoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.pushButtonSelectThumbnail = QPushButton(self.layoutWidget_3)
        self.pushButtonSelectThumbnail.setObjectName(u"pushButtonSelectThumbnail")

        self.horizontalLayout.addWidget(self.pushButtonSelectThumbnail)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.graphicsViewIcon = QGraphicsView(self.layoutWidget_3)
        self.graphicsViewIcon.setObjectName(u"graphicsViewIcon")

        self.gridLayout_2.addWidget(self.graphicsViewIcon, 1, 0, 1, 1)

        self.tabWidgetInfo.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget_4 = QWidget(self.tab_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 30, 1185, 196))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.layoutWidget_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.pushButtonUserAdd = QPushButton(self.layoutWidget_4)
        self.pushButtonUserAdd.setObjectName(u"pushButtonUserAdd")

        self.horizontalLayout_3.addWidget(self.pushButtonUserAdd)

        self.pushButtonUserMinus = QPushButton(self.layoutWidget_4)
        self.pushButtonUserMinus.setObjectName(u"pushButtonUserMinus")

        self.horizontalLayout_3.addWidget(self.pushButtonUserMinus)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.tableViewUsers_2 = QTableView(self.layoutWidget_4)
        self.tableViewUsers_2.setObjectName(u"tableViewUsers_2")

        self.verticalLayout_4.addWidget(self.tableViewUsers_2)

        self.tabWidgetInfo.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget_5 = QWidget(self.tab_3)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 40, 1185, 257))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.layoutWidget_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.pushButtonClientsAdd = QPushButton(self.layoutWidget_5)
        self.pushButtonClientsAdd.setObjectName(u"pushButtonClientsAdd")

        self.horizontalLayout_4.addWidget(self.pushButtonClientsAdd)

        self.pushButtonClientsMinus = QPushButton(self.layoutWidget_5)
        self.pushButtonClientsMinus.setObjectName(u"pushButtonClientsMinus")

        self.horizontalLayout_4.addWidget(self.pushButtonClientsMinus)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tableViewClients = QTableView(self.layoutWidget_5)
        self.tableViewClients.setObjectName(u"tableViewClients")

        self.verticalLayout_5.addWidget(self.tableViewClients)

        self.tabWidgetInfo.addTab(self.tab_3, "")

        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.ClickedA)

        self.tabWidgetInfo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        # self.parent.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Client Editor", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Clicked", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Group Name", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_idText.setText(QCoreApplication.translate("Form", u"Id : 2", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Thumbnail", None))
        self.pushButtonSelectThumbnail.setText(QCoreApplication.translate("Form", u"Select", None))
        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Info", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Users", None))
        self.pushButtonUserAdd.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButtonUserMinus.setText(QCoreApplication.translate("Form", u"-", None))
        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Users", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Clients", None))
        self.pushButtonClientsAdd.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButtonClientsMinus.setText(QCoreApplication.translate("Form", u"-", None))
        self.tabWidgetInfo.setTabText(self.tabWidgetInfo.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Clients", None))
    # retranslateUi

