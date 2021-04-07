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
    User = new UsersClass();
     Group = new GroupsClass();
     ClientClass *Client = new ClientClass();
     ProjectsClass *Project = new ProjectsClass();
#ifdef QT_DEBUG
   DatabaseManager = new VLTDatabaseManager(QCoreApplication::applicationDirPath() +"/mockdb.db");
#else
    DatabaseManager = new VLTDatabaseManager(QCoreApplication::applicationDirPath() +"/productiondb.db");
#endif
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

void UsersDialog::SetLoaded()
{
    Loaded = true;

}


void UsersDialog::RefreshDB(){



LoadUser();

LoadUserGroups();


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
    qDebug() << " Check 1 | "+ QString::number(CurrentGroup_->GetGroupId());
//    DatabaseManager->GetGroupClients(QString::number(CurrentGroup_->GroupId), modalclients);
    DatabaseManager->GetGroupClients(QString::number(CurrentGroup_->GetGroupId()), modalclients);
    // modal->setQuery(queryy);



    ui->tableView_Clients->setModel(modalclients);
      ClientsLoaded = true;
      ui->comboBoxClients->clear();
      Clients.clear();
       for(int i = 0; i < modalclients->rowCount(); ++i)
       {
//           ClientClass neclient(this);
           ClientClass *neclient = new ClientClass();
//            neclient.ClientFromRecord(modalclients->record(i));
            neclient->SetClient(modalclients->record(i).value("ClientId").toInt(),modalclients->record(i).value("GroupId").toInt(), modalclients->record(i).value("Name").toString(),modalclients->record(i).value("Description").toString(),modalclients->record(i).value("Icon").toString(),modalclients->record(i).value("FilePath").toString());
//            neclient.id = modalclients->record(i).value("ClientId").toInt();
            qDebug() << modalclients->record(i).value("ClientId").toInt();
            qDebug() << neclient->id;
            Clients.append(neclient);
           ui->comboBoxClients->addItem(modalclients->record(i).value("Name").toString());
      //     qDebug() << modalgroup->record(i).value("Name").toString();
       }



}

void UsersDialog::on_tableView_Clients_clicked(const QModelIndex &index)
{
    QSqlQueryModel *modalprojects = new QSqlQueryModel(this);
//    QString ClientId=index.sibling(index.row(),0).data().toString();

    QString ClientId= QString::number(Clients.at(index.row())->id);
//    QString Namee = index.sibling(index.row(),1).data().toString();
//    QString Descriptionn = index.sibling(index.row(),2).data().toString();
//    QString Iconn = index.sibling(index.row(),3).data().toString();
//    int UserId=index.sibling(index.row(),4).data().toInt();
//   CurrentGroup_ = new GroupsClass(this );
    DatabaseManager->GetClientProjects(ClientId,modalprojects);
    qDebug() <<ClientId;
    ui->tableView_Projects->setModel(modalprojects);
    ui->comboBoxProjects->clear();
    for(int i = 0; i < modalprojects->rowCount(); ++i)
    {
        ui->comboBoxProjects->addItem(modalprojects->record(i).value("Name").toString());
   //     qDebug() << modalgroup->record(i).value("Name").toString();
    }
}

void UsersDialog::LoadClientFromIndex(int index)
{
    if(index > -1){
    ui->tableView_Clients->model()->index(index, 0).data().toString();

//        ClientClass *Client = Clients.at(index);
    //         on_tableView_Clients_clicked(ui->tableView_Clients->model()->index(index, 0));
    QSqlQueryModel *modalprojects = new QSqlQueryModel(this);
    //    QString ClientId=index.sibling(index.row(),0).data().toString();

    QString ClientId= QString::number(Clients.at(index)->id);
    //    QString Namee = index.sibling(index.row(),1).data().toString();
    //    QString Descriptionn = index.sibling(index.row(),2).data().toString();
    //    QString Iconn = index.sibling(index.row(),3).data().toString();
    //    int UserId=index.sibling(index.row(),4).data().toInt();
    //   CurrentGroup_ = new GroupsClass(this );
    DatabaseManager->GetClientProjects(ClientId,modalprojects);
    qDebug() <<ClientId;
    ui->tableView_Projects->setModel(modalprojects);
    ui->comboBoxProjects->clear();
    for(int i = 0; i < modalprojects->rowCount(); ++i)
    {
        ProjectsClass *newproj = new ProjectsClass(this);
        newproj->SetProject(modalprojects->record(i).value("ProjectId").toInt(), modalprojects->record(i).value("Name").toString(), modalprojects->record(i).value("Description").toString(),modalprojects->record(i).value("Icon").toString(),modalprojects->record(i).value("Client").toInt(),modalprojects->record(i).value("ProjectType").toString(),modalprojects->record(i).value("Delivery").toString(),modalprojects->record(i).value("Status").toInt(),modalprojects->record(i).value("FilePath").toString());
//        void ProjectsClass::SetProject(int Id, QString Name_, QString Description_, QString Icon_, int Client_, QString ProjectType_, QString Delivery_, int Status_, QString FilePath_)
                ui->comboBoxProjects->addItem(modalprojects->record(i).value("Name").toString());
        //     qDebug() << modalgroup->record(i).value("Name").toString();
    }
    }else{
        qDebug() << index;

    }
}

void UsersDialog::on_comboBoxGroups_currentIndexChanged(int index)
{

    if(Loaded == true){
    try {
//            if(ClientsLoaded == true){

            Group->GroupFromQModelIndex(ui->tableView_Groups->model()->index(index,0));
        ui->tableView_Groups->model()->index(index, 0).data().toString();
//        CurrentGroup_ = new GroupsClass(this );
                CurrentGroup_ = Groups.at(index);

//qDebug() << Groups.at(index);

//qDebug() << CurrentGroup_;
//        CurrentGroup_ = Groups.at(index)->GroupId;
//        CurrentGroupIndex = index;
//         CurrentGroup_->GroupFromQModelIndex(ui->tableView_Groups->model()->index(index, 0));
//         CurrentGroup_->GroupFromQModelIndex(ui->tableView_Groups->model()->index(index, 0));

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
                // Update Table

        LoadClientFromIndex(index);
//        LoadClientFromIndex(Clients.at(index)->id);



    }
        }catch (...) {

    }
    }
}

void UsersDialog::LoadUser()
{
    QSqlQueryModel *modal = new QSqlQueryModel(this);
    DatabaseManager->GetUsername("default", modal);
   // modal->setQuery(queryy);

    auto record = modal->record(0);
    ui->tableView->setModel(modal);
    User = new UsersClass();

//    User->UserFromRecord(record);
User->UserCreate(record.value("UserId").toInt(),record.value("Name").toString(),record.value("Password").toString(),record.value("GroupNameOveride").toString(),record.value("About").toString(),record.value("Email").toString(),record.value("Signature").toString(),record.value("Website").toString(),record.value("Description").toString(),record.value("Icon").toString());
//void UsersClass::UserCreate(int Id_, QString Name_, QString Password_, QString GroupNameOveride_, QString About_, QString Email_, QString Signature_, QString Website_, QString Description_, QString Icon_ )
qDebug() << User;
}

void UsersDialog::LoadUserGroups()
{


    QSqlQueryModel *modalgroup = new QSqlQueryModel(this);
    // Get Groups from User ID
    DatabaseManager->GetUserGroups("9999", modalgroup);
//    DatabaseManager->GetUserGroups(QString::number(User->id), modalgroup);
    ui->tableView_Groups->setModel(modalgroup);

   ui->comboBoxGroups->clear();
    for(int i = 0; i < modalgroup->rowCount(); ++i)
    {
       GroupsClass* negg = new (GroupsClass);
        negg->GroupFromRecord(modalgroup->record(i));
        negg->GroupId = modalgroup->record(i).value("GroupId").toInt();
        Groups.append(negg);
ui->comboBoxGroups->addItem(modalgroup->record(i).value("Name").toString());
    }
qDebug() << Groups.at(0)->GroupId;
qDebug() << Groups.at(0)->GroupId;
//    Groups;
//    qDebug() << Groups.count();
}


void UsersDialog::on_comboBoxGroups_highlighted(const QString &arg1)
{
//    qDebug() << "Poo";
    SetLoaded();
}
