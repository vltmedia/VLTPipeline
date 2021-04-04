#include "tcprestresponse.h"

#include <QJsonDocument>
TCPRestResponse::TCPRestResponse()
{

}

void TCPRestResponse::SetSuccess(QString Message, QJsonObject Data){

    QString thing =  QJsonDocument(Data).toJson(QJsonDocument::Compact).toStdString().c_str();
    Success = true;
status_code = "200";
message = Message;
data = Data;
CreateResponse();
//CurrentResponse = ResponseTemplate.replace("%RESPCODE%", status_code).replace("%JSDATA%", thing);

}


void TCPRestResponse::SetError(QString Message, QString ErrorCode , QJsonObject Data){
    Success = false;
status_code = "500";
error_code = ErrorCode;
message = Message;
data = Data;
CreateResponse();
//CurrentResponse = ResponseTemplate.replace("%RESPCODE%", status_code).replace("%JSDATA%", thing);

}

void TCPRestResponse::CreateResponse(){
    QJsonObject responseObject;
    responseObject.insert("success", QJsonValue::fromVariant(Success));
    responseObject.insert("message", QJsonValue::fromVariant(message));
    responseObject.insert("status_code", QJsonValue::fromVariant(status_code.toInt()));
    if(!Success){
    responseObject.insert("error_code", QJsonValue::fromVariant(error_code));
    }
    responseObject.insert("data", QJsonValue::fromVariant(data));

     QString ResponseString =  QJsonDocument(responseObject).toJson(QJsonDocument::Compact).toStdString().c_str();
    CurrentResponse = ResponseTemplate.replace("%RESPCODE%", status_code).replace("%JSDATA%", ResponseString);
    CurrentJSONResponse = ResponseString;

//    qDebug() << CurrentResponse;

}

QString TCPRestResponse::GetResponse(bool HTTPResponse){

    QString Response = CurrentResponse;
    if (HTTPResponse == true){
         return CurrentResponse ;}
     else{
         return CurrentJSONResponse ;
     }
}


