#include "postwizardwindow.h"
#include "ui_postwizardwindow.h"

PostWizardWindow::PostWizardWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::PostWizardWindow)
{
    ui->setupUi(this);
}

PostWizardWindow::~PostWizardWindow()
{
    delete ui;
}
