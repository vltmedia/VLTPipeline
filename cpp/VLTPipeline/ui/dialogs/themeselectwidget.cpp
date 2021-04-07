#include "themeselectwidget.h"
#include "ui_themeselectwidget.h"
#include "../../models/usersettingsclass.h"

#include <QDir>
#include <qDebug>

ThemeSelectWidget::ThemeSelectWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ThemeSelectWidget)
{
    ui->setupUi(this);
    LoadComboBox();
    Loaded = true;
}

ThemeSelectWidget::~ThemeSelectWidget()
{
    delete ui;
}




void ThemeSelectWidget::SetSelectedTheme(QString filepath)
{
    QFile file(filepath + ".qss");
    qDebug() << "Attempted Load | A 1";
    qDebug() <<filepath;
    if(file.open(QFile::ReadOnly)) {
         qDebug() << "Attempted Load | A";
       QString StyleSheet = QLatin1String(file.readAll());
            qDebug() << "Attempted Load | B";
       qApp->setStyleSheet(StyleSheet);
       qDebug() << "Attempted Load | !";
    }

}
void ThemeSelectWidget::LoadComboBox()
{
    QDir directory( QCoreApplication::applicationDirPath() +"/styles");
    QStringList themes = directory.entryList(QStringList() << "*.qss" << "*.QSS",QDir::Files);
    ThemeFileNames = themes;
    ThemeFiles.clear();
    foreach(QString theme, themes ){
        QString filepath = QCoreApplication::applicationDirPath() +"/styles/" + theme;
//        qDebug() << filepath;
        ThemeFiles.append(filepath);
        ui->comboBoxThemes->addItem(theme.replace(".qss", ""));

    }
}



//void ThemeSelectWidget::on_comboBoxThemes_currentIndexChanged(const QString &arg1)
//{
//    if(Loaded == true){
//     QString filepath = QCoreApplication::applicationDirPath() +"/styles/" + arg1;
//     SetSelectedTheme(filepath);
////qDebug() << filepath;
//    }
//}

void ThemeSelectWidget::on_comboBoxThemes_currentTextChanged(const QString &arg1)
{
    if(Loaded == true){
       QString filepath = QCoreApplication::applicationDirPath() +"/styles/" + arg1;
       CurrentTheme = arg1;
       SetSelectedTheme(filepath);
  //qDebug() << filepath;
      }
}

void ThemeSelectWidget::on_pushButton_SetTheme_clicked()
{
    UserSettingsClass usersetting(this);
    usersetting.SetTheme(CurrentTheme);

}
