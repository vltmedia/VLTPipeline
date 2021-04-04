#ifndef USERSDIALOG_H
#define USERSDIALOG_H
#include "../../dbmanager.h"
#include "../../models/userslist.h"
#include "../../models/groupsclass.h"
#include "models/vltdatabasemanager.h"
#include <QDialog>

namespace Ui {
class UsersDialog;
}

class UsersDialog : public QDialog
{
    Q_OBJECT

public:
    explicit UsersDialog(QWidget *parent = nullptr);
    ~UsersDialog();

     void RefreshDB();
     bool Loaded = false;
     bool ClientsLoaded = false;
     bool ProjectsLoaded = false;
     DbManager *dbManager;
     VLTDatabaseManager *DatabaseManager;

     UsersList *usersList;
     QModelIndex CurrentGroup;
     GroupsClass *CurrentGroup_;

private slots:
    void on_pushButtonLoadusers_clicked();


    void on_pushButtonLoadclients_clicked();

    void on_tableView_Groups_clicked(const QModelIndex &index);

    void LoadClientsFromCurrentGroup();

    void on_tableView_Clients_clicked(const QModelIndex &index);

    void on_comboBoxGroups_currentIndexChanged(int index);

    void on_comboBoxClients_currentIndexChanged(int index);

private:
    Ui::UsersDialog *ui;
};

#endif // USERSDIALOG_H
