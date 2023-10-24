# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Line.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QSpacerItem, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton, SearchLineEdit,
    StrongBodyLabel, TableWidget, TitleLabel, VerticalSeparator)

class Ui_Line(object):
    def setupUi(self, Line):
        if not Line.objectName():
            Line.setObjectName(u"Line")
        Line.resize(786, 672)
        self.verticalLayout = QVBoxLayout(Line)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineLabel = TitleLabel(Line)
        self.lineLabel.setObjectName(u"lineLabel")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lineLabel.setFont(font)
        self.lineLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = SearchLineEdit(Line)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.lineRefresh = PushButton(Line)
        self.lineRefresh.setObjectName(u"lineRefresh")

        self.horizontalLayout_2.addWidget(self.lineRefresh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.lineTable = TableWidget(Line)
        if (self.lineTable.columnCount() < 4):
            self.lineTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.lineTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.lineTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.lineTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.lineTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.lineTable.setObjectName(u"lineTable")
        self.lineTable.horizontalHeader().setDefaultSectionSize(150)
        self.lineTable.horizontalHeader().setStretchLastSection(False)
        self.lineTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.lineTable)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineNew = PushButton(Line)
        self.lineNew.setObjectName(u"lineNew")

        self.horizontalLayout_4.addWidget(self.lineNew)

        self.lineRemove = PushButton(Line)
        self.lineRemove.setObjectName(u"lineRemove")

        self.horizontalLayout_4.addWidget(self.lineRemove)

        self.lineUpdate = PrimaryPushButton(Line)
        self.lineUpdate.setObjectName(u"lineUpdate")

        self.horizontalLayout_4.addWidget(self.lineUpdate)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.VerticalSeparator = VerticalSeparator(Line)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout.addWidget(self.VerticalSeparator)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.workLabel = StrongBodyLabel(Line)
        self.workLabel.setObjectName(u"workLabel")
        font1 = QFont()
        font1.setPointSize(14)
        self.workLabel.setFont(font1)
        self.workLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.workLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.workNew = PushButton(Line)
        self.workNew.setObjectName(u"workNew")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workNew.sizePolicy().hasHeightForWidth())
        self.workNew.setSizePolicy(sizePolicy)
        self.workNew.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_3.addWidget(self.workNew)

        self.workRemove = PushButton(Line)
        self.workRemove.setObjectName(u"workRemove")
        sizePolicy.setHeightForWidth(self.workRemove.sizePolicy().hasHeightForWidth())
        self.workRemove.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.workRemove)

        self.workUpdate = PrimaryPushButton(Line)
        self.workUpdate.setObjectName(u"workUpdate")
        sizePolicy.setHeightForWidth(self.workUpdate.sizePolicy().hasHeightForWidth())
        self.workUpdate.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.workUpdate)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.workTable = TableWidget(Line)
        if (self.workTable.columnCount() < 3):
            self.workTable.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.workTable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.workTable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.workTable.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.workTable.setObjectName(u"workTable")
        self.workTable.horizontalHeader().setCascadingSectionResizes(False)
        self.workTable.horizontalHeader().setDefaultSectionSize(200)
        self.workTable.horizontalHeader().setHighlightSections(True)
        self.workTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.workTable.horizontalHeader().setStretchLastSection(False)
        self.workTable.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.workTable)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)

        self.retranslateUi(Line)

        QMetaObject.connectSlotsByName(Line)
    # setupUi

    def retranslateUi(self, Line):
        Line.setWindowTitle(QCoreApplication.translate("Line", u"Form", None))
        self.lineLabel.setText(QCoreApplication.translate("Line", u"\u5de5\u827a\u8def\u7ebf\u7a97\u53e3", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Line", u"\u8f93\u5165\u5de5\u827a\u8def\u7ebf\u540d\u8fdb\u884c\u641c\u7d22", None))
        self.lineRefresh.setText(QCoreApplication.translate("Line", u"\u5237\u65b0", None))
        ___qtablewidgetitem = self.lineTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Line", u"\u5de5\u827a\u8def\u7ebfID", None));
        ___qtablewidgetitem1 = self.lineTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Line", u"\u5de5\u827a\u8def\u7ebf\u540d", None));
        ___qtablewidgetitem2 = self.lineTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Line", u"\u63cf\u8ff0", None));
        ___qtablewidgetitem3 = self.lineTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Line", u"\u5de5\u4f5c\u4e2d\u5fc3", None));
        self.lineNew.setText(QCoreApplication.translate("Line", u"\u65b0\u5efa\u5de5\u827a\u8def\u7ebf", None))
        self.lineRemove.setText(QCoreApplication.translate("Line", u"\u5220\u9664\u5de5\u827a\u8def\u7ebf", None))
        self.lineUpdate.setText(QCoreApplication.translate("Line", u"\u540c\u6b65", None))
        self.workLabel.setText(QCoreApplication.translate("Line", u"\u5de5\u5e8f\u4fe1\u606f", None))
        self.workNew.setText(QCoreApplication.translate("Line", u"\u65b0\u5efa\u5de5\u5e8f", None))
        self.workRemove.setText(QCoreApplication.translate("Line", u"\u5220\u9664\u5de5\u5e8f", None))
        self.workUpdate.setText(QCoreApplication.translate("Line", u"\u540c\u6b65", None))
        ___qtablewidgetitem4 = self.workTable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Line", u"\u5de5\u5e8f\u53f7", None));
        ___qtablewidgetitem5 = self.workTable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Line", u"\u5de5\u5e8f\u63cf\u8ff0", None));
        ___qtablewidgetitem6 = self.workTable.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Line", u"\u6240\u5c5e\u5de5\u827a\u8def\u7ebf\u53f7", None));
    # retranslateUi

