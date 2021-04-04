#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "postwizardwindow.h"
#include "ui/dialogs/usersdialog.h"
#include "dbmanager.h"
#include "models/userslist.h"
#include "server/tcpserver.h"
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    PostWizardWindow *postwindow;
    DbManager *dbManager;
    UsersDialog *usersDialog;
    UsersList *usersList;
    TCPServer *tcpserver;
    ~MainWindow();

private slots:
    void on_actionPost_Production_triggered();

    void on_pushButton_clicked();



    void on_actionUsers_List_triggered();

    void on_actionRefresh_triggered();

    void on_pushButton_2_clicked();

public slots:
    void RefreshDB();
    void openPostWizardWindow();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
