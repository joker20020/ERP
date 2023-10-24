# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddCharacter.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PlainTextEdit, PrimaryPushButton,
    SpinBox)

class Ui_AddCharacter(object):
    def setupUi(self, AddCharacter):
        if not AddCharacter.objectName():
            AddCharacter.setObjectName(u"AddCharacter")
        AddCharacter.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AddCharacter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.characterAuthorityL = BodyLabel(AddCharacter)
        self.characterAuthorityL.setObjectName(u"characterAuthorityL")

        self.gridLayout.addWidget(self.characterAuthorityL, 1, 0, 1, 1)

        self.characterName = LineEdit(AddCharacter)
        self.characterName.setObjectName(u"characterName")

        self.gridLayout.addWidget(self.characterName, 0, 1, 1, 1)

        self.characterDesL = BodyLabel(AddCharacter)
        self.characterDesL.setObjectName(u"characterDesL")

        self.gridLayout.addWidget(self.characterDesL, 2, 0, 1, 1)

        self.groupDes = PlainTextEdit(AddCharacter)
        self.groupDes.setObjectName(u"groupDes")

        self.gridLayout.addWidget(self.groupDes, 2, 1, 1, 1)

        self.characterNameL = BodyLabel(AddCharacter)
        self.characterNameL.setObjectName(u"characterNameL")

        self.gridLayout.addWidget(self.characterNameL, 0, 0, 1, 1)

        self.characterAuthority = SpinBox(AddCharacter)
        self.characterAuthority.setObjectName(u"characterAuthority")

        self.gridLayout.addWidget(self.characterAuthority, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.ok = PrimaryPushButton(AddCharacter)
        self.ok.setObjectName(u"ok")

        self.verticalLayout.addWidget(self.ok)


        self.retranslateUi(AddCharacter)

        QMetaObject.connectSlotsByName(AddCharacter)
    # setupUi

    def retranslateUi(self, AddCharacter):
        AddCharacter.setWindowTitle(QCoreApplication.translate("AddCharacter", u"Form", None))
        self.characterAuthorityL.setText(QCoreApplication.translate("AddCharacter", u"\u6743\u9650\u4ee3\u7801", None))
        self.characterDesL.setText(QCoreApplication.translate("AddCharacter", u"\u6743\u9650\u4ee3\u7801\u542b\u4e49", None))
        self.characterNameL.setText(QCoreApplication.translate("AddCharacter", u"\u89d2\u8272\u540d\u79f0", None))
        self.ok.setText(QCoreApplication.translate("AddCharacter", u"\u786e\u8ba4", None))
    # retranslateUi

