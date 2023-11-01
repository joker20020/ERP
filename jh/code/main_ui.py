# 导入sys
import sys
import os
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
sys.path.append(os.path.abspath("../../xt/code"))
sys.path.append(os.path.abspath("../../kc"))
from PySide6.QtWidgets import QApplication, QWidget, QApplication, QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
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
from datetime import date, datetime, timedelta
import time

from qfluentwidgets import InfoBar,InfoBarIcon,InfoBarPosition


from inventory import InventoryManager

'''
UPDATE:数据库路径修改为传入,修改日志数据库路径为传入，避免错误 line 33
'''


# 继承QWidget类，以获取其属性和方法
class JHWidget(QWidget):
    def __init__(self, user_name, xt_file, xs_file, kc_file, cg_file, file_path="JHdatabase.db", log_path ="../../test.db"):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.file_path = file_path
        self.xt_file = xt_file
        self.xs_file = xs_file
        self.kc_file = kc_file
        self.cg_file = cg_file
        self.log_path = log_path
        self.user_name = user_name

        # 数据库和日志库路径均改为传入参数
        self.jh_db = JHDataBase(self.user_name, file_path, xt_file, xs_file, kc_file, cg_file)

        self.log = XtContainer(1, log_path, user_name)

        self.jh_db.MPS_table("MPS_table")
        self.jh_db.MRP_table("MRP_table")
        self.jh_db.chejiancaigou_table("caigou_table")
        self.jh_db.chejianzuoye_table("zuoye_table")
        self.jh_db.paigong_table("paigong_table")
        self.jh_db.lingliao_table("lingliao_table")


        self.MPS = table_MPS1()
        self.MRP = table_MRP1()
        self.caigou = table_caigou1()
        self.chejianzuoye = table_chejianzuoye1()
        self.paigong = table_paigong1()
        self.lingliao = table_lingliao1()

        self.bind()
        # self.loadin()

    def jihua(self):
        try:

            self.jh_db.MRP_calculate()
            self.jh_db.caigou_cal()
            self.jh_db.chejianzuoye_cal()
            self.jh_db.paigong_cal()
            self.jh_db.lingliao_cal()

            InfoBar.success(
                title="计划成功",
                content="计划已生成",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=2000,  # won't disappear automatically
                parent=self
            )
        except Exception as e:
            print(e)
            InfoBar.error(
                title="计划失败",
                content="计划未生成",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=2000,  # won't disappear automatically
                parent=self
            )

    def update_MPS(self):

        try:
            for i in range(self.MPS.ui.tableWidget.rowCount()):
                p_id = self.MPS.ui.tableWidget.item(i, 0).text()
                amount = self.MPS.ui.tableWidget.item(i, 1).text()
                ddl = self.MPS.ui.tableWidget.item(i, 2).text()
                self.jh_db.sql_cmd(f"UPDATE MPS_table SET planned_amount={int(amount)} WHERE product_id = {int(p_id)} AND planned_deadline = {ddl}")
            InfoBar.success(
                title="修改成功",
                content="MPS修改已录入",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=2000,  # won't disappear automatically
                parent=self
            )
        except Exception as e:
            InfoBar.error(
                title="修改失败",
                content="MPS计划不变",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=2000,  # won't disappear automatically
                parent=self
            )




    def open(self):

        mode = self.ui.target.currentText()
        self.log.generate_log(OperationCode.JH_CHANGE)

        try:
            start = self.ui.start.date.toPython()
            ddl = self.ui.ddl.date.toPython()

        except ValueError as e:
            print(e)
            start = ""
            ddl = ""

        if mode == "MPS主生产计划":
            MPS = self.jh_db.find_info("MPS_table", [])
            row1 = len(MPS)

            if start == "":
                self.MPS.ui.tableWidget.setRowCount(row1)
                for i in range(row1):
                    for j in range(len(MPS[i])):
                        self.MPS.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(MPS[i][j])))
                self.MPS.show()
                return

            t = 0
            k = 0
            for i in range(row1):
                num_mon = int(MPS[i][2])
                num_year = int(time.localtime().tm_year)
                if num_mon in (1, 3, 5, 7, 8, 10, 12):
                    deadline = datetime.strptime(str(num_year)+'-'+str(num_mon)+'-31', "%Y-%m-%d").date()
                elif num_mon == 2:
                    if num_year % 400 == 0 or (num_year % 100 != 0 and num_year % 4 == 0):
                        deadline = datetime.strptime(str(num_year)+'-'+str(num_mon)+'-29', "%Y-%m-%d").date()
                    else:
                        deadline = datetime.strptime(str(num_year)+'-'+str(num_mon)+'-28', "%Y-%m-%d").date()
                else:
                    deadline = datetime.strptime(str(num_year)+'-'+str(num_mon)+'-30', "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        t = t+1

            self.MPS.ui.tableWidget.setRowCount(t)

            for i in range(row1):
                num_mon = int(MPS[i][2])
                num_year = int(time.localtime().tm_year)
                if num_mon in (1, 3, 5, 7, 8, 10, 12):
                    deadline = datetime.strptime(str(num_year) + '-' + str(num_mon) + '-31', "%Y-%m-%d").date()
                elif num_mon == 2:
                    if num_year % 400 == 0 or (num_year % 100 != 0 and num_year % 4 == 0):
                        deadline = datetime.strptime(str(num_year) + '-' + str(num_mon) + '-29', "%Y-%m-%d").date()
                    else:
                        deadline = datetime.strptime(str(num_year) + '-' + str(num_mon) + '-28', "%Y-%m-%d").date()
                else:
                    deadline = datetime.strptime(str(num_year) + '-' + str(num_mon) + '-30', "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        k = k+1
                        for j in range(len(MPS[i])):
                            self.MPS.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(MPS[i][j])))

            self.MPS.show()

        elif mode == "MRP物料需求计划":

            MRP = self.jh_db.find_info("MRP_table", [])
            row2 = len(MRP)

            if start == "":
                self.MRP.ui.tableWidget.setRowCount(row2)
                for i in range(row2):
                    for j in range(len(MRP[i])):
                        self.MRP.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(MRP[i][j])))
                self.MRP.show()
                return

            t = 0
            k = 0
            for i in range(row2):
                deadline = datetime.strptime(MRP[i][2], "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        t = t+1
            self.MRP.ui.tableWidget.setRowCount(t)

            for i in range(row2):
                deadline = datetime.strptime(MRP[i][2], "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        k = k+1
                        for j in range(len(MRP[i])):
                            self.MRP.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(MRP[i][j])))

            self.MRP.show()

        elif mode == "车间工作采购单":
            caigou = self.jh_db.find_info("caigou_table", [])
            row3 = len(caigou)

            if start == "":
                self.caigou.ui.tableWidget.setRowCount(row3)
                for i in range(row3):
                    for j in range(len(caigou[i])):
                        self.caigou.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(caigou[i][j])))
                self.caigou.show()
                return

            t = 0
            k = 0
            for i in range(row3):
                deadline = datetime.strptime(caigou[i][2], "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        t = t+1
            self.caigou.ui.tableWidget.setRowCount(t)

            for i in range(row3):
                deadline = datetime.strptime(caigou[i][2], "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        k = k+1
                        for j in range(len(caigou[i])):
                            self.caigou.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(caigou[i][j])))

            self.caigou.show()

        elif mode == "车间工作作业计划":
            zuoye = self.jh_db.find_info("zuoye_table", [])
            row4 = len(zuoye)

            if start == "":
                self.chejianzuoye.ui.tableWidget.setRowCount(row4)
                for i in range(row4):
                    for j in range(len(zuoye[i])):
                        self.chejianzuoye.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(zuoye[i][j])))
                self.chejianzuoye.show()
                return

            t = 0
            k = 0
            for i in range(row4):
                deadline = datetime.strptime(zuoye[i][3], "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        t = t+1
            self.chejianzuoye.ui.tableWidget.setRowCount(t)

            for i in range(row4):
                deadline = datetime.strptime(zuoye[i][3], "%Y-%m-%d").date()
                if deadline > start:
                    if deadline <= ddl:
                        k = k+1
                        for j in range(len(zuoye[i])):
                            self.chejianzuoye.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(zuoye[i][j])))

            self.chejianzuoye.show()

            # zuoye = self.jh_db.find_info("zuoye_table", ["product_id", "product_amount", "ddl_time"])
            # inventor_manager = InventoryManager(self.kc_file)
            # for i in range(len(zuoye)):
            #     inventor_manager.add_inventory(zuoye[i][2], zuoye[i][0], int(zuoye[i][1]), self.user_name)

        elif mode == "派工单":

            work_id = self.ui.workID.text()
            if work_id != "":
                paigong = self.jh_db.sql_cmd(f"SELECT * FROM paigong_table WHERE work_id LIKE '{work_id}-%'")
                self.paigong.ui.tableWidget.clearContents()
                row5 = len(paigong)

                if start == "":
                    self.paigong.ui.tableWidget.setRowCount(row5)
                    for i in range(row5):
                        for j in range(len(paigong[i])):
                            self.paigong.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(paigong[i][j])))
                    self.paigong.show()
                    return

                t = 0
                k = 0
                for i in range(row5):
                    deadline = datetime.strptime(paigong[i][4], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            t = t+1
                self.paigong.ui.tableWidget.setRowCount(t)

                for i in range(row5):
                    deadline = datetime.strptime(paigong[i][4], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            k = k + 1
                            for j in range(len(paigong[i])):
                                self.paigong.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(paigong[i][j])))

            else:
                paigong_table = self.jh_db.find_info("paigong_table", [])
                self.paigong.ui.tableWidget.clearContents()
                row5 = len(paigong_table)

                if start == "":
                    self.paigong.ui.tableWidget.setRowCount(row5)
                    for i in range(row5):
                        for j in range(len(paigong_table[i])):
                            self.paigong.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(paigong_table[i][j])))
                    self.paigong.show()
                    return

                t = 0
                k = 0
                for i in range(row5):
                    deadline = datetime.strptime(paigong_table[i][4], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            t = t+1
                self.paigong.ui.tableWidget.setRowCount(t)

                for i in range(row5):
                    deadline = datetime.strptime(paigong_table[i][4], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            k = k+1
                            for j in range(len(paigong_table[i])):
                                self.paigong.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(paigong_table[i][j])))

            self.paigong.show()

        elif mode == "领料单":
            work_id = self.ui.workID.text()
            if work_id != "":
                lingliao = self.jh_db.sql_cmd(f"SELECT * FROM lingliao_table WHERE work_id LIKE '{work_id}-%'")
                self.lingliao.ui.tableWidget.clearContents()
                row6 = len(lingliao)

                if start == "":
                    self.lingliao.ui.tableWidget.setRowCount(row6)
                    for i in range(row6):
                        for j in range(len(lingliao[i])):
                            self.lingliao.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(lingliao[i][j])))
                    self.lingliao.show()
                    return

                t = 0
                k = 0
                for i in range(row6):
                    deadline = datetime.strptime(lingliao[i][3], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            t = t+1
                self.lingliao.ui.tableWidget.setRowCount(t)

                for i in range(row6):
                    deadline = datetime.strptime(lingliao[i][3], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            k = k+1
                            for j in range(len(lingliao[i])):
                                self.lingliao.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(lingliao[i][j])))

            else:
                lingliao_table = self.jh_db.find_info("lingliao_table", [])
                self.lingliao.ui.tableWidget.clearContents()
                row6 = len(lingliao_table)

                if start == "":
                    self.lingliao.ui.tableWidget.setRowCount(row6)
                    for i in range(row6):
                        for j in range(len(lingliao_table[i])):
                            self.lingliao.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(lingliao_table[i][j])))
                    self.lingliao.show()
                    return

                t = 0
                k = 0
                for i in range(row6):
                    deadline = datetime.strptime(lingliao_table[i][3], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            t = t+1
                self.lingliao.ui.tableWidget.setRowCount(t)

                for i in range(row6):
                    deadline = datetime.strptime(lingliao_table[i][3], "%Y-%m-%d").date()
                    if deadline > start:
                        if deadline <= ddl:
                            k = k+1
                            for j in range(len(lingliao_table[i])):
                                self.lingliao.ui.tableWidget.setItem(k-1, j, QTableWidgetItem(str(lingliao_table[i][j])))
            self.lingliao.show()

            # lingliao = self.jh_db.find_info("lingliao_table", ["goods_id", "goods_amount", "needed_time"])
            # inventor_manager = InventoryManager(self.kc_file)
            # for i in range(len(lingliao)):
            #     inventor_manager.substact_inventory(lingliao[i][2], lingliao[i][0], int(lingliao[i][1]), self.user_name)

    def bind(self):
        self.ui.pushButton.clicked.connect(self.open)
        self.ui.pushButton_2.clicked.connect(self.jihua)
        self.MPS.ui.pushButton_2.clicked.connect(self.update_MPS)

    # def loadin(self):
        # MPS_table = self.jh_db.find_info("MPS_table", [])
        # self.MPS.ui.tableWidget.clearContents()
        # rows1 = len(MPS_table)
        # self.MPS.ui.tableWidget.setRowCount(rows1)
        # for i in range(rows1):
        #     for j in range(len(MPS_table[i])):
        #         self.MPS.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(MPS_table[i][j])))

        # MRP_table = self.jh_db.find_info("MRP_table", [])
        # self.MRP.ui.tableWidget.clearContents()
        # rows2 = len(MRP_table)
        # self.MRP.ui.tableWidget.setRowCount(rows2)
        # for i in range(rows2):
        #     for j in range(len(MRP_table[i])):
        #         self.MRP.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(MRP_table[i][j])))

        # caigou_table = self.jh_db.find_info("caigou_table", [])
        # self.caigou.ui.tableWidget.clearContents()
        # rows3 = len(caigou_table)
        # self.caigou.ui.tableWidget.setRowCount(rows3)
        # for i in range(rows3):
        #     for j in range(len(caigou_table[i])):
        #         self.caigou.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(caigou_table[i][j])))
        #
        # zuoye_table = self.jh_db.find_info("zuoye_table", [])
        # self.chejianzuoye.ui.tableWidget.clearContents()
        # rows4 = len(zuoye_table)
        # self.chejianzuoye.ui.tableWidget.setRowCount(rows4)
        # for i in range(rows4):
        #     for j in range(len(zuoye_table[i])):
        #         self.chejianzuoye.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(zuoye_table[i][j])))

        # paigong_table = self.jh_db.find_info("paigong_table", [])
        # self.paigong.ui.tableWidget.clearContents()
        # rows5 = len(paigong_table)
        # self.paigong.ui.tableWidget.setRowCount(rows5)
        # for i in range(rows5):
        #     for j in range(len(paigong_table[i])):
        #         self.paigong.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(paigong_table[i][j])))

        # lingliao_table = self.jh_db.find_info("lingliao_table", [])
        # self.lingliao.ui.tableWidget.clearContents()
        # rows6 = len(lingliao_table)
        # self.lingliao.ui.tableWidget.setRowCount(rows6)
        # for i in range(rows6):
        #     for j in range(len(lingliao_table[i])):
        #         self.lingliao.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(lingliao_table[i][j])))

class table_MPS1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_MPS()
        self.ui.setupUi(self)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

class table_MRP1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_MRP()
        self.ui.setupUi(self)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

class table_caigou1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_caigou()
        self.ui.setupUi(self)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

class table_chejianzuoye1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_chejianzuoye()
        self.ui.setupUi(self)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

class table_paigong1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_paigong()
        self.ui.setupUi(self)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

class table_lingliao1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = table_lingliao()
        self.ui.setupUi(self)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = JHWidget("lzj", "../../test.db", "../../xs/lk.db", "../../kc/inventory.db", "../../cg/cg_db/Purchase Detail.db")
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())