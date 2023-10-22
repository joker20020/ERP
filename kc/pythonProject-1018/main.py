# 导入sys
import sys


# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from ui import Ui_kcwidget
import sqlite3

# 继承QWidget类，以获取其属性和方法
class MykcWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_kcwidget()
        self.ui.setupUi(self)

        self.chaxun()
        self.bindkc()

    def chaxun(self):
        mode = self.ui.comboBox_chaxun.currentText()
        if mode == "大众自动钳":
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()

            cursor.execute("SELECT product_ID FROM products LIMIT 1")
            row = cursor.fetchone()

            if row:
                product_value = row[0]
                self.ui.lineEdit_chaxunid.setText(str(product_value))

            cursor.close()
            conn.close()

    def bindkc(self):
        self.ui.pushButton_chaxun.clicked.connect(self.chaxun)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MykcWidget()
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
