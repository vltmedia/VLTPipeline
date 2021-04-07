#ifndef SELECTTHEMEWIDGET_H
#define SELECTTHEMEWIDGET_H

#include <QDialog>

namespace Ui {
class SelectThemeWidget;
}

class SelectThemeWidget : public QDialog
{
    Q_OBJECT

public:
    explicit SelectThemeWidget(QWidget *parent = nullptr);
    ~SelectThemeWidget();

    void LoadComboBox();
    void SetSelectedTheme(QString filepath);
    bool Loaded = false;
private slots:
    void on_comboBoxThemes_currentIndexChanged(const QString &arg1);

private:
    Ui::SelectThemeWidget *ui;
    QStringList ThemeFiles;
    QStringList ThemeFileNames;
};

#endif // SELECTTHEMEWIDGET_H
