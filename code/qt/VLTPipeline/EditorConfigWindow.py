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
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog, QWidget, QAction, QMenuBar,QMenu,QStatusBar,  QListWidgetItem, QListWidget, QLabel,QGridLayout, QTableView, QComboBox , QTextEdit, QGraphicsView

# This Python file uses the following encoding: utf-8
import sys
import os
import subprocess
class EditorConfigWindow(QMainWindow):
    def __init__(self):
        super(EditorConfigWindow, self).__init__()
        self.started = False
        self.widget = QWidget()
        self.setupUi(self)
        
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
        self.gridLayoutWidget.setGeometry(QRect(20, 70, 1261, 621))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        self.show()
        # self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGroup_Editor.setText(QCoreApplication.translate("MainWindow", u"Group Editor", None))
        self.actionClient_Editor.setText(QCoreApplication.translate("MainWindow", u"Client Editor", None))
        self.actionProject_Editor.setText(QCoreApplication.translate("MainWindow", u"Project Editor", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEditors.setTitle(QCoreApplication.translate("MainWindow", u"Editors", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])

    window = EditorConfigWindow()
    window.show()

    sys.exit(app.exec_())