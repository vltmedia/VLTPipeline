import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class UserMemoryClass():
    def __init__(self, User):
        super(UserMemoryClass, self).__init__()
        self.User = User
        self.LoggedIn = False
        self.CurrentGroup = "-"
        self.CurrentClient = "-"
        self.CurrentProject = "-"
        self.LastOpenedFilePath = "-"

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
