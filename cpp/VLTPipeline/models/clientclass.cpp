#include "clientclass.h"
#include "vltdatabasemanager.h"
#include "groupsclass.h"
#include <QSqlQueryModel>
#include <QSqlRecord>
#include <QCoreApplication>
ClientClass::ClientClass(QObject *parent) : QObject(parent)
{

}

void ClientClass::GetClientFromId(QString ClientId)
{
QSqlQueryModel *modalgroup = new QSqlQueryModel(this);
#ifdef QT_DEBUG
   VLTDatabaseManager vltdatabaseman(QCoreApplication::applicationDirPath() +"/mockdb.db");
#else
    VLTDatabaseManager vltdatabaseman(QCoreApplication::applicationDirPath() +"/productiondb.db");
#endif

    vltdatabaseman.GetClientid(ClientId, modalgroup);
    id =  modalgroup->record(0).value("UserId").toInt() ;
    GroupId =  modalgroup->record(0).value("Group_").toInt() ;
    Name =  modalgroup->record(0).value("Name").toString() ;
    FilePath =  modalgroup->record(0).value("FilePath").toString() ;
     Description = modalgroup->record(0).value("Description").toString()  ;
    Icon = modalgroup->record(0).value("Icon").toString()  ;

}

void ClientClass::SetGroup(GroupsClass *GroupToUse)
{
    Group_ = GroupToUse;
}
