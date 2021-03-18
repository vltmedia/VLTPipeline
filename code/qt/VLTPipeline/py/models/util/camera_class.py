import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from .transform_class import Transform, TransformKeyframe
from .exports_class import Exports

class Camera():
    def __init__(self, User):
        super(Camera, self).__init__()
        self.CameraName = "Camera.Tight"
        self.Resolution = [1920, 1080]
        self.CameraKeyframes = []
        self.Cameras=[]
        self.SavedCamerasPaths=[]
        self.Exports = Exports()

    def addCameraKeyframe(self, CameraKey):
        self.CameraKeyframes.append(CameraKey)
    def addCamera(self, Camera):
        self.Cameras.append(Camera)
    def addSavedCamerasPath(self, SavedCamerasPath):
        self.SavedCamerasPaths.append(SavedCamerasPath)
    def addCameraKeyframe(self, CameraKey):
        self.CameraKeyframes.append(CameraKey)

    def setCameraName(self, Name):
        self.CameraName = Name
    def setResolution(self, ResolutionX, ResolutionY):
        self.Resolution = [ResolutionX,ResolutionY]

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__


class CameraKeyframe():
    def __init__(self):
        super(CameraKeyframe, self).__init__()
        self.Frame = 0
        self.Interpolation = "Linear"
        self.Transform = Transform()
        self.PixelAspectRatio=1
        self.Projection= "Perspective" # {Perspective , Orthographic, Parallel}
        self.FocalLength = 50
        self.FilmBack = 35.5
        self.ShutterTime = 0.5
        self.FocusDistance = 10
        self.Fstop = 2.8
        self.Bokeh = "radial"
        self.BackgroundImage = ""


    def setTransform(self, Transformclass):
        self.Transform = Transformclass

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
