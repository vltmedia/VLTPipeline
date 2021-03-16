
from configparser import ConfigParser
import os

config = ConfigParser()

class Project:
   
        
        
        
    # def __init__(self, ProjectName, Version, AudioFile, OutputFolder, EditJson, EditCSV):
    def UpdateProject(self, ProjectName, Version, AudioFile, OutputFolder, EditJson, EditCSV):
        self.ProjectName = ProjectName
        self.Version = Version
        self.AudioFile = AudioFile
        self.OutputFolder = OutputFolder
        self.EditJson = EditJson
        self.EditCSV = EditCSV
        
        
        
    def __iter__(self):
        for key, value in self.Dict.items():
            yield key, value
            
    def FromIni(self,filepath):
        if os.path.exists(filepath):
            config.read(filepath)
            self.ProjectName = config['settings']['projectname']
            self.Version = config['settings']['version']
            self.AudioFile = config['pipeline']['audiofile']
            self.OutputFolder = config['pipeline']['outputfolder']
            self.EditJson = config['pipeline']['editjson']
            self.EditCSV = config['pipeline']['editcsv']
            self.OutputPathPipleline = config['pipeline']['pipelinepath']
            self.IniPath = config['settings']['inipath']
            return True
        else:
            return False
            
            
    def CreateConfig(self, OutputPath):
        self.IniPath = OutputPath
        
        config['settings'] = {
            
            'ProjectName':self.ProjectName,
            'Version':self.Version,
            'INIPath':OutputPath
                            
                            
                            }
        config['pipeline'] = {
            
            'PipelinePath':self.OutputPathPipleline,
            'AudioFile':self.AudioFile,
            'OutputFolder':self.OutputFolder,
            'EditJson':self.EditJson,
            'EditCSV':self.EditCSV
                            
                            
                            }
        
        # config.read_dict(self)
        
        
        # with open('M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/out/01/pipeline/project.ini', 'w') as f:
        with open(OutputPath, 'w') as f:
            config.write(f)
            f.close()
            
        with open(self.OutputPathPipleline, 'w') as f:
            config.write(f)
            f.close()
            
