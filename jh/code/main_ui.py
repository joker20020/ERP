# 导入sys
import os
import sys
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget, QApplication, QTableWidget, QTableWidgetItem
# 导入我们生成的界面

from .window_chaxun import Ui_Form
from .table_MPS import table_MPS
from .table_MRP import table_MRP
from .table_caigou import table_caigou
from .table_chejianzuoye import table_chejianzuoye
from .table_paigong import table_paigong
from .table_lingliao import table_lingliao

from .JH_SQL import JHDataBase

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QStandardItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6 import QtCore

# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    def __init__(self,file_path="JHdatabase.db"):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.jh_db = JHDataBase(file_path)

        self.MPS = table_MPS1()
        self.MRP = table_MRP1()
        self.caigou = table_caigou1()
        self.chejianzuoye = table_chejianzuoye1()
        self.paigong = table_paigong1()
        self.lingliao = table_lingliao1()

        self.bind()
        self.loadin()

    def open(self):
        mode = self.ui.target.currentText()
        if mode == "MPS主生产计划":
            self.MPS.show()
        if mode == "MRP物料需求计划":
            self.MRP.show()
        if mode == "车间工作采购单":
            self.caigou.show()
        if mode == "车间工作作业计划":
            self.chejianzuoye.show()
        if mode == "派工单":
            self.paigong.show()
        if mode == "领料单":
            self.lingliao.show()

    def bind(self):
        self.ui.pushButton.clicked.connect(self.open)

    def loadin(self):
        MPS_table = self.jh_db.find_info("MPS_table", [])
        self.MPS.ui.tableWidget.clearContents()
        rows1 = len(MPS_table)
        self.MPS.ui.tableWidget.setRowCount(rows1)
        for i in range(rows1):
            for j in range(len(MPS_table[i])):
                self.MPS.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(MPS_table[i][j])))

        MRP_table = self.jh_db.find_info("MRP_table", [])
        self.MRP.ui.tableWidget.clearContents()
        rows2 = len(MPS_table)
        self.MRP.ui.tableWidget.setRowCount(rows2)
        for i in range(rows2):
            for j in range(len(MPS_table[i])):
                self.MPS.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(MPS_table[i][j])))

class table_MPS1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_MPS()
        self.ui.setupUi(self)

class table_MRP1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_MRP()
        self.ui.setupUi(self)

class table_caigou1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_caigou()
        self.ui.setupUi(self)

class table_chejianzuoye1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_chejianzuoye()
        self.ui.setupUi(self)

class table_paigong1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_paigong()
        self.ui.setupUi(self)

class table_lingliao1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_lingliao()
        self.ui.setupUi(self)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
