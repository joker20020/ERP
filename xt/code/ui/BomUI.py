# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bom.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLayout,
    QListWidgetItem, QSizePolicy, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ListWidget, PrimaryPushButton, PushButton, SearchLineEdit,
    TableWidget, VerticalSeparator)

class Ui_Bom(object):
    def setupUi(self, Bom):
        if not Bom.objectName():
            Bom.setObjectName(u"Bom")
        Bom.resize(856, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Bom.sizePolicy().hasHeightForWidth())
        Bom.setSizePolicy(sizePolicy)
        self.partNew = QAction(Bom)
        self.partNew.setObjectName(u"partNew")
        self.partNew.setMenuRole(QAction.NoRole)
        self.partRemove = QAction(Bom)
        self.partRemove.setObjectName(u"partRemove")
        self.partRemove.setMenuRole(QAction.NoRole)
        self.openLine = QAction(Bom)
        self.openLine.setObjectName(u"openLine")
        self.openLine.setMenuRole(QAction.NoRole)
        self.horizontalLayout = QHBoxLayout(Bom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bomInput = SearchLineEdit(Bom)
        self.bomInput.setObjectName(u"bomInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bomInput.sizePolicy().hasHeightForWidth())
        self.bomInput.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.bomInput)

        self.bomRefresh = PushButton(Bom)
        self.bomRefresh.setObjectName(u"bomRefresh")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bomRefresh.sizePolicy().hasHeightForWidth())
        self.bomRefresh.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.bomRefresh)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.bomList = ListWidget(Bom)
        self.bomList.setObjectName(u"bomList")

        self.verticalLayout_2.addWidget(self.bomList)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bomNew = PushButton(Bom)
        self.bomNew.setObjectName(u"bomNew")

        self.horizontalLayout_3.addWidget(self.bomNew)

        self.bomRemove = PushButton(Bom)
        self.bomRemove.setObjectName(u"bomRemove")

        self.horizontalLayout_3.addWidget(self.bomRemove)

        self.bomUpdate = PrimaryPushButton(Bom)
        self.bomUpdate.setObjectName(u"bomUpdate")

        self.horizontalLayout_3.addWidget(self.bomUpdate)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.VerticalSeparator = VerticalSeparator(Bom)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout.addWidget(self.VerticalSeparator)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bomTable = TableWidget(Bom)
        if (self.bomTable.columnCount() < 8):
            self.bomTable.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.bomTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.bomTable.rowCount() < 1):
            self.bomTable.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.bomTable.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.bomTable.setItem(0, 1, __qtablewidgetitem9)
        self.bomTable.setObjectName(u"bomTable")
        self.bomTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.bomTable.setRowCount(1)
        self.bomTable.horizontalHeader().setDefaultSectionSize(200)
        self.bomTable.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.bomTable)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 4)

        self.retranslateUi(Bom)

        QMetaObject.connectSlotsByName(Bom)
    # setupUi

    def retranslateUi(self, Bom):
        Bom.setWindowTitle(QCoreApplication.translate("Bom", u"Form", None))
        self.partNew.setText(QCoreApplication.translate("Bom", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.partNew.setShortcut(QCoreApplication.translate("Bom", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.partRemove.setText(QCoreApplication.translate("Bom", u"\u5220\u9664", None))
#if QT_CONFIG(shortcut)
        self.partRemove.setShortcut(QCoreApplication.translate("Bom", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.openLine.setText(QCoreApplication.translate("Bom", u"\u6253\u5f00\u5de5\u827a\u8def\u7ebf", None))
#if QT_CONFIG(shortcut)
        self.openLine.setShortcut(QCoreApplication.translate("Bom", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.bomRefresh.setText(QCoreApplication.translate("Bom", u"\u5237\u65b0", None))
        self.bomNew.setText(QCoreApplication.translate("Bom", u"\u65b0\u5efa", None))
        self.bomRemove.setText(QCoreApplication.translate("Bom", u"\u5220\u9664", None))
        self.bomUpdate.setText(QCoreApplication.translate("Bom", u"\u540c\u6b65", None))
        ___qtablewidgetitem = self.bomTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Bom", u"ID", None));
        ___qtablewidgetitem1 = self.bomTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Bom", u"bom\u5c42\u7ea7", None));
        ___qtablewidgetitem2 = self.bomTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Bom", u"\u96f6\u4ef6\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.bomTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Bom", u"\u7236\u96f6\u4ef6ID", None));
        ___qtablewidgetitem4 = self.bomTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Bom", u"\u96f6\u4ef6\u6210\u672c", None));
        ___qtablewidgetitem5 = self.bomTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Bom", u"\u96f6\u4ef6\u751f\u4ea7\u5468\u671f", None));
        ___qtablewidgetitem6 = self.bomTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Bom", u"\u662f\u5426\u5916\u8d2d", None));
        ___qtablewidgetitem7 = self.bomTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Bom", u"\u6ce8\u91ca", None));

        __sortingEnabled = self.bomTable.isSortingEnabled()
        self.bomTable.setSortingEnabled(False)
        self.bomTable.setSortingEnabled(__sortingEnabled)

    # retranslateUi

