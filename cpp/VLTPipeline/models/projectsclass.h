#ifndef PROJECTSCLASS_H
#define PROJECTSCLASS_H

#include <QObject>

class ProjectsClass : public QObject
{
    Q_OBJECT
public:
    explicit ProjectsClass(QObject *parent = nullptr);
    int id;
    QString Name;
    QString Description;
    QString Icon;

    QString ProjectType;
    int Client;
    QString Delivery;

    int Status;
    QString FilePath;



    void SetProject(int Id, QString Name_,
    QString Description_,
    QString Icon_,
    int Client_,
    QString ProjectType_,
    QString Delivery_,
    int Status_,
    QString FilePath_);

signals:

};

#endif // PROJECTSCLASS_H
