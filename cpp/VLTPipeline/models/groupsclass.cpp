#include "groupsclass.h"

#include <QModelIndex>
#include <QCoreApplication>
#include <QSqlQueryModel>
#include <QSqlRecord>
#include <qDebug>
#include "usersclass.h"
#include "vltdatabasemanager.h"
GroupsClass::GroupsClass(QObject *parent, int GroupId_,QString Name_ ,int UserId_,QString Description_,QString Icon_) : QObject(parent)
{
    GroupId = GroupId_;
    UserId = UserId_;
    Name = Name_;
    Description = Description_;
    Icon = Icon_;
}

void GroupsClass::GroupFromQModelIndex(QModelIndex index)
{
    GroupId=index.sibling(index.row(),0).data().toInt();
    Name = index.sibling(index.row(),1).data().toString();
    Description = index.sibling(index.row(),2).data().toString();
     Icon = index.sibling(index.row(),3).data().toString();
    UserId=index.sibling(index.row(),4).data().toInt();
#ifdef QT_DEBUG
   VLTDatabaseManager vltdatabaseman(QCoreApplication::applicationDirPath() +"/mockdb.db");
#else
    VLTDatabaseManager vltdatabaseman(QCoreApplication::applicationDirPath() +"/productiondb.db");
#endif
    QSqlQueryModel *modalUser;
   vltdatabaseman.GetUserid(QString::number(UserId), modalUser);

//    User.UserFromQSqlQueryModel(modalUser);


//    qDebug() << this;

}
