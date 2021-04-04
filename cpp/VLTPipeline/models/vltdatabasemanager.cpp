#include "vltdatabasemanager.h"

#include <QCoreApplication>
#include <QSqlQuery>
#include <QSqlResult >
#include <qDebug>
#include <QSqlRecord>
#include <QSqlQueryModel>

VLTDatabaseManager::VLTDatabaseManager(QString DatabasePath)
{
    databasePath = DatabasePath;
}

void VLTDatabaseManager::RefreshDatabase(QString DatabasePath)
{
   databasePath = DatabasePath;
}

QSqlQueryModel* VLTDatabaseManager::GetUsers()
{



    dbManager = new DbManager(databasePath);
    QString SelectCommand =  "select Name, GroupNameOveride FROM User_;";

     QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);
     QSqlQueryModel *modal = new QSqlQueryModel();
     modal->setQuery(queryy);
     return modal;
}

void VLTDatabaseManager::GetClientid(QString ClientId, QSqlQueryModel *modal)
{
     modal = new QSqlQueryModel();
    dbManager = new DbManager(databasePath);
//    QString SelectCommand =  "select UserId, Name, Password, GroupNameOveride, About, Email, Signature, Website, Description, Icon FROM User_ where UserId = " + UserId + ";";
    QString SelectCommand =  "select * FROM Client_ where ClientId = "+ClientId+";";

     QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);

     qDebug() << SelectCommand;
//     qDebug() << queryy.record();
//     qDebug() << queryy.result()->handle();
     try {
           modal->setQuery(queryy);
     }  catch (...) {
         qDebug() << "Nothing In Query";
//         qDebug() << queryy;
     }

}

void VLTDatabaseManager::GetUserid(QString UserId, QSqlQueryModel *modal)
{
    modal = new QSqlQueryModel();
    dbManager = new DbManager(databasePath);
    //    QString SelectCommand =  "select UserId, Name, Password, GroupNameOveride, About, Email, Signature, Website, Description, Icon FROM User_ where UserId = " + UserId + ";";
    QString SelectCommand =  "select * FROM User_ where UserId = 9999;";

    QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);

    qDebug() << SelectCommand;
    //     qDebug() << queryy.record();
    //     qDebug() << queryy.result()->handle();
    try {
        modal->setQuery(queryy);
    }  catch (...) {
        qDebug() << "Nothing In Query";
        //         qDebug() << queryy;
    }

}

void VLTDatabaseManager::GetUsername(QString UserName , QSqlQueryModel *modal)
{
    dbManager = new DbManager(databasePath);
    QString SelectCommand =  "select UserId, Name, Password, GroupNameOveride, About, Email, Signature, Website, Description, Icon FROM User_ where Name = '" + UserName + "';";
//    QString SelectCommand =  "select * FROM User_ where Name = '" + UserName + "';";

     QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);

     qDebug() << SelectCommand;
//     qDebug() << queryy.result()->handle();
     modal->setQuery(queryy);

}

void VLTDatabaseManager::GetUserGroups(QString UserId , QSqlQueryModel *modal)
{
    dbManager = new DbManager(databasePath);
    QString SelectCommand =  "select * from  Group_ where User = " + UserId + ";";

    QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);

    qDebug() << SelectCommand;
    //     qDebug() << queryy.result()->handle();
    modal->setQuery(queryy);

}

void VLTDatabaseManager::GetGroupClients(QString GroupId , QSqlQueryModel *modal)
{
    dbManager = new DbManager(databasePath);
    QString SelectCommand =  "select * from  Client_ where Group_ = " + GroupId + ";";

    QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);

    qDebug() << SelectCommand;
    //     qDebug() << queryy.result()->handle();
    modal->setQuery(queryy);

}

void VLTDatabaseManager::GetClientProjects(QString ClientId , QSqlQueryModel *modal)
{
    if( ClientId != ""){
    dbManager = new DbManager(databasePath);
//    modal = new QSqlQueryModel();
    QString SelectCommand =  "select * from  Project_ where Client = " + ClientId + ";";

    QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);

    qDebug() << SelectCommand;
    //     qDebug() << queryy.result()->handle();
    modal->setQuery(queryy);
}
}

QSqlQuery VLTDatabaseManager::GetUsersQuery()
{



    dbManager = new DbManager(databasePath);
//    QString SelectCommand =  "select Name, GroupNameOveride FROM User_;";
    QString SelectCommand =  "select * FROM User_;";

    QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);

    return queryy;
}

void VLTDatabaseManager::GetClients(int UserId)
{

}
