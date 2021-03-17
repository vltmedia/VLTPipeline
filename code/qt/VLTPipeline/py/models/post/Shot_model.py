import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class ShotModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(ShotModel, self).__init__()
        self.ProjectName = ""
        self.SceneName = ""
        self.ShotName = ""
        self.Version = ""
        self.Version = ""
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
