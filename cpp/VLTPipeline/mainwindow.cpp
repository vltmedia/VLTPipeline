#include "mainwindow.h"
#include "postwizardwindow.h"
#include "ui/dialogs/usersdialog.h"
#include "ui_mainwindow.h"
#include "dbmanager.h"
#include "models/userslist.h"
#include <QSqlQuery>
#include "server/tcpserver.h"
//#include "ui_postwizardwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
     tcpserver = new TCPServer(6778);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_actionPost_Production_triggered()
{

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
