import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class UserClass():
    def __init__(self):
        super(UserClass, self).__init__()
        self.id = 0
        self.Name = "dev"
        self.Groups = "-"
        self.GroupNameOveride = "-"
        self.About = "-"
        self.Email = "dev@company.com"
        self.Signature = "-"
        self.Website = "google.com"
        self.Description = "-"
        self.Icon = "-"
        
