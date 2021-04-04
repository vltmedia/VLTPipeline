#ifndef VLTDATABASEMANAGER_H
#define VLTDATABASEMANAGER_H
#include "../models/userslist.h"
#include <QObject>
#include <QSqlQueryModel>

class VLTDatabaseManager :public QObject
{
    Q_OBJECT
public:
    VLTDatabaseManager(QString DatabasePath);

    QString databasePath;
    DbManager *dbManager;

    void RefreshDatabase(QString DatabasePath);
    QSqlQueryModel* GetUsers();
    void GetUserid(QString UserId , QSqlQueryModel *modal);
    void GetClientid(QString ClientId, QSqlQueryModel *modal);
    void GetClientProjects(QString ClientId, QSqlQueryModel *modal);
    void GetUsername(QString UserName , QSqlQueryModel *modal);
    void GetUserGroups(QString UserId , QSqlQueryModel *modal);
    void GetGroupClients(QString GroupId , QSqlQueryModel *modal);
    QSqlQuery GetUsersQuery();
    void GetClients(int UserId);
};

#endif // VLTDATABASEMANAGER_H
