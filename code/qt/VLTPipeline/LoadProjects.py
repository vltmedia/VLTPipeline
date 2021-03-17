# This Python file uses the following encoding: utf-8
import sys
import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
from palette.FusioPalette import QDarkPalette

from PySide2.QtCore import QFile, Slot
from PySide2.QtWidgets import QPushButton, QLineEdit, QStatusBar
from PySide2.QtCore import  QObject, QUrl
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog, QWidget, QListWidgetItem, QListWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

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

class loadProjects(QMainWindow):                           # <===
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Load Projects")
        self.parent = parent
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
        print(item.row())
        print(self.projects)
        selectedProject = self.projects["Projects"][item.row()]
        self.selectedProject = selectedProject
        print(selectedProject)
    
    def LoadSelectedProjectFile(self):
        filepath = self.selectedProject["FilePath"]
        self.parent.ImportConfigStrict(filepath)
        self.ShowStatusMessage("Succesfully loaded | " + self.selectedProject["Project"] + " !!")
        
            
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "loadProjectsWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        
        self.statusbar = self.window.findChild(QStatusBar, 'statusbar')
        self.listWidget = self.window.findChild(QListWidget, 'listWidget')
                                                                
        self.listWidget.clicked.connect(self.ItemClicked)
        
                
        pushButtonLoadProject = self.window.findChild(QPushButton, 'pushButtonLoadProject')
        pushButtonLoadProject.clicked.connect(self.LoadSelectedProjectFile)
        
        # newitem = QListWidgetItem("thing 1")
        # self.listWidget.addItem(newitem)
        self.GetProjects()
        self.window.show()
        
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = loadProjects()
    widget.window.show()
    DarkPalette = QDarkPalette()
    DarkPalette.set_app(app)
    sys.exit(app.exec_())
