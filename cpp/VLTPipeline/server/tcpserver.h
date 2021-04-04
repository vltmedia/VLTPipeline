#ifndef TCPSERVER_H
#define TCPSERVER_H

#include <QObject>

#include <QMainWindow>
#include <QTcpServer>
#include <QTcpSocket>
#include <QJsonObject>

class TCPServer :public QObject
{
    Q_OBJECT
public:
    TCPServer(quint16 port);

public slots:
    void onNewConnection();
    void onSocketStateChanged(QAbstractSocket::SocketState socketState);
    void onReadyRead();
    void ParseRestRequestToJson(QString request);
    void ParseRestRequestToJson(QJsonObject templateObj, QString key_ ,  QJsonObject &jsonObj);
    void RouteRestRequest(QJsonObject request);
    void ParseHTTPRestRequestToJson(QString request );
    void CheckRestRequestType(QString request );

private:
    QTcpSocket* currentsocket;
    QTcpSocket* currentsender;
    QTcpServer  _server;
    QList<QTcpSocket*>  _sockets;
    bool HTTPRequest = false;
};

#endif // TCPSERVER_H
