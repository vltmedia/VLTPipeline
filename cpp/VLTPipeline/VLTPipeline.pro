QT       += core gui network

QT += sql

# Copies the given files to the destination directory
defineTest(copyToDestdir) {

    message($$1/*)
    message($$OUT_PWD/debug/$$1)
    COPIES += styles_files
    styles_files.files = $$files($$1/*)
    styles_files.path =  $$OUT_PWD/debug/$$1


}
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    dbmanager.cpp \
    main.cpp \
    mainwindow.cpp \
    models/clientclass.cpp \
    models/groupsclass.cpp \
    models/projectsclass.cpp \
    models/usersclass.cpp \
    models/usersettingsclass.cpp \
    models/userslist.cpp \
    models/vltdatabasemanager.cpp \
    postwizardwindow.cpp \
    server/tcprestresponse.cpp \
    server/tcproutes.cpp \
    server/tcpserver.cpp \
    ui/dialogs/selectthemewidget.cpp \
    ui/dialogs/themeselectwidget.cpp \
    ui/dialogs/userpreferencesdialog.cpp \
    ui/dialogs/usersdialog.cpp

HEADERS += \
    dbmanager.h \
    mainwindow.h \
    models/clientclass.h \
    models/groupsclass.h \
    models/projectsclass.h \
    models/usersclass.h \
    models/usersettingsclass.h \
    models/userslist.h \
    models/vltdatabasemanager.h \
    postwizardwindow.h \
    server/tcprestresponse.h \
    server/tcproutes.h \
    server/tcpserver.h \
    ui/dialogs/selectthemewidget.h \
    ui/dialogs/themeselectwidget.h \
    ui/dialogs/userpreferencesdialog.h \
    ui/dialogs/usersdialog.h

FORMS += \
    mainwindow.ui \
    postwizardwindow.ui \
    ui/dialogs/selectthemewidget.ui \
    ui/dialogs/themeselectwidget.ui \
    ui/dialogs/userpreferencesdialog.ui \
    ui/dialogs/usersdialog.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    models/db/sql/InitializeTables.sql \
    py/apps/blender/blendertcpclient.py \
    styles/MaterialBlue.qss

#copyToDestdir(styles)

# //////////////////////////////////////////////////////////////////////

# Copy Extra Files to the Directory this way
COPIES += styles_files
styles_files.files = $$files(styles/*)
styles_files.path =  $$OUT_PWD/debug/styles
COPIES += styles_files_Release
styles_files_Release.files = $$files(styles/*)
styles_files_Release.path =  $$OUT_PWD/release/styles

# //////////////////////////////////////////////////////////////////////



# //////////////////////////////////////////////////////////////////////

# Copy Extra Files to the Directory this way
COPIES += blenderpy_files
blenderpy_files.files = $$files(py/apps/blender/*)
blenderpy_files.path =  $$OUT_PWD/debug/py/apps/blender
# Copy Extra Files to the Directory this way
COPIES += blenderpy_files_Release
blenderpy_files_Release.files = $$files(py/apps/blender/*)
blenderpy_files_Release.path =  $$OUT_PWD/release/py/apps/blender

# //////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////

# Copy Extra Files to the Directory this way
COPIES += models_files
models_files.files = $$files(models/db/sql/*)
models_files.path =  $$OUT_PWD/debug/models/db/sql/
COPIES += models_files_Release
models_files_Release.files = $$files(models/db/sql/*)
models_files_Release.path =  $$OUT_PWD/release/models/db/sql/

# //////////////////////////////////////////////////////////////////////





