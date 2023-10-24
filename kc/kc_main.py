# 导入sys
import os.path
import sys


# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from ui import Ui_kcwidget
import sqlite3

# 继承QWidget类，以获取其属性和方法
class MykcWidget(QWidget):
    def __init__(self,file_path):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_kcwidget()
        self.ui.setupUi(self)
        self.file_path = file_path

        # self.chaxun()
        self.bindkc()

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

    def bindkc(self):
        self.ui.pushButton_chaxun.clicked.connect(self.chaxun)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MykcWidget('./inventory.db')
    window.show()

    # 结束QApplication
    sys.exit(app.exec())
