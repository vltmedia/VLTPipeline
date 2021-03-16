# This Python file uses the following encoding: utf-8
import sys
import os
import json
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

from PySide2.QtCore import QFile, Slot
from PySide2.QtWidgets import QPushButton, QLineEdit, QStatusBar
from PySide2.QtCore import  QObject, QUrl
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog, QWidget, QListWidgetItem, QListWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from py.postpipelinefiles import PostPipeline
import py.Blender.BlenderRunScript as BlenderRunScript
import glob
import time
import webbrowser

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

class SetBlendFiles(QMainWindow):                           # <===
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Load Projects")
        self.parent = parent
        self.blendfiles = []
        self.projectspath = parent.PostPipeline.dirname +"projects"
        self.load_ui()

    def ShowStatusMessage(self, message):
        self.statusbar.showMessage(self.tr(message))

    def GetProjects(self):
        projects = {"Projects" : []}
        for name in glob.glob(self.projectspath + '/project_*.ini'):
            proj = {"Project": os.path.basename(name), "FilePath":name}
            projects["Projects"].append(proj)
            newitem = QListWidgetItem(os.path.basename(name))
            self.listWidget.addItem(newitem)
        self.projects = projects
        self.ShowStatusMessage("Found "+str(len(projects["Projects"]))+" projects!")


    def ItemClicked(self, item):
        selectedBlend = self.blendfiles[item.row()]
        self.selectedBlend = selectedBlend
        self.ShowStatusMessage("Selected | " + selectedBlend)
        
        # print(selectedBlend)

    def LoadSelectedProjectFile(self):
        filepath = self.selectedProject["FilePath"]
        self.parent.ImportConfigStrict(filepath)
        self.ShowStatusMessage("Succesfully loaded | " + self.selectedProject["Project"] + " !!")
        
    def SelectBlendFiles(self):
        fileNames = QFileDialog.getOpenFileNames(self,
        self.tr("Select Scene_Shot_Version.blend Files"), "/", self.tr("Scene_Shot_Version.blend Files' (*.blend)"))
        filess = fileNames[0]
        for f in filess:
            newitem = QListWidgetItem(os.path.basename(f))
            self.listWidgetBlendFilesImport.addItem(newitem)
        
            self.blendfiles.append(f)
            # print('f[1]   |' , f[1])
        self.ShowStatusMessage("Succesfully added | " + str(len(self.blendfiles)) + " Blend files!!")
        
    def SaveBlendFilesToConfig(self):
        self.parent.PostPipeline.MainProject.BlendFiles = self.blendfiles   
        self.parent.SaveConfigFile() 
        self.ShowStatusMessage("Succesfully added | " + str(len(self.blendfiles)) + " Blend files to the Project!!")
    
    def LoadProjectBlendFiles(self):
        # print(self.parent.PostPipeline.MainProject.BlendFiles)
        # print(type(self.parent.PostPipeline.MainProject.BlendFiles))
        if self.parent.PostPipeline.MainProject.BlendFiles != []:
            self.blendfiles = self.parent.PostPipeline.MainProject.BlendFiles
            for bfile in self.parent.PostPipeline.MainProject.BlendFiles:
                newitem = QListWidgetItem(os.path.basename(bfile))
                self.listWidgetBlendFilesImport.addItem(newitem)
        
    def actionExport_All_Cameras_In_File(self):
        # print(self.parent.PostPipeline.MainProject.BlendFiles)
        # print(type(self.parent.PostPipeline.MainProject.BlendFiles))
        select = os.path.splitext(os.path.basename(self.selectedBlend))[0]
        cleanedname = "_".join(select.split("_")[f] for f in range(2))
        
        self.outFolder = self.parent.PostPipeline.MainProject.OutputFolder + "/" + self.parent.PostPipeline.MainProject.Version+ "/" + cleanedname
        argg = '"' + self.outFolder + '",ExportAll'
        camfolder = self.outFolder + "/cameras" 
        if not os.path.exists(camfolder):
            os.makedirs(camfolder)
        print("------------------------------------------------------------")
        print("self.outFolder | " , self.outFolder)
        print("------------------------------------------------------------")
        BlenderRunScript.RunProcess(self.selectedBlend,self.CameraExporterFilesPath, argg  )
        webbrowser.open('file:///' + camfolder)
        self.ShowStatusMessage("Succesfully saved FBX and Alembic Cameras to files | " + camfolder)
        
        # if self.parent.PostPipeline.MainProject.BlendFiles != []:
        #     self.blendfiles = self.parent.PostPipeline.MainProject.BlendFiles
        #     for bfile in self.parent.PostPipeline.MainProject.BlendFiles:
        #         newitem = QListWidgetItem(os.path.basename(bfile))
        #         self.listWidgetBlendFilesImport.addItem(newitem)
            
    def Export_All_Cameras_In_AllFiles(self):
        # print(self.parent.PostPipeline.MainProject.BlendFiles)
        # print(type(self.parent.PostPipeline.MainProject.BlendFiles))
        for bfile in self.blendfiles:
            # select = os.path.splitext(os.path.basename(self.selectedBlend))[0]
            self.selectedBlend = bfile
            select = os.path.splitext(os.path.basename(self.selectedBlend))[0]
            cleanedname = "_".join(select.split("_")[f] for f in range(2))
            
            self.outFolder = self.parent.PostPipeline.MainProject.OutputFolder + "/" + self.parent.PostPipeline.MainProject.Version+ "/" + cleanedname
            argg = '"' + self.outFolder + '",ExportAll'
            camfolder = self.outFolder + "/cameras" 
            if not os.path.exists(camfolder):
                os.makedirs(camfolder)
            print("------------------------------------------------------------")
            print("self.outFolder | " , self.outFolder)
            print("------------------------------------------------------------")
            BlenderRunScript.RunProcess(self.selectedBlend,self.CameraExporterFilesPath, argg  )
            # webbrowser.open('file:///' + camfolder)
            self.ShowStatusMessage("Succesfully saved FBX and Alembic Cameras to files | " + camfolder)
            
        # if self.parent.PostPipeline.MainProject.BlendFiles != []:
        #     self.blendfiles = self.parent.PostPipeline.MainProject.BlendFiles
        #     for bfile in self.parent.PostPipeline.MainProject.BlendFiles:
        #         newitem = QListWidgetItem(os.path.basename(bfile))
        #         self.listWidgetBlendFilesImport.addItem(newitem)
    
    def CreateRenderPostFiles(self):
        self.ShowStatusMessage("Creating Render Post Files. Please Wait ... 10%"  )
        time.sleep(0.3)
        argg = '"' + self.parent.PostPipeline.MainProject.OutputFolder + '",go'
        BlenderRunScript.RunProcess(self.selectedBlend,self.SaveRenderFilesPath, argg  )
        self.ShowStatusMessage("Succesfully Created the Blender Post Files!" )
        
    def CreateRenderPostAllFiles(self):
        
        self.ShowStatusMessage("Creating Render Post Files. Please Wait ... 10%"  )
        time.sleep(0.3)
        count = 0
        outbatpb =  self.parent.PostPipeline.MainProject.OutputFolder + "\\pipeline\\batchexportpb.bat"
        outbateevee =  self.parent.PostPipeline.MainProject.OutputFolder + "\\pipeline\\batchexporteevee.bat"
        os.remove(outbatpb)
        os.remove(outbateevee)
        for file in self.blendfiles:
            percc = str(100 * (count / len(self.blendfiles))) + "%"
            self.ShowStatusMessage("Creating Render Post Files. Please Wait ... "+percc  )
            time.sleep(0.3)
            argg = '"' + self.parent.PostPipeline.MainProject.OutputFolder + '",clear'
            BlenderRunScript.RunProcess(file,self.SaveRenderFilesPath, argg  )
            newcount = 1 + count
            count = newcount   
        self.ShowStatusMessage("Succesfully Created the Blender Post Files!" )
        
        
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "setBlendFiles.ui")
        self.CameraExporterFilesPath = os.path.join(os.path.dirname(__file__), "py/Blender/post/CameraExporter.py")
        self.SaveRenderFilesPath = os.path.join(os.path.dirname(__file__), "py/Blender/post/SaveRenderFiles.py")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)

        self.statusbar = self.window.findChild(QStatusBar, 'statusbar')
        self.listWidgetBlendFilesImport = self.window.findChild(QListWidget, 'listWidgetBlendFilesImport')

        self.listWidgetBlendFilesImport.clicked.connect(self.ItemClicked)


        pushButtonSelectBlendFiles = self.window.findChild(QPushButton, 'pushButtonSelectBlendFiles')
        pushButtonSelectBlendFiles.clicked.connect(self.SelectBlendFiles)

        pushButtonSaveToProjectFile = self.window.findChild(QPushButton, 'pushButtonSaveToProjectFile')
        pushButtonSaveToProjectFile.clicked.connect(self.SaveBlendFilesToConfig)

        pushButtonSaveRenderFilesSelected = self.window.findChild(QPushButton, 'pushButtonSaveRenderFilesSelected')
        pushButtonSaveRenderFilesSelected.clicked.connect(self.CreateRenderPostFiles)

        pushButtonSaveRenderFilesAll = self.window.findChild(QPushButton, 'pushButtonSaveRenderFilesAll')
        pushButtonSaveRenderFilesAll.clicked.connect(self.CreateRenderPostAllFiles)

        actionPlayblast_Eevee_Setup_2 = self.window.findChild(QObject, 'actionPlayblast_Eevee_Setup_2')
        actionPlayblast_Eevee_Setup_2.triggered.connect(self.CreateRenderPostAllFiles)

        actionPlayblast_Eevee_Setup = self.window.findChild(QObject, 'actionPlayblast_Eevee_Setup')
        actionPlayblast_Eevee_Setup.triggered.connect(self.CreateRenderPostFiles)

        actionSave_Project_File = self.window.findChild(QObject, 'actionSave_Project_File')
        actionSave_Project_File.triggered.connect(self.SaveBlendFilesToConfig)

        actionAdd_Blend_Files = self.window.findChild(QObject, 'actionAdd_Blend_Files')
        actionAdd_Blend_Files.triggered.connect(self.SelectBlendFiles)

        actionExport_All_Cameras_In_File = self.window.findChild(QObject, 'actionExport_All_Cameras_In_File')
        actionExport_All_Cameras_In_File.triggered.connect(self.actionExport_All_Cameras_In_File)

        actionExport_All_Cameras_In_File_2 = self.window.findChild(QObject, 'actionExport_All_Cameras_In_File_2')
        actionExport_All_Cameras_In_File_2.triggered.connect(self.Export_All_Cameras_In_AllFiles)

        # newitem = QListWidgetItem("thing 1")
        # self.listWidget.addItem(newitem)
        self.LoadProjectBlendFiles()
        self.window.show()
        print(self.SaveRenderFilesPath)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = loadProjects()
    widget.window.show()
    sys.exit(app.exec_())
