#include "selectthemewidget.h"
#include "ui_selectthemewidget.h"
#include <QDir>
#include <qDebug>
SelectThemeWidget::SelectThemeWidget(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SelectThemeWidget)
{
//
    ui->setupUi(this);
LoadComboBox();
Loaded = true;
}

SelectThemeWidget::~SelectThemeWidget()
{

    delete ui;
}




void SelectThemeWidget::SetSelectedTheme(QString filepath)
{
//    QFile file(filepath);
//    if(file.open(QFile::ReadOnly)) {
//       QString StyleSheet = QLatin1String(file.readAll());
//       qApp->setStyleSheet(StyleSheet);
//       qDebug() << "Attempted Load";
//    }

     qDebug() << "Attempted Load";
}
void SelectThemeWidget::LoadComboBox()
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



void SelectThemeWidget::on_comboBoxThemes_currentIndexChanged(const QString &arg1)
{
    if(Loaded == true){
     QString filepath = QCoreApplication::applicationDirPath() +"/styles/" + arg1;
     SetSelectedTheme(filepath);
//qDebug() << filepath;
    }
}
