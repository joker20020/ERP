import copy
import sys
import os

sys.path.append(os.path.abspath("./cg"))
sys.path.append(os.path.abspath("./jh/code"))
sys.path.append(os.path.abspath("./kc"))
sys.path.append(os.path.abspath("./xs"))
sys.path.append(os.path.abspath("./xt/code"))


from PySide6.QtWidgets import QApplication, QWidget,QMessageBox, QTreeWidgetItem, QTableWidgetItem,QHeaderView
from PySide6.QtCore import Qt,Signal
from qfluentwidgets import RoundMenu,FluentIcon,Action,setTheme, Theme,InfoBar,InfoBarIcon,InfoBarPosition


from xt.code.windows import XTMainWindow,XTLoginWindow

from cg.cg_widget import MyWindow as cgUI

from jh.code.main_ui import MyWidget as jhUI


class MainWindow(XTMainWindow):
    def __init__(self,authority,file_path):
        super().__init__(authority,file_path)

        self.resize(800,600)
        # setTheme(Theme.DARK)

        self.cg = cgUI("cg/cg_db/Purchase List.db")
        self.jh = jhUI("jh/code/JHdatabase.db")

        self.addSubInterface(self.cg, FluentIcon.ALBUM, "采购管理")
        self.addSubInterface(self.jh, FluentIcon.ACCEPT, "计划管理")


        # self.navigationInterface.setCurrentItem("admin_wind")
        # self.stackedWidget.setCurrentIndex(0)

class LoginWindow(XTLoginWindow):
    def __init__(self,icon,background,file_path,title="login window"):
        super().__init__(icon,background,file_path,title)
        self.file_path = file_path
        self.bind()


    def bind(self):
        self.ui.login.clicked.connect(self.check)

    def check(self):
        user = self.ui.userName.text()
        if user=="":
            InfoBar.error(
                title='登录失败',
                content="用户名不能为空",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=2000,  # won't disappear automatically
                parent=self
            )
            return
        password = self.xt.get_pwd(user)
        if password==[]:
            InfoBar.error(
                title='登录失败',
                content="用户名不存在",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=2000,  # won't disappear automatically
                parent=self
            )
            return
        else:
            password = password[0][0]
        pwd = self.ui.password.text()
        if pwd == password:
            self.ui.userName.clear()
            self.ui.password.clear()
            self.close()
            authorities = self.xt.get_authority(user)
            authority = authorities[0][0]
            for each in authorities:
                authority &= each[0]
                print(authority)
            self.mainWindow = MainWindow(authority,self.file_path)
            self.mainWindow.show()
        else:
            InfoBar.error(
                title='登录失败',
                content="用户名或密码错误",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=2000,  # won't disappear automatically
                parent=self
            )




if __name__ == "__main__":
    app = QApplication()
    login = LoginWindow("res/logo.png","res/background.jpg","test.db")
    login.show()
    # main = MainWindow(7,"test.db")
    # main.show()
    app.exec()