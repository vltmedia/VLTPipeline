import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from .exports_class import  Export, Exports, PreviewExport, FinalExport, Delivery

class GroupClass():
    def __init__(self, Name):
        super(GroupClass, self).__init__()
        self.Id = 0
        self.Name = Name
        self.Clients = []
        self.Users = []
        self.Description = "-"
        self.Icon = "-"
        
    def setName(self, Name):
        self.Name = Name
                
    def setDescription(self, Description):
        self.Description = Description
                
    def setContacts(self, Contacts):
        self.Contacts = Contacts
                
    def setIcon(self, Icon):
        self.Icon = Icon
        
    def addClient(self, Client):
        self.Clients.append(Client)
        
    def addUser(self, User):
        self.Users.append(User)

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

class ClientClass():
    def __init__(self, Name):
        super(ClientClass, self).__init__()
        self.Id = 0
        self.ClientName = Name
        self.Projects = []
        self.Groups = []
        self.Users = []
        self.Description = "-"
        self.Contacts = "-"
        self.Website = "-"
        self.Icon = "-"
        
    def setClientName(self, ClientName):
        self.ClientName = ClientName
                
    def setDescription(self, Description):
        self.Description = Description
                
    def setContacts(self, Contacts):
        self.Contacts = Contacts
                
    def setWebsite(self, Website):
        self.Website = Website
                        
    def setIcon(self, Icon):
        self.Icon = Icon
        
    def addProject(self, Project):
        self.Projects.append(Project)
        
    def addUser(self, User):
        self.Users.append(User)
        
    def addGroup(self, Group):
        self.Groups.append(Group)

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

class ProjectClass():
    def __init__(self, Name,ProjectType):
        super(ProjectClass, self).__init__()
        self.Id = 0
        self.ProjectName = Name
        self.Client = ClientClass("Default")
        self.ProjectType = ProjectType
        self.Scenes = []
        self.Exports = Exports()
        self.Delivery = Delivery()

    def setClient(self, Client):
        self.Client = Client
        
    def setProjectType(self, Client):
        self.ProjectType = ProjectType
        
    def setProjectName(self, ProjectName):
        self.ProjectName = ProjectName
        
    def addScene(self, Scenes):
        self.Scenes.append(Scenes)

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
