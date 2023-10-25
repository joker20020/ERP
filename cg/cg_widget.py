'''
命名规则：
请购单接收：Requisition Receipt
采购订单管理：Order Management
到货接收：Recieve Upon
供应商管理与评价：Supplier Management
采购业务综合查询：Comprehensive Query

TODO: 貌似很多头函数没用上，后续可能会删除或者精简一下
TODO: 检查所有文件的路径、相对路径/绝对路径、是否有同名文件、是否最新，以及文件名
FIXME: 重新写了之后貌似相对路径又有点问题
TODO: 有一个巨大的bug，就是忘记写初始化和清栈的操作了，导致每次加载数据和文件后，相应控件不能重新显示新的内容
TODO: 1.完善功能，确定物理表结构 2.确保每次点击按钮都可以刷新(完成) 3.动态调用.ui文件改成py文件(完成) 4.优化代码，减少功能重复 5.界面美化，使用qfluetwidget库重新生成ui
'''

import sys
import os
import time

from PySide6.QtWidgets import (QApplication, QWidget, QComboBox,
QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,
QGroupBox, QMainWindow, QRadioButton, QGridLayout, QTableView,
QFormLayout, QStackedLayout, QScrollArea, QFileDialog, 
QGraphicsView, QGraphicsScene, QGraphicsPixmapItem)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QThread, Signal, Slot, QModelIndex
from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel, QPixmap, QPainter, QImage
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6 import QtCore
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from cg_ui.version2 import Ui_cg_sector
import cg_database

# 这是生成采购部门模块的类
class cg_widget(QWidget):
    # 继承父类，并执行类的方法，一些基础的设定
    def __init__(self):
        super().__init__()
        # 定义窗体大小
        self.resize(800, 480)
        # 执行初始化方法
        self.init_ui()
        # 设定左上角标题
        self.setWindowTitle("采购模块")
        # 设定左上角图标，图标png文件使用绝对路径
        file_path = 'D:/Python/ERP/ERP/cg/cg_ui/u102.png'
        icon = QIcon(file_path)
        self.setWindowIcon(icon)
        # 定义一个线程的状态
        self.thread_running = False

    # 一些初始化操作
    def init_ui(self):

        # 实例化Ui_cg_sector
        self.ui = Ui_cg_sector()
        self.ui.setupUi(self)

        # 现在可以直接绑定槽函数
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)

    # 识别当前窗口的槽函数，并跳转到相应页面的初始化函数
    @Slot()
    def tab_changed(self, x):
        print("Current Change: ", x+1)
        match x:
            case 0:
                self.init_requisition()
            case 1:
                self.init_order()
            case 2:
                self.init_recieve()
            case 3:
                self.init_supplier()
            case 4:
                self.init_query()
            case _:
                print("Unreasonable Error!!!")

    # 1.请购单接收页面
    def init_requisition(self):
        # 直接绑定函数
        self.ui.requisition_receipt_btn.clicked.connect(self.view_requisition_list)
        self.ui.requisition_accept_btn.clicked.connect(self.accept_requisition)

    # 2.采购订单页面
    def init_order(self):
        # TODO: 设定信号，绑定函数
        pass

    # 3.到货接收页面
    # TODO: 到货接收页面
    def init_recieve(self):
        # 直接绑定槽函数
        self.ui.receive_add.clicked.connect(self.receive_add_item)

    # 4.供应商管理与评价页面
    def init_supplier(self):
        # 连接数据库，因为有一个下拉菜单的内容需要访问数据库
        # 设定数据库类型
        self.supplier_database = QSqlDatabase.addDatabase("QSQLITE")
        # 链接数据库，采用相对路径访问
        filename = "D:/Python/ERP/ERP/cg/cg_db/Purchase Supplier.db"
        self.supplier_database.setDatabaseName(filename)
        # 打开数据库，顺便有一个错误处理
        if not self.supplier_database.open():
            print("Error: Could not open the database")

        # 设定信号，绑定函数
        # TODO: 写这个代码块的注释
        self.ui.supplier_choose_box.clear()
        self.supplier_query = QSqlQuery()
        self.supplier_query.exec("SELECT cg_supplier_name FROM cg_supplier_info")
        while self.supplier_query.next():
            data = self.supplier_query.value(0)
            self.ui.supplier_choose_box.addItem(data)
        self.ui.supplier_choose_box.show()

        self.ui.supplier_choose_box.currentTextChanged.connect(self.update_info)
        self.ui.supplier_list.clicked.connect(self.supplier_table_view)
        self.ui.supplier_evaluate.clicked.connect(self.supplier_evaluation)        

    # TODO: 采购业务页面的编写
    # 5.采购业务页面
    def init_query(self):
        self.ui.query_choose_btn.clicked.connect(self.query_table)

    # 以下是各个页面初始化后需要用到的一些槽函数操作
    # 已经按页面顺序和运行的顺序排好
    # 1的槽函数：点击按钮后接收请购单的方法
    def view_requisition_list(self):
        # 设定数据库类型
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        # 链接数据库
        filename = "D:/Python/ERP/ERP/cg/cg_db/Purchase List.db"
        self.database.setDatabaseName(filename)
        # 一个错误处理
        if not self.database.open():
            print("Error: Could not open the database")
        
        # TODO: 写这个代码块的注释
        # 设置tableView的模型以及表的名称
        self.model = QSqlTableModel(self, self.database)
        self.model.setTable('cg_purchase_list')

        self.model.setHeaderData(0, Qt.Horizontal, "采购请求号")
        self.model.setHeaderData(1, Qt.Horizontal, "计划分配号")
        self.model.setHeaderData(2, Qt.Horizontal, "备注")
        self.model.select()
        # 显示表格
        self.ui.requisition_table_view.setModel(self.model)
        self.ui.requisition_table_view.resizeColumnsToContents()

        # 嵌套了一个槽函数，对选择的行进行判断        
        self.selected_row = None
        self.ui.requisition_table_view.selectionModel().selectionChanged.connect(self.handle_selection_change)

    # TODO: 写这个代码块的注释
    # 1的槽函数：选择某行并返回索引
    # 已经在Qt Designer中设置好了每行数据只读，并且按行读，所以直接返回下标就可以
    @Slot()
    def handle_selection_change(self, selected):
        if selected.indexes():
            selected_row = selected.indexes()[0].row()
            self.selected_row = selected_row

    # TODO: 写这个代码块的注释，以及实现子线程函数操作
    # 1的槽函数：选择某行后再点击确认按钮，就执行此操作
    # 实现交互操作：点击某行，确认，就可以将请购单中的某行内容添加到内部的采购计划表中
    @Slot()
    def accept_requisition(self):
        if self.selected_row is not None:
            # You can now use self.selected_row to access the selected row
            print(f"Selected Row: {self.selected_row}")
        else:
            print("No row selected")

    # TODO: 完成代码
    # FIXME: 为什么这个代码会重复执行，然后一直叠加？
    # 3的槽函数，点击增加后，直接判断当前输入，然后把信息都加入到数据库文件中
    def receive_add_item(self):
        print("add item success!")

    # FIXME: 供应商页面有个bug，就是comboBox的内容会一直堆栈堆进去，缺一个初始化清空的操作
    # FIXME: 更多bug：所有控件的文本都没清空
    # FIXME: 产生两组列表以后点击评估按钮会闪退
    # TODO: 写这个代码块的注释
    # 4的槽函数：列举供应商信息
    def update_info(self):
        # 读取选取的供应商名字
        selected_supplier_name = self.ui.supplier_choose_box.currentText()
        # 相似的数据库访问操作
        supplier_query = QSqlQuery()
        supplier_query.prepare("SELECT * FROM cg_supplier_info WHERE cg_supplier_name = :supplier_name")
        supplier_query.bindValue(":supplier_name", selected_supplier_name)
        supplier_query.exec()

        # 对当前的供应商信息进行提取，从数据库取出来的数据与各控件对应
        if supplier_query.next():
            company_id = supplier_query.value(0)
            company_tel = supplier_query.value(2)
            company_address = supplier_query.value(3)
            remarks = supplier_query.value(4)

            self.ui.supplier_id.setText(f"{company_id}")
            self.ui.supplier_tel.setText(f"{company_tel}")
            self.ui.supplier_location.setText(f"{company_address}")
            self.ui.supplier_profile.setPlainText(remarks)

            # 同时，加载该供应商的logo图片，图片储存在cg_gr中
            self.load_supplier_logo(company_id)
    
    # TODO: 写这个代码块的注释
    # 4的槽函数：加载供应商的logo在控件self.supplier.logo中
    def load_supplier_logo(self, company_id):
        # 从上面传过来供应商id，并且在文件夹中找到同id的png文件
        logo_path = f"D:/Python/ERP/ERP/cg/cg_gr/{company_id}.png"
        
        logo_pixmap = QPixmap(logo_path)

        scene = QGraphicsScene()
        item = QGraphicsPixmapItem(logo_pixmap)
        scene.addItem(item)

        self.ui.supplier_logo.setScene(scene)

        del logo_pixmap
        del scene

    # TODO: 写这个代码块，考虑重新生成一张供货商的供货明细表
    # 4的槽函数：点击后显示该供应商的售货明细
    def supplier_table_view(self):
        # 设定数据库类型
        database = QSqlDatabase.addDatabase("QSQLITE")
        # 链接数据库
        filename = "D:/Python/ERP/ERP/cg/cg_db/Purchase List.db"
        database.setDatabaseName(filename)
        # 一个错误处理
        if not database.open():
            print("Error: Could not open the database")
        
        # TODO: 写这个代码块的注释
        # 设置tableView的模型以及表的名称
        try:
            self.model = QSqlTableModel(self, database)
            self.model.setTable('cg_purchase_list')

            self.model.setHeaderData(0, Qt.Horizontal, "采购请求号")
            self.model.setHeaderData(1, Qt.Horizontal, "计划分配号")
            self.model.setHeaderData(2, Qt.Horizontal, "备注")
            self.model.select()
            # 显示表格
            self.ui.supplier_table.setModel(self.model)
            self.ui.supplier_table.resizeColumnsToContents()
        finally:
            database.close()

    # TODO: 写这个代码块
    # FIXME: 调试后可以发现，是因为点击一次后线程已经在运行，点击第二次就会导致堆叠任务导致内存占用过多
    # 4的槽函数，点击后执行子线程，对该供应商进行综合评价，生成3张图标，显示在窗体中
    @Slot()
    def supplier_evaluation(self):
        if not self.thread_running:
            self.supplier_thread = supplier_eval()
            self.supplier_thread.image_generated.connect(self.supplier_diaplay_image)
            self.supplier_thread.finished.connect(self.on_thread_finished)
            self.supplier_thread.start()

            self.thread_running = True
        else:
            print(f"Evaluation is already in progress")

    # 不知道这个槽函数是否需要
    @Slot()
    def on_thread_finished(self):
        self.thread_running = False
        print("Thread finished.")


    # TODO: 写这个代码块
    # 4的槽函数，紧跟在supplier_evaluation后面，访问路径并显示图像    
    def supplier_diaplay_image(self, image_file_name):
        logo_path = image_file_name
        logo_pixmap = QPixmap(logo_path)

        scene = QGraphicsScene()
        item = QGraphicsPixmapItem(logo_pixmap)
        scene.addItem(item)

        self.ui.supplier_graphic_1.setScene(scene)

    # 5的槽函数，点击选择文件后，弹出选择文件的对话框，进行文件的选择
    # TODO: 可能需要优化一下界面以及交互
    def query_table(self):
        path, _ = QFileDialog.getOpenFileName(self, u"打开sqlite文件",os.getcwd(), "sqlite db(*.db)")
        if path:
            self.data_file = path
        filename = os.path.join(os.path.dirname(__file__),self.data_file)
        self.database.setDatabaseName(filename)

        if not self.database.open():
            print("Error: Could not open the database")

                # 设置tableView的模型以及表的名称
        self.model = QSqlTableModel(self, self.database)
        self.model.setTable('cg_purchase_list')

        self.model.select()
        # 显示表格
        self.ui.query_list_view.setModel(self.model)
        self.ui.query_list_view.resizeColumnsToContents() 

# TODO: 这里是子线程函数
# 4的子线程，在点击供应商评估后完成对供应商数据的计算，生成图表并展示在窗体上
class supplier_eval(QThread):
    # 自定义一个信号
    image_generated = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            image_file_name = "D:/Python/ERP/ERP/cg/cg_gr/40004001.png"

            self.image_generated.emit(image_file_name)
        except Exception as e:
            print(f"Exception during evaluation: {str(e)}")
        finally:
            self.quit()


"""     def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(self, u"打开sqlite文件",os.getcwd(), "sqlite db(*.db)")
        if path:
            self.data_file = path
        filename = os.path.join(os.path.dirname(__file__),self.data_file)
        self.database.setDatabaseName(filename)

        if not self.database.open():
            print("Error: Could not open the database")

                # 设置tableView的模型以及表的名称
        self.model = QSqlTableModel(self, self.database)
        self.model.setTable('cg_purchase_list')

        self.model.select()
        # 显示表格
        self.purchase_list_view.setModel(self.model)
        self.purchase_list_view.resizeColumnsToContents() """

if __name__ == '__main__':
    # 创建一个名为app的实例，代表应用本身，用于设置GUI并处理事件
    app = QApplication(sys.argv)
    # 实例化MyWindow
    widget = cg_widget()
    # 在屏幕上显示QWiget窗口
    widget.show()
    # 启动QApplication的循环，直到用户关闭窗口
    sys.exit(app.exec())