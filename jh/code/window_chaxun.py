# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_chaxun.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CalendarPicker, CaptionLabel, ComboBox, LineEdit,
    PrimaryPushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(545, 419)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Baoli SC"])
        font.setPointSize(64)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = CaptionLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"STHeiti"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 700 18pt \"STHeiti\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setMargin(0)

        self.horizontalLayout.addWidget(self.label_2)

        self.target = ComboBox(Form)
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.setObjectName(u"target")
        self.target.setEnabled(True)
        self.target.setStyleSheet(u"font: 18pt \"STKaiti\";")
        # self.target.setFrame(True)

        self.horizontalLayout.addWidget(self.target)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 18pt \"STHeiti\";")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.start = CalendarPicker(Form)
        self.start.setObjectName(u"start")
        self.start.setStyleSheet(u"font: 18pt \"STKaiti\";")

        self.horizontalLayout_3.addWidget(self.start)

        self.label_5 = CaptionLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 18pt \"STHeiti\";")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.ddl = CalendarPicker(Form)
        self.ddl.setObjectName(u"ddl")
        self.ddl.setStyleSheet(u"font: 18pt \"STKaiti\";")

        self.horizontalLayout_3.addWidget(self.ddl)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        font2 = QFont()
        font2.setFamilies([u"STKaiti"])
        font2.setPointSize(18)
        self.lineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = CaptionLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setStyleSheet(u"font: 700 18pt \"Heiti SC\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.workID = LineEdit(Form)
        self.workID.setObjectName(u"workID")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workID.sizePolicy().hasHeightForWidth())
        self.workID.setSizePolicy(sizePolicy)
        self.workID.setStyleSheet(u"font: 18pt \"STKaiti\";")
        self.workID.setFrame(True)

        self.horizontalLayout_4.addWidget(self.workID)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = PrimaryPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font: 24pt \"STKaiti\";")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8ba1\u5212\u7ba1\u7406\u67e5\u8be2\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u76ee\u6807\uff1a", None))
        self.target.setItemText(0, QCoreApplication.translate("Form", u"MPS\u4e3b\u751f\u4ea7\u8ba1\u5212", None))
        self.target.setItemText(1, QCoreApplication.translate("Form", u"MRP\u7269\u6599\u9700\u6c42\u8ba1\u5212", None))
        self.target.setItemText(2, QCoreApplication.translate("Form", u"\u8f66\u95f4\u5de5\u4f5c\u91c7\u8d2d\u5355", None))
        self.target.setItemText(3, QCoreApplication.translate("Form", u"\u8f66\u95f4\u5de5\u4f5c\u4f5c\u4e1a\u8ba1\u5212", None))
        self.target.setItemText(4, QCoreApplication.translate("Form", u"\u6d3e\u5de5\u5355", None))
        self.target.setItemText(5, QCoreApplication.translate("Form", u"\u9886\u6599\u5355", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u8d77\u59cb\u65f6\u95f4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u622a\u6b62\u65f6\u95f4\uff1a", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\u82e5\u67e5\u8be2\u76ee\u6807\u4e3a\u6d3e\u5de5\u5355\u6216\u9886\u6599\u5355\uff0c\u8bf7\u8f93\u5165\u9700\u67e5\u8be2\u7684\u5de5\u4f5c\u4e2d\u5fc3ID\u3002", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5de5\u4f5c\u4e2d\u5fc3ID\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
    # retranslateUi

