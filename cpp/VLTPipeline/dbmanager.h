#ifndef DBMANAGER_H
#define DBMANAGER_H
#include "models/usersclass.h"
#include "models/userslist.h"
#include <QString>;
#include <QSqlDatabase>
#include <QSqlDatabase>
#include <QSqlDriver>
#include <QSqlError>
#include <QSqlQuery>
#include <QVector>

class DbManager
{
public:
    DbManager(const QString& path);

    void RunCommandsFromFile(QString& path);
    void RunCommand(QString& path);
//    void GetUsersCommand(bool useMock);
    QSqlQuery RunCommandWithReturn(QString& command);

private:
    QSqlDatabase m_db;

};

#endif // DBMANAGER_H
