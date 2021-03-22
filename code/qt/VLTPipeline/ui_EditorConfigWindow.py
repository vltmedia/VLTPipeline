# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditorConfigWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1301, 755)
        self.actionGroup_Editor = QAction(MainWindow)
        self.actionGroup_Editor.setObjectName(u"actionGroup_Editor")
        self.actionClient_Editor = QAction(MainWindow)
        self.actionClient_Editor.setObjectName(u"actionClient_Editor")
        self.actionProject_Editor = QAction(MainWindow)
        self.actionProject_Editor.setObjectName(u"actionProject_Editor")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 40, 1271, 661))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 340, 23))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1301, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEditors = QMenu(self.menubar)
        self.menuEditors.setObjectName(u"menuEditors")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEditors.menuAction())
        self.menuEditors.addAction(self.actionGroup_Editor)
        self.menuEditors.addAction(self.actionClient_Editor)
        self.menuEditors.addAction(self.actionProject_Editor)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.ShowClients)
        self.pushButton_2.clicked.connect(MainWindow.ShowProjects)
        self.pushButton_3.clicked.connect(MainWindow.ShowShots)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGroup_Editor.setText(QCoreApplication.translate("MainWindow", u"Group Editor", None))
        self.actionClient_Editor.setText(QCoreApplication.translate("MainWindow", u"Client Editor", None))
        self.actionProject_Editor.setText(QCoreApplication.translate("MainWindow", u"Project Editor", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Show Groups", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Show Clients", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Show Projects", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Show Shots", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEditors.setTitle(QCoreApplication.translate("MainWindow", u"Editors", None))
    # retranslateUi

