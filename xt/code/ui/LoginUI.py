# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PasswordLineEdit, PrimaryPushButton)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(710, 596)
        Login.setMinimumSize(QSize(700, 500))
        self.horizontalLayout = QHBoxLayout(Login)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLabel = QLabel(Login)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.imageLabel)

        self.verticalWidget = QWidget(Login)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(360, 0))
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.logo = QLabel(self.verticalWidget)
        self.logo.setObjectName(u"logo")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.logo)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.userNameL = BodyLabel(self.verticalWidget)
        self.userNameL.setObjectName(u"userNameL")
        self.userNameL.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.userNameL)

        self.userName = LineEdit(self.verticalWidget)
        self.userName.setObjectName(u"userName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.userName)

        self.password = PasswordLineEdit(self.verticalWidget)
        self.password.setObjectName(u"password")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password)

        self.passwordL = BodyLabel(self.verticalWidget)
        self.passwordL.setObjectName(u"passwordL")
        self.passwordL.setScaledContents(False)
        self.passwordL.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.passwordL)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.login = PrimaryPushButton(self.verticalWidget)
        self.login.setObjectName(u"login")

        self.verticalLayout.addWidget(self.login)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.verticalWidget)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.imageLabel.setText("")
        self.logo.setText("")
        self.userNameL.setText(QCoreApplication.translate("Login", u"\u7528\u6237\u540d", None))
        self.passwordL.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801", None))
        self.login.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
    # retranslateUi

