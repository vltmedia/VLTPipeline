QT       += core gui network
QT += sql


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
    models/userslist.cpp \
    models/vltdatabasemanager.cpp \
    postwizardwindow.cpp \
    server/tcprestresponse.cpp \
    server/tcproutes.cpp \
    server/tcpserver.cpp \
    ui/dialogs/usersdialog.cpp

HEADERS += \
    dbmanager.h \
    mainwindow.h \
    models/clientclass.h \
    models/groupsclass.h \
    models/projectsclass.h \
    models/usersclass.h \
    models/userslist.h \
    models/vltdatabasemanager.h \
    postwizardwindow.h \
    server/tcprestresponse.h \
    server/tcproutes.h \
    server/tcpserver.h \
    ui/dialogs/usersdialog.h

FORMS += \
    mainwindow.ui \
    postwizardwindow.ui \
    ui/dialogs/usersdialog.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    models/db/sql/InitializeTables.sql \
    py/apps/blender/blendertcpclient.py
