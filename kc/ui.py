# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hello.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_kcwidget(object):
    def setupUi(self, kcwidget):
        if not kcwidget.objectName():
            kcwidget.setObjectName(u"kcwidget")
        kcwidget.resize(646, 517)
        self.verticalLayout_2 = QVBoxLayout(kcwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 9, 20, 30)
        self.tabWidget = QTabWidget(kcwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget_2 = QTableWidget(self.tab_3)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        if (self.tableWidget_2.rowCount() < 8):
            self.tableWidget_2.setRowCount(8)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem25)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_3.addWidget(self.tableWidget_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.comboBox_chaxun = QComboBox(self.tab)
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.addItem("")
        self.comboBox_chaxun.setObjectName(u"comboBox_chaxun")

        self.verticalLayout.addWidget(self.comboBox_chaxun)

        self.pushButton_chaxun = QPushButton(self.tab)
        self.pushButton_chaxun.setObjectName(u"pushButton_chaxun")

        self.verticalLayout.addWidget(self.pushButton_chaxun)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.lineEdit_chaxunid = QLineEdit(self.tab)
        self.lineEdit_chaxunid.setObjectName(u"lineEdit_chaxunid")

        self.verticalLayout.addWidget(self.lineEdit_chaxunid)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.lineEdit_chaxunshuliang = QLineEdit(self.tab)
        self.lineEdit_chaxunshuliang.setObjectName(u"lineEdit_chaxunshuliang")

        self.verticalLayout.addWidget(self.lineEdit_chaxunshuliang)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_tianjiamingcheng = QLineEdit(self.tab)
        self.lineEdit_tianjiamingcheng.setObjectName(u"lineEdit_tianjiamingcheng")

        self.verticalLayout.addWidget(self.lineEdit_tianjiamingcheng)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_tianjiashuliang = QLineEdit(self.tab)
        self.lineEdit_tianjiashuliang.setObjectName(u"lineEdit_tianjiashuliang")

        self.verticalLayout.addWidget(self.lineEdit_tianjiashuliang)

        self.pushButton_tianjia = QPushButton(self.tab)
        self.pushButton_tianjia.setObjectName(u"pushButton_tianjia")

        self.verticalLayout.addWidget(self.pushButton_tianjia)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.lineEdit_shanchuid = QLineEdit(self.tab)
        self.lineEdit_shanchuid.setObjectName(u"lineEdit_shanchuid")

        self.verticalLayout.addWidget(self.lineEdit_shanchuid)

        self.pushButton_shancbu = QPushButton(self.tab)
        self.pushButton_shancbu.setObjectName(u"pushButton_shancbu")

        self.verticalLayout.addWidget(self.pushButton_shancbu)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(kcwidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(kcwidget)
    # setupUi

    def retranslateUi(self, kcwidget):
        kcwidget.setWindowTitle(QCoreApplication.translate("kcwidget", u"\u5e93\u5b58\u7ba1\u7406\u7cfb\u7edf", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("kcwidget", u"\u5165\u5e93\u65f6\u95f4", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1id", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1\u6570\u91cf", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("kcwidget", u"\u5165\u5e93\u4f4d\u7f6e", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("kcwidget", u"\u64cd\u4f5c\u4eba\u5458", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("kcwidget", u"0", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("kcwidget", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("kcwidget", u"2", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("kcwidget", u"3", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("kcwidget", u"4", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("kcwidget", u"5", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("kcwidget", u"6", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("kcwidget", u"7", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("kcwidget", u"\u5165\u5e93", None))
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("kcwidget", u"\u51fa\u5e93\u65f6\u95f4", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1id", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1\u6570\u91cf", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("kcwidget", u"\u51fa\u5e93\u4f4d\u7f6e", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("kcwidget", u"\u64cd\u4f5c\u4eba\u5458", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("kcwidget", u"0", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("kcwidget", u"1", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("kcwidget", u"2", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("kcwidget", u"3", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("kcwidget", u"4", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("kcwidget", u"5", None));
        ___qtablewidgetitem24 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("kcwidget", u"6", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("kcwidget", u"7", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("kcwidget", u"\u51fa\u5e93", None))
        self.label_8.setText(QCoreApplication.translate("kcwidget", u"\u5e93\u5b58\u67e5\u8be2", None))
        self.comboBox_chaxun.setItemText(0, QCoreApplication.translate("kcwidget", u"\u5927\u4f17\u81ea\u52a8\u94b3", None))
        self.comboBox_chaxun.setItemText(1, QCoreApplication.translate("kcwidget", u"\u58f3\u4f532", None))
        self.comboBox_chaxun.setItemText(2, QCoreApplication.translate("kcwidget", u"\u652f\u67b61", None))
        self.comboBox_chaxun.setItemText(3, QCoreApplication.translate("kcwidget", u"\u914d\u4ef6", None))
        self.comboBox_chaxun.setItemText(4, QCoreApplication.translate("kcwidget", u"\u5de6\u58f3\u4f531", None))
        self.comboBox_chaxun.setItemText(5, QCoreApplication.translate("kcwidget", u"\u53f3\u58f3\u4f531", None))
        self.comboBox_chaxun.setItemText(6, QCoreApplication.translate("kcwidget", u"\u5bc6\u5c01\u57082", None))
        self.comboBox_chaxun.setItemText(7, QCoreApplication.translate("kcwidget", u"\u6d3b\u585e1", None))
        self.comboBox_chaxun.setItemText(8, QCoreApplication.translate("kcwidget", u"\u5851\u6599\u59571", None))
        self.comboBox_chaxun.setItemText(9, QCoreApplication.translate("kcwidget", u"\u6a61\u80f6\u59571", None))
        self.comboBox_chaxun.setItemText(10, QCoreApplication.translate("kcwidget", u"\u653e\u6c14\u87ba\u68131", None))
        self.comboBox_chaxun.setItemText(11, QCoreApplication.translate("kcwidget", u"\u9632\u5c18\u5e3d1", None))
        self.comboBox_chaxun.setItemText(12, QCoreApplication.translate("kcwidget", u"\u5185\u516d\u89d2\u87ba\u68131", None))
        self.comboBox_chaxun.setItemText(13, QCoreApplication.translate("kcwidget", u"\u6469\u64e6\u72472", None))
        self.comboBox_chaxun.setItemText(14, QCoreApplication.translate("kcwidget", u"\u9694\u57ab1", None))
        self.comboBox_chaxun.setItemText(15, QCoreApplication.translate("kcwidget", u"\u5f00\u53e3\u5bfc\u5411\u5957\u7ba12", None))

        self.pushButton_chaxun.setText(QCoreApplication.translate("kcwidget", u"\u67e5\u8be2", None))
        self.label_11.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1id", None))
        self.label_12.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1\u6570\u91cf", None))
        self.label_4.setText(QCoreApplication.translate("kcwidget", u"\u6dfb\u52a0\u65b0\u5546\u54c1", None))
        self.label_3.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("kcwidget", u"\u6dfb\u52a0\u6570\u91cf", None))
        self.pushButton_tianjia.setText(QCoreApplication.translate("kcwidget", u"\u786e\u8ba4", None))
        self.label_6.setText(QCoreApplication.translate("kcwidget", u"\u5220\u9664\u5546\u54c1", None))
        self.label_7.setText(QCoreApplication.translate("kcwidget", u"\u5546\u54c1id", None))
        self.pushButton_shancbu.setText(QCoreApplication.translate("kcwidget", u"\u786e\u8ba4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("kcwidget", u"\u67e5\u8be2\u589e\u6539", None))
    # retranslateUi
