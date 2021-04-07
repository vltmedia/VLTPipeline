#include "mainwindow.h"
#include "postwizardwindow.h"
#include "ui/dialogs/usersdialog.h"
#include "ui_mainwindow.h"
#include "dbmanager.h"
#include "models/userslist.h"
#include "models/usersettingsclass.h"
#include "ui/dialogs/selectthemewidget.h"
#include "ui/dialogs/userpreferencesdialog.h"
#include <QFile>
#include <QFileInfo>
#include <QSqlQuery>
#include "server/tcpserver.h"
//#include "ui_postwizardwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
     tcpserver = new TCPServer(6778);
     LoadSettings();
LoadStyle();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::LoadStyle(){
     qDebug() << "Attempted Load | 1";
     userSettings->LoadTheme();
//     QString MockUserFilepath =   QCoreApplication::applicationDirPath() +"/styles/MaterialBlue.qss";
//     qDebug() <<  QCoreApplication::applicationDirPath();
//     qDebug() << QFileInfo(MockUserFilepath).exists();

////     QString MockUserFilepath =   "D:/Projects/Apps/VLTPipeline/cpp/build-VLTPipeline-Desktop_Qt_5_15_1_MSVC2019_64bit-Debug/styles\MaterialBlue.qss";
//    QFile file(MockUserFilepath);
//    if(file.open(QFile::ReadOnly)) {
//       QString StyleSheet = QLatin1String(file.readAll());
//          qDebug() << StyleSheet;
//       qApp->setStyleSheet(StyleSheet);
//       qDebug() << "Attempted Load";
//    }
}

void MainWindow::on_actionPost_Production_triggered()
{

}

void MainWindow::LoadSettings()
{
    userSettings = new UserSettingsClass(this);

}

void MainWindow::openPostWizardWindow()
{
    postwindow = new PostWizardWindow(); // Be sure to destroy your window somewhere
    postwindow->show();
}

void MainWindow::on_pushButton_clicked()
{
    openPostWizardWindow();
}

void MainWindow::on_actionUsers_List_triggered()
{
    usersDialog = new UsersDialog(this); // Be sure to destroy your window somewhere
    usersDialog->RefreshDB();
    usersDialog->show();
//    usersDialog->SetLoaded();
}
void MainWindow::RefreshDB(){
dbManager = new DbManager("pipelinegroup.db");

QString MockUserFilepath =  "D:/Projects/Apps/VLTPipeline/cpp/build-VLTPipeline-Desktop_Qt_5_15_1_MSVC2019_64bit-Debug/debug/mock/MOCK_USERS.sql";
QString SelectCommand =  "select * from MOCK_users ;";
usersList = new UsersList();

 QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);
usersList->AddUsersFromQuery(queryy);


//usersList->GetUsers(*dbManager);
//dbManager->RunCommand(SelectCommand);

// dbManager->RunCommandsFromFile(MockUserFilepath);

};
void MainWindow::on_actionRefresh_triggered()
{
RefreshDB();
}

void MainWindow::on_pushButton_2_clicked()
{
  tcpserver = new TCPServer(6778);
//  qDebug() << "Testt";
}

void MainWindow::on_actionGeneral_triggered()
{
     userPrefs = new UserPreferencesDialog(this);
    userPrefs->show();
}
