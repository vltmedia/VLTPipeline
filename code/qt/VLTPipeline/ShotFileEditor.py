# This Python file uses the following encoding: utf-8
import sys
import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
from palette.FusioPalette import QDarkPalette

from PySide2.QtCore import QFile, Slot
from PySide2.QtWidgets import QPushButton, QLineEdit, QStatusBar
from PySide2.QtCore import  QObject, QUrl
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog, QWidget, QListWidgetItem, QListWidget, QTableView, QComboBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from py.models.util.software_class import SoftwarePackageBlender, SoftwarePackageHoudini, SoftwarePackageCinema4D, SoftwarePackageFusion,SoftwarePackageAfterEffects,SoftwarePackagePremiere, SoftwarePackageMaya
from py.models.util.scene_class import ShotFileClass, ShotClass, SceneClass
from py.models.util.project_class import ProjectClass
from py.postpipelinefiles import PostPipeline
from py.createffmpegeditfiles import RunMainProcess, RunProcessProject, RunProcessBatsProject
import glob

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

class shotFileEditor(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Load Projects")
        self.load_ui()
        self.NewShot()
        
        
    def ShowStatusMessage(self, message):
        self.statusbar.showMessage(self.tr(message))   
            
    def NewShot(self):
        scene = SceneClass("Untitled")   
        if hasattr(self, "Shot"):
            scene = self.Shot.Scene   
            
        shot = ShotClass("SHOW01",scene)   
        self.ShotFile = ShotFileClass(shot)
        self.ShowStatusMessage("Created a New Shot!")
        self.RefreshUI()
        
            
    def GetProjects(self):
        projects = {"Projects" : []}
        for name in glob.glob(self.projectspath + 'ShotFileEditor.ini'):
            proj = {"Project": os.path.basename(name), "FilePath":name}
            projects["Projects"].append(proj)
            newitem = QListWidgetItem(os.path.basename(name))
            self.listWidget.addItem(newitem)
        self.projects = projects   
        self.ShowStatusMessage("Found "+str(len(projects["Projects"]))+" projects!")
    
    
    def ItemClicked(self, item):
        print(item.row())
        print(self.projects)
        selectedProject = self.projects["Projects"][item.row()]
        self.selectedProject = selectedProject
        print(selectedProject)
        
    def ChangedRenderEngines(self, item):
        print(item)
            
    def ChangedSoftware(self, item):
        Softwaree = ["Blender","Houdini","Maya","Cinema4D","Fusion","After Effects","Premiere"]
        Softwaree = [SoftwarePackageBlender("Name"),SoftwarePackageHoudini("Name"),SoftwarePackageMaya("Name"),SoftwarePackageCinema4D("Name"),SoftwarePackageFusion("Name"),SoftwarePackageAfterEffects("Name"),SoftwarePackagePremiere("Name")]
        self.ShotFile.SoftwarePackage = Softwaree[item]
        self.ShowStatusMessage("Set Shot File Software Package to | "+ self.ShotFile.SoftwarePackage.SoftwareName )
        print(self.ShotFile.SoftwarePackage)
    
    def LoadSelectedProjectFile(self):
        filepath = self.selectedProject["FilePath"]
        self.parent.ImportConfigStrict(filepath)
        self.ShowStatusMessage("Succesfully loaded | " + self.selectedProject["Project"] + " !!")
        
        
    def SelectFilepath(self):
        fileNames = QFileDialog.getOpenFileNames(self,
        self.tr("Select Scene_Shot_Version.blend Files"), "/", self.tr("Scene_Shot_Version.blend Files' (*.blend)"))
        filess = fileNames[0]
        for f in filess:
            newitem = QListWidgetItem(os.path.basename(f))
            self.listWidgetBlendFilesImport.addItem(newitem)
        
            self.blendfiles.append(f)
            # print('f[1]   |' , f[1])
        self.ShowStatusMessage("Succesfully added | " + str(len(self.blendfiles)) + " Blend files!!")
        
    def RefreshUI(self):
        self.lineEditVersion_ShotID.setText( self.ShotFile.Shot.ShotID)
        self.lineEditFullID.setText(self.ShotFile.Shot.FullID)
        self.lineFilepath.setText(self.ShotFile.FilePath)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "ShotFileEditor.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        
        self.statusbar = self.window.findChild(QStatusBar, 'statusbar')
        self.tableViewCameras = self.window.findChild(QTableView, 'tableViewCameras')
        self.tableViewExports = self.window.findChild(QTableView, 'tableViewExports')
        self.tableViewSceneTable = self.window.findChild(QTableView, 'tableViewSceneTable')
        self.tableViewProject = self.window.findChild(QTableView, 'tableViewProject')
        self.tableViewShot = self.window.findChild(QTableView, 'tableViewShot')
        self.lineFilepath = self.window.findChild(QLineEdit, 'lineFilepath')
        self.lineEditVersion_ShotID = self.window.findChild(QLineEdit, 'lineEditVersion_ShotID')
        self.lineEditFullID = self.window.findChild(QLineEdit, 'lineEditFullID')
        
                                                                
        
                
        pushButtonSelectFilepath = self.window.findChild(QPushButton, 'pushButtonSelectFilepath')
        pushButtonSelectFilepath.clicked.connect(self.SelectFilepath)
        
        actionNew = self.window.findChild(QObject, 'actionNew')
        actionNew.triggered.connect(self.NewShot)
                                        
                
        self.pushButtonClearShotFile = self.window.findChild(QPushButton, 'pushButtonClearShotFile')
        self.pushButtonClearShotFile.clicked.connect(self.NewShot)
                                                
                
        # self.pushButtonOpenFilePath = self.window.findChild(QPushButton, 'pushButtonOpenFilePath')
        # self.pushButtonOpenFilePath.clicked.connect(self.LoadSelectedShotFile)
        
                
        # self.pushButtonCameraAdd = self.window.findChild(QPushButton, 'pushButtonCameraAdd')
        # self.pushButtonCameraAdd.clicked.connect(self.CameraAdd)
        
                
        # self.pushButtonCamerMinus = self.window.findChild(QPushButton, 'pushButtonCamerMinus')
        # self.pushButtonCamerMinus.clicked.connect(self.CameraMinus)
        
                
        # self.pushButtonExportsAdd = self.window.findChild(QPushButton, 'pushButtonExportsAdd')
        # self.pushButtonExportsAdd.clicked.connect(self.ExportsAdd)
        
                
        # self.pushButtonExportsMinus = self.window.findChild(QPushButton, 'pushButtonExportsMinus')
        # self.pushButtonExportsMinus.clicked.connect(self.ExportsMinus)
        
                
        # self.pushButtonSelectProject = self.window.findChild(QPushButton, 'pushButtonSelectProject')
        # self.pushButtonSelectProject.clicked.connect(self.SelectProject)
        
                
        self.comboBoxRenderEngines = self.window.findChild(QObject, 'comboBoxRenderEngines')
        self.comboBoxRenderEngines.currentIndexChanged.connect(self.ChangedRenderEngines)
        
                
        self.comboBoxSoftware = self.window.findChild(QComboBox, 'comboBoxSoftware')
        self.comboBoxSoftware.currentIndexChanged.connect(self.ChangedSoftware)
        

        
        # newitem = QListWidgetItem("thing 1")
        # self.listWidget.addItem(newitem)
        self.window.show()
        
        ui_file.close()

class shotFileEditorSChild(shotFileEditor):                           # <===
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Load Projects")
        self.parent = parent
        self.projectspath = parent.PostPipeline.dirname +"projects"
        self.load_ui()


if __name__ == "__main__":
    app = QApplication([])
    # widget = shotFileEditor()
    widget = shotFileEditor()
    widget.window.show()
    DarkPalette = QDarkPalette()
    DarkPalette.set_app(app)
    sys.exit(app.exec_())
