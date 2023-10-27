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
from qfluentwidgets import RoundMenu,FluentIcon,Action,setTheme, Theme,InfoBar,InfoBarIcon,InfoBarPosition,NavigationItemPosition


from xt.code.xt_windows import XTMainWindow,XTLoginWindow

from cg.cg_widget import cg_widget as cgUI
from xs.xs_sql import MyWindow as xsUI
from jh.code.main_ui import JHWidget as jhUI
from kc.kc_main import MykcWidget as kcUI



class MainWindow(XTMainWindow):
    def __init__(self,authority,file_path,avatar,user_name,password,parent=None):
        super().__init__(authority,file_path,avatar,user_name,password,parent=parent)
        # setTheme(Theme.DARK)

        if authority & 8:
            self.cg = cgUI("cg/cg_db/Purchase Detail.db","cg/cg_db/Purchase List.db","cg/cg_db/Purchase Receipt.db","cg/cg_db/Purchase Supplier.db",)
            self.cg.setObjectName("cj")
            self.addSubInterface(self.cg, FluentIcon.MARKET, "采购管理", position=NavigationItemPosition.SCROLL)
        if authority & 16:
            self.jh = jhUI(self.user_name,"test.db","xs/lk.db","kc/inventory.db","cg/cg_db/Purchase Detail.db","jh/code/JHdatabase.db","test.db")
            self.jh.setObjectName("jh")
            self.addSubInterface(self.jh, FluentIcon.EDIT, "计划管理", position=NavigationItemPosition.SCROLL)
        if authority & 32:
            self.kc = kcUI("kc/inventory.db","test.db",self.user_name)
            self.kc.setObjectName("kc")
            self.addSubInterface(self.kc, FluentIcon.BOOK_SHELF, "库存管理", position=NavigationItemPosition.SCROLL)
        if authority & 64:
            self.xs = xsUI(self.user_name,"kc/inventory.db","test.db","xs/lk.db")
            self.xs.setObjectName("xs")
            self.addSubInterface(self.xs, FluentIcon.FEEDBACK, "销售管理", position=NavigationItemPosition.SCROLL)

        # self.navigationInterface.setCurrentItem("admin_wind")
        # self.stackedWidget.setCurrentIndex(0)


class LoginWindow(XTLoginWindow):
    def __init__(self,icon,background,file_path,title="login window"):
        super().__init__(icon,background,file_path,title)
        self.icon = icon

    def check(self):
        user = self.ui.userName.text()
        if user == "":
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
        if password == []:
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
            self.hide()
            authorities = self.xt.get_authority(user)
            authority = authorities[0][0]
            for each in authorities:
                authority |= each[0]
                # print(authority)
            self.mainWindow = MainWindow(authority, self.file_path,self.icon,user,password)
            self.user_name = user
            self.pwd = password
            self.mainWindow.logOut.out.triggered.connect(self.back)
            self.mainWindow.home.show_user(self.user_name,self.pwd)
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
    login = LoginWindow("res/logo.png","res/background.png","test.db",title="星言ERP")
    login.show()
    app.exec()