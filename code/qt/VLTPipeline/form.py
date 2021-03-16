# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Apps\VLTPipeline\code\qt\VLTPipeline\form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSelectCSV = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSelectCSV.setGeometry(QtCore.QRect(70, 70, 111, 21))
        self.pushButtonSelectCSV.setObjectName("pushButtonSelectCSV")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 100, 111, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 130, 111, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 200, 111, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 70, 111, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 100, 111, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        self.pushButtonSelectCSV.clicked.connect(mainwindow.slot1)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "mainwindow"))
        self.pushButtonSelectCSV.setText(_translate("mainwindow", "Select CSV"))
        self.pushButton_2.setText(_translate("mainwindow", "Select Audio File"))
        self.pushButton_3.setText(_translate("mainwindow", "Select Output Folder"))
        self.pushButton_4.setText(_translate("mainwindow", "Create Edit JSON"))
        self.pushButton_5.setText(_translate("mainwindow", "Load Config File"))
        self.pushButton_6.setText(_translate("mainwindow", "Create Config File"))

