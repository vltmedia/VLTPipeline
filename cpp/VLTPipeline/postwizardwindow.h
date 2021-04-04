#ifndef POSTWIZARDWINDOW_H
#define POSTWIZARDWINDOW_H

#include <QMainWindow>

namespace Ui {
class PostWizardWindow;
}

class PostWizardWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit PostWizardWindow(QWidget *parent = nullptr);
    ~PostWizardWindow();

private:
    Ui::PostWizardWindow *ui;
};

#endif // POSTWIZARDWINDOW_H
