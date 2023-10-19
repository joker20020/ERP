# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddWorker.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_AddWorker(object):
    def setupUi(self, AddWorker):
        if not AddWorker.objectName():
            AddWorker.setObjectName(u"AddWorker")
        AddWorker.resize(400, 260)
        self.horizontalLayout = QHBoxLayout(AddWorker)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.workerNameL = QLabel(AddWorker)
        self.workerNameL.setObjectName(u"workerNameL")
        font = QFont()
        font.setPointSize(10)
        self.workerNameL.setFont(font)
        self.workerNameL.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.workerNameL)

        self.workerName = QLineEdit(AddWorker)
        self.workerName.setObjectName(u"workerName")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.workerName)

        self.workerAgeL = QLabel(AddWorker)
        self.workerAgeL.setObjectName(u"workerAgeL")
        self.workerAgeL.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.workerAgeL)

        self.workerAge = QLineEdit(AddWorker)
        self.workerAge.setObjectName(u"workerAge")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.workerAge)

        self.workerGenderL = QLabel(AddWorker)
        self.workerGenderL.setObjectName(u"workerGenderL")
        self.workerGenderL.setFont(font)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.workerGenderL)

        self.workerGender = QLineEdit(AddWorker)
        self.workerGender.setObjectName(u"workerGender")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.workerGender)

        self.workerPlaceL = QLabel(AddWorker)
        self.workerPlaceL.setObjectName(u"workerPlaceL")
        self.workerPlaceL.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.workerPlaceL)

        self.workerPlace = QLineEdit(AddWorker)
        self.workerPlace.setObjectName(u"workerPlace")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.workerPlace)

        self.workerGroupL = QLabel(AddWorker)
        self.workerGroupL.setObjectName(u"workerGroupL")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.workerGroupL)

        self.workerGroup = QComboBox(AddWorker)
        self.workerGroup.setObjectName(u"workerGroup")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.workerGroup)

        self.workerUserNameL = QLabel(AddWorker)
        self.workerUserNameL.setObjectName(u"workerUserNameL")
        self.workerUserNameL.setFont(font)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.workerUserNameL)

        self.workerUserName = QLineEdit(AddWorker)
        self.workerUserName.setObjectName(u"workerUserName")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.workerUserName)

        self.workerPasswordL = QLabel(AddWorker)
        self.workerPasswordL.setObjectName(u"workerPasswordL")
        self.workerPasswordL.setFont(font)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.workerPasswordL)

        self.workerPassword = QLineEdit(AddWorker)
        self.workerPassword.setObjectName(u"workerPassword")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.workerPassword)

        self.workerCharacterL = QLabel(AddWorker)
        self.workerCharacterL.setObjectName(u"workerCharacterL")
        self.workerCharacterL.setFont(font)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.workerCharacterL)

        self.workerCharacter = QComboBox(AddWorker)
        self.workerCharacter.setObjectName(u"workerCharacter")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.workerCharacter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_2.setItem(8, QFormLayout.LabelRole, self.horizontalSpacer)

        self.ok = QPushButton(AddWorker)
        self.ok.setObjectName(u"ok")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.ok)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.retranslateUi(AddWorker)

        QMetaObject.connectSlotsByName(AddWorker)
    # setupUi

    def retranslateUi(self, AddWorker):
        AddWorker.setWindowTitle(QCoreApplication.translate("AddWorker", u"Form", None))
        self.workerNameL.setText(QCoreApplication.translate("AddWorker", u"\u59d3\u540d", None))
        self.workerAgeL.setText(QCoreApplication.translate("AddWorker", u"\u5e74\u9f84", None))
        self.workerGenderL.setText(QCoreApplication.translate("AddWorker", u"\u6027\u522b", None))
        self.workerPlaceL.setText(QCoreApplication.translate("AddWorker", u"\u5de5\u4f5c\u5730\u70b9", None))
        self.workerGroupL.setText(QCoreApplication.translate("AddWorker", u"\u6240\u5c5e\u7ec4\u7ec7", None))
        self.workerUserNameL.setText(QCoreApplication.translate("AddWorker", u"\u7528\u6237\u540d", None))
        self.workerPasswordL.setText(QCoreApplication.translate("AddWorker", u"\u5bc6\u7801", None))
        self.workerCharacterL.setText(QCoreApplication.translate("AddWorker", u"\u89d2\u8272", None))
        self.ok.setText(QCoreApplication.translate("AddWorker", u"\u786e\u8ba4", None))
    # retranslateUi

