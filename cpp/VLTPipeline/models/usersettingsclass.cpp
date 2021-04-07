#include "usersettingsclass.h"

#include <QFile>
#include <qDebug>
#include <QApplication>
#include <QSettings>

UserSettingsClass::UserSettingsClass(QObject *parent) : QObject(parent)
{
LoadSettings();
}

void UserSettingsClass::LoadSettings() {

//QSettings settings(SettingsFilePath, QSettings::IniFormat);
//QString sText = settings.value("t", "").toString();

QSettings settings("VLT Media", "ProjectPipeline");

settings.beginGroup("UI");
Theme = settings.value("Theme", "ManjaroMix").toString();
settings.endGroup();
}

void UserSettingsClass::LoadTheme()
{
    QFile file( QCoreApplication::applicationDirPath() +"/styles/" + Theme + ".qss");
    qDebug() <<  QCoreApplication::applicationDirPath() +"/styles/" + Theme + ".qss";
    if(file.open(QFile::ReadOnly)) {
       QString StyleSheet = QLatin1String(file.readAll());
       qApp->setStyleSheet(StyleSheet);
    }
}

void UserSettingsClass::SetTheme(QString ThemeToLoad)
{
    Theme = ThemeToLoad;
    QFile file( QCoreApplication::applicationDirPath() +"/styles/" + Theme + ".qss");
    qDebug() <<  QCoreApplication::applicationDirPath() +"/styles/" + Theme + ".qss";
    if(file.open(QFile::ReadOnly)) {
       QString StyleSheet = QLatin1String(file.readAll());
       qApp->setStyleSheet(StyleSheet);
    }
    WriteSettings();
}

void UserSettingsClass::WriteSettings()
{
    QSettings settings("VLT Media", "ProjectPipeline");

    settings.beginGroup("UI");
    settings.setValue("Theme", Theme);

    settings.endGroup();
}

