#ifndef USERSLIST_H
#define USERSLIST_H
#include <QSqlQuery>
#include <QObject>;
#include "../dbmanager.h"
#include "usersclass.h"
#include <qDebug>;
class UsersList
{
public:
    UsersList();

    QVector<UsersClass> Users;
    void GetUsers();
     void AddUsersFromQuery(QSqlQuery query);
//    void AppendUser(UserClass NewUser);
};

#endif // USERSLIST_H
