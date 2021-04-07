#ifndef USERSETTINGSCLASS_H
#define USERSETTINGSCLASS_H

#include <QObject>

class UserSettingsClass : public QObject
{
    Q_OBJECT
public:
    explicit UserSettingsClass(QObject *parent = nullptr);
    QString Theme = "MacOS";
    QString SettingsFilePath;

    void LoadTheme();

    void LoadSettings();
    void WriteSettings();
public slots:
    void SetTheme(QString ThemeToLoad);
signals:

};

#endif // USERSETTINGSCLASS_H
