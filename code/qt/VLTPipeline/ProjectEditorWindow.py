import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_EditorConfigWindow import Ui_MainWindow as EditorConfigWindow
from ui_ClientEdit import ClientEdit
# from ShotEditor  import Ui_Form as ShotEditor
from ui_ShotEditor  import  ShotEditor
from ProjectEditor    import ProjectEditor
# from ClientEditor import ClientEdit
from palette.FusioPalette import QDarkPalette


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = EditorConfigWindow()
        self.ui.setupUi(self)
        self.windowup = False

    def ShowClients(self):
        if self.windowup:
            self.clientswindow.deleteLater()
        self.windowup = True    
        self.clientswindow = ClientEdit(self)
        self.clientswindow.setupUi(self)
        self.loadedwindow = self.clientswindow
        # self.clientswindow.show()
        self.ui.gridLayout.addWidget(self.clientswindow.widget)
        
    def ShowProjects(self):
        if self.windowup:
            self.clientswindow.deleteLater()
        self.windowup = True    
        
        self.clientswindow = ProjectEditor(self)
        self.clientswindow.setupUi(self)
        self.loadedwindow = self.clientswindow
        
        # self.clientswindow.show()
        self.ui.gridLayout.addWidget(self.clientswindow.widget)
                
    def ShowShots(self):
        if self.windowup:
            self.clientswindow.deleteLater()
        self.windowup = True    
        
        self.clientswindow = ShotEditor(self)
        self.clientswindow.setupUi(self)
        self.loadedwindow = self.clientswindow
        
        # self.clientswindow.show()
        # self.shotswindow = ShotEditor(self)
        # self.shotswindow.setupUi(self)
        # self.clientswindow.show()
        self.ui.gridLayout.addWidget(self.clientswindow.widget)
        
    def ClickedA(self):
        
        self.clientswindow = ClientEdit()
        self.clientswindow.setupUi(self)
        # self.clientswindow.show()
        self.ui.gridLayout.addWidget(self.clientswindow)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.ShowProjects()
    
    DarkPalette = QDarkPalette()
    DarkPalette.set_app(app)
    sys.exit(app.exec_())