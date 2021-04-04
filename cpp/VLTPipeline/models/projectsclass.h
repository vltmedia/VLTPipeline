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
    QString ProjectType;
    QString GroupNameOveride;
    QString Client;
    QString FilePath;
    QString Delivery;
    QString Website;
    QString Description;
    QString Icon;

signals:

};

#endif // PROJECTSCLASS_H
