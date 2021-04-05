#ifndef CLIENTCLASS_H
#define CLIENTCLASS_H

#include <QObject>
#include "groupsclass.h"

class ClientClass : public QObject
{
    Q_OBJECT
public:
    explicit ClientClass(QObject *parent = nullptr);
    int id;
    QString Name;
    QString Description;
    QString Icon;
    QString FilePath;
    GroupsClass *Group_;
    int GroupId;

    void GetClientFromId(QString ClientId);
    void SetGroup(GroupsClass *GroupToUse);
    void ClientFromRecord(QSqlRecord Record);


    void SetClient(int Id_, int GroupId_, QString Name_, QString Description_, QString Icon_, QString FilePath_);
signals:

};

#endif // CLIENTCLASS_H
