#include "dbmanager.h"
#include <qDebug>;
#include <QFile>;
#include "models/usersclass.h"
#include "models/userslist.h"

DbManager::DbManager(const QString& path)
{
   m_db = QSqlDatabase::addDatabase("QSQLITE");
   m_db.setDatabaseName(path);

   if (!m_db.open())
   {
      qDebug() << "Error: connection with database failed";
   }
   else
   {
      qDebug() << "Database: connection ok";
   }


}

void DbManager::RunCommandsFromFile( QString& path)
{

    QFile file(path);
    QString bigstring;
    if(!file.exists()){
           qDebug() << "NO existe el archivo "<<path;
       }else{
           qDebug() << path<<" encontrado...";
       }
       QString line;

       if (file.open(QIODevice::ReadOnly | QIODevice::Text)){
           QTextStream stream(&file);
           while (!stream.atEnd()){
               line = stream.readLine();
               QString newbig =  bigstring+line+"\n";
               bigstring = newbig;
               //qDebug() << "linea: "<<line;
           }
           QSqlQuery query;
           bool success = false;
             query.prepare("DELETE FROM people WHERE name = (:name)");

             success = query.exec();

             if(!success)
             {
                 qDebug() << "Run SQL From File Error:"
                          << query.lastError();
             }
       }
       file.close();

       qDebug() << "Successfully Opened / Ran File!";

}

//void DbManager::GetUsersCommand(bool useMock)
//{

//        QSqlQuery query;


//        bool success = false;

//            query.prepare("Select * from " );

//            success = query.exec();

//            if(!success)
//            {
//                qDebug() << "Run SQL From File Error:"
//                        << query.lastError();
//            }else{
//                qDebug() << "Successfully Ran Command!";
//                 while(query.next())
//            {
//            UsersClass newuser ;
//            QString id = "";

//            newuser.id = query.value(0).toInt();
//            newuser.Name = query.value("Name").toString();
//            newuser.Groups = query.value("Groups").toString();

//            newuser.GroupNameOveride = query.value("GroupNameOveride").toString();
//            newuser.About = query.value("About").toString();
//            newuser.Email = query.value("Email").toString();
//            newuser.Signature = query.value("Signature").toString();
//            newuser.Website = query.value("Website").toString();
//            newuser.Description = query.value("Description").toString();
//            newuser.Icon = query.value("Icon").toString();
////            Users.AppendUser(newuser);
//            }
//            }




//}

void DbManager::RunCommand( QString& command)
{

        QSqlQuery query;
        bool success = false;
            query.prepare(command);

            success = query.exec();

            if(!success)
            {
                qDebug() << "Run SQL From File Error:"
                        << query.lastError();
            }else{
                qDebug() << "Successfully Ran Command!";
                 while(query.next())
            {
            qDebug() << query.value(0).toString();
            qDebug() << query.value("GroupNameOveride").toString();
            qDebug() << query.value("About").toString();
            }
            }



}
QSqlQuery DbManager::RunCommandWithReturn( QString& command)
{

        QSqlQuery query;
        bool success = false;
            query.prepare(command);

            success = query.exec();

            if(!success)
            {
                qDebug() << "Run SQL From File Error:"
                        << query.lastError();
            }else{
                qDebug() << "Successfully Ran Command!";
//                 while(query.next())
//            {
////            qDebug() << query.value(0).toString();
////            qDebug() << query.value("GroupNameOveride").toString();
////            qDebug() << query.value("About").toString();

//            }
                 return (query);
            }



}
