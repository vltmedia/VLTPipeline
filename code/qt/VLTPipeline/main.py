# This Python file uses the following encoding: utf-8
import sys
import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

from PySide2.QtCore import QFile, Slot
from PySide2.QtWidgets import QPushButton, QLineEdit, QStatusBar
from PySide2.QtCore import  QObject, QUrl
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog, QTableWidget, QTableView
from PySide2.QtCore import QFile, Qt
from PySide2.QtUiTools import QUiLoader

from py.models.util.user_model import UserClass, UsersModel
from py.models.util.UniversalTable import UniversalTableModel, UniversalTableFromClassModel
from py.postpipelinefiles import PostPipeline
from py.createffmpegeditfiles import RunMainProcess, RunProcessProject, RunProcessBatsProject

from LoadProjects import  loadProjects
from setBlendFiles import  SetBlendFiles

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])


# class Window2(QMainWindow):                           # <===
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Window22222")
#         self.load_ui()
        
#     def load_ui(self):
#         loader = QUiLoader()
#         path = os.path.join(os.path.dirname(__file__), "loadProjectsWindow.ui")
#         ui_file = QFile(path)
#         ui_file.open(QFile.ReadOnly)
#         self.window = loader.load(ui_file, self)
        
#         self.statusbar = self.window.findChild(QStatusBar, 'statusbar')
                
    
        
#         self.window.show()
        
#         ui_file.close()

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.PostPipeline = PostPipeline()
        self.load_ui()
        
    
    def SelectCSV(self):
        fileName = QFileDialog.getOpenFileName(self,
        self.tr("Select an Edit CSV File"), "/", self.tr("Edit CSV' (*.csv)"))
        self.PostPipeline.select_file(fileName[0])
        # self.lineEditCSVPath.setText(self.PostPipeline.csvfile)
        self.UpdateLineEdits()
        self.ShowStatusMessage("Succesfully Set Edit CSV File! | " + self.PostPipeline.csvfile)
        
        print(self.PostPipeline.csvfile)
        print("Fuck")
            
    
    def SelectAudio(self):
        fileName = QFileDialog.getOpenFileName(self,
        self.tr("Select an Audio File"), "/", self.tr("Audio file' (*.wav)"))
        self.PostPipeline.select_audio_file(fileName[0])
        self.ShowStatusMessage("Succesfully Set Edit Audio File! | " + fileName[0])

        
        # self.lineEditCSVPath.setText(self.PostPipeline.csvfile)
        self.UpdateLineEdits()
        
    def SelectOutputFolder(self):
        dir = QFileDialog.getExistingDirectory(self,
        self.tr("Select Scene Output Directory"),
                                    "/",
                                    QFileDialog.ShowDirsOnly
                                    | QFileDialog.DontResolveSymlinks)
        self.PostPipeline.getFolderPath(dir)
        print(dir)
        self.ShowStatusMessage("Succesfully set the Scene Output Directory! | " + dir)

        # self.lineEditCSVPath.setText(self.PostPipeline.csvfile)
        self.UpdateLineEdits()
        
    def UpdateLineEdits(self):
        self.lineEditCSVPath.setText(self.PostPipeline.MainProject.EditCSV)
        self.lineEditAudio.setText(self.PostPipeline.MainProject.AudioFile)
        self.lineEditOutputFolder.setText(self.PostPipeline.MainProject.OutputFolder)
        print("self.PostPipeline.MainProject.OutputFolder 3 | " ,self.PostPipeline.MainProject.OutputFolder)
        self.lineEditConfigLocation.setText(self.PostPipeline.MainProject.IniPath)
        self.lineEditVersion.setText(self.PostPipeline.MainProject.Version)
        self.lineEditProjectName.setText(self.PostPipeline.MainProject.ProjectName)
    
    def SaveConfigFile(self):
        if not os.path.exists(self.PostPipeline.dirname +"/projects"):
            os.makedirs(self.PostPipeline.dirname +"/projects")
        outputpath = self.PostPipeline.dirname +"/projects/project_"+self.PostPipeline.MainProject.ProjectName+".ini"
        projoutpath = outputpath
        self.PostPipeline.MainProject.CreateConfig(outputpath)
        
        outputpath = self.PostPipeline.dirname +"/projects/project_current.ini"
        self.PostPipeline.MainProject.CreateConfig(outputpath)
        
        print("Saved Config File! | ", projoutpath)
        self.ShowStatusMessage("Saved Config File! | " + projoutpath)
        
        
    def LoadConfigFile(self):
        if os.path.exists(self.PostPipeline.dirname + "/projects/project_current.ini"):
            self.ImportConfigStrict(self.PostPipeline.dirname + "/projects/project_current.ini")
            print("self.PostPipeline.MainProject.OutputFolder 1 | " ,self.PostPipeline.MainProject.OutputFolder)
            
            # self.PostPipeline.LoadProjectInfo()
            print("self.PostPipeline.MainProject.OutputFolder 2 | " ,self.PostPipeline.MainProject.OutputFolder)
            
            self.UpdateLineEdits()
            print("self.PostPipeline.MainProject.OutputFolder 4 | " ,self.PostPipeline.MainProject.OutputFolder)
            
            self.ShowStatusMessage("Loaded Config File! | " + self.PostPipeline.dirname + "/projects/project_current.ini")
            print("Loaded Config File! | ", self.PostPipeline.dirname + "/projects/project_current.ini")
            print("MainProject.EditCS | ", self.PostPipeline.MainProject.EditCSV )
        else:
            self.ShowStatusMessage("Failed Loading Config File! | No Config File Available")
            
    def Create_Edit_JSON(self):
        if self.PostPipeline.outjsonpath != "":
            req = self.PostPipeline.CreateEditJSONFile()
            if os.path.exists(self.PostPipeline.outjsonpath):
                self.ShowStatusMessage(req)
            else:
                self.ShowStatusMessage("Failed Exporting JSON | " + self.PostPipeline.outjsonpath)
                

    def SaveFFMPEGBAtchScripts(self):
        # print("Proj ", self.PostPipeline.MainProject)
        req = RunProcessProject(self.PostPipeline.MainProject)
        
        print(req)
        if req == True:
            self.ShowStatusMessage("Succesfully saved the bat FFMPEG Scripts!")
        else:
            self.ShowStatusMessage("Failed saving the bat FFMPEG Scripts!")
        # RunMainProcess(self.PostPipeline.MainProject.EditJson, self.PostPipeline.MainProject.OutputFolder, self.PostPipeline.MainProject.ProjectName, self.PostPipeline.MainProject.AudioFile )

    def actionSave_Combine_Video_Scripts(self):
        req = RunProcessBatsProject(self.PostPipeline.MainProject)
        print(req)
        if req == True:
            self.ShowStatusMessage("Succesfully saved the bat FFMPEG Scripts and MP4 Files!!")
        else:
            self.ShowStatusMessage("Failed saving the bat FFMPEG Scripts and MP4 Files!!")
        # RunMainProcess(self.PostPipeline.MainProject.EditJson, self.PostPipeline.MainProject.OutputFolder, self.PostPipeline.MainProject.ProjectName, self.PostPipeline.MainProject.AudioFile )


    def actionOpen_Project_Pipeline_Folder(self):
        explore(self.PostPipeline.MainProject.OutputPathPipleline)

    def actionOpen_Project_Scene_Output_Folder(self):
        explore(self.PostPipeline.MainProject.OutputFolder)

    def lineEditVersionEdited(self):
        self.PostPipeline.MainProject.Version = self.lineEditVersion.text()
        self.ShowStatusMessage("Succesfully set the Version to | " + self.lineEditVersion.text())

    def UpdateProjectName(self):
        self.PostPipeline.MainProject.ProjectName = self.lineEditProjectName.text()
        self.ShowStatusMessage("Succesfully set the Project Name to | " + self.lineEditProjectName.text())

            
    def ShowStatusMessage(self, message):
        self.statusbar.showMessage(self.tr(message))       
                    
    def OpenLoadProjectsWindow(self, message):
        # self.loadprojectswindow = loadprojects(self)
        # self.loadprojectswindow.show()
        # self.w = Window2()
        self.w = loadProjects(self)
        self.w.show()
        self.hide()
        # LoadProjectWindow()
                        
    def OpenSetBlendFilesWindow(self, message):
        # self.loadprojectswindow = loadprojects(self)
        # self.loadprojectswindow.show()
        # self.w = Window2()
        self.setBlendFiles = SetBlendFiles(self)
        self.setBlendFiles.show()
        self.hide()
        # LoadProjectWindow()
    
    def ImportConfig(self):
        fileName = QFileDialog.getOpenFileName(self,
        self.tr("Select a project_.ini file"), "/", self.tr("Project Config ini' (*.ini)"))
        self.PostPipeline.LoadProjectInfoFile(fileName[0])
        
        self.UpdateLineEdits()
        self.ShowStatusMessage("Imported Config File! | " + fileName[0])
        
    def ImportConfigStrict(self, filepath):
        fileName = filepath
        self.PostPipeline.LoadProjectInfoFile(fileName)
        
        self.UpdateLineEdits()
        self.ShowStatusMessage("Imported Config File! | " + fileName)
            
    def Refresh_User(self):
        # self.user = UserClass()
        
        # self.user.UpdateQTTableEntry(self.tableWidgetUser)
        
        
        self.users = [UserClass("dev").GetDict(),UserClass("Bon").GetDict(),UserClass("roll").GetDict(),UserClass("dug").GetDict()]
        self.usersb = [UserClass("dev"),UserClass("Bon"),UserClass("roll"),UserClass("dug")]
        # self.usersmodel = UniversalTableModel(self.users)
        self.usersmodel = UniversalTableFromClassModel(self.usersb)
        # self.users = UsersModel()
        # self.users.setHeaderData(1, Qt.Horizontal, 'Date')
        # self.tableViewUsers.setModel(self.users)
        self.tableViewUsers.setModel(self.usersmodel)
        # self.user.UpdateQTTableEntry(self.tableViewUsers)
        
        # print(self.users)
        self.ShowStatusMessage("Succesfully Refreshed the user! | " + self.users[0]["Name"])
    
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        
        self.statusbar = self.window.findChild(QStatusBar, 'statusbar')
                
        btn = self.window.findChild(QPushButton, 'pushButtonSelectCSV')
        btn.clicked.connect(self.SelectCSV)
        
        pushButton_AudioFileSelect = self.window.findChild(QPushButton, 'pushButton_AudioFileSelect')
        pushButton_AudioFileSelect.clicked.connect(self.SelectAudio)
        
        pushButton_OutputFolder = self.window.findChild(QPushButton, 'pushButton_OutputFolder')
        pushButton_OutputFolder.clicked.connect(self.SelectOutputFolder)
                
        actionSave_Config = self.window.findChild(QObject, 'actionSave_Config')
        actionSave_Config.triggered.connect(self.SaveConfigFile)
        
        actionLoad_Config = self.window.findChild(QObject, 'actionLoad_Config')
        actionLoad_Config.triggered.connect(self.LoadConfigFile)
                
        actionCreate_Edit_JSON = self.window.findChild(QObject, 'actionCreate_Edit_JSON')
        actionCreate_Edit_JSON.triggered.connect(self.Create_Edit_JSON)
                        
        actionSave_Combine_Video_Scripts_2 = self.window.findChild(QObject, 'actionSave_Combine_Video_Scripts_2')
        actionSave_Combine_Video_Scripts_2.triggered.connect(self.SaveFFMPEGBAtchScripts)
                                
        actionOpen_Project_Pipeline_Folder = self.window.findChild(QObject, 'actionOpen_Project_Pipeline_Folder')
        actionOpen_Project_Pipeline_Folder.triggered.connect(self.actionOpen_Project_Pipeline_Folder)
                                        
        actionOpen_Project_Scene_Output_Folder = self.window.findChild(QObject, 'actionOpen_Project_Scene_Output_Folder')
        actionOpen_Project_Scene_Output_Folder.triggered.connect(self.actionOpen_Project_Scene_Output_Folder)
                                        
        actionSave_Combine_Video_Scripts = self.window.findChild(QObject, 'actionSave_Combine_Video_Scripts')
        actionSave_Combine_Video_Scripts.triggered.connect(self.actionSave_Combine_Video_Scripts)
                                                
        actionLoad_Project_Window = self.window.findChild(QObject, 'actionLoad_Project_Window')
        actionLoad_Project_Window.triggered.connect(self.OpenLoadProjectsWindow)
                                                        
        actionImport_Config = self.window.findChild(QObject, 'actionImport_Config')
        actionImport_Config.triggered.connect(self.ImportConfig)
                                                                
        actionSet_Scene_Shot_Blender_Files = self.window.findChild(QObject, 'actionSet_Scene_Shot_Blender_Files')
        actionSet_Scene_Shot_Blender_Files.triggered.connect(self.OpenSetBlendFilesWindow)
                                                                        
        actionSet_Scene_Shot_Blender_Files = self.window.findChild(QObject, 'actionSet_Scene_Shot_Blender_Files')
        actionSet_Scene_Shot_Blender_Files.triggered.connect(self.OpenSetBlendFilesWindow)
                                                                                
        actionRefresh_User = self.window.findChild(QObject, 'actionRefresh_User')
        actionRefresh_User.triggered.connect(self.Refresh_User)
        
        self.tableWidgetUser = self.window.findChild(QTableWidget, 'tableWidgetUser')
        self.tableViewUsers = self.window.findChild(QTableView, 'tableViewUsers')
        
        self.lineEditCSVPath = self.window.findChild(QLineEdit, 'lineEditCSVPath')
        self.lineEditCSVPath.setText("-")
        
        self.lineEditAudio = self.window.findChild(QLineEdit, 'lineEditAudio')
        self.lineEditAudio.setText("-")
        
        self.lineEditOutputFolder = self.window.findChild(QLineEdit, 'lineEditOutputFolder')
        self.lineEditOutputFolder.setText("-")
        
        self.lineEditConfigLocation = self.window.findChild(QLineEdit, 'lineEditConfigLocation')
        self.lineEditConfigLocation.setText("-")
        
        self.lineEditProjectName = self.window.findChild(QLineEdit, 'lineEditProjectName')
        self.lineEditProjectName.setText("-")
        
                
        self.lineEditVersion = self.window.findChild(QLineEdit, 'lineEditVersion')
        self.lineEditVersion.editingFinished.connect(self.lineEditVersionEdited)
        
        self.lineEditVersion.setText("-")
        
        
        self.lineEditProjectName = self.window.findChild(QLineEdit, 'lineEditProjectName')
        self.lineEditProjectName.editingFinished.connect(self.UpdateProjectName)
        
        self.lineEditProjectName.setText("-")
        
        
        
        
        self.LoadConfigFile()
        self.Refresh_User()
        
        self.window.show()
        
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = mainwindow()
    widget.show()
    sys.exit(app.exec_())
