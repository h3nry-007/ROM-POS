# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1024, 600)
        Login.setStyleSheet(u"")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 50, 251, 81))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.horizontalLayoutWidget = QWidget(Login)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(289, 160, 441, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.usernameField = QLineEdit(self.horizontalLayoutWidget)
        self.usernameField.setObjectName(u"usernameField")
        self.usernameField.setEnabled(True)
        self.usernameField.setFont(font1)

        self.horizontalLayout.addWidget(self.usernameField)

        self.horizontalLayoutWidget_2 = QWidget(Login)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(289, 250, 441, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.passwordField = QLineEdit(self.horizontalLayoutWidget_2)
        self.passwordField.setObjectName(u"passwordField")
        self.passwordField.setFont(font1)

        self.horizontalLayout_2.addWidget(self.passwordField)

        self.signinBtn = QPushButton(Login)
        self.signinBtn.setObjectName(u"signinBtn")
        self.signinBtn.setGeometry(QRect(619, 340, 111, 41))
        self.signinBtn.setFont(font1)
        self.signinBtn.setStyleSheet(u"background-color:blue;\n"
"color:white;\n"
"border-radius: 10px")
        self.cancleBtn = QPushButton(Login)
        self.cancleBtn.setObjectName(u"cancleBtn")
        self.cancleBtn.setGeometry(QRect(490, 340, 111, 41))
        self.cancleBtn.setFont(font1)
        self.cancleBtn.setStyleSheet(u"background-color: \"transparent\";\n"
"color: white;\n"
"border : 1px solid white;\n"
"border-radius: 10px")
        self.label_4 = QLabel(Login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 424, 211, 20))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_4.setFont(font2)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login", u"Login ROM PoS", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Password ", None))
        self.signinBtn.setText(QCoreApplication.translate("Login", u"Sign in", None))
        self.cancleBtn.setText(QCoreApplication.translate("Login", u"Cancle", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"forget password?", None))
    # retranslateUi

