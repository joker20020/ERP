# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddGroup.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, ComboBox, LineEdit, PlainTextEdit)

class Ui_AddGroup(object):
    def setupUi(self, AddGroup):
        if not AddGroup.objectName():
            AddGroup.setObjectName(u"AddGroup")
        AddGroup.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AddGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupFather = ComboBox(AddGroup)
        self.groupFather.setObjectName(u"groupFather")

        self.gridLayout.addWidget(self.groupFather, 1, 1, 1, 1)

        self.groupNameL = BodyLabel(AddGroup)
        self.groupNameL.setObjectName(u"groupNameL")

        self.gridLayout.addWidget(self.groupNameL, 0, 0, 1, 1)

        self.groupFatherL = BodyLabel(AddGroup)
        self.groupFatherL.setObjectName(u"groupFatherL")

        self.gridLayout.addWidget(self.groupFatherL, 1, 0, 1, 1)

        self.groupName = LineEdit(AddGroup)
        self.groupName.setObjectName(u"groupName")

        self.gridLayout.addWidget(self.groupName, 0, 1, 1, 1)

        self.groupDesL = BodyLabel(AddGroup)
        self.groupDesL.setObjectName(u"groupDesL")

        self.gridLayout.addWidget(self.groupDesL, 2, 0, 1, 1)

        self.groupDes = PlainTextEdit(AddGroup)
        self.groupDes.setObjectName(u"groupDes")

        self.gridLayout.addWidget(self.groupDes, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.ok = QPushButton(AddGroup)
        self.ok.setObjectName(u"ok")

        self.verticalLayout.addWidget(self.ok)


        self.retranslateUi(AddGroup)

        QMetaObject.connectSlotsByName(AddGroup)
    # setupUi

    def retranslateUi(self, AddGroup):
        AddGroup.setWindowTitle(QCoreApplication.translate("AddGroup", u"Form", None))
        self.groupNameL.setText(QCoreApplication.translate("AddGroup", u"\u7ec4\u7ec7\u540d\u79f0", None))
        self.groupFatherL.setText(QCoreApplication.translate("AddGroup", u"\u7236\u7ec4\u7ec7", None))
        self.groupDesL.setText(QCoreApplication.translate("AddGroup", u"\u63cf\u8ff0", None))
        self.ok.setText(QCoreApplication.translate("AddGroup", u"\u786e\u8ba4", None))
    # retranslateUi

