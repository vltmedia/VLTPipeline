#include "usersclass.h"
//#include "../dbmanager.h"
#include <QSqlQuery>
UserClass::UserClass(QObject *parent) : QObject(parent)
{


}

//void UserClass::GetUsers(DbManager &db){
//QString command = "SELECT * from MOCK_users;";
// QSqlQuery query = db.RunCommandWithReturn(command);
// QVector<UserClass> Users;
// while(query.next())
//            {
//            UserClass *newuser = new UserClass(nullptr);
//            newuser->id << query.value("id").toString();
//            newuser->Name << query.value("Name").toString();
//            newuser->Name << query.value("Groups").toString();
//            newuser->Name = query.value("GroupNameOveride").toString();
//////            qDebug() << query.value(0).toString();
//////            qDebug() << query.value("GroupNameOveride").toString();
//////            qDebug() << query.value("About").toString();

//           }
//}
