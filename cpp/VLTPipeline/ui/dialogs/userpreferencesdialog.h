#ifndef USERPREFERENCESDIALOG_H
#define USERPREFERENCESDIALOG_H
#include "themeselectwidget.h"

#include <QDialog>

namespace Ui {
class UserPreferencesDialog;
}

class UserPreferencesDialog : public QDialog
{
    Q_OBJECT

public:
    explicit UserPreferencesDialog(QWidget *parent = nullptr);
    ~UserPreferencesDialog();

    void LoadThemeSelector();
private:
    Ui::UserPreferencesDialog *ui;
    ThemeSelectWidget *themeSelectWidget;
};

#endif // USERPREFERENCESDIALOG_H
