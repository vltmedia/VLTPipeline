
from configparser import ConfigParser
import os
import ast
import json

config = ConfigParser()

class UniversalParser:

    

        
    def __iter__(self):
        for key, value in self.Dict.items():
            yield key, value
            
    def ToClassFromGeneratedIni(self,InputPath, ClassObject):
        #Turn a .ini file created by this class into another target class
        if os.path.exists(InputPath):
            config.read(InputPath)
            
            classobj = ClassObject.__dict__
            self.columns = list(classobj.keys())
            self.horizontalHeaders = [''] * len(self.columns)
            outjs = {'settings': {}}
            
            for classobjindex in self.columns:
                setattr(ClassObject, classobjindex, config['settings'][classobjindex]) #equivalent to: self.varname= 'something'


            return True
        else:
            return False
            
            
    def FromClassCreateConfig(self, ClassObject,OutputPath):
        #Turn a target class into a .ini file.
        
        classobj = ClassObject.__dict__
        self.columns = list(classobj.keys())
        self.horizontalHeaders = [''] * len(self.columns)
        outjs = {'settings': {}}
        
        for classobjindex in self.columns:
            outjs['settings'][classobjindex] = classobj[classobjindex]
        
        print(outjs)
            
        # self.IniPath = OutputPath
        
        config['settings'] = outjs['settings']
        
        folderpath = OutputPath.split( os.path.basename(OutputPath))[0]
        print("Folderpath | ", folderpath)

        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
            
        with open(OutputPath, 'w') as f:
            config.write(f)
            f.close()
            
