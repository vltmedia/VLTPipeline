#include "userslist.h"
#include <QSqlQuery>
#include <QObject>
#include "../dbmanager.h"
#include <qDebug>
#include <QSqlQuery>
#include <QVector>
UsersList::UsersList()
{

}

//void UsersList::GetUsers(){

//    QString command = "SELECT * from MOCK_users;";
////     Users = db.GetUsersCommand(true);

//     qDebug() << Users.count();


//};



void UsersList::AddUsersFromQuery(QSqlQuery query){
//    QVector<UserClass> users;
    while (query.next()) {
    UsersClass newuser;
    newuser.id = query.value("id").toInt();
    newuser.Name = query.value("Name").toString();
    Users.append(newuser);
    }
   qDebug() << Users.count();
};
