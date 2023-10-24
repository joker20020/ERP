# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'version2.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTableView,
    QWidget)

class Ui_cg_sector(object):
    def setupUi(self, cg_sector):
        if not cg_sector.objectName():
            cg_sector.setObjectName(u"cg_sector")
        cg_sector.resize(736, 499)
        self.horizontalLayout = QHBoxLayout(cg_sector)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(cg_sector)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.purchase_list_view = QTableView(self.tab_1)
        self.purchase_list_view.setObjectName(u"purchase_list_view")
        self.purchase_list_view.setGeometry(QRect(10, 90, 691, 351))
        self.purchase_list_receipt = QPushButton(self.tab_1)
        self.purchase_list_receipt.setObjectName(u"purchase_list_receipt")
        self.purchase_list_receipt.setGeometry(QRect(10, 60, 101, 24))
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 200, 231, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 170, 231, 16))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 170, 231, 16))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_5 = QLabel(self.tab_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 190, 231, 16))
        self.tabWidget.addTab(self.tab_5, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(cg_sector)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(cg_sector)
    # setupUi

    def retranslateUi(self, cg_sector):
        cg_sector.setWindowTitle(QCoreApplication.translate("cg_sector", u"Form", None))
        self.purchase_list_receipt.setText(QCoreApplication.translate("cg_sector", u"\u8bf7\u8d2d\u5355\u63a5\u6536", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("cg_sector", u"\u8bf7\u8d2d\u5355\u63a5\u6536", None))
        self.label.setText(QCoreApplication.translate("cg_sector", u"\u8fd9\u662f\u91c7\u8d2d\u4e1a\u52a1\u7ba1\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("cg_sector", u"\u91c7\u8d2d\u8ba2\u5355\u7ba1\u7406", None))
        self.label_3.setText(QCoreApplication.translate("cg_sector", u"\u8fd9\u662f\u5230\u8d27\u63a5\u6536\u4e1a\u52a1\u7ba1\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("cg_sector", u"\u5230\u8d27\u63a5\u6536", None))
        self.label_4.setText(QCoreApplication.translate("cg_sector", u"\u8fd9\u662f\u4f9b\u5e94\u5546\u7ba1\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("cg_sector", u"\u4f9b\u5e94\u5546\u7ba1\u7406\u4e0e\u8bc4\u4ef7", None))
        self.label_5.setText(QCoreApplication.translate("cg_sector", u"\u8fd9\u662f\u91c7\u8d2d\u4e1a\u52a1\u67e5\u8be2\u7ba1\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("cg_sector", u"\u91c7\u8d2d\u4e1a\u52a1\u7efc\u5408\u67e5\u8be2", None))
    # retranslateUi

