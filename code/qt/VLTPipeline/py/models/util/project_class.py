import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class GroupMetaClass():
    def __init__(self, Name):
        super(GroupMetaClass, self).__init__()
        self.Id = 0
        self.Name = Name
        self.Clients = []
        self.Users = []
        self.Description = "-"
        self.Icon = "-"

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

class ClientMetaClass():
    def __init__(self, Name):
        super(ClientMetaClass, self).__init__()
        self.Id = 0
        self.ClientName = Name
        self.Projects = []
        self.Groups = []
        self.Users = []
        self.Description = "-"
        self.Contacts = "-"
        self.Website = "-"
        self.Icon = "-"

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

class ProjectMetaClass():
    def __init__(self, Name,ProjectType):
        super(ProjectMetaClass, self).__init__()
        self.Id = 0
        self.ProjectName = Name
        self.Client = ClientMetaClass("Default")
        self.ProjectType = ProjectType
        self.Scenes = []
        self.PreviewExports = []
        self.FinalExports = []
        self.Delivery = "-"


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
