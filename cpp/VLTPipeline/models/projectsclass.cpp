#include "projectsclass.h"

ProjectsClass::ProjectsClass(QObject *parent) : QObject(parent)
{

}

void ProjectsClass::SetProject(int Id, QString Name_, QString Description_, QString Icon_, int Client_, QString ProjectType_, QString Delivery_, int Status_, QString FilePath_)
{
    id = Id;
Name = Name_;
ProjectType = ProjectType_;

Client = Client_;
FilePath = FilePath_;
Delivery = Delivery_;
Status = Status_;
Description = Description_;
Icon = Icon_;
}

