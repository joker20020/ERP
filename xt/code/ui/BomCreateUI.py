# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BomCreate.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_BomCreate(object):
    def setupUi(self, BomCreate):
        if not BomCreate.objectName():
            BomCreate.setObjectName(u"BomCreate")
        BomCreate.resize(394, 295)
        self.verticalLayout = QVBoxLayout(BomCreate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(BomCreate)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bomCreateName = QLineEdit(BomCreate)
        self.bomCreateName.setObjectName(u"bomCreateName")

        self.horizontalLayout.addWidget(self.bomCreateName)

        self.bomCreate = QPushButton(BomCreate)
        self.bomCreate.setObjectName(u"bomCreate")

        self.horizontalLayout.addWidget(self.bomCreate)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(BomCreate)

        QMetaObject.connectSlotsByName(BomCreate)
    # setupUi

    def retranslateUi(self, BomCreate):
        BomCreate.setWindowTitle(QCoreApplication.translate("BomCreate", u"Form", None))
        self.label.setText(QCoreApplication.translate("BomCreate", u"\u65b0\u5efaBOM\u8868\u540d\u79f0", None))
        self.bomCreate.setText(QCoreApplication.translate("BomCreate", u"\u786e\u8ba4", None))
    # retranslateUi

