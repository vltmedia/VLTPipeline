#include "tcpserver.h"
#include "tcprestresponse.h"
#include "tcproutes.h"




#include <QDebug>
#include <qDebug>
#include <QJsonDocument>
#include <QJsonObject>
#include <QHostAddress>
#include <QAbstractSocket>

TCPServer::TCPServer(quint16 port) :  _server(this)


{

    _server.listen(QHostAddress::Any, port);
//    _server.listen(QHostAddress::Any, 4242);
    connect(&_server, SIGNAL(newConnection()), this, SLOT(onNewConnection()));
}


void TCPServer::onNewConnection()
{
   QTcpSocket *clientSocket = _server.nextPendingConnection();
   connect(clientSocket, SIGNAL(readyRead()), this, SLOT(onReadyRead()));
   connect(clientSocket, SIGNAL(stateChanged(QAbstractSocket::SocketState)), this, SLOT(onSocketStateChanged(QAbstractSocket::SocketState)));

    _sockets.push_back(clientSocket);
    for (QTcpSocket* socket : _sockets) {

        qDebug() << QString::fromStdString(clientSocket->peerAddress().toString().toStdString() + " connected to server !\n");
//        socket->write(QByteArray::fromStdString(clientSocket->peerAddress().toString().toStdString() + " connected to server !\n"));
    }
}

void TCPServer::onSocketStateChanged(QAbstractSocket::SocketState socketState)
{
    if (socketState == QAbstractSocket::UnconnectedState)
    {

        QTcpSocket* sender = static_cast<QTcpSocket*>(QObject::sender());
        _sockets.removeOne(sender);
        qDebug() << QString::fromStdString(sender->peerAddress().toString().toStdString() + " LEFT server !\n");
    }
}

void TCPServer::ParseHTTPRestRequestToJson(QString request ){
    // Example:
    // "GET / HTTP/1.1\r\nHost: localhost:6778\r\nUser-Agent: insomnia/2021.2.2\r\nContent-Type: application/json\r\nAccept: */*\r\nContent-Length: 154\r\n\r\n{\n  \"Type\": \"GET\",\n  \"Route\": \"/\",\n  \"Data\": {\n    \"Name\": \"Get Ping\",\n    \"Data\": {}\n  },\n  \"Sender\": {\n    \"Name\": \"Blender\",\n    \"Reason\": \"Init\"\n  }\n}"
HTTPRequest = true;
    auto splitt = request.split("{");
    splitt.removeFirst();
    QString newjs = "{" + splitt.join("{").replace("\n", "");
    QByteArray json_bytes = newjs.toLocal8Bit();

    // step 3
    auto json_doc = QJsonDocument::fromJson(json_bytes);

    if (json_doc.isNull()) {
        qDebug() << "Failed to create JSON doc." ;

    }
    if (!json_doc.isObject()) {
        qDebug() << "JSON is not an object." ;

    }

    QJsonObject json_obj = json_doc.object();

    if (json_obj.isEmpty()) {
        qDebug() << "JSON object is empty." ;

    }
    RouteRestRequest(json_obj);
}

void TCPServer::CheckRestRequestType(QString request){
    if (request.contains("Content-Type: application/json")){
        HTTPRequest = true;
        // If it does contain it, it's from am HTTP request. Process it Differently
        ParseHTTPRestRequestToJson(request);

    }
    else{
        HTTPRequest = false;
   ParseRestRequestToJson( request);
    }
}


void TCPServer::ParseRestRequestToJson(QString request){

    // Example Request:
    // {"Type":"GET","Route":"\/","Data":{"Name":"Get Ping","Data":{}},"Sender":{"Name":"Blender","Reason":"Init"}}


    QByteArray json_bytes = request.toLocal8Bit();

    // step 3
    auto json_doc = QJsonDocument::fromJson(json_bytes);

    if (json_doc.isNull()) {
        qDebug() << "Failed to create JSON doc." ;

    }
    if (!json_doc.isObject()) {
        qDebug() << "JSON is not an object." ;

    }

    QJsonObject json_obj = json_doc.object();

    if (json_obj.isEmpty()) {
        qDebug() << "JSON object is empty." ;

    }
    RouteRestRequest(json_obj);

    // step 4
//    auto result = json_obj.toVariantMap();

}



void TCPServer::ParseRestRequestToJson(QJsonObject templateObj, QString key_ ,  QJsonObject &jsonObj){

    QJsonObject ChoiceObj = templateObj.value(QString(key_)).toObject();
     jsonObj = ChoiceObj;

//     jsonObj = QJsonDocument::fromJson(templateObj[key_].toString().toLocal8Bit()).object();



}


void TCPServer::RouteRestRequest(QJsonObject request){

    QString Type = request["Type"].toString();
    QString Route = request["Route"].toString();
    QJsonObject SenderJs;
    ParseRestRequestToJson(request, "Sender",SenderJs );

    if(Type == "GET"){
        TCPRoutes Routes;
        Routes.ParseGETRoute(Route);
        if (HTTPRequest){
        currentsocket->write(QByteArray::fromStdString("HTTP/1.1 200 OK \nContent-Type: application/vnd.api+json \n{\"Success\":true,\"data\":{\"Client\":\"Nike\"},\"message\":\"Requested : GET\",\"status_code\":\"200\"} "));
        }else{
                    QJsonObject responseObject;
                    responseObject.insert("Client", QJsonValue::fromVariant("Nike"));
                    QString Resp = "Requested : " +  Type;
                    TCPRestResponse tcpresponse;
                    tcpresponse.SetSuccess(Resp, responseObject);
                    auto responsee = tcpresponse.GetResponse(HTTPRequest);
                    QByteArray ContentType = ("HTTP/1.0 200 OK\r\n");
                    currentsocket->write(QByteArray::fromStdString(responsee.toStdString()));

        }
    }


}

void TCPServer::onReadyRead()
{
    QTcpSocket* sender = static_cast<QTcpSocket*>(QObject::sender());
    currentsender = sender;
    currentsocket = sender;
    QByteArray datas = sender->readAll();

    for (QTcpSocket* socket : _sockets) {
        if (socket != sender){

            currentsocket = socket;

            socket->write(QByteArray::fromStdString(sender->peerAddress().toString().toStdString() + ": " + datas.toStdString()));
        }
    }

    // Parse the request that was sent.
    QString parseddata = QString::fromStdString(datas.toStdString());
    CheckRestRequestType(parseddata);
    //    qDebug() << parseddata;


}
