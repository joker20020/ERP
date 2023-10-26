# 导入sys
import sys
import os
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
sys.path.append(os.path.abspath("../../xt/code"))
from PySide6.QtWidgets import QApplication, QWidget, QApplication, QTableWidget, QTableWidgetItem
# 导入我们生成的界面
from JH_SQL import JHDataBase
from window_chaxun import Ui_Form
from table_MPS import table_MPS
from table_MRP import table_MRP
from table_caigou import table_caigou
from table_chejianzuoye import table_chejianzuoye
from table_paigong import table_paigong
from table_lingliao import table_lingliao

from xt_container import XtContainer,OperationCode

'''
UPDATE:数据库路径修改为传入,修改日志数据库路径为传入，避免错误 line 33
'''


# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    def __init__(self, user_name,file_path="JHdatabase.db",log_path ="../../test.db" ):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 数据库和日志库路径均改为传入参数
        self.jh_db = JHDataBase(file_path)

        self.log = XtContainer(1,log_path,user_name)

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
        self.log.generate_log(OperationCode.JH_CHANGE)
        if mode == "MPS主生产计划":
            self.MPS.show()
        elif mode == "MRP物料需求计划":
            self.MRP.show()
        elif mode == "车间工作采购单":
            self.caigou.show()
        elif mode == "车间工作作业计划":
            self.chejianzuoye.show()
        elif mode == "派工单":
            self.paigong.show()
        elif mode == "领料单":
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
        rows2 = len(MRP_table)
        self.MRP.ui.tableWidget.setRowCount(rows2)
        for i in range(rows2):
            for j in range(len(MRP_table[i])):
                self.MRP.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(MRP_table[i][j])))

        caigou_table = self.jh_db.find_info("caigou_table", [])
        self.caigou.ui.tableWidget.clearContents()
        rows3 = len(caigou_table)
        self.caigou.ui.tableWidget.setRowCount(rows3)
        for i in range(rows3):
            for j in range(len(caigou_table[i])):
                self.caigou.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(caigou_table[i][j])))

        zuoye_table = self.jh_db.find_info("zuoye_table", [])
        self.chejianzuoye.ui.tableWidget.clearContents()
        rows4 = len(zuoye_table)
        self.chejianzuoye.ui.tableWidget.setRowCount(rows4)
        for i in range(rows3):
            for j in range(len(zuoye_table[i])):
                self.chejianzuoye.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(zuoye_table[i][j])))

        paigong_table = self.jh_db.find_info("paigong_table", [])
        self.paigong.ui.tableWidget.clearContents()
        rows5 = len(paigong_table)
        self.paigong.ui.tableWidget.setRowCount(rows5)
        for i in range(rows5):
            for j in range(len(caigou_table[i])):
                self.paigong.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(paigong_table[i][j])))

        lingliao_table = self.jh_db.find_info("lingliao_table", [])
        self.lingliao.ui.tableWidget.clearContents()
        rows6 = len(lingliao_table)
        self.lingliao.ui.tableWidget.setRowCount(rows6)
        for i in range(rows6):
            for j in range(len(lingliao_table[i])):
                self.lingliao.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(lingliao_table[i][j])))

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
    window = MyWidget("/Users/jackie/Documents/BUAA/Grade4fir/ERP/jh/code","lzj")
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
