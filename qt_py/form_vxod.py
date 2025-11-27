# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_vxodpEkiYT.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Form_vxod(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 547)
        MainWindow.setStyleSheet(u"background-color:rgb(183, 217, 156);\n"
"color: rgb(109, 29, 29);\n"
"border-color: 2px rgb(114, 165, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vxod_butt = QPushButton(self.centralwidget)
        self.vxod_butt.setObjectName(u"vxod_butt")
        self.vxod_butt.setGeometry(QRect(60, 310, 281, 31))
        self.vxod_butt.setStyleSheet(u"background-color:rgb(212, 255, 193);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 170, 191, 20))
        self.label_2.setStyleSheet(u"\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.textEdit_login = QTextEdit(self.centralwidget)
        self.textEdit_login.setObjectName(u"textEdit_login")
        self.textEdit_login.setGeometry(QRect(60, 200, 281, 31))
        self.textEdit_login.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 20, 321, 20))
        self.label.setStyleSheet(u"\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.textEdit_pasword = QTextEdit(self.centralwidget)
        self.textEdit_pasword.setObjectName(u"textEdit_pasword")
        self.textEdit_pasword.setGeometry(QRect(60, 250, 281, 31))
        font = QFont()
        font.setFamilies([u"Small Fonts"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.textEdit_pasword.setFont(font)
        self.textEdit_pasword.setStyleSheet(u"background-color: rgb(209, 248, 178);\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 60, 331, 421))
        self.label_3.setStyleSheet(u"\n"
"font: 700 10pt \"Small Fonts\";\n"
"color: rgb(111, 0, 0);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c - \u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u0441\u0440\u043e\u043a\u043e\u0432", None))
        self.vxod_butt.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d \u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.textEdit_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u0434\u0435\u0434\u043b\u0430\u0439\u043d\u043e\u0432!", None))
        self.textEdit_pasword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u0441\u0440\u043e\u043a\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \n"
"\n"
"\n"
"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0434\u043b\u044f \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447\u0430\u043c\u0438 \u0438 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044f \u0434\u0435\u0434\u043b\u0430\u0439\u043d\u043e\u0432 \u0432 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438, \u0441 \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435\u043c \u043f\u0440\u0430\u0432 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043c\u0435\u0436\u0434\u0443 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430\u043c\u0438 \u0438 \u043e\u0431\u044b\u0447\u043d\u044b\u043c\u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430\u043c\u0438.\n"
"\n"
"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\n"
"\n"
"\u041f"
                        "\u043e\u043b\u043d\u044b\u0439 \u0434\u043e\u0441\u0442\u0443\u043f \u043a\u043e \u0432\u0441\u0435\u043c \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c\n"
"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435/\u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435/\u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\n"
"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0432\u0441\u0435\u0445 \u043e\u0442\u0434\u0435\u043b\u043e\u0432 \u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432\n"
"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0440\u043e\u043a\u0430\u043c\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f\n"
"\n"
"\n"
"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\n"
"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447\n"
"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f \u043f\u043e \u043e\u0442\u0434"
                        "\u0435\u043b\u0430\u043c \u0438 \u0434\u0430\u0442\u0430\u043c", None))
    # retranslateUi

