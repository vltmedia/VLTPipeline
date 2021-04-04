#include "tcproutes.h"
#include <qDebug>
#include <QJsonDocument>
TCPRoutes::TCPRoutes()
{

}

void TCPRoutes::ParseGETRoute(QString Route)
{
    auto RouteSplit = Route.split("/");


    if(Route == "/users"){

    }


    if(Route == "/clients"){
qDebug() << "Client!";
    }


    if(Route == "/projects"){

    }


    if(Route == "/clients"){

    }


}
