# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_taskMMXCms.ui'
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
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Delete_tsk(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(379, 425)
        Form.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        Form.setStyleSheet(u"background-color:rgb(183, 217, 156);\n"
"color: rgb(109, 29, 29);\n"
"border-color: 2px rgb(114, 165, 100);")
        self.dateEdit_del = QDateEdit(Form)
        self.dateEdit_del.setObjectName(u"dateEdit_del")
        self.dateEdit_del.setGeometry(QRect(20, 30, 331, 41))
        self.dateEdit_del.setStyleSheet(u"background-color: rgb(225, 255, 190);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(125, 7, 23);\n"
"\n"
"")
        self.joi_otdel_for_admin_del = QComboBox(Form)
        self.joi_otdel_for_admin_del.setObjectName(u"joi_otdel_for_admin_del")
        self.joi_otdel_for_admin_del.setGeometry(QRect(20, 80, 331, 31))
        self.joi_otdel_for_admin_del.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.exit_del = QPushButton(Form)
        self.exit_del.setObjectName(u"exit_del")
        self.exit_del.setGeometry(QRect(210, 370, 141, 41))
        self.exit_del.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"border-color: rgb(85, 85, 0);\n"
"color: rgb(111, 0, 0);")
        self.exit_del.setCheckable(False)
        self.exit_del.setAutoRepeat(False)
        self.save_delete = QPushButton(Form)
        self.save_delete.setObjectName(u"save_delete")
        self.save_delete.setGeometry(QRect(20, 370, 151, 41))
        self.save_delete.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.save_delete.setCheckable(False)
        self.save_delete.setAutoRepeat(False)
        self.listView_del = QListWidget(Form)
        self.listView_del.setObjectName(u"listView_del")
        self.listView_del.setGeometry(QRect(20, 160, 331, 191))
        self.listView_del.setStyleSheet(u"background-color: rgb(225, 255, 190);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(125, 7, 23);\n"
"\n"
"")
        self.listView_del.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.joi_sotr_for_admin_del = QComboBox(Form)
        self.joi_sotr_for_admin_del.setObjectName(u"joi_sotr_for_admin_del")
        self.joi_sotr_for_admin_del.setGeometry(QRect(20, 120, 331, 31))
        self.joi_sotr_for_admin_del.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0441\u0440\u043e\u043a\u0430", None))
        self.joi_otdel_for_admin_del.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0442\u0434\u0435\u043b...", None))
        self.exit_del.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.save_delete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.joi_sotr_for_admin_del.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430...", None))
    # retranslateUi

