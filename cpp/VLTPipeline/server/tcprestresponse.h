#ifndef TCPRESTRESPONSE_H
#define TCPRESTRESPONSE_H
#include <QJsonObject>
#include <QObject>
#include <QJsonObject>
class TCPRestResponse : public QObject
{

    Q_OBJECT
public:

    bool Success = true;
    QString message = "User logged in successfully";
    QString status_code = "200";
    QString error_code = "0";
    QJsonObject data;

    QString ResponseTemplate = "HTTP/1.1 %RESPCODE% OK \nContent-Type: application/vnd.api+json \n{  %JSDATA% }";
    QString CurrentResponse = "HTTP/1.1 200 OK \nContent-Type: application/vnd.api+json \n{ \"data\": {\"data\": \"Hey\":} }";
    QString CurrentJSONResponse = "{}";

    TCPRestResponse();
    void SetSuccess(QString Message, QJsonObject Data);
    void SetError(QString Message, QString ErrorCode , QJsonObject Data);
    QString GetResponse(bool HTTPResponse);
    void CreateResponse();

};

#endif // TCPRESTRESPONSE_H
