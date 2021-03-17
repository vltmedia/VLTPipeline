# Pass any List of objects in JSON like form to become a QTableView table of strings.  [UsersClass(), UsersClass()]

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class UniversalTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(UniversalTableModel, self).__init__()
        self.horizontalHeaders = [''] * 11
        self.dictdata = data
        self.columns = list(self.dictdata[0].keys())
        self._data = data
        for k in range(0 , len(self.columns)):
            
            self.setHeaderData(k, Qt.Horizontal, self.columns[k])


    def data(self, index, role):
        row = self.dictdata[index.row()]
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


class UniversalTableFromClassModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(UniversalTableFromClassModel, self).__init__()
        dictlist = []
        for k in data:
            dictlist.append(k.__dict__)
            
        self.dictdata = dictlist
        self.columns = list(self.dictdata[0].keys())
        self.horizontalHeaders = [''] * len(self.columns)
        
        self._data = dictlist
        for k in range(0 , len(self.columns)):
            
            self.setHeaderData(k, Qt.Horizontal, self.columns[k])


    def data(self, index, role):
        row = self.dictdata[index.row()]
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

