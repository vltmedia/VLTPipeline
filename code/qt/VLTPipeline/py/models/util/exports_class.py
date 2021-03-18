# Use Exports() to reference A full pipelin for Preview and Final Exports


import sys
import os

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
# from ..util.project_class import ProjectClass, ClientClass, GroupClass
from .software_class import RenderEngine
from .software_class import RenderEngineArnold , RenderEngineCycles, RenderEngineEevee , RenderEngineKarma, RenderEngineMantra , RenderEngineOctane, RenderEngineOpenGL , RenderEnginePhysicalC4D, RenderEngineRedshift , RenderEngineStandardC4D, RenderEngineUnity , RenderEngineUnreal, RenderEngineVRay , RenderEngineWorkBench
# from .project_class import ProjectClass , GroupClass, ClientClass


class ExportsFilepaths():
    def __init__(self):
        super(ExportsFilepaths, self).__init__()
        self.Id = 0
        self.ExportedImages=[]
        self.ExportedVideos=[]
        self.CompedVideos=[]

    def addImage (self,image):
        self.ExportedImages.append(image)
        
        
    def addVideo (self,video):
        self.ExportedVideos.append(video)
                
    def addCompedVideo (self,video):
        self.CompedVideos.append(video)
        
    def getVideos (self):
        return self.ExportedVideos
        
        
                
    def getImages (self):
        return self.ExportedImages
        
                        
    def getCompedVideos (self):
        return self.CompedVideos
        
        
        
    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__


class Export():
    def __init__(self):
        super(Export, self).__init__()
        self.RenderEngineChoices = [RenderEngineArnold() , RenderEngineCycles(), RenderEngineEevee() , RenderEngineKarma(), RenderEngineMantra() , RenderEngineOctane(), RenderEngineOpenGL() , RenderEnginePhysicalC4D(), RenderEngineRedshift() , RenderEngineStandardC4D(), RenderEngineUnity() , RenderEngineUnreal(), RenderEngineVRay() , RenderEngineWorkBench()]
        self.RenderEngine = [RenderEngine()]
        self.FilePath = ""
        self.ExportType = "Preview"
        self.Version = "01"
        self.Comped = True
        self.CompBatPath = ""
        self.SceneFile = ""
        self.FPS = 24
        self.Frames = 55
        self.StartFrame = 1000
        self.EndFrame = 1055
        self.Exports = ExportsFilepaths()

    def addImage (self,image):
        self.Exports.ExportedImages.append(image)
        
        
    def addVideo (self,video):
        self.Exports.ExportedVideos.append(video)
                
    def addCompedVideo (self,video):
        self.Exports.CompedVideos.append(video)
        
    def getVideos (self):
        return self.Exports.ExportedVideos
        
        
                
    def getImages (self):
        return self.Exports.ExportedImages
        
                        
    def getCompedVideos (self):
        return self.Exports.CompedVideos
        
        
        
    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

class PreviewExport(Export):
    def __init__(self):
        super().__init__()
        self.RenderEngineChoices = [RenderEngineArnold() , RenderEngineCycles(), RenderEngineEevee() , RenderEngineKarma(), RenderEngineMantra() , RenderEngineOctane(), RenderEngineOpenGL() , RenderEnginePhysicalC4D(), RenderEngineRedshift() , RenderEngineStandardC4D(), RenderEngineUnity() , RenderEngineUnreal(), RenderEngineVRay() , RenderEngineWorkBench()]
        self.RenderEngine = [RenderEngine()]
    
        self.ExportType = "Preview"
        self.FilePath = ""
        
        self.Version = "01"
        self.Comped = True
        self.CompBatPath = ""
        self.SceneFile = ""
        self.FPS = 24
        self.Frames = 55
        self.StartFrame = 1000
        self.EndFrame = 1055
        self.Exports = ExportsFilepaths()

    def addImage (self,image):
        self.Exports.ExportedImages.append(image)
        
        
    def addVideo (self,video):
        self.Exports.ExportedVideos.append(video)
                
    def addCompedVideo (self,video):
        self.Exports.CompedVideos.append(video)
        
    def getVideos (self):
        return self.Exports.ExportedVideos
        
        
                
    def getImages (self):
        return self.Exports.ExportedImages
        
                        
    def getCompedVideos (self):
        return self.Exports.CompedVideos
        
        
        
    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__

class FinalExport(Export):
    def __init__(self):
        super().__init__()
        self.RenderEngineChoices = [RenderEngineArnold() , RenderEngineCycles(), RenderEngineEevee() , RenderEngineKarma(), RenderEngineMantra() , RenderEngineOctane(), RenderEngineOpenGL() , RenderEnginePhysicalC4D(), RenderEngineRedshift() , RenderEngineStandardC4D(), RenderEngineUnity() , RenderEngineUnreal(), RenderEngineVRay() , RenderEngineWorkBench()]
        self.RenderEngine = [RenderEngine()]
        
        self.ExportType = "Final"
        self.FilePath = ""
        
        self.Version = "01"
        self.Comped = True
        self.CompBatPath = ""
        self.SceneFile = ""
        self.FPS = 24
        self.Frames = 55
        self.StartFrame = 1000
        self.EndFrame = 1055
        self.Exports = ExportsFilepaths()

    def addImage (self,image):
        self.Exports.ExportedImages.append(image)
        
        
    def addVideo (self,video):
        self.Exports.ExportedVideos.append(video)
                
    def addCompedVideo (self,video):
        self.Exports.CompedVideos.append(video)
        
    def getVideos (self):
        return self.Exports.ExportedVideos
        
        
                
    def getImages (self):
        return self.Exports.ExportedImages
        
                        
    def getCompedVideos (self):
        return self.Exports.CompedVideos
        
        
        
    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__


# Use this to reference A ppelin for Exports
class Exports():
    def __init__(self):
        super(Exports, self).__init__()
        self.PreviewExports = []
        self.FinalExports = []
        

    def addPreviewExports (self,PreviewExport):
        self.Exports.PreviewExports.append(PreviewExport)
        
        
    def addFinalExport (self,FinalExport):
        self.Exports.FinalExports.append(FinalExport)

        
    def removeFinalExport (self,index):
        self.Exports.FinalExports.pop(index)


        
    def removePreviewExport (self,index):
        self.Exports.PreviewExports.pop(index)
        
    def getFinalExport (self,index):
        return self.Exports.FinalExports[index]


        
    def getPreviewExport (self,index):
        return self.Exports.PreviewExports[index]
        
    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    
    



class Delivery():
    def __init__(self, project):
        super(Delivery, self).__init__()
        self.ProjectMeta = project
        self.Version = "0.0.0"
        self.Description = ""
        self.DistributionURL = ""
        self.FilesIncluded = []

    def addFile (self,filepath):
        self.FilesIncluded.append(filepath)
        

    def getFilesIncluded (self):
        return self.FilesIncluded
        
        

    def changeVersion (self, version):
        self.Version  =version
        
    def changeProject (self, project):
        self.ProjectMeta  =project
        

    def changeDescription (self, Description):
        self.Description  =Description
        
    def changeDistributionURL (self, DistributionURL):
        self.DistributionURL  =DistributionURL
        
        
    def overwriteFilesIncluded (self, filepathArray):
        self.FilesIncluded  =filepathArray
        

        
    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__


ex = ExportsFilepaths()
print(ex)