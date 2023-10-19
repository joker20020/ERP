# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin.ui'
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
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Admin(object):
    def setupUi(self, Admin):
        if not Admin.objectName():
            Admin.setObjectName(u"Admin")
        Admin.resize(812, 637)
        self.horizontalLayout = QHBoxLayout(Admin)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupTree = QTreeWidget(Admin)
        self.groupTree.setObjectName(u"groupTree")
        self.groupTree.header().setVisible(True)

        self.verticalLayout.addWidget(self.groupTree)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.workerNameL = QLabel(Admin)
        self.workerNameL.setObjectName(u"workerNameL")
        font = QFont()
        font.setPointSize(10)
        self.workerNameL.setFont(font)
        self.workerNameL.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.workerNameL)

        self.wokerName = QLineEdit(Admin)
        self.wokerName.setObjectName(u"wokerName")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.wokerName)

        self.workerAgeL = QLabel(Admin)
        self.workerAgeL.setObjectName(u"workerAgeL")
        self.workerAgeL.setFont(font)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.workerAgeL)

        self.workerAge_2 = QLineEdit(Admin)
        self.workerAge_2.setObjectName(u"workerAge_2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.workerAge_2)

        self.workerGenderL = QLabel(Admin)
        self.workerGenderL.setObjectName(u"workerGenderL")
        self.workerGenderL.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.workerGenderL)

        self.workerGender = QLineEdit(Admin)
        self.workerGender.setObjectName(u"workerGender")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.workerGender)

        self.workerPlaceL = QLabel(Admin)
        self.workerPlaceL.setObjectName(u"workerPlaceL")
        self.workerPlaceL.setFont(font)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.workerPlaceL)

        self.workerPlace = QLineEdit(Admin)
        self.workerPlace.setObjectName(u"workerPlace")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.workerPlace)

        self.workerUserNameL = QLabel(Admin)
        self.workerUserNameL.setObjectName(u"workerUserNameL")
        self.workerUserNameL.setFont(font)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.workerUserNameL)

        self.workerUserName = QLineEdit(Admin)
        self.workerUserName.setObjectName(u"workerUserName")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.workerUserName)

        self.workerPasswordL = QLabel(Admin)
        self.workerPasswordL.setObjectName(u"workerPasswordL")
        self.workerPasswordL.setFont(font)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.workerPasswordL)

        self.workerPassword = QLineEdit(Admin)
        self.workerPassword.setObjectName(u"workerPassword")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.workerPassword)

        self.workerCharacterL = QLabel(Admin)
        self.workerCharacterL.setObjectName(u"workerCharacterL")
        self.workerCharacterL.setFont(font)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.workerCharacterL)

        self.workerCharacter = QComboBox(Admin)
        self.workerCharacter.setObjectName(u"workerCharacter")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.workerCharacter)

        self.workerGroupL = QLabel(Admin)
        self.workerGroupL.setObjectName(u"workerGroupL")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.workerGroupL)

        self.workerGroup = QComboBox(Admin)
        self.workerGroup.setObjectName(u"workerGroup")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.workerGroup)

        self.workerIDL = QLabel(Admin)
        self.workerIDL.setObjectName(u"workerIDL")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.workerIDL)

        self.workerID = QLineEdit(Admin)
        self.workerID.setObjectName(u"workerID")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.workerID)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.characterNew = QPushButton(Admin)
        self.characterNew.setObjectName(u"characterNew")

        self.horizontalLayout_4.addWidget(self.characterNew)

        self.characteradd = QPushButton(Admin)
        self.characteradd.setObjectName(u"characteradd")

        self.horizontalLayout_4.addWidget(self.characteradd)

        self.characterRemove = QPushButton(Admin)
        self.characterRemove.setObjectName(u"characterRemove")

        self.horizontalLayout_4.addWidget(self.characterRemove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label = QLabel(Admin)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.characterList = QListWidget(Admin)
        self.characterList.setObjectName(u"characterList")

        self.verticalLayout_2.addWidget(self.characterList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupNew = QPushButton(Admin)
        self.groupNew.setObjectName(u"groupNew")

        self.horizontalLayout_2.addWidget(self.groupNew)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupRemove = QPushButton(Admin)
        self.groupRemove.setObjectName(u"groupRemove")

        self.horizontalLayout_2.addWidget(self.groupRemove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.workerNew = QPushButton(Admin)
        self.workerNew.setObjectName(u"workerNew")

        self.horizontalLayout_3.addWidget(self.workerNew)

        self.workerUpdate = QPushButton(Admin)
        self.workerUpdate.setObjectName(u"workerUpdate")

        self.horizontalLayout_3.addWidget(self.workerUpdate)

        self.workerRemove = QPushButton(Admin)
        self.workerRemove.setObjectName(u"workerRemove")

        self.horizontalLayout_3.addWidget(self.workerRemove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Admin)

        QMetaObject.connectSlotsByName(Admin)
    # setupUi

    def retranslateUi(self, Admin):
        Admin.setWindowTitle(QCoreApplication.translate("Admin", u"Form", None))
        ___qtreewidgetitem = self.groupTree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Admin", u"ID", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Admin", u"\u7c7b\u578b", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Admin", u"\u540d\u79f0", None));
        self.workerNameL.setText(QCoreApplication.translate("Admin", u"\u59d3\u540d", None))
        self.workerAgeL.setText(QCoreApplication.translate("Admin", u"\u5e74\u9f84", None))
        self.workerGenderL.setText(QCoreApplication.translate("Admin", u"\u6027\u522b", None))
        self.workerPlaceL.setText(QCoreApplication.translate("Admin", u"\u5de5\u4f5c\u5730\u70b9", None))
        self.workerUserNameL.setText(QCoreApplication.translate("Admin", u"\u7528\u6237\u540d", None))
        self.workerPasswordL.setText(QCoreApplication.translate("Admin", u"\u5bc6\u7801", None))
        self.workerCharacterL.setText(QCoreApplication.translate("Admin", u"\u89d2\u8272", None))
        self.workerGroupL.setText(QCoreApplication.translate("Admin", u"\u6240\u5c5e\u7ec4\u7ec7", None))
        self.workerIDL.setText(QCoreApplication.translate("Admin", u"\u5458\u5de5\u7f16\u53f7", None))
        self.characterNew.setText(QCoreApplication.translate("Admin", u"\u65b0\u5efa\u89d2\u8272", None))
        self.characteradd.setText(QCoreApplication.translate("Admin", u"\u4e3a\u5458\u5de5\u6dfb\u52a0\u89d2\u8272", None))
        self.characterRemove.setText(QCoreApplication.translate("Admin", u"\u5220\u9664\u89d2\u8272", None))
        self.label.setText(QCoreApplication.translate("Admin", u"\u5458\u5de5\u89d2\u8272", None))
        self.groupNew.setText(QCoreApplication.translate("Admin", u"\u65b0\u5efa\u7ec4\u7ec7", None))
        self.groupRemove.setText(QCoreApplication.translate("Admin", u"\u5220\u9664\u7ec4\u7ec7", None))
        self.workerNew.setText(QCoreApplication.translate("Admin", u"\u65b0\u5efa\u5458\u5de5", None))
        self.workerUpdate.setText(QCoreApplication.translate("Admin", u"\u4fee\u6539\u5458\u5de5\u4fe1\u606f", None))
        self.workerRemove.setText(QCoreApplication.translate("Admin", u"\u5220\u9664\u5458\u5de5", None))
    # retranslateUi

