"""import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Test")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(100, 100, 100, 40)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.button.setText("Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())"""

#框架
"""from PySide6.QtWidgets import QApplication, QMainWindow
# PySide6-uic demo.ui -o ui_demo.py
# from ui_demo import Ui_Demo


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = Ui_Demo()  # UI类的实例化()
        # self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出"""
"""from PySide6.QtWidgets import QApplication, QWidget,QLineEdit,QVBoxLayout
# PySide6-uic demo.ui -o ui_demo.py
from form import Ui_Form


class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MyWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出"""