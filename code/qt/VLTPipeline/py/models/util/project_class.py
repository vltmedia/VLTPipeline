import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from .exports_class import  Export, Exports, PreviewExport, FinalExport, Delivery
# CREATE TABLE author (
#     author_id INTEGER NOT NULL PRIMARY KEY,
#     first_name VARCHAR,
#     last_name VARCHAR
# );

# CREATE TABLE book (
#     book_id INTEGER NOT NULL PRIMARY KEY,
#     author_id INTEGER REFERENCES author,
#     title VARCHAR
# );

# CREATE TABLE publisher (
#     publisher_id INTEGER NOT NULL PRIMARY KEY,
#     name VARCHAR
# );
class GroupClass():
    def __init__(self, Name):
        super(GroupClass, self).__init__()
        self.Id = id(self)
        self.Name = Name
        self.Clients = []
        self.Users = []
        self.Description = "-"
        self.Icon = "-"
        
    def setName(self, Name):
        self.Name = Name
        
    def loadFromSQL(self, array):
        self.Id = array[0]
        self.Name = array[1]
        if array[2] != None:
            self.Clients = array[2]
        if array[3] != None:
            self.Users = array[3]
        self.Description = array[4]
        self.Icon = array[5]
        
    def sqlTableGenerate(self):
        commandd = "CREATE TABLE IF NOT EXISTS 'group' (           id INTEGER NOT NULL PRIMARY KEY, Name TEXT, Clients integer[], Users integer[], Description TEXT,Icon TEXT)"
        # print("```````````````````Type``````````````````",type(commandd))
        return commandd
            
    def sqlTableGetAll(self, db):
        rows = db.cursor.execute("SELECT * FROM 'group'").fetchall()
        return rows
                    
    def sqlUpdate(self, db, cursor):
        params = (self.Id, self.Name, str(self.Clients), str(self.Users), self.Description,
        self.Icon)
        print(params)
        commandd = """
INSERT INTO 'group' (id, Name, Clients, Users, Description, Icon)
VALUES (?, ?, ?, ?, ? , ?);"""
        cursor.execute(commandd, params)
        db.commit()
    
    
        return commandd
   
    
                
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
        self.Delivery = Delivery(self)

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
