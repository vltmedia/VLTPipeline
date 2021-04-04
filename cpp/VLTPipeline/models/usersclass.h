#ifndef USERSCLASS_H
#define USERSCLASS_H

#include <QString>
#include <QSqlQueryModel>

class UsersClass
{
public:
    UsersClass();
    int id;
    QString Name;
    QString Groups;
    QString GroupNameOveride;
    QString About;
    QString Email;
    QString Signature;
    QString Website;
    QString Description;
    QString Icon;

    void UserFromQSqlQueryModel(QSqlQueryModel *model);
};

#endif // USERSCLASS_H
