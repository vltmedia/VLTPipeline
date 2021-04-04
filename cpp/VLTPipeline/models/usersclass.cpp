#include "usersclass.h"
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
    Groups =  model->record(0).value("Groups").toString() ;
    GroupNameOveride = model->record(0).value("GroupNameOveride").toString()  ;
    About =  model->record(0).value("About").toString() ;
    Email = model->record(0).value("Email").toString() ;
    Signature =  model->record(0).value("Signature").toString() ;
    Website =  model->record(0).value("Website").toString() ;
    Description = model->record(0).value("Description").toString()  ;
    Icon = model->record(0).value("Icon").toString()  ;
}
