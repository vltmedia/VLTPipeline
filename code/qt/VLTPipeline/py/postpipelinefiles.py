from .createeditbat import CreateEditJSON
from .createffmpegeditfiles import LoadJSON
from .pipelineclasses import Project
import os
import csv
import json

class PostPipeline:
    def __init__(self):
        newproj = Project()
        self.MainProject = newproj
        self.scriptloc = os.path.dirname(__file__) + "/" +os.path.basename(__file__)
        self.dirname  = os.path.dirname(__file__)+ "/"
        self.outjsonpath = self.dirname + "editjson.json"
        
        self.csvfile = ""

        self.audiofile = ""
        self.outputfolderpath = ""
        self.Loaded = newproj.FromIni(self.dirname + "project.ini")
        self.version = newproj.Version
        self.projectname = newproj.ProjectName


    
    def LoadProjectInfo(self):
        self.Loaded = self.MainProject.FromIni(self.dirname + "project.ini")
        print("Loading \ " + self.dirname + "project.ini")
        
        if self.Loaded == True:
            print("Loaded \ " + self.dirname + "project.ini")
            self.audiofile=self.MainProject.AudioFile
            self.outputfolderpath=self.MainProject.OutputFolder
            self.outjsonpath=self.MainProject.EditJson
            self.csvfile=self.MainProject.EditCSV
            print("AudioFile \ " + self.MainProject.AudioFile)
            
            self.updateFolderPaths()
            print("AudioFile \ " + self.MainProject.AudioFile)
        else:
            print("Failed Loading")
        
        
    
    def LoadProjectInfoFile(self, filepath):
        self.Loaded = self.MainProject.FromIni(filepath)
        print("Loading \ " + filepath)
        
        if self.Loaded == True:
            print("Loaded \ " + filepath)
            self.audiofile=self.MainProject.AudioFile
            self.outputfolderpath=self.MainProject.OutputFolder
            self.outjsonpath=self.MainProject.EditJson
            self.csvfile=self.MainProject.EditCSV
            print("AudioFile \ " + self.MainProject.AudioFile)
            
            self.updateFolderPaths()
            self.MainProject.IniPath = filepath
            print("AudioFile \ " + self.MainProject.AudioFile)
        else:
            print("Failed Loading")
        
        
    def getFolderPath(self,directorypath):
    
        folder_selected = directorypath
        self.outputfolderpath=folder_selected
        self.outjsonpath = self.outputfolderpath + "/pipeline/" + "editjson.json"
        self.MainProject.OutputPathPipleline =  self.outputfolderpath + "/pipeline/" + "project.ini"
        self.UpdateProjectClass()
        # try:
        #     if not os.path.exists(outputfolderpath + "/pipeline")
        #         os.makedirs(outputfolderpath + "/pipeline")
        # except :
        #     print("Failed making Pipeline Dir")
                
    def updateFolderPaths(self):
        
        self.outjsonpath = self.outputfolderpath + "/pipeline/" + "editjson.json"
        self.MainProject.OutputPathPipleline =  self.outputfolderpath + "/pipeline/" + "project.ini"
        self.UpdateProjectClass()
        # try:
        #     if not os.path.exists(outputfolderpath + "/pipeline")
        #         os.makedirs(outputfolderpath + "/pipeline")
        # except :
        #     print("Failed making Pipeline Dir")
        
    def select_file(self,filepath):
        # filetypes = (
        #     ('Edit CSV', '*.csv'),
        #     ('Premiere Markers CSV', '*.csv'),
        #     ('All files', '*.*')
        # )

        # filename = fd.askopenfilename(
        #     title='Select an Edit CSV File',
        #     initialdir='/',
        #     filetypes=filetypes)

        # showinfo(
        #     title='Selected File',
        #     message=filename
        # )
        self.csvfile = filepath
        self.UpdateProjectClass()
        return self.MainProject

        
    def select_audio_file(self,filepath):
        # filetypes = (
        #     ('Audio file', '*.wav'),
        #     ('All files', '*.*')
        # )

        # filename = fd.askopenfilename(
        #     title='Select an Audio File',
        #     initialdir='/',
        #     filetypes=filetypes)

        # showinfo(
        #     title='Selected File',
        #     message=filename
        # )
        self.audiofile = filepath
        self.UpdateProjectClass()
        
    def CreateEditJSONFile(self):
        jsonpath = self.outjsonpath
        
        CreateEditJSON(self.csvfile, 'utf-16', self.outjsonpath )
        # showinfo(
        #     title='Success!',
        #     message="Successfully created the Edit JSON File! : " + outjsonpath
        # )
        return "Successfully created the Edit JSON File! : " + self.outjsonpath
        
    def UpdateProjectClass(self):
        # global self.MainProject
        
        # self.MainProject.UpdateProject(self.projectname, self.version, self.audiofile, self.outputfolderpath, self.outjsonpath, self.csvfile)
        self.MainProject.UpdateProject(self.MainProject.ProjectName, self.MainProject.Version, self.audiofile, self.outputfolderpath, self.outjsonpath, self.csvfile)
        

    def CheckCSVFile(self):
        # global self.MainProject
        outputpath = self.dirname +"/project.ini"
        outpipelineprojpath = self.outputfolderpath + "/pipeline/" + "project.ini"
        self.UpdateProjectClass()
        # self.MainProject.UpdateProject("VTBITCY2101H", "01", audiofile, outputfolderpath, outjsonpath, csvfile)
        # self.MainProject.OutputPathPipleline = outpipelineprojpath
        self.MainProject.CreateConfig(outputpath)
        print(self.csvfile)
        print(self.outputfolderpath)