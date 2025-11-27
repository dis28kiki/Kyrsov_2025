# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_admjpGzpc.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Wi_adm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 577)
        Form.setStyleSheet(u"background-color:rgb(183, 217, 156);\n"
"color: rgb(109, 29, 29);\n"
"border-color: 2px rgb(114, 165, 100);")
        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 30, 411, 351))
        self.calendarWidget.setStyleSheet(u"background-color: rgb(225, 255, 190);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(125, 7, 23);\n"
"\n"
"")
        self.text_vv = QListWidget(Form)
        self.text_vv.setObjectName(u"text_vv")
        self.text_vv.setGeometry(QRect(450, 30, 321, 451))
        font = QFont()
        font.setFamilies([u"Small Fonts"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.text_vv.setFont(font)
        self.text_vv.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.text_vv.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.text_vv.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.text_vv.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_vv.setWordWrap(True)
        self.joi_otdel_for_admin = QComboBox(Form)
        self.joi_otdel_for_admin.setObjectName(u"joi_otdel_for_admin")
        self.joi_otdel_for_admin.setGeometry(QRect(20, 390, 411, 41))
        self.joi_otdel_for_admin.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.avatar = QLabel(Form)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setGeometry(QRect(20, 500, 51, 51))
        self.avatar.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.doljnost = QLabel(Form)
        self.doljnost.setObjectName(u"doljnost")
        self.doljnost.setGeometry(QRect(80, 500, 261, 21))
        self.doljnost.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(80, 530, 261, 21))
        self.name.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.exit_avtoriz = QPushButton(Form)
        self.exit_avtoriz.setObjectName(u"exit_avtoriz")
        self.exit_avtoriz.setGeometry(QRect(350, 510, 81, 31))
        self.exit_avtoriz.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.add_deadlines = QPushButton(Form)
        self.add_deadlines.setObjectName(u"add_deadlines")
        self.add_deadlines.setGeometry(QRect(450, 510, 101, 41))
        self.add_deadlines.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.add_deadlines.setCheckable(False)
        self.add_deadlines.setAutoRepeat(False)
        self.delete_deadlines = QPushButton(Form)
        self.delete_deadlines.setObjectName(u"delete_deadlines")
        self.delete_deadlines.setGeometry(QRect(670, 510, 101, 41))
        self.delete_deadlines.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.btm_izmen_dead = QPushButton(Form)
        self.btm_izmen_dead.setObjectName(u"btm_izmen_dead")
        self.btm_izmen_dead.setGeometry(QRect(560, 510, 101, 41))
        self.btm_izmen_dead.setStyleSheet(u"background-color: rgb(206, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.btm_izmen_dead.setCheckable(False)
        self.btm_izmen_dead.setAutoRepeat(False)
        self.joi_sotr_for_admin = QComboBox(Form)
        self.joi_sotr_for_admin.setObjectName(u"joi_sotr_for_admin")
        self.joi_sotr_for_admin.setGeometry(QRect(20, 440, 411, 41))
        self.joi_sotr_for_admin.setStyleSheet(u"background-color: rgb(234, 245, 211);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u0441\u0440\u043e\u043a\u043e\u0432 - \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430\u043c\u0438", None))
        self.joi_otdel_for_admin.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0442\u0434\u0435\u043b...", None))
        self.avatar.setText(QCoreApplication.translate("Form", u"\u0410\u0412\u0410", None))
        self.doljnost.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.name.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.exit_avtoriz.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.add_deadlines.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.delete_deadlines.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_izmen_dead.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.joi_sotr_for_admin.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430...", None))
    # retranslateUi

