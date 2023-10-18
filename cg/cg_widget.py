import sys
import os
import os

from PySide6.QtWidgets import (QApplication, QWidget,
QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, 
QGroupBox, QMainWindow, QRadioButton, QGridLayout, QTableView,
QFormLayout, QStackedLayout, QScrollArea, QFileDialog)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QStandardItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6 import QtCore

class MyWindow(QWidget):
    # 继承父类，并执行类的方法
    def __init__(self):
        super().__init__()
        # 定义窗体大小
        self.resize(800, 480)
        # 执行初始化方法
        self.init_ui()
        # 设定左上角标题
        self.ui.setWindowTitle("采购模块")
        # 设定左上角图标，图标png文件使用绝对路径
        icon = QIcon('../cg_ui/u102.png')
        self.ui.setWindowIcon(icon)

    # 一些初始化操作
    def init_ui(self):

        # 实例化QUiloader，并加载绝对路径下的.ui文件
        loader = QUiLoader()
        ui_file = "cg_ui/version2.ui"
        self.ui = loader.load(ui_file)

        # 从ui文件中取出一些需要用到的控件名称，并定义为类的属性
        self.purchase_receipt_btn = self.ui.purchase_list_receipt
        self.purchase_list_view = self.ui.purchase_list_view

        self.purchase_receipt_btn.clicked.connect(self.view_list)
    
    def view_list(self):
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("cg_db/Purchase List.db")
        if not self.database.open():
            print("Error: Could not open the database")
        
        self.model = QSqlTableModel(self, self.database)
        self.model.setTable('cg_purchase_list')

        self.model.select()

        self.purchase_list_view.setModel(self.model)
        self.purchase_list_view.resizeColumnsToContents()

if __name__ == '__main__':
    # 创建一个名为app的实例，代表应用本身，用于设置GUI并处理事件
    app = QApplication(sys.argv)
    # 实例化MyWindow
    w = MyWindow()
    # 在屏幕上显示QWiget窗口
    w.ui.show()
    # 启动QApplication的循环，直到用户关闭窗口
    app.exec()