#ifndef THEMESELECTWIDGET_H
#define THEMESELECTWIDGET_H

#include <QWidget>

namespace Ui {
class ThemeSelectWidget;
}

class ThemeSelectWidget : public QWidget
{
    Q_OBJECT

public:
    explicit ThemeSelectWidget(QWidget *parent = nullptr);
    ~ThemeSelectWidget();

    void SetSelectedTheme(QString filepath);
    void LoadComboBox();
    QString CurrentTheme = "ManjaroMix.qss";
private slots:
    void on_comboBoxThemes_currentTextChanged(const QString &arg1);

    void on_pushButton_SetTheme_clicked();

private:
    Ui::ThemeSelectWidget *ui;
    QStringList ThemeFiles;
    QStringList ThemeFileNames;
    bool Loaded = false;
};

#endif // THEMESELECTWIDGET_H
