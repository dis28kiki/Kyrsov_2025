# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_taskcjyKmh.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Add_task(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(369, 427)
        Form.setStyleSheet(u"background-color:rgb(183, 217, 156);\n"
"color: rgb(109, 29, 29);\n"
"border-color: 2px rgb(114, 165, 100);")
        self.dateEdit_add = QDateEdit(Form)
        self.dateEdit_add.setObjectName(u"dateEdit_add")
        self.dateEdit_add.setGeometry(QRect(20, 20, 331, 41))
        self.dateEdit_add.setStyleSheet(u"background-color: rgb(225, 255, 190);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(125, 7, 23);\n"
"\n"
"")
        self.add_task_descrip = QTextEdit(Form)
        self.add_task_descrip.setObjectName(u"add_task_descrip")
        self.add_task_descrip.setGeometry(QRect(20, 190, 331, 161))
        self.add_task_descrip.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.add_task_descrip.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.joi_otdel_for_admin_add = QComboBox(Form)
        self.joi_otdel_for_admin_add.setObjectName(u"joi_otdel_for_admin_add")
        self.joi_otdel_for_admin_add.setGeometry(QRect(20, 70, 331, 31))
        self.joi_otdel_for_admin_add.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.exit_save = QPushButton(Form)
        self.exit_save.setObjectName(u"exit_save")
        self.exit_save.setGeometry(QRect(200, 370, 141, 41))
        self.exit_save.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.exit_save.setCheckable(False)
        self.exit_save.setAutoRepeat(False)
        self.save_add = QPushButton(Form)
        self.save_add.setObjectName(u"save_add")
        self.save_add.setGeometry(QRect(30, 370, 141, 41))
        self.save_add.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.save_add.setCheckable(False)
        self.save_add.setAutoRepeat(False)
        self.add_task_title = QTextEdit(Form)
        self.add_task_title.setObjectName(u"add_task_title")
        self.add_task_title.setGeometry(QRect(20, 150, 331, 31))
        self.add_task_title.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.add_task_title.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.joi_sotrud_for_admin_add = QComboBox(Form)
        self.joi_sotrud_for_admin_add.setObjectName(u"joi_sotrud_for_admin_add")
        self.joi_sotrud_for_admin_add.setGeometry(QRect(20, 110, 331, 31))
        self.joi_sotrud_for_admin_add.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.add_task_descrip.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u0438 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f...", None))
        self.joi_otdel_for_admin_add.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0442\u0434\u0435\u043b...", None))
        self.exit_save.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.save_add.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.add_task_title.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f...", None))
        self.joi_sotrud_for_admin_add.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430...", None))
    # retranslateUi

