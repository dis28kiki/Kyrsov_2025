# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'izmen_taskWMKFYn.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_izmen(object):
    def setupUi(self, izmen):
        if not izmen.objectName():
            izmen.setObjectName(u"izmen")
        izmen.resize(366, 427)
        izmen.setStyleSheet(u"background-color:rgb(183, 217, 156);\n"
"color: rgb(109, 29, 29);\n"
"border-color: 2px rgb(114, 165, 100);")
        self.dateEdit_izm = QDateEdit(izmen)
        self.dateEdit_izm.setObjectName(u"dateEdit_izm")
        self.dateEdit_izm.setGeometry(QRect(20, 20, 331, 41))
        self.dateEdit_izm.setStyleSheet(u"background-color: rgb(225, 255, 190);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(125, 7, 23);\n"
"\n"
"")
        self.joi_otdel_for_admin_izm = QComboBox(izmen)
        self.joi_otdel_for_admin_izm.setObjectName(u"joi_otdel_for_admin_izm")
        self.joi_otdel_for_admin_izm.setGeometry(QRect(20, 70, 331, 31))
        self.joi_otdel_for_admin_izm.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.exit_izmm = QPushButton(izmen)
        self.exit_izmm.setObjectName(u"exit_izmm")
        self.exit_izmm.setGeometry(QRect(200, 370, 141, 41))
        self.exit_izmm.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.exit_izmm.setCheckable(False)
        self.exit_izmm.setAutoRepeat(False)
        self.save_izm = QPushButton(izmen)
        self.save_izm.setObjectName(u"save_izm")
        self.save_izm.setGeometry(QRect(30, 370, 141, 41))
        self.save_izm.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.save_izm.setCheckable(False)
        self.save_izm.setAutoRepeat(False)
        self.izm_task = QListWidget(izmen)
        self.izm_task.setObjectName(u"izm_task")
        self.izm_task.setGeometry(QRect(20, 150, 331, 61))
        self.izm_task.setStyleSheet(u"background-color: rgb(225, 255, 190);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(125, 7, 23);\n"
"\n"
"")
        self.izm_task.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.joi_sotr_for_admin_izm = QComboBox(izmen)
        self.joi_sotr_for_admin_izm.setObjectName(u"joi_sotr_for_admin_izm")
        self.joi_sotr_for_admin_izm.setGeometry(QRect(20, 110, 331, 31))
        self.joi_sotr_for_admin_izm.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.izm_task_descrip = QTextEdit(izmen)
        self.izm_task_descrip.setObjectName(u"izm_task_descrip")
        self.izm_task_descrip.setGeometry(QRect(20, 220, 331, 131))
        self.izm_task_descrip.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.izm_task_descrip.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.retranslateUi(izmen)

        QMetaObject.connectSlotsByName(izmen)
    # setupUi

    def retranslateUi(self, izmen):
        izmen.setWindowTitle(QCoreApplication.translate("izmen", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None))
        self.joi_otdel_for_admin_izm.setPlaceholderText(QCoreApplication.translate("izmen", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0442\u0434\u0435\u043b...", None))
        self.exit_izmm.setText(QCoreApplication.translate("izmen", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.save_izm.setText(QCoreApplication.translate("izmen", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.joi_sotr_for_admin_izm.setPlaceholderText(QCoreApplication.translate("izmen", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430...", None))
        self.izm_task_descrip.setPlaceholderText(QCoreApplication.translate("izmen", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u0438 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f...", None))
    # retranslateUi

