#ifndef USERSCLASS_H
#define USERSCLASS_H
//#include "vltdatabasemanager.h"
#include <QString>
#include <QSqlQueryModel>
#include <QSqlRecord>

class UsersClass
{
public:
    UsersClass();
    int id;
    QString Name;
    QString Password;
    QString GroupNameOveride;
    QString About;
    QString Email;
    QString Signature;
    QString Website;
    QString Description;
    QString Icon;

    void UserFromQSqlQueryModel(QSqlQueryModel *model);

    void UserFromRecord(QSqlRecord record);
    void UserCreate(int Id_, QString Name_, QString Password_, QString GroupNameOveride_, QString About_, QString Email_, QString Signature_, QString Website_, QString Description_, QString Icon_);
};

#endif // USERSCLASS_H
