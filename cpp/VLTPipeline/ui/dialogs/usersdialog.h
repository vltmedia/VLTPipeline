#ifndef USERSDIALOG_H
#define USERSDIALOG_H
#include "../../dbmanager.h"
#include "../../models/userslist.h"
#include "../../models/usersclass.h"
#include "../../models/clientclass.h"
#include "../../models/projectsclass.h"
#include "../../models/groupsclass.h"
#include "models/vltdatabasemanager.h"
#include <QDialog>
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

     GroupsClass *Group;
     UsersClass *User;

     ClientClass *Client;
     ProjectsClass *Project;
     QList<GroupsClass*> Groups;
     QList<ClientClass*> Clients;
     QList<ProjectsClass*> Projects;
     UsersList *usersList;
     QModelIndex CurrentGroup;
     int CurrentGroupIndex;
     GroupsClass *CurrentGroup_;
     void SetLoaded();
     void LoadClientFromIndex(int index);
private slots:
    void on_pushButtonLoadusers_clicked();



    void on_pushButtonLoadclients_clicked();

    void on_tableView_Groups_clicked(const QModelIndex &index);

    void LoadClientsFromCurrentGroup();

    void on_tableView_Clients_clicked(const QModelIndex &index);

    void on_comboBoxGroups_currentIndexChanged(int index);

    void on_comboBoxClients_currentIndexChanged(int index);

    void LoadUser();
    void LoadUserGroups();

    void on_comboBoxGroups_highlighted(const QString &arg1);

private:
    Ui::UsersDialog *ui;
};

#endif // USERSDIALOG_H
