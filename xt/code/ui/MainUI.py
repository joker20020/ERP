# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QGridLayout,
    QHBoxLayout, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QToolButton, QVBoxLayout,
    QWidget,QButtonGroup)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        self.cg_page = QWidget()
        self.cg_page.setObjectName(u"cg_page")
        self.horizontalLayout = QHBoxLayout(self.cg_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_3 = QRadioButton(self.cg_page)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.cg_page)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.cg_page)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.stack.addWidget(self.cg_page)
        self.jh_page = QWidget()
        self.jh_page.setObjectName(u"jh_page")
        self.verticalLayout_2 = QVBoxLayout(self.jh_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.jh_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.jh_page)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.stack.addWidget(self.jh_page)
        self.kc_page = QWidget()
        self.kc_page.setObjectName(u"kc_page")
        self.horizontalLayout_2 = QHBoxLayout(self.kc_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButton = QToolButton(self.kc_page)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_2.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.kc_page)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_2.addWidget(self.toolButton_2)

        self.stack.addWidget(self.kc_page)
        self.xs_page = QWidget()
        self.xs_page.setObjectName(u"xs_page")
        self.verticalLayout = QVBoxLayout(self.xs_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.commandLinkButton = QCommandLinkButton(self.xs_page)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout.addWidget(self.commandLinkButton)

        self.checkBox = QCheckBox(self.xs_page)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.stack.addWidget(self.xs_page)
        self.xt_page = QWidget()
        self.xt_page.setObjectName(u"xt_page")
        self.horizontalLayout_3 = QHBoxLayout(self.xt_page)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tab = QTabWidget(self.xt_page)
        self.tab.setObjectName(u"tab")
        self.tab.setTabPosition(QTabWidget.North)
        self.tab.setTabsClosable(False)
        self.tab.setTabBarAutoHide(False)
        self.bomTab = QWidget()
        self.bomTab.setObjectName(u"bomTab")
        self.horizontalLayout_5 = QHBoxLayout(self.bomTab)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bomLayout = QHBoxLayout()
        self.bomLayout.setObjectName(u"bomLayout")

        self.horizontalLayout_5.addLayout(self.bomLayout)

        self.tab.addTab(self.bomTab, "")
        self.adminTab = QWidget()
        self.adminTab.setObjectName(u"adminTab")
        self.horizontalLayout_4 = QHBoxLayout(self.adminTab)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.adminLayout = QHBoxLayout()
        self.adminLayout.setObjectName(u"adminLayout")

        self.horizontalLayout_4.addLayout(self.adminLayout)

        self.tab.addTab(self.adminTab, "")

        self.horizontalLayout_3.addWidget(self.tab)

        self.stack.addWidget(self.xt_page)

        self.gridLayout_2.addWidget(self.stack, 0, 1, 1, 1)

        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setStyleSheet(u"QToolButton{\n"
"		border: none;\n"
"         margin:0px;\n"
"		min-width: 80px;                            /* \u63a7\u4ef6\u6700\u5c0f\u5bbd\u5ea6 */\n"
"    		min-height: 80px;\n"
"}")
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.xs = QToolButton(self.gridWidget)
        self.xs.setObjectName(u"xs")
        self.xs.setCheckable(True)
        self.xs.setAutoExclusive(False)

        self.gridLayout.addWidget(self.xs, 3, 0, 1, 1)

        self.jh = QToolButton(self.gridWidget)
        self.jh.setObjectName(u"jh")
        self.jh.setCheckable(True)
        self.jh.setAutoExclusive(False)

        self.gridLayout.addWidget(self.jh, 1, 0, 1, 1)

        self.cg = QToolButton(self.gridWidget)
        self.cg.setObjectName(u"cg")
        self.cg.setCheckable(True)
        self.cg.setAutoExclusive(False)

        self.gridLayout.addWidget(self.cg, 0, 0, 1, 1)

        self.kc = QToolButton(self.gridWidget)
        self.kc.setObjectName(u"kc")
        self.kc.setCheckable(True)
        self.kc.setAutoExclusive(False)

        self.gridLayout.addWidget(self.kc, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.xt = QToolButton(self.gridWidget)
        self.xt.setObjectName(u"xt")
        self.xt.setCheckable(True)
        self.xt.setAutoExclusive(False)

        self.gridLayout.addWidget(self.xt, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(4)
        self.tab.setCurrentIndex(0)

        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.cg, 0)
        self.btn_group.addButton(self.jh, 1)
        self.btn_group.addButton(self.kc, 2)
        self.btn_group.addButton(self.xs, 3)
        self.btn_group.addButton(self.xt, 4)



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.tab.setTabText(self.tab.indexOf(self.bomTab), QCoreApplication.translate("MainWindow", u"BOM\u8868", None))
        self.tab.setTabText(self.tab.indexOf(self.adminTab), QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
        self.xs.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.jh.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.cg.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.kc.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.xt.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

