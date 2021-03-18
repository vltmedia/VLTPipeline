import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class Transform():
    def __init__(self, User):
        super(Transform, self).__init__()
        self.Position = [0,0,0]
        self.RotationEuler = [0,0,0]
        self.RotationQuaternion = [0,0,0,0]
        self.Scale = [0,0,0]


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__


class TransformKeyframe():
    def __init__(self, TransformClass):
        super(TransformKeyframe, self).__init__()
        self.Transform = TransformClass
        self.InTangent = Transform()
        self.OutTangent = Transform()
        self.Frame = 0
        self.Interpolation = "Linear"



    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
