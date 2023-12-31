# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLayout, QListWidgetItem, QSizePolicy,
    QSpacerItem, QTreeWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, ComboBox, LineEdit, ListWidget,
    PasswordLineEdit, PrimaryPushButton, PushButton, StrongBodyLabel,
    TitleLabel, ToolButton, TreeWidget, VerticalSeparator)

class Ui_Admin(object):
    def setupUi(self, Admin):
        if not Admin.objectName():
            Admin.setObjectName(u"Admin")
        Admin.resize(812, 637)
        self.horizontalLayout = QHBoxLayout(Admin)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.workerIDL = BodyLabel(Admin)
        self.workerIDL.setObjectName(u"workerIDL")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.workerIDL)

        self.workerID = LineEdit(Admin)
        self.workerID.setObjectName(u"workerID")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.workerID)

        self.workerNameL = BodyLabel(Admin)
        self.workerNameL.setObjectName(u"workerNameL")
        font = QFont()
        font.setPointSize(10)
        self.workerNameL.setFont(font)
        self.workerNameL.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.workerNameL)

        self.workerName = LineEdit(Admin)
        self.workerName.setObjectName(u"workerName")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.workerName)

        self.workerAgeL = BodyLabel(Admin)
        self.workerAgeL.setObjectName(u"workerAgeL")
        self.workerAgeL.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.workerAgeL)

        self.workerAge = LineEdit(Admin)
        self.workerAge.setObjectName(u"workerAge")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.workerAge)

        self.workerGenderL = BodyLabel(Admin)
        self.workerGenderL.setObjectName(u"workerGenderL")
        self.workerGenderL.setFont(font)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.workerGenderL)

        self.workerGender = LineEdit(Admin)
        self.workerGender.setObjectName(u"workerGender")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.workerGender)

        self.workerPlaceL = BodyLabel(Admin)
        self.workerPlaceL.setObjectName(u"workerPlaceL")
        self.workerPlaceL.setFont(font)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.workerPlaceL)

        self.workerPlace = LineEdit(Admin)
        self.workerPlace.setObjectName(u"workerPlace")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.workerPlace)

        self.workerGroupL = BodyLabel(Admin)
        self.workerGroupL.setObjectName(u"workerGroupL")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.workerGroupL)

        self.workerGroup = ComboBox(Admin)
        self.workerGroup.setObjectName(u"workerGroup")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.workerGroup)

        self.workerUserNameL = BodyLabel(Admin)
        self.workerUserNameL.setObjectName(u"workerUserNameL")
        self.workerUserNameL.setFont(font)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.workerUserNameL)

        self.workerUserName = LineEdit(Admin)
        self.workerUserName.setObjectName(u"workerUserName")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.workerUserName)

        self.workerPasswordL = BodyLabel(Admin)
        self.workerPasswordL.setObjectName(u"workerPasswordL")
        self.workerPasswordL.setFont(font)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.workerPasswordL)

        self.workerPassword = PasswordLineEdit(Admin)
        self.workerPassword.setObjectName(u"workerPassword")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.workerPassword)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.line_3 = QFrame(Admin)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.workerCharacterL = StrongBodyLabel(Admin)
        self.workerCharacterL.setObjectName(u"workerCharacterL")
        self.workerCharacterL.setFont(font)
        self.workerCharacterL.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.workerCharacterL)

        self.workerCharacter = ComboBox(Admin)
        self.workerCharacter.setObjectName(u"workerCharacter")

        self.horizontalLayout_6.addWidget(self.workerCharacter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.characterNew = PushButton(Admin)
        self.characterNew.setObjectName(u"characterNew")

        self.horizontalLayout_4.addWidget(self.characterNew)

        self.characterRemove = PrimaryPushButton(Admin)
        self.characterRemove.setObjectName(u"characterRemove")

        self.horizontalLayout_4.addWidget(self.characterRemove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.line = QFrame(Admin)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = TitleLabel(Admin)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.characterAdd = PushButton(Admin)
        self.characterAdd.setObjectName(u"characterAdd")

        self.horizontalLayout_5.addWidget(self.characterAdd)

        self.characterDelete = PrimaryPushButton(Admin)
        self.characterDelete.setObjectName(u"characterDelete")

        self.horizontalLayout_5.addWidget(self.characterDelete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.characterList = ListWidget(Admin)
        self.characterList.setObjectName(u"characterList")

        self.verticalLayout_2.addWidget(self.characterList)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.workerNew = PushButton(Admin)
        self.workerNew.setObjectName(u"workerNew")

        self.horizontalLayout_3.addWidget(self.workerNew)

        self.workerUpdate = PushButton(Admin)
        self.workerUpdate.setObjectName(u"workerUpdate")

        self.horizontalLayout_3.addWidget(self.workerUpdate)

        self.workerRemove = PrimaryPushButton(Admin)
        self.workerRemove.setObjectName(u"workerRemove")

        self.horizontalLayout_3.addWidget(self.workerRemove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(Admin)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.refresh = ToolButton(Admin)
        self.refresh.setObjectName(u"refresh")

        self.horizontalLayout_2.addWidget(self.refresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupNew = PushButton(Admin)
        self.groupNew.setObjectName(u"groupNew")

        self.horizontalLayout_2.addWidget(self.groupNew)

        self.groupRemove = PrimaryPushButton(Admin)
        self.groupRemove.setObjectName(u"groupRemove")

        self.horizontalLayout_2.addWidget(self.groupRemove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(9, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.VerticalSeparator = VerticalSeparator(Admin)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout.addWidget(self.VerticalSeparator)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupTree = TreeWidget(Admin)
        self.groupTree.setObjectName(u"groupTree")
        self.groupTree.header().setVisible(True)

        self.verticalLayout.addWidget(self.groupTree)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(2, 4)

        self.retranslateUi(Admin)

        QMetaObject.connectSlotsByName(Admin)
    # setupUi

    def retranslateUi(self, Admin):
        Admin.setWindowTitle(QCoreApplication.translate("Admin", u"Form", None))
        self.workerIDL.setText(QCoreApplication.translate("Admin", u"\u5458\u5de5\u7f16\u53f7", None))
        self.workerNameL.setText(QCoreApplication.translate("Admin", u"\u59d3\u540d", None))
        self.workerAgeL.setText(QCoreApplication.translate("Admin", u"\u5e74\u9f84", None))
        self.workerGenderL.setText(QCoreApplication.translate("Admin", u"\u6027\u522b", None))
        self.workerPlaceL.setText(QCoreApplication.translate("Admin", u"\u5de5\u4f5c\u5730\u70b9", None))
        self.workerGroupL.setText(QCoreApplication.translate("Admin", u"\u6240\u5c5e\u7ec4\u7ec7", None))
        self.workerUserNameL.setText(QCoreApplication.translate("Admin", u"\u7528\u6237\u540d", None))
        self.workerPasswordL.setText(QCoreApplication.translate("Admin", u"\u5bc6\u7801", None))
        self.workerCharacterL.setText(QCoreApplication.translate("Admin", u"\u89d2\u8272\u64cd\u4f5c\u6846", None))
        self.characterNew.setText(QCoreApplication.translate("Admin", u"\u65b0\u5efa\u89d2\u8272", None))
        self.characterRemove.setText(QCoreApplication.translate("Admin", u"\u5220\u9664\u89d2\u8272", None))
        self.label.setText(QCoreApplication.translate("Admin", u"\u5458\u5de5\u89d2\u8272", None))
        self.characterAdd.setText(QCoreApplication.translate("Admin", u"\u4e3a\u5458\u5de5\u6dfb\u52a0\u89d2\u8272", None))
        self.characterDelete.setText(QCoreApplication.translate("Admin", u"\u4e3a\u5458\u5de5\u5220\u9664\u89d2\u8272", None))
        self.workerNew.setText(QCoreApplication.translate("Admin", u"\u65b0\u5efa\u5458\u5de5", None))
        self.workerUpdate.setText(QCoreApplication.translate("Admin", u"\u4fee\u6539\u5458\u5de5\u4fe1\u606f", None))
        self.workerRemove.setText(QCoreApplication.translate("Admin", u"\u5220\u9664\u5458\u5de5", None))
        self.refresh.setText("")
        self.groupNew.setText(QCoreApplication.translate("Admin", u"\u65b0\u5efa\u7ec4\u7ec7", None))
        self.groupRemove.setText(QCoreApplication.translate("Admin", u"\u5220\u9664\u7ec4\u7ec7", None))
        ___qtreewidgetitem = self.groupTree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Admin", u"ID", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Admin", u"\u7c7b\u578b", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Admin", u"\u540d\u79f0", None));
    # retranslateUi

