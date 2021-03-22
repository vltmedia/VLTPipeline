# This Python file uses the following encoding: utf-8
import sys
import os
import subprocess

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
from palette.FusioPalette import QDarkPalette

from PySide2.QtCore import QFile, Slot
from PySide2.QtWidgets import QPushButton, QLineEdit, QStatusBar
from PySide2.QtCore import  QObject, QUrl
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog, QWidget, QListWidgetItem, QListWidget, QLabel,QGridLayout, QTableView, QComboBox , QTextEdit, QGraphicsView
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from py.models.util.UniversalTable import UniversalTableModel, UniversalTableFromClassModel
from ClientEditor import ClientEdit

from py.models.util.software_class import SoftwarePackageBlender, SoftwarePackageHoudini, SoftwarePackageCinema4D, SoftwarePackageFusion,SoftwarePackageAfterEffects,SoftwarePackagePremiere, SoftwarePackageMaya
from py.models.util.sqlite_class import PipelineSQL
from py.models.util.scene_class import ShotFileClass, ShotClass, SceneClass, GroupClass
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

class groupEditor(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Load Projects")
        self.load_ui()
        self.NewGroup()
        self.StartDB()
        self.CreateGroupDB()
        self.GetGroups()
        # self.UpdateGroupDB()
        # self.NewGroup()

    def StartDB(self):
        self.db = PipelineSQL()        
        self.db.ConnectToDB("pipelinegroup.db")       
    
    def CreateGroupDB(self):
        self.db.ExecuteSQL(self.Group.sqlTableGenerate())       
        # self.db.LoadFromSQLFile("mock/MOCK_Group.sql")      
        
    def LoadGroupsFromFile(self):
        self.db.LoadFromSQLFile("mock/MOCK_Group.sql")    
        self.ShowStatusMessage("Imported all groups from file!")

        
    def UpdateGroupDB(self):
        self.Group.sqlUpdate(self.db.connection, self.db.cursor)
        self.db.SaveSQL()
        self.ShowStatusMessage("Saved and Updated Group!")
        # self.Group.sqlTableGetReference(self.db.cursor)
        
        # self.db.ExecuteSQL(self.Group.sqlUpdate(self.db.cursor))       
    
                
    def Clear_ALL_Groups(self):
        self.db.ExecuteSQL("DROP TABLE 'group'")
        self.CreateGroupDB()
        self.GetGroups()
        self.Refresh_GroupList()
        self.RefreshUI()  
        self.ShowStatusMessage("Cleared Group!")
        # self.Group.sqlTableGetReference(self.db.cursor)
        
        # self.db.ExecuteSQL(self.Group.sqlUpdate(self.db.cursor))       
    
        
    def GetGroups(self):
        
        groups = self.Group.sqlTableGetAll(self.db) 
        self.groups = []
        for g in groups:
            newgroup = GroupClass(g[1])
            newgroup.loadFromSQL(g)
            self.groups.append(newgroup)

        self.Refresh_GroupList()
                    
    def ShowStatusMessage(self, message):
        self.statusbar.showMessage(self.tr(message))   
            
    def NewGroup(self):
        scene = SceneClass("Untitled")   
        if hasattr(self, "Shot"):
            scene = self.Shot.Scene   
            
        shot = ShotClass("SHOW01",scene)   
        self.Group = GroupClass("Untitled")
        self.ShowStatusMessage("Created a New Group!")
        self.RefreshUI()
        
            
    def GetProjects(self):
        projects = {"Projects" : []}
        for name in glob.glob(self.projectspath + 'GroupEditor.ini'):
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
        
        
    def SelectThumbnailFilepath(self):
        fileNames = QFileDialog.getOpenFileNames(self,
        self.tr("Select Thumbnail File"), "/", self.tr("png' (*.png)"))
        filess = fileNames[0]
        for f in filess:
            newitem = QListWidgetItem(os.path.basename(f))
            self.listWidgetBlendFilesImport.addItem(newitem)
        
            self.blendfiles.append(f)
            # print('f[1]   |' , f[1])
        self.ShowStatusMessage("Succesfully added | " + str(len(self.blendfiles)) + " Blend files!!")
        
    def LoadGroupsFromFilepath(self):
        fileNames = QFileDialog.getOpenFileNames(self,
        self.tr("Select SQL File"), "/", self.tr("sql for 'groups' (*.sql)"))
        filess = fileNames[0]
        self.db.LoadFromSQLFile(filess[0])  
        self.GetGroups()
        self.Refresh_GroupList()
        self.RefreshUI()  
        self.ShowStatusMessage("Imported all groups from file!")

            # print('f[1]   |' , f[1])
        
    def RefreshUI(self):
        self.lineEditGroupName.setText( self.Group.Name)
        # self.textEditDescription.setText(self.Group.Description)
        self.label_idText.setText("Id : " + str(self.Group.Id))
        
    def RefreshDescriptionUI(self):
        self.lineEditGroupName.setText( self.Group.Name)
        self.textEditDescription.setText(self.Group.Description)
        self.label_idText.setText("Id : " + str(self.Group.Id))
        
    def Refresh_GroupList(self):
        try:
            self.groupsmodel = UniversalTableFromClassModel(self.groups)
            self.tableViewGroupsList.setModel(self.groupsmodel)

            self.ShowStatusMessage("Succesfully Refreshed the Group List! | ")
        except:
            
            self.ShowStatusMessage("Failed Refreshed the Group List! | ")
            
    
    def UpdateGroupname(self, text):
        self.Group.Name = text
        self.RefreshDescriptionUI()
        self.ShowStatusMessage("Succesfully updated the Group Name" )
        
        
    def LoadSelectedGroup(self):
        self.Group = self.groups[self.tableViewGroupsList.selectedIndexes ()[0].row()]
        self.RefreshUI()
        print("Selectedd",self.groups[self.tableViewGroupsList.selectedIndexes ()[0].row()].Name)
        self.ShowStatusMessage("Succesfully Loaded Selected Group" )
        
        
    def UpdateGroupDescription(self):
        self.Group.Description = self.textEditDescription.toPlainText()
        self.RefreshUI()
        self.ShowStatusMessage("Succesfully updated the Description " )
                
    def OpenClients(self):

        self.clientswindow = ClientEdit(self)
        self.clientswindow.setupUi(self)
        # self.clientswindow.show()
        self.gridLayout_3.addWidget(self.clientswindow.widget)
        
        
        self.ShowStatusMessage("Succesfully updated the Description " )
        
    def ClickedA(self):
        print("Clicked A Damn")
            
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "GroupEditor.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        
        self.statusbar = self.window.findChild(QStatusBar, 'statusbar')
        self.tableViewUsers = self.window.findChild(QTableView, 'tableViewUsers')
        self.tableViewClients = self.window.findChild(QTableView, 'tableViewClients')
        self.tableViewGroupsList = self.window.findChild(QTableView, 'tableViewGroupsList')
        
        self.lineEditGroupName = self.window.findChild(QLineEdit, 'lineEditGroupName')
        self.lineEditGroupName.textChanged.connect(self.UpdateGroupname)
        
        self.textEditDescription = self.window.findChild(QTextEdit, 'textEditDescription')
        self.textEditDescription.textChanged.connect(self.UpdateGroupDescription)
        
        self.graphicsViewIcon = self.window.findChild(QGraphicsView, 'graphicsViewIcon')
        self.label_idText = self.window.findChild(QLabel, 'label_idText')
        self.tableViewGroupsList = self.window.findChild(QTableView, 'tableViewGroupsList')
        
                                                                
        
                
        self.gridLayout_3 = self.window.findChild(QGridLayout, 'gridLayout_3')
        pushButtonOpenClients = self.window.findChild(QPushButton, 'pushButtonOpenClients')
        pushButtonOpenClients.clicked.connect(self.OpenClients)
                                
        pushButtonSelectThumbnail = self.window.findChild(QPushButton, 'pushButtonSelectThumbnail')
        pushButtonSelectThumbnail.clicked.connect(self.SelectThumbnailFilepath)
                
                
        pushButtonGetGroups = self.window.findChild(QPushButton, 'pushButtonGetGroups')
        pushButtonGetGroups.clicked.connect(self.GetGroups)
                                
        pushButtonLoadSelectedGroup = self.window.findChild(QPushButton, 'pushButtonLoadSelectedGroup')
        pushButtonLoadSelectedGroup.clicked.connect(self.LoadSelectedGroup)
                
        pushButtonSaveGroup = self.window.findChild(QPushButton, 'pushButtonSaveGroup')
        pushButtonSaveGroup.clicked.connect(self.UpdateGroupDB)
                
        pushButtonImportGroups = self.window.findChild(QPushButton, 'pushButtonImportGroups')
        pushButtonImportGroups.clicked.connect(self.LoadGroupsFromFile)

                                    
        self.actionNew_Group = self.window.findChild(QObject, 'actionNew_Group')
        self.actionNew_Group.triggered.connect(self.NewGroup)
                                        
                                                
        self.actionLoad_From_Mock_sql = self.window.findChild(QObject, 'actionLoad_From_Mock_sql')
        self.actionLoad_From_Mock_sql.triggered.connect(self.LoadGroupsFromFilepath)
                                                               
        self.actionClear_ALL_Groups = self.window.findChild(QObject, 'actionClear_ALL_Groups')
        self.actionClear_ALL_Groups.triggered.connect(self.Clear_ALL_Groups)
                                        
                
        # self.pushButtonClearShotFile = self.window.findChild(QPushButton, 'pushButtonClearShotFile')
        # self.pushButtonClearShotFile.clicked.connect(self.NewGroup)
                                                
                                
        # self.pushButtonUserMinus = self.window.findChild(QPushButton, 'pushButtonUserMinus')
        # self.pushButtonUserMinus.clicked.connect(self.NewGroup)
                                                
                                
        # self.pushButtonUserAdd = self.window.findChild(QPushButton, 'pushButtonUserAdd')
        # self.pushButtonUserAdd.clicked.connect(self.NewGroup)
                                                
                                
        # self.pushButtonClientsAdd = self.window.findChild(QPushButton, 'pushButtonClientsAdd')
        # self.pushButtonClientsAdd.clicked.connect(self.NewGroup)
                                                
                                
        # self.pushButtonClientsMinus = self.window.findChild(QPushButton, 'pushButtonClientsMinus')
        # self.pushButtonClientsMinus.clicked.connect(self.NewGroup)
                                                
                
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
        
                
   
        
        # newitem = QListWidgetItem("thing 1")
        # self.listWidget.addItem(newitem)
        self.window.show()
        
        ui_file.close()

class groupEditorChild(groupEditor):                           # <===
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Load Projects")
        self.parent = parent
        self.projectspath = parent.PostPipeline.dirname +"projects"
        self.load_ui()


if __name__ == "__main__":
    app = QApplication([])
    # widget = GroupEditor()
    widget = groupEditor()
    widget.show()
    DarkPalette = QDarkPalette()
    DarkPalette.set_app(app)
    sys.exit(app.exec_())
