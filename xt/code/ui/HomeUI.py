# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QSizePolicy, QSpacerItem, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (AvatarWidget, BodyLabel, CalendarPicker, LineEdit,
    PasswordLineEdit, PrimaryPushButton, PrimaryToolButton, SplitPushButton,
    TableWidget, TimePicker)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(552, 479)
        self.verticalLayout = QVBoxLayout(HomePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.avater = AvatarWidget(HomePage)
        self.avater.setObjectName(u"avater")

        self.horizontalLayout.addWidget(self.avater)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.userNameL = BodyLabel(HomePage)
        self.userNameL.setObjectName(u"userNameL")

        self.gridLayout.addWidget(self.userNameL, 0, 0, 1, 1)

        self.passwordL = BodyLabel(HomePage)
        self.passwordL.setObjectName(u"passwordL")

        self.gridLayout.addWidget(self.passwordL, 1, 0, 1, 1)

        self.userName = LineEdit(HomePage)
        self.userName.setObjectName(u"userName")

        self.gridLayout.addWidget(self.userName, 0, 1, 1, 1)

        self.password = PasswordLineEdit(HomePage)
        self.password.setObjectName(u"password")

        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)

        self.passwordChange = PrimaryPushButton(HomePage)
        self.passwordChange.setObjectName(u"passwordChange")

        self.gridLayout.addWidget(self.passwordChange, 1, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.date = CalendarPicker(HomePage)
        self.date.setObjectName(u"date")

        self.horizontalLayout_2.addWidget(self.date)

        self.time = TimePicker(HomePage)
        self.time.setObjectName(u"time")

        self.horizontalLayout_2.addWidget(self.time)

        self.query = SplitPushButton(HomePage)
        self.query.setObjectName(u"query")

        self.horizontalLayout_2.addWidget(self.query)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.logTable = TableWidget(HomePage)
        if (self.logTable.columnCount() < 3):
            self.logTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.logTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.logTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.logTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.logTable.setObjectName(u"logTable")

        self.verticalLayout.addWidget(self.logTable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.logRemove = PrimaryToolButton(HomePage)
        self.logRemove.setObjectName(u"logRemove")

        self.horizontalLayout_3.addWidget(self.logRemove)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Form", None))
        self.avater.setText(QCoreApplication.translate("HomePage", u"\u5934\u50cf", None))
        self.userNameL.setText(QCoreApplication.translate("HomePage", u"\u7528\u6237\u540d", None))
        self.passwordL.setText(QCoreApplication.translate("HomePage", u"\u5bc6\u7801", None))
        self.passwordChange.setText(QCoreApplication.translate("HomePage", u"\u4fee\u6539\u5bc6\u7801", None))
        self.date.setText("")
        self.time.setText("")
        self.query.setText(QCoreApplication.translate("HomePage", u"\u67e5\u8be2", None))
        ___qtablewidgetitem = self.logTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HomePage", u"\u64cd\u4f5c\u65f6\u95f4", None));
        ___qtablewidgetitem1 = self.logTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HomePage", u"\u64cd\u4f5c\u7528\u6237", None));
        ___qtablewidgetitem2 = self.logTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HomePage", u"\u64cd\u4f5c", None));
        self.logRemove.setText("")
    # retranslateUi

