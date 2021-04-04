#ifndef TCPROUTES_H
#define TCPROUTES_H

#include <QObject>

class TCPRoutes:public QObject
{
    Q_OBJECT
public:
    TCPRoutes();

    void ParseGETRoute(QString Route);

};

#endif // TCPROUTES_H
