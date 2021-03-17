import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class UserClass():
    def __init__(self, name):
        super(UserClass, self).__init__()
        self.id = 0
        self.Name = name
        self.Groups = "-"
        self.GroupNameOveride = "-"
        self.About = "-"
        self.Email = "dev@company.com"
        self.Signature = "-"
        self.Website = "google.com"
        self.Description = "-"
        self.Icon = "-"
    def __iter__(self):
        return vars(self).iteritems()
        
    def GetInfoArray(self):
        data1 = ['id','Name','Groups','GroupNameOveride','About','Email','Signature','Website','Groups','Description','Icon']
        data2 = [self.id,self.Name,self.Groups,self.GroupNameOveride,self.About,self.Email,self.Signature,self.Website,self.Groups,self.Description,self.Icon]
        return [data1, data2]        
    
    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    
    def UpdateQTTableEntry(self, table):
        self.table = table
        # self.table = QtGui.QTableWidget()
        self.table.setColumnCount(11)
        # self.setCentralWidget(self.table)
        self.infoarray = self.GetInfoArray()

        self.table.setRowCount(11)

        for index in range(11):
            item1 = QtGui.QTableWidgetItem(self.infoarray[0][index])
            self.table.setItem(index,0,item1)
            item2 = QtGui.QTableWidgetItem(self.infoarray[1][index])
            self.table.setItem(index,1,item2)
        return table


class UsersModel(QtCore.QAbstractTableModel):
    def __init__(self):
        super(UsersModel, self).__init__()
        self.horizontalHeaders = [''] * 11
        self.users = [UserClass("dev").GetDict(), UserClass("bon").GetDict()]
        self.columns = list(self.users[0].keys())
        self._data = [UserClass("dev").GetDict(), UserClass("bon").GetDict()]
        for k in range(0 , len(self.columns)):
            
            self.setHeaderData(k, Qt.Horizontal, self.columns[k])
        # self.setHeaderData(0, Qt.Horizontal, "Driver")
        # self.setHeaderData(1, Qt.Horizontal, "Range")
        # self.setHeaderData(2, Qt.Horizontal, "Driven")

    def data(self, index, role):
        row = self.users[index.row()]
        column = self.columns[index.column()]
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            # return self._data[index.row()][index.column()]
            return str(row[column])

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
    
    def setHeaderData(self, section, orientation, data, role=Qt.EditRole):
        if orientation == Qt.Horizontal and role in (Qt.DisplayRole, Qt.EditRole):
            try:
                self.horizontalHeaders[section] = data
                return True
            except:
                return False
        return super().setHeaderData(section, orientation, data, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            try:
                return self.horizontalHeaders[section]
            except:
                pass
        return super().headerData(section, orientation, role)

