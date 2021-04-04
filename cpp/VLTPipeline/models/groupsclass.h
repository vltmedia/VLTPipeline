#ifndef GROUPSCLASS_H
#define GROUPSCLASS_H

#include <QObject>
#include "usersclass.h"

class GroupsClass : public QObject
{
    Q_OBJECT
public:
    explicit GroupsClass(QObject *parent = nullptr,int GroupId_ = 7, QString Name_ = "",int UserId_ = 9999,QString Description_ = "",QString Icon_ = "");
    int GroupId = 0;
    int UserId = 0;
    UsersClass User;
    QString Name;
    QString Description;
    QString Icon;

    void GroupFromQModelIndex(QModelIndex index);

signals:

};

#endif // GROUPSCLASS_H
