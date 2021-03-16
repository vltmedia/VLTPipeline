from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from VLTPipeline import form

class MainWindow(form.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        # self.ui = main()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    app.exec_()
    # sys.exit()