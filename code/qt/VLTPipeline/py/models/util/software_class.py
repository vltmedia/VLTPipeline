import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

class SoftwarePackage():
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 0
        self.FilePath = ""
        self.SoftwareName = "Blender"
        self.RenderEngine = RenderEngineEevee()
        self.AvailableRenderEngines = [RenderEngineEevee(), RenderEngineWorkBench(), RenderEngineCycles()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/blender.png"

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__



class SoftwarePackageBlender(SoftwarePackage):
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 10
        self.FilePath = ""
        self.SoftwareName = "Blender"
        self.RenderEngine = RenderEngineEevee()
        self.AvailableRenderEngines = [RenderEngineEevee(), RenderEngineWorkBench(), RenderEngineCycles(), RenderEngineArnold(), RenderEngineOctane(), RenderEngineVRay(), RenderEngineRedshift()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/blender.png"
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__






class SoftwarePackageHoudini(SoftwarePackage):
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 20
        self.FilePath = ""
        self.SoftwareName = "Houdini"
        self.RenderEngine = RenderEngineMantra()
        self.AvailableRenderEngines = [ RenderEngineMantra(), RenderEngineKarma(), RenderEngineOpenGL(),  RenderEngineOctane(),RenderEngineArnold(), RenderEngineVRay(), RenderEngineRedshift()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/houdini.png"
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__






class SoftwarePackageCinema4D(SoftwarePackage):
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 30
        self.FilePath = ""
        self.SoftwareName = "Cinema 4D"
        self.RenderEngine = RenderEngineMantra()
        self.AvailableRenderEngines = [ RenderEnginePhysicalC4D(), RenderEngineStandardC4D(), RenderEngineOpenGL(),  RenderEngineOctane(),RenderEngineArnold(), RenderEngineVRay(), RenderEngineRedshift(), RenderEngineCycles()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/cinema.png"
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__





class SoftwarePackageMaya(SoftwarePackage):
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 40
        self.FilePath = ""
        self.SoftwareName = "Maya"
        self.RenderEngine = RenderEngineMantra()
        self.AvailableRenderEngines = [ RenderEngineOpenGL(),  RenderEngineOctane(),RenderEngineArnold(), RenderEngineVRay(), RenderEngineRedshift(), RenderEngineCycles()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/maya.png"
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__




class SoftwarePackageFusion(SoftwarePackage):
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 50
        self.FilePath = ""
        self.SoftwareName = "Fusion"
        self.RenderEngine = RenderEngineMantra()
        self.AvailableRenderEngines = [ RenderEngineOpenGL()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/maya.png"
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__



class SoftwarePackageAfterEffects(SoftwarePackage):
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 60
        self.FilePath = ""
        self.SoftwareName = "AfterEffects"
        self.RenderEngine = RenderEngineMantra()
        self.AvailableRenderEngines = [ RenderEngineOpenGL()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/maya.png"
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__



class SoftwarePackagePremiere(SoftwarePackage):
    def __init__(self, Name):
        super(SoftwarePackage, self).__init__()
        self.Id = 70
        self.FilePath = ""
        self.SoftwareName = "Premiere"
        self.RenderEngine = RenderEngineMantra()
        self.AvailableRenderEngines = [ RenderEngineOpenGL()]
        self.CommandArguments = ""
        self.Description = ""
        self.Icon = "images/icons/software/maya.png"
        

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__




# Render Engine info here


class RenderEngine():
    def __init__(self):
        self.Id = 0
        self.FilePath = ""
        self.RenderEngineName = "Eevee"
        self.Type = "Real-Time"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/openGL.png"

    def getRenderEngines(self):
        self.RenderEngineChoices = [RenderEngineArnold() , RenderEngineCycles(), RenderEngineEevee() , RenderEngineKarma(), RenderEngineMantra() , RenderEngineOctane(), RenderEngineOpenGL() , RenderEnginePhysicalC4D(), RenderEngineRedshift() , RenderEngineStandardC4D(), RenderEngineUnity() , RenderEngineUnreal(), RenderEngineVRay() , RenderEngineWorkBench()]
        
        return self.RenderEngineChoices

    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__


class RenderEngineEevee(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 20
        self.FilePath = ""
        self.RenderEngineName = "Eevee"
        self.Type = "Real-Time"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/eevee.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineWorkBench(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 10
        self.FilePath = ""
        self.RenderEngineName = "Work Bench"
        self.Type = "Real-Time"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/workBench.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineCycles(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 30
        self.FilePath = ""
        self.RenderEngineName = "Cycles"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/cycles.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineOctane(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 40
        self.FilePath = ""
        self.RenderEngineName = "Octane"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/octane.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineArnold(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 50
        self.FilePath = ""
        self.RenderEngineName = "Arnold"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/arnold.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineVRay(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 60
        self.FilePath = ""
        self.RenderEngineName = "VRay"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/vRay.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineOpenGL(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 70
        self.FilePath = ""
        self.RenderEngineName = "OpenGL"
        self.Type = "Real-Time"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/openGL.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineUnreal(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 80
        self.FilePath = ""
        self.RenderEngineName = "Unreal"
        self.Type = "Game Engine"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/unreal.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineUnity(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 80
        self.FilePath = ""
        self.RenderEngineName = "Unity"
        self.Type = "Game Engine"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/unity.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineRedshift(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 90
        self.FilePath = ""
        self.RenderEngineName = "Redshift"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/redshift.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    



class RenderEngineMantra(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 100
        self.FilePath = ""
        self.RenderEngineName = "Mantra"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/mantra.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineKarma(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 110
        self.FilePath = ""
        self.RenderEngineName = "Karma"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/karma.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEnginePhysicalC4D(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 120
        self.FilePath = ""
        self.RenderEngineName = "Physical C4D"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/PhysicalC4D.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    


class RenderEngineStandardC4D(RenderEngine):
    def __init__(self):
        super().__init__()
        self.Id = 130
        self.FilePath = ""
        self.RenderEngineName = "Standard C4D"
        self.Type = "PBR"
        self.CommandArguments = ""
        self.Description = ""
        self.Quality = 100
        self.Icon = "images/icons/software/StandardC4D.png"
        


    def __iter__(self):
        return vars(self).iteritems()

    def GetDict(self):
        # print(self.__dict__)
        return self.__dict__
    
