# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xs2.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PrimaryPushButton, PushButton,
    RadioButton, TableWidget, TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(604, 349)
        self.formLayout_4 = QFormLayout(Form)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout_3 = QFormLayout(self.tab)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = BodyLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = BodyLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = BodyLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = BodyLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = BodyLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = LineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = LineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = LineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = LineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.lineEdit_5 = LineEdit(self.tab)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_2.addWidget(self.lineEdit_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.textBrowser = TextEdit(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(100, 100))
        self.textBrowser.setMaximumSize(QSize(16500, 150))

        self.horizontalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = RadioButton(self.tab)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = RadioButton(self.tab)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_4 = RadioButton(self.tab)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.radioButton_3 = RadioButton(self.tab)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_3 = PrimaryPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayout_5 = QFormLayout(self.tab_2)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = BodyLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = BodyLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = BodyLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = BodyLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_7 = LineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_6.addWidget(self.lineEdit_7)

        self.lineEdit_8 = LineEdit(self.tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_6.addWidget(self.lineEdit_8)

        self.lineEdit_9 = LineEdit(self.tab_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_6.addWidget(self.lineEdit_9)

        self.lineEdit_10 = LineEdit(self.tab_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_6.addWidget(self.lineEdit_10)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_7)

        self.textBrowser_3 = TextEdit(self.tab_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMaximumSize(QSize(16500, 150))

        self.horizontalLayout_16.addWidget(self.textBrowser_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_5 = RadioButton(self.tab_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_6.addWidget(self.radioButton_5)

        self.radioButton_6 = RadioButton(self.tab_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_6.addWidget(self.radioButton_6)

        self.radioButton_7 = RadioButton(self.tab_2)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_6.addWidget(self.radioButton_7)

        self.radioButton_8 = RadioButton(self.tab_2)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.horizontalLayout_6.addWidget(self.radioButton_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.pushButton = PushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = PushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayout = QFormLayout(self.tab_3)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.verticalLayout_20.addLayout(self.verticalLayout_11)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.verticalLayout_20)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = BodyLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.label_15 = BodyLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_9.addWidget(self.label_15)

        self.label_16 = BodyLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_9.addWidget(self.label_16)


        self.horizontalLayout_9.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEdit_12 = LineEdit(self.tab_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_10.addWidget(self.lineEdit_12)

        self.lineEdit_14 = LineEdit(self.tab_3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout_10.addWidget(self.lineEdit_14)

        self.lineEdit_15 = LineEdit(self.tab_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.verticalLayout_10.addWidget(self.lineEdit_15)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)


        self.verticalLayout_18.addLayout(self.horizontalLayout_9)

        self.lineEdit_13 = LineEdit(self.tab_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_18.addWidget(self.lineEdit_13)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.pushButton_5 = PushButton(self.tab_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_15.addWidget(self.pushButton_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)

        self.pushButton_6 = PushButton(self.tab_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_15.addWidget(self.pushButton_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)


        self.verticalLayout_19.addLayout(self.horizontalLayout_15)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_19)

        self.tableWidget = TableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 15):
            self.tableWidget.setRowCount(15)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.tableWidget)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.formLayout_6 = QFormLayout(self.tab_5)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = BodyLabel(self.tab_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.label_11 = BodyLabel(self.tab_5)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.label_18 = BodyLabel(self.tab_5)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_12.addWidget(self.label_18)

        self.label_14 = BodyLabel(self.tab_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_12.addWidget(self.label_14)

        self.label_22 = BodyLabel(self.tab_5)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_12.addWidget(self.label_22)

        self.label_12 = BodyLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_12.addWidget(self.label_12)

        self.label_17 = BodyLabel(self.tab_5)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_12.addWidget(self.label_17)

        self.label_19 = BodyLabel(self.tab_5)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_12.addWidget(self.label_19)


        self.horizontalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lineEdit_17 = LineEdit(self.tab_5)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.verticalLayout_13.addWidget(self.lineEdit_17)

        self.lineEdit_18 = LineEdit(self.tab_5)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.verticalLayout_13.addWidget(self.lineEdit_18)

        self.lineEdit_19 = LineEdit(self.tab_5)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.verticalLayout_13.addWidget(self.lineEdit_19)

        self.lineEdit_11 = LineEdit(self.tab_5)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_13.addWidget(self.lineEdit_11)

        self.lineEdit_20 = LineEdit(self.tab_5)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_13.addWidget(self.lineEdit_20)

        self.lineEdit_21 = LineEdit(self.tab_5)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_13.addWidget(self.lineEdit_21)

        self.lineEdit_6 = LineEdit(self.tab_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_13.addWidget(self.lineEdit_6)

        self.lineEdit_26 = LineEdit(self.tab_5)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.verticalLayout_13.addWidget(self.lineEdit_26)


        self.horizontalLayout_10.addLayout(self.verticalLayout_13)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_12)

        self.textBrowser_2 = TextEdit(self.tab_5)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMaximumSize(QSize(200, 150))

        self.horizontalLayout_17.addWidget(self.textBrowser_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_10)

        self.pushButton_7 = PushButton(self.tab_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_14.addWidget(self.pushButton_7)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.pushButton_8 = PushButton(self.tab_5)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_14.addWidget(self.pushButton_8)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radioButton_9 = RadioButton(self.tab_5)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.horizontalLayout_11.addWidget(self.radioButton_9)

        self.radioButton_12 = RadioButton(self.tab_5)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_11.addWidget(self.radioButton_12)

        self.radioButton_10 = RadioButton(self.tab_5)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_11.addWidget(self.radioButton_10)

        self.radioButton_11 = RadioButton(self.tab_5)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.horizontalLayout_11.addWidget(self.radioButton_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.formLayout_6.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.formLayout_2 = QFormLayout(self.tab_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_21 = QLabel(self.tab_6)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_17.addWidget(self.label_21)


        self.formLayout_2.setLayout(1, QFormLayout.LabelRole, self.verticalLayout_17)

        self.tableWidget_2 = TableWidget(self.tab_6)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        if (self.tableWidget_2.rowCount() < 15):
            self.tableWidget_2.setRowCount(15)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setRowCount(15)
        self.tableWidget_2.setColumnCount(4)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.tableWidget_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.pushButton_9 = PushButton(self.tab_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_13.addWidget(self.pushButton_9)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_13)

        self.tabWidget.addTab(self.tab_6, "")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237ID", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u59d3\u540d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u5730\u5740", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u90ae\u7bb1", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u79ef\u5206", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u4fe1\u606f\u5f55\u5165", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u4fe1\u606f\u67e5\u8be2", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u4fe1\u606f\u5220\u9664", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u4fe1\u606f\u66f4\u65b0", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5ba2\u6237\u4fe1\u606f\u7ba1\u7406", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458ID", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u59d3\u540d", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u804c\u52a1", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u5bc6\u5319", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u4fe1\u606f\u5f55\u5165", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u4fe1\u606f\u67e5\u8be2", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u4fe1\u606f\u5220\u9664", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u4fe1\u606f\u66f4\u65b0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u4fe1\u606f\u7ba1\u7406", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1ID", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u5458ID", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u5bc6\u5319", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u5e93\u5b58\uff08\u4ef6\uff09", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u5b9a\u4ef7(\u5143)", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u4ea7\u54c1\u4fe1\u606f\u67e5\u8be2", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u8ba2\u5355ID", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u8ba2\u5355\u65e5\u671f", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u5546\u54c1ID", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u540d\u79f0", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u8ba2\u5355\u6570\u91cf", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237ID", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458ID", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u5bc6\u5319", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        self.radioButton_9.setText(QCoreApplication.translate("Form", u"\u63d0\u8d27", None))
        self.radioButton_12.setText(QCoreApplication.translate("Form", u"\u51fa\u8d27", None))
        self.radioButton_10.setText(QCoreApplication.translate("Form", u"\u8ba2\u5355\u4fe1\u606f\u67e5\u8be2", None))
        self.radioButton_11.setText(QCoreApplication.translate("Form", u"\u8ba2\u5355\u4fe1\u606f\u66f4\u6539", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u9500\u552e\u8ba2\u5355\u7ba1\u7406", None))
        self.label_21.setText("")
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458ID", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u59d3\u540d", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u6210\u4ea4\u8ba2\u5355\u6570", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u4e1a\u52a1\u603b\u503c\uff08\u5143\uff09", None));
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u4e1a\u7ee9\u5206\u6790", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u9500\u552e\u5458\u4e1a\u7ee9\u5206\u6790", None))
    # retranslateUi

