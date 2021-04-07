#include "userpreferencesdialog.h"
#include "ui_userpreferencesdialog.h"
#include "themeselectwidget.h"
#include <qDebug>
#include <qboxlayout.h>
UserPreferencesDialog::UserPreferencesDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::UserPreferencesDialog)
{
    ui->setupUi(this);

LoadThemeSelector();

}

UserPreferencesDialog::~UserPreferencesDialog()
{
    delete ui;
}

void UserPreferencesDialog::LoadThemeSelector()
{
    themeSelectWidget = new ThemeSelectWidget(this);
        auto layout = new QVBoxLayout();
        layout->addWidget(themeSelectWidget);
        ui->frameTheme->setLayout(layout);
}
