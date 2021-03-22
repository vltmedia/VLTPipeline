import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from .project_class import ProjectClass, ClientClass, GroupClass
from .software_class import SoftwarePackageBlender, SoftwarePackageCinema4D, SoftwarePackageHoudini, SoftwarePackageMaya
from .exports_class import Export, Exports, PreviewExport, FinalExport, Delivery
from .camera_class import Camera, CameraKeyframe

class SceneClass():
    def __init__(self, Name):
        super(SceneClass, self).__init__()
        self.Id = 0
        self.SceneID = Name
        self.Shots = []
        self.Exports = Exports()
        self.Project = ProjectClass("Untitled", "VFX")
        self.Version = "01"
        self.Description = "-"
        self.Icon = "-"

    def addShot(self, Shot):
        self.Shots.append(Shot)
        
    def setProject(self, Project):
        self.Project = Project
                
    def setSceneID(self, SceneID):
        self.SceneID = SceneID
                        
    def setVersion(self, Version):
        self.Version = Version
                        
    def setIcon(self, Icon):
        self.Icon = Icon
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

class ShotClass():
    def __init__(self, Name,Scene):
        super(ShotClass, self).__init__()
        self.Id = 0
        self.ShotID = Name
        self.FullID = Scene.SceneID + "_" + Name
        self.Scene = Scene
        self.Version = "01"
        self.Description = "-"
        self.ShotFiles = []
        self.MainShotFile = ShotFileClass(self)
        self.Icon = "-"

    def addShot(self, ShotFile):
        self.ShotFiles.append(ShotFile)
        
    def setMainShotFile(self, ShotFile):
        self.MainShotFile = ShotFile

    def setScene(self, Scene):
        self.Scene = Scene
        self.FullID = Scene.SceneID + "_" + self.ShotID
        
    
    def setIcon(self, Icon):
        self.Icon = Icon
        
        
    def setShotID(self, ShotID):
        self.ShotID = ShotID
        self.FullID = Scene.SceneID + "_" + self.ShotID
        
    
    def setVersion(self, Version):
        self.Version = Version
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__


class ShotFileClass():
    def __init__(self, Shot):
        super(ShotFileClass, self).__init__()
        self.Id = 0
        self.FilePath = ""
        self.SoftwarePackage = SoftwarePackageBlender("Blender")
        self.Shot = Shot
        self.Dependencies = []
        self.Cameras=[]
        self.Exports = Exports()
        
    def setShot(self, Shot):
        self.Shot = Shot
            
    def setFilePath(self, FilePath):
        self.FilePath = FilePath
        
    def addDependency(self, Dependency):
        self.Dependencies.append(Dependency)

        
    def addCamera(self, Camera):
        self.Cameras.append(Camera)



    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

