#include "usersdialog.h"
#include "ui_usersdialog.h"
#include "../../dbmanager.h"
#include "../../models/userslist.h"
# include "../../models/groupsclass.h"
# include "../../models/clientclass.h"
#include <QSqlQuery>
#include <QSqlRecord>
#include <QSqlQueryModel>
#include "models/vltdatabasemanager.h"

UsersDialog::UsersDialog(QWidget *parent) : QDialog(parent),
    ui(new Ui::UsersDialog)
{
    ui->setupUi(this);
#ifdef QT_DEBUG
   DatabaseManager = new VLTDatabaseManager(QCoreApplication::applicationDirPath() +"/mockdb.db");
#else
    DatabaseManager = new VLTDatabaseManager(QCoreApplication::applicationDirPath() +"/productiondb.db");
#endif
Loaded = true;
}


UsersDialog::~UsersDialog()
{

    delete ui;
}

void UsersDialog::on_pushButtonLoadusers_clicked()
{

    QString MockUserFilepath =   QCoreApplication::applicationDirPath() +"/mockdb.db";

    for(int i = 0 ; i < 499; i++){

        if(i % 7 == 0){
            dbManager = new DbManager(MockUserFilepath);
            QString SelectCommand =  "update Group_ SET User = 9999 Where GroupId = "+QString::number(i)+";";
            qDebug() << SelectCommand;
             QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);
        }

    }


RefreshDB();



}
void UsersDialog::RefreshDB(){


QString MockUserFilepath =   QCoreApplication::applicationDirPath() +"/mockdb.db";

dbManager = new DbManager(MockUserFilepath);
QString SelectCommand =  "select  * from User_ where Name = 'default'; ";

 QSqlQuery queryy = dbManager->RunCommandWithReturn(SelectCommand);
 QSqlQueryModel *modal = new QSqlQueryModel(this);
 DatabaseManager->GetUsername("default", modal);
// modal->setQuery(queryy);


 ui->tableView->setModel(modal);

 QSqlQueryModel *modalgroup = new QSqlQueryModel(this);
 DatabaseManager->GetUserGroups("9999", modalgroup);
 // modal->setQuery(queryy);


 ui->tableView_Groups->setModel(modalgroup);

ui->comboBoxGroups->clear();
 for(int i = 0; i < modalgroup->rowCount(); ++i)
 {
     ui->comboBoxGroups->addItem(modalgroup->record(i).value("Name").toString());
//     qDebug() << modalgroup->record(i).value("Name").toString();
 }


//usersList->AddUsersFromQuery(DatabaseManager->GetUsersQuery());


//usersList->GetUsers(*dbManager);
//dbManager->RunCommand(SelectCommand);

// dbManager->RunCommandsFromFile(MockUserFilepath);

}

void UsersDialog::on_pushButtonLoadclients_clicked()
{

 LoadClientsFromCurrentGroup();

}

void UsersDialog::on_tableView_Groups_clicked(const QModelIndex &index)
{
    int GroupId=index.sibling(index.row(),0).data().toInt();
    QString Namee = index.sibling(index.row(),1).data().toString();
    QString Descriptionn = index.sibling(index.row(),2).data().toString();
    QString Iconn = index.sibling(index.row(),3).data().toString();
    int UserId=index.sibling(index.row(),4).data().toInt();
   CurrentGroup_ = new GroupsClass(this );
    CurrentGroup_->GroupFromQModelIndex(index);

 LoadClientsFromCurrentGroup();


}

void UsersDialog::LoadClientsFromCurrentGroup()
{
    QSqlQueryModel *modalclients = new QSqlQueryModel(this);
    qDebug() << ui->tableView_Groups->selectionModel()->selectedIndexes();
    DatabaseManager->GetGroupClients(QString::number(CurrentGroup_->GroupId), modalclients);
    // modal->setQuery(queryy);


    ui->tableView_Clients->setModel(modalclients);
      ClientsLoaded = true;
      ui->comboBoxClients->clear();
       for(int i = 0; i < modalclients->rowCount(); ++i)
       {
           ui->comboBoxClients->addItem(modalclients->record(i).value("Name").toString());
      //     qDebug() << modalgroup->record(i).value("Name").toString();
       }
}

void UsersDialog::on_tableView_Clients_clicked(const QModelIndex &index)
{
    QSqlQueryModel *modalprojects = new QSqlQueryModel(this);
    QString ClientId=index.sibling(index.row(),0).data().toString();
//    QString Namee = index.sibling(index.row(),1).data().toString();
//    QString Descriptionn = index.sibling(index.row(),2).data().toString();
//    QString Iconn = index.sibling(index.row(),3).data().toString();
//    int UserId=index.sibling(index.row(),4).data().toInt();
//   CurrentGroup_ = new GroupsClass(this );
    DatabaseManager->GetClientProjects(ClientId,modalprojects);
//    qDebug() <<ClientId;
    ui->tableView_Projects->setModel(modalprojects);
    ui->comboBoxProjects->clear();
    for(int i = 0; i < modalprojects->rowCount(); ++i)
    {
        ui->comboBoxProjects->addItem(modalprojects->record(i).value("Name").toString());
   //     qDebug() << modalgroup->record(i).value("Name").toString();
    }
}

void UsersDialog::on_comboBoxGroups_currentIndexChanged(int index)
{
    if(Loaded == true){
    try {
//            if(ClientsLoaded == true){
        ui->tableView_Groups->model()->index(index, 0).data().toString();
        CurrentGroup_ = new GroupsClass(this );
         CurrentGroup_->GroupFromQModelIndex(ui->tableView_Groups->model()->index(index, 0));

      LoadClientsFromCurrentGroup();

//    }
        }catch (...) {

    }
}

}

void UsersDialog::on_comboBoxClients_currentIndexChanged(int index)
{
    if(Loaded == true){
    try {
            if(ClientsLoaded == true){
        ui->tableView_Clients->model()->index(index, 0).data().toString();

         on_tableView_Clients_clicked(ui->tableView_Clients->model()->index(index, 0));


    }
        }catch (...) {

    }
}
}
