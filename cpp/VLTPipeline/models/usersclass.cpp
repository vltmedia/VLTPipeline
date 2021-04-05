#include "usersclass.h"
//#include "vltdatabasemanager.h"
#include <QSqlQueryModel>
#include <QSqlRecord>
#include <QSqlRecord>
UsersClass::UsersClass()
{

}

void UsersClass::UserFromQSqlQueryModel(QSqlQueryModel *model)
{

    id =  model->record(0).value("UserId").toInt() ;
    Name =  model->record(0).value("Name").toString() ;
    Password =  model->record(0).value("Password").toString() ;
    GroupNameOveride = model->record(0).value("GroupNameOveride").toString()  ;
    About =  model->record(0).value("About").toString() ;
    Email = model->record(0).value("Email").toString() ;
    Signature =  model->record(0).value("Signature").toString() ;
    Website =  model->record(0).value("Website").toString() ;
    Description = model->record(0).value("Description").toString()  ;
    Icon = model->record(0).value("Icon").toString()  ;
}

void UsersClass::UserFromRecord(QSqlRecord record)
{
     id =  record.value("UserId").toInt() ;
}

void UsersClass::UserCreate(int Id_, QString Name_, QString Password_, QString GroupNameOveride_, QString About_, QString Email_, QString Signature_, QString Website_, QString Description_, QString Icon_ )
{
    id =  Id_ ;
    Name =  Name_ ;
    Password =  Password_ ;
    GroupNameOveride = GroupNameOveride_  ;
    About =  About_ ;
    Email = Email_ ;
    Signature =  Signature_ ;
    Website = Website_ ;
    Description = Description_  ;
    Icon = Icon_  ;
}
