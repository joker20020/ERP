# 导入sys
import os.path
import sys

from PySide6.QtWidgets import QTableWidgetItem
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from ui import Ui_kcwidget
import sqlite3

'''
UPDATE：修改构造函数，将数据库文件作为参数传入，避免错误 line 25
'''

# 继承QWidget类，以获取其属性和方法
class MykcWidget(QWidget):
    def __init__(self,file_path):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_kcwidget()
        self.ui.setupUi(self)

        # 将数据库文件作为参数传入，避免错误
        self.file_path = file_path

        # self.chaxun()
        self.bindkc()
        self.bindruku()
        self.bindchuku()

    # 查询函数
    def chaxun(self):
        mode = self.ui.comboBox_chaxun.currentText()
        if mode == "大众自动钳":

            conn = sqlite3.connect(self.file_path)

            self.ui.lineEdit_chaxunid.setText("1")

            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "壳体2":
            self.ui.lineEdit_chaxunid.setText("2")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "支架1":
            self.ui.lineEdit_chaxunid.setText("3")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "配件":
            self.ui.lineEdit_chaxunid.setText("4")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "左壳体1":
            self.ui.lineEdit_chaxunid.setText("5")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "右壳体1":
            self.ui.lineEdit_chaxunid.setText("6")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "密封圈2":
            self.ui.lineEdit_chaxunid.setText("7")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "活塞1":
            self.ui.lineEdit_chaxunid.setText("8")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "塑料套1":
            self.ui.lineEdit_chaxunid.setText("9")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "橡胶套1":
            self.ui.lineEdit_chaxunid.setText("10")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "放气螺栓1":
            self.ui.lineEdit_chaxunid.setText("11")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "防尘帽1":
            self.ui.lineEdit_chaxunid.setText("12")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "内六角螺栓1":
            self.ui.lineEdit_chaxunid.setText("13")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "摩擦片2":
            self.ui.lineEdit_chaxunid.setText("14")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "隔垫1":
            self.ui.lineEdit_chaxunid.setText("15")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

        if mode == "开口导向套管2":
            self.ui.lineEdit_chaxunid.setText("16")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT quantity FROM products WHERE name = ?", (mode,))
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunshuliang.setText(str(product_value))

            cursor.close()
            conn.close()

    # 入库函数
    def ruku(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        cursor.execute('SELECT entry_time, product_id, quantity, operator FROM ruku LIMIT 16')
        rows = cursor.fetchall()

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        conn.close()

    # 出库函数
    def chuku(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        cursor.execute('SELECT exit_time, product_id, quantity, operator FROM chuku LIMIT 16')
        rows = cursor.fetchall()

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                self.ui.tableWidget_2.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        conn.close()

    def bindkc(self):
        self.ui.pushButton_chaxun.clicked.connect(self.chaxun)

    def bindruku(self):
        self.ui.pushButton_rukugx.clicked.connect(self.ruku)

    def bindchuku(self):
        self.ui.pushButton_chukugx.clicked.connect(self.chuku)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MykcWidget('./inventory.db')
    window.show()

    # 结束QApplication
    sys.exit(app.exec())
