import copy
import sys
import os


# sys.path.append(os.path.abspath("./cg"))
# sys.path.append(os.path.abspath("./"))
# print(sys.path)


from PySide6.QtWidgets import QApplication, QWidget, QTreeWidgetItem, QTableWidgetItem,QHeaderView
from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QIcon,QPixmap
from qfluentwidgets import RoundMenu,FluentWindow,FluentIcon,Action,NavigationItemPosition,NavigationPushButton,NavigationTreeWidget,SplitTitleBar,MessageBox,InfoBar,InfoBarIcon,InfoBarPosition
from qframelesswindow import AcrylicWindow
from graphviz import Graph

if __name__ == "__main__":
    from ui.BomUI import Ui_Bom
    from ui.LineUI import Ui_Line
    from ui.AdminUI import Ui_Admin
    from ui.BomCreateUI import Ui_BomCreate
    from ui.AddGroupUI import Ui_AddGroup
    from ui.AddCharacterUI import Ui_AddCharacter
    from ui.AddWorkerUI import Ui_AddWorker
    from ui.LoginUI import Ui_Login
    from ui.HomeUI import Ui_HomePage
    from xt_container import XtContainer, AuthorityError
else:
    from .ui.BomUI import Ui_Bom
    from .ui.LineUI import Ui_Line
    from .ui.AdminUI import Ui_Admin
    from .ui.BomCreateUI import Ui_BomCreate
    from .ui.AddGroupUI import Ui_AddGroup
    from .ui.AddCharacterUI import Ui_AddCharacter
    from .ui.AddWorkerUI import Ui_AddWorker
    from .ui.LoginUI import Ui_Login
    from .ui.HomeUI import Ui_HomePage
    from .xt_container import XtContainer,AuthorityError


def BOOL(data):
    data = str(data)
    if data.upper() == "YES" or data == "是" or data == "1" or data.upper() == "TRUE":
        return True
    return False

class BomCreateWindow(QWidget):
    closed = Signal()
    def __init__(self,container,parent=None):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_BomCreate()
        self.ui.setupUi(self)
        self.container = container
        self.name = ""
        self.parent = parent
        self.bind()

    def bind(self):
        self.ui.bomCreate.clicked.connect(self.create_bom)


    def create_bom(self):
        try:
            self.name = self.ui.bomCreateName.text()
            if self.name != "":
                self.container.create_bom(self.name)
                self.closed.emit()
                self.ui.bomCreateName.setText("")
                self.close()
            else:
                self.close()
        except AuthorityError as e:
            self.close()
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self.parent).exec()

class BomWindow(QWidget):
    def __init__(self,authority,user_name,parent=None,file_path="test.db"):
        super().__init__(parent=parent)
        # 设置界面为我们生成的界面
        self.ui = Ui_Bom()
        self.ui.setupUi(self)
        self.xt = XtContainer(authority,file_path,user_name)
        self.bcw = BomCreateWindow(self.xt,parent=self)
        self.lineWindow = LineWindow(self.xt)
        self.ui.bomList.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.draw_action = Action(text="输出树状图")

        self.head = ["ID","bom层级","零件名称","父零件ID","零件成本","零件生产周期","是否外购","注释"]

        self.ui.bomTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Custom)

        self.data_type = [int,int,str,int,float,float,BOOL,str]
        # self.refresh_boms()
        self.bind()

    def bind(self):

        self.ui.bomTable.customContextMenuRequested.connect(self.show_menu)
        self.ui.bomList.customContextMenuRequested.connect(self.show_draw)
        self.ui.bomNew.clicked.connect(self.create_bom)
        self.ui.bomRefresh.clicked.connect(self.refresh_boms)
        self.ui.bomRemove.clicked.connect(self.remove_bom)
        self.ui.partNew.triggered.connect(self.add_bom)
        self.ui.partRemove.triggered.connect(self.del_bom)
        self.ui.openLine.triggered.connect(self.open_line)
        self.ui.bomList.currentItemChanged.connect(self.show_bom)
        self.ui.bomUpdate.clicked.connect(self.sync_bom)
        self.bcw.closed.connect(self.refresh_boms)
        self.ui.bomInput.searchSignal.connect(self.find_bom)
        self.draw_action.triggered.connect(self.draw_tree)

    def draw_tree(self):
        if self.ui.bomList.currentItem():
            bom_name = self.ui.bomList.currentItem().text()
            tree = Graph(bom_name,format="svg")
            boms = self.xt.get_in_bom(bom_name)
            root = [0]
            temp = copy.deepcopy(boms)
            while root != []:
                finish = len(root)
                for bom in boms:
                    if bom[3] in root:
                        if bom[3]==0:
                            root.append(bom[0])
                            tree.node(bom[2])
                            temp.remove(bom)
                        else:
                            root.append(bom[0])
                            tree.node(bom[2])
                            tree.edge(boms[bom[3]-1][2],bom[2])
                            temp.remove(bom)
                root = root[finish:]
                boms = temp
            tree.render(filename=bom_name,view=True)
        else:
            InfoBar.error(
                title='BOM树导出',
                content="BOM树导出失败，请检查选择的BOM表",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,  # won't disappear automatically
                parent=self
            )

    def show_draw(self,pos):
        menu = RoundMenu(self.ui.bomList)
        menu.addAction(self.draw_action)
        menu.exec(self.ui.bomList.mapToGlobal(pos))


    def show_menu(self,pos):
        menu = RoundMenu(self.ui.bomTable)
        menu.addAction(self.ui.partNew)
        menu.addAction(self.ui.partRemove)
        menu.addAction(self.ui.openLine)
        menu.exec(self.ui.bomTable.mapToGlobal(pos))

    """
    以下为对BOM表的操作
    """
    def create_bom(self):
        self.bcw.show()

    def remove_bom(self):
        try:
            name = self.ui.bomList.currentItem().text()
            self.xt.remove_boms(name)
            self.refresh_boms()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def refresh_boms(self):
        try:
            boms = self.xt.find_boms()
            self.ui.bomList.clear()
            for bom in boms:
                bom = bom[0][7:]
                self.ui.bomList.addItem(bom)
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def find_bom(self,text):
        try:
            self.ui.bomList.clear()
            boms = self.xt.find_bom(text)
            for bom in boms:
                bom = bom[0][7:]
                self.ui.bomList.addItem(bom)
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def add_bom(self):
        self.ui.bomTable.setRowCount(self.ui.bomTable.rowCount()+1)
        for i in range(self.ui.bomTable.columnCount()):
            self.ui.bomTable.setItem(self.ui.bomTable.rowCount() - 1,i,QTableWidgetItem(""))
        if self.ui.bomTable.rowCount() == 1:
            ids = self.xt.production.db.find_info("line",["LINE_ID"],LINE_ID="ASC")
            if ids == []:
                self.ui.bomTable.setItem(self.ui.bomTable.rowCount() - 1, 0, QTableWidgetItem("1"))
            else:
                ids = ids[-1][0]
                self.ui.bomTable.setItem(self.ui.bomTable.rowCount() - 1, 0, QTableWidgetItem(str(ids+1)))
            return
        self.ui.bomTable.setItem(self.ui.bomTable.rowCount()-1, 0, QTableWidgetItem(str(
            int(self.ui.bomTable.item(self.ui.bomTable.rowCount()-2,0).text())+1
        )))

    def del_bom(self):
        try:
            id = int(self.ui.bomTable.item(self.ui.bomTable.currentRow(), 0).text())
            self.ui.bomTable.removeRow(self.ui.bomTable.currentRow())
            name = self.ui.bomList.currentItem().text()
            self.xt.delete_bom(name,id)
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def show_bom(self,current,previous):
        if not current:
            return
        name = current.text()
        parts = self.xt.get_in_bom(name)
        self.ui.bomTable.clearContents()
        rows = len(parts)
        self.ui.bomTable.setRowCount(rows)
        for i in range(rows):
            for j in range(len(parts[i])):
                if parts[i][j] or parts[i][j]==0:
                    self.ui.bomTable.setItem(i,j,QTableWidgetItem(str(self.data_type[j](parts[i][j]))))
                else:
                    self.ui.bomTable.setItem(i, j, QTableWidgetItem(""))

    def sync_bom(self):
        try:
            name = self.ui.bomList.currentItem().text()
            if name == None:
                return
            data = []

            for i in range(self.ui.bomTable.rowCount()):
                # for j in range(self.ui.bomTable.columnCount()):
                #     print(self.ui.bomTable.item(i,j))
                #     print(self.ui.bomTable.item(i, j).text())
                data.append([self.data_type[j](self.ui.bomTable.item(i,j).text()) if self.ui.bomTable.item(i,j).text() else "" for j in range(self.ui.bomTable.columnCount())])
            self.xt.update_bom(name,data)
            self.show_bom(self.ui.bomList.currentItem(),None)
        except ValueError as e:
            MessageBox("数据错误","非空检验失败，请填写非空列后再同步",self).exec()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    """
    以下为对工艺路线表操作
    """

    def open_line(self):
        if not self.ui.bomTable.currentItem():
            return

        self.lineWindow.bom_name = self.ui.bomList.currentItem().text()
        self.lineWindow.bom_id = self.ui.bomTable.item(self.ui.bomTable.currentRow(),0).text()
        self.lineWindow.refresh_line()
        self.lineWindow.show()


class LineWindow(QWidget):
    def __init__(self,container:XtContainer):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Line()
        self.ui.setupUi(self)
        self.container = container
        self.bom_name = ""
        self.bom_id = ""
        self.Ldata_type = [int,str,str,str]
        self.Wdata_type = [int,int,str,str,int]

        self.ui.lineTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.workTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)



        self.bind()
        self.setWindowModality(Qt.WindowModality.WindowModal.ApplicationModal)

    def bind(self):
        self.ui.lineNew.clicked.connect(self.add_line)
        self.ui.lineRemove.clicked.connect(self.del_line)
        self.ui.lineRefresh.clicked.connect(self.refresh_line)
        self.ui.lineUpdate.clicked.connect(self.sync_line)
        self.ui.workNew.clicked.connect(self.add_work)
        self.ui.workRemove.clicked.connect(self.del_work)
        self.ui.workUpdate.clicked.connect(self.sync_work)
        self.ui.lineTable.itemClicked.connect(self.refresh_work)
        self.ui.lineEdit.searchSignal.connect(self.find_lines)

    """
    以下为对工艺路线操作
    """

    def refresh_line(self):
        lines = self.container.get_lines(self.bom_name,self.bom_id)
        self.ui.lineTable.clearContents()
        rows = len(lines)
        self.ui.lineTable.setRowCount(rows)
        for i in range(rows):
            for j in range(len(lines[i])):
                if lines[i][j]:
                    self.ui.lineTable.setItem(i, j, QTableWidgetItem(str(self.Ldata_type[j](lines[i][j]))))
                else:
                    self.ui.lineTable.setItem(i, j, QTableWidgetItem(""))

    def find_lines(self,text):
        lines = self.container.find_lines(self.bom_name,self.bom_id,text)
        self.ui.lineTable.clearContents()
        rows = len(lines)
        self.ui.lineTable.setRowCount(rows)
        for i in range(rows):
            for j in range(len(lines[i])):
                if lines[i][j]:
                    self.ui.lineTable.setItem(i, j, QTableWidgetItem(str(self.Ldata_type[j](lines[i][j]))))
                else:
                    self.ui.lineTable.setItem(i, j, QTableWidgetItem(""))

    def add_line(self):
        self.ui.lineTable.setRowCount(self.ui.lineTable.rowCount() + 1)
        for i in range(self.ui.lineTable.columnCount()):
            self.ui.lineTable.setItem(self.ui.lineTable.rowCount() - 1,i,QTableWidgetItem(""))

        if self.ui.lineTable.rowCount() == 1:
            ids = self.container.production.db.find_info("line",["LINE_ID"],LINE_ID="ASC")
            if ids == []:
                self.ui.lineTable.setItem(self.ui.lineTable.rowCount() - 1, 0, QTableWidgetItem("1"))
            else:
                ids = ids[-1][0]
                self.ui.lineTable.setItem(self.ui.lineTable.rowCount() - 1, 0, QTableWidgetItem(str(ids+1)))
            return
        self.ui.lineTable.setItem(self.ui.lineTable.rowCount() - 1, 0, QTableWidgetItem(str(
            int(self.ui.lineTable.item(self.ui.lineTable.rowCount() - 2, 0).text()) + 1
        )))

    def del_line(self):
        id = int(self.ui.lineTable.item(self.ui.lineTable.currentRow(), 0).text())
        self.ui.lineTable.removeRow(self.ui.lineTable.currentRow())
        self.container.del_line(id)

    def sync_line(self):
        try:
            data = []
            for i in range(self.ui.lineTable.rowCount()):
                # for j in range(self.ui.bomTable.columnCount()):
                #     print(self.ui.bomTable.item(i,j))
                #     print(self.ui.bomTable.item(i, j).text())
                data.append(
                    [self.Ldata_type[j](self.ui.lineTable.item(i, j).text()) if self.ui.lineTable.item(i, j).text() else "" for
                     j in range(self.ui.lineTable.columnCount())])
            self.container.update_line(self.bom_name,self.bom_id, data)
            self.refresh_line()
        except ValueError as e:
            MessageBox("数据错误","非空检验失败，请填写非空列后再同步",self).exec()

    """
    以下为对工序操作
    """
    def refresh_work(self,item):
        a = item.row()
        b = self.ui.lineTable.currentRow()
        if item == None :  # or (item.row() == self.ui.lineTable.currentRow()and item.row()!=0)
            return
        works = self.container.get_works(self.ui.lineTable.item(self.ui.lineTable.currentRow(), 0).text())
        self.ui.workTable.clearContents()
        rows = len(works)
        self.ui.workTable.setRowCount(rows)
        for i in range(rows):
            for j in range(len(works[i])):
                if works[i][j]:
                    self.ui.workTable.setItem(i, j, QTableWidgetItem(str(self.Wdata_type[j](works[i][j]))))
                else:
                    self.ui.workTable.setItem(i, j, QTableWidgetItem(""))

    def add_work(self):
        self.ui.workTable.setRowCount(self.ui.workTable.rowCount() + 1)
        for i in range(self.ui.workTable.columnCount()):
            self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1,i,QTableWidgetItem(""))
        if self.ui.workTable.rowCount() == 1:
            self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1, 0, QTableWidgetItem("1"))
            self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1, 4, QTableWidgetItem(
                self.ui.lineTable.item(self.ui.lineTable.currentRow(), 0).text()))
            return
        self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1, 0, QTableWidgetItem(str(
            int(self.ui.workTable.item(self.ui.workTable.rowCount() - 2, 0).text()) + 1
        )))
        self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1,4,QTableWidgetItem(self.ui.lineTable.item(self.ui.lineTable.currentRow(),0).text()))

    def del_work(self):
        id = int(self.ui.workTable.item(self.ui.workTable.currentRow(), 0).text())
        self.ui.workTable.removeRow(self.ui.workTable.currentRow())
        self.container.del_work(self.ui.lineTable.item(self.ui.lineTable.currentRow(),0).text(),id)

    def sync_work(self):
        try:
            data = []
            for i in range(self.ui.workTable.rowCount()):
                if self.ui.workTable.item(i, 4).text() != self.ui.lineTable.item(self.ui.lineTable.currentRow(),0).text():
                    return
                data.append(
                    [self.Wdata_type[j](self.ui.workTable.item(i, j).text()) if self.ui.workTable.item(i, j).text() else "" for
                     j in range(self.ui.workTable.columnCount())])
            self.container.update_work(self.ui.lineTable.item(self.ui.lineTable.currentRow(), 0).text(),data)
        except ValueError as e :
            MessageBox("数据错误","非空检验失败，请填写非空列后再同步",self).exec()


class AddGroupWindow(QWidget):
    success = Signal()
    def __init__(self,container:XtContainer):
        super().__init__()
        self.ui = Ui_AddGroup()
        self.ui.setupUi(self)
        self.container = container
        self.bind()

    def bind(self):
        self.ui.ok.clicked.connect(self.add)

    def add(self):
        # print([self.ui.groupName.text(),self.ui.groupFather.currentText(),self.ui.groupDes.toPlainText()])
        try:
            self.container.add_group([self.ui.groupName.text(),self.ui.groupFather.currentText(),self.ui.groupDes.toPlainText()])
            self.success.emit()
            self.clear_all()
            self.close()
        except ValueError as e:
            MessageBox("数据错误","非空检验失败，请填写非空列后再同步",self).exec()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def clear_all(self):
        self.ui.groupName.clear()
        self.ui.groupFather.setCurrentIndex(0)
        self.ui.groupDes.clear()

    def refresh_combo(self):
        groups = self.container.get_groups()
        fathers = ["root"]
        for group in groups:
            if group[0] not in fathers:
                fathers.append(group[0])
        self.ui.groupFather.clear()
        self.ui.groupFather.addItems(fathers)

class AddCharacterWindow(QWidget):
    success = Signal()
    def __init__(self,container:XtContainer):
        super().__init__()
        self.ui = Ui_AddCharacter()
        self.ui.setupUi(self)
        self.container = container
        self.setWindowModality(Qt.WindowModality.WindowModal.ApplicationModal)
        self.bind()

    def bind(self):
        self.ui.ok.clicked.connect(self.add)

    def add(self):
        # print([self.ui.groupName.text(),self.ui.groupFather.currentText(),self.ui.groupDes.toPlainText()])
        try:
            self.container.new_character([self.ui.characterName.text(),int(self.ui.characterAuthority.text())])
            self.success.emit()
            self.clear_all()
            self.close()
        except ValueError as e:
            MessageBox("数据错误","非空检验失败，请填写非空列后再同步",self).exec()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def clear_all(self):
        self.ui.characterName.clear()
        self.ui.characterAuthority.setValue(0)

class AddWorkerWindow(QWidget):
    success = Signal()
    def __init__(self,container:XtContainer):
        super().__init__()
        self.ui = Ui_AddWorker()
        self.ui.setupUi(self)
        self.container = container
        self.bind()

    def bind(self):
        self.ui.ok.clicked.connect(self.add)

    def add(self):
        # print([self.ui.groupName.text(),self.ui.groupFather.currentText(),self.ui.groupDes.toPlainText()])
        try:
            self.container.add_worker(self.ui.workerGroup.currentText(),self.ui.workerCharacter.currentText(),[self.ui.workerName.text(),int(self.ui.workerAge.text()),self.ui.workerGender.text(),self.ui.workerPlace.text(),self.ui.workerUserName.text(),self.ui.workerPassword.text()])
            self.success.emit()
            self.clear_all()
            self.close()
        except ValueError as e:
            MessageBox("数据错误","非空检验失败，请填写非空列后再同步",self).exec()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def clear_all(self):
        self.ui.workerName.clear()
        self.ui.workerAge.clear()
        self.ui.workerGender.clear()
        self.ui.workerPlace.clear()
        self.ui.workerUserName.clear()
        self.ui.workerPassword.clear()
        self.ui.workerGroup.setCurrentIndex(0)
        self.ui.workerCharacter.setCurrentIndex(0)

    def refresh_combo(self):
        self.ui.workerGroup.clear()
        groups = self.container.get_groups()
        for i in range(len(groups)):
            groups[i] = groups[i][0]
        self.ui.workerGroup.addItems(groups)

        self.ui.workerCharacter.clear()
        characters = self.container.get_characters()
        for i in range(len(characters)):
            characters[i] = characters[i][0]
        self.ui.workerCharacter.addItems(characters)

class AdminWindow(QWidget):
    def __init__(self,authority,user_name,file_path="test.db"):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Admin()
        self.ui.setupUi(self)
        self.ui.refresh.setIcon(FluentIcon.SYNC)
        self.xt = XtContainer(authority,file_path,user_name)
        self.add_group = AddGroupWindow(self.xt)
        self.new_character = AddCharacterWindow(self.xt)
        self.add_worker = AddWorkerWindow(self.xt)
        self.bind()

    def bind(self):
        self.ui.groupNew.clicked.connect(self.open_group_window)
        self.ui.groupRemove.clicked.connect(self.del_group)
        self.ui.characterNew.clicked.connect(self.open_character_window)
        self.ui.characterDelete.clicked.connect(self.del_character)
        self.ui.characterRemove.clicked.connect(self.rem_character)
        self.ui.characterAdd.clicked.connect(self.add_character)
        self.ui.workerNew.clicked.connect(self.open_worker_window)
        self.ui.workerRemove.clicked.connect(self.del_worker)
        self.ui.workerUpdate.clicked.connect(self.update_worker)
        self.ui.groupTree.itemClicked.connect(self.show_worker)
        self.ui.refresh.clicked.connect(self.refresh_all)
        self.add_group.success.connect(self.refresh_group)
        self.add_group.success.connect(self.refresh_combo)
        self.new_character.success.connect(self.refresh_character)
        self.new_character.success.connect(self.refresh_combo)
        self.add_worker.success.connect(self.refresh_character)
        self.add_worker.success.connect(self.refresh_group)


    """
    以下为组织关系树操作
    """
    def open_group_window(self):
        try:
            self.add_group.refresh_combo()
            self.add_group.show()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def open_character_window(self):
        self.new_character.show()

    def open_worker_window(self):
        try:
            self.add_worker.refresh_combo()
            self.add_worker.show()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def add_character(self):
        worker_id = int(self.ui.workerID.text())
        character = self.ui.workerCharacter.currentText()
        self.xt.add_character([worker_id,character])
        self.refresh_character()

    def show_worker(self,item):
        if not item or item.text(2)=="":
            return
        self.refresh_combo()
        worker_id = int(self.ui.groupTree.currentItem().text(2))
        worker = self.xt.get_worker(worker_id)[0]
        if item.parent():
            group = item.parent().text(0)
        else:
            group = "root"
        self.ui.workerID.setText(str(worker[0]))
        self.ui.workerName.setText(str(worker[1]))
        self.ui.workerAge.setText(str(worker[2]))
        self.ui.workerGender.setText(str(worker[3]))
        self.ui.workerPlace.setText(str(worker[4]))
        self.ui.workerGroup.setCurrentText(group)
        self.ui.workerUserName.setText(str(worker[5]))
        self.ui.workerPassword.setText(str(worker[6]))
        self.refresh_character()


    def refresh_group(self):
        self.ui.groupTree.clear()
        groups = self.xt.get_groups()
        root = ["root"]
        temp = copy.deepcopy(groups)
        workers = self.xt.get_worker_group("root")
        for worker in workers:
            witem = QTreeWidgetItem(self.ui.groupTree)
            witem.setText(0, worker[1])
            witem.setText(1, "人员")
            witem.setText(2, str(worker[0]))
            self.ui.groupTree.addTopLevelItem(witem)
        while root != []:
            finish = len(root)
            for group in groups:
                if group[1] in root:
                    if group[1] == "root":
                        root.append(group[0])
                        item = QTreeWidgetItem(self.ui.groupTree)
                        item.setText(0,group[0])
                        item.setText(1, "组织")
                        self.ui.groupTree.addTopLevelItem(item)
                        workers = self.xt.get_worker_group(group[0])
                        for worker in workers:
                            witem = QTreeWidgetItem(item)
                            witem.setText(0, worker[1])
                            witem.setText(1, "人员")
                            witem.setText(2, str(worker[0]))
                            item.addChild(witem)
                        temp.remove(group)
                    else:
                        root.append(group[0])
                        items = [self.ui.groupTree.topLevelItem(i) for i in range(self.ui.groupTree.topLevelItemCount())]
                        father = None
                        for item in items:
                            father = self.__get_tree_item__(group[1],item)
                            if father:
                                break
                        if not father:
                            continue
                        item = QTreeWidgetItem(father)
                        item.setText(0, group[0])
                        item.setText(1, "组织")
                        father.addChild(item)
                        workers = self.xt.get_worker_group(group[0])
                        for worker in workers:
                            witem = QTreeWidgetItem(item)
                            witem.setText(0, worker[1])
                            witem.setText(1, "人员")
                            witem.setText(2, str(worker[0]))
                            item.addChild(witem)
                        temp.remove(group)
                        # print(father.text(0))
            root = root[finish:]
            groups = copy.deepcopy(temp)

    def refresh_character(self):
        self.ui.characterList.clear()
        user_id = self.ui.workerID.text()
        if user_id == "":
            characters = self.xt.get_characters()
        else:
            characters = self.xt.get_characters(user_id)
            # print(characters)
        for each in characters:
            self.ui.characterList.addItem(each[0])

    def refresh_combo(self):
        self.ui.workerGroup.clear()
        groups = self.xt.get_groups()
        for i in range(len(groups)):
            groups[i] = groups[i][0]
        self.ui.workerGroup.addItems(groups)

        self.ui.workerCharacter.clear()
        characters = self.xt.get_characters()
        for i in range(len(characters)):
            characters[i] = characters[i][0]
        self.ui.workerCharacter.addItems(characters)

    def refresh_all(self):
        try:
            self.refresh_group()
            self.refresh_character()
            self.refresh_combo()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def clear_all(self):
        self.ui.workerName.clear()
        self.ui.workerAge.clear()
        self.ui.workerGender.clear()
        self.ui.workerPlace.clear()
        self.ui.workerUserName.clear()
        self.ui.workerPassword.clear()
        self.ui.workerGroup.setCurrentIndex(0)
        self.ui.workerCharacter.setCurrentIndex(0)

    def del_group(self):
        self.del_tree(self.ui.groupTree.currentItem())
        self.refresh_group()

    def rem_character(self):
        try:
            character = self.ui.workerCharacter.currentText()
            self.xt.rem_character(character)
            self.refresh_character()
            self.refresh_combo()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def del_character(self):
        try:
            character = self.ui.characterList.currentItem().text()
            worker_id = int(self.ui.workerID.text())
            self.xt.del_character(worker_id,character)
            self.refresh_character()
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def del_worker(self):
        worker_id = int(self.ui.workerID.text())
        self.xt.del_worker(worker_id)
        self.refresh_group()
        self.clear_all()


    def update_worker(self):
        worker_id = int(self.ui.workerID.text())
        data = [self.ui.workerName.text(),int(self.ui.workerAge.text()),self.ui.workerGender.text(),self.ui.workerPlace.text(),self.ui.workerUserName.text(),self.ui.workerPassword.text()]
        self.xt.update_worker(worker_id,data)
        self.xt.update_worker_group(worker_id,self.ui.workerGroup.currentText())
        self.show_worker(self.ui.groupTree.currentItem())
        self.refresh_group()


    def __get_tree_item__(self,text:str,root:QTreeWidgetItem):
        if root.text(0) == text:
            return root
        for each in [root.child(i) for i in range(root.childCount())]:
            return self.__get_tree_item__(text,each)
        return None

    def del_tree(self,root:QTreeWidgetItem):
        for each in [root.child(i) for i in range(root.childCount())]:
            return self.del_tree(each)
        if root.text(1) == "组织":
            self.xt.del_group(root.text(0))
        elif root.text(1) == "人员":
            self.xt.update_worker_root(root.text(2))

class LogOut(NavigationPushButton):

    def __init__(self, parent=None):
        super().__init__(FluentIcon.SETTING,"用户设置",isSelectable=False, parent=parent)
        self.out = Action(text="退出登录")
        self.log = Action(text="导出操作日志")


    def show_info(self) -> None:

        menu = RoundMenu()
        menu.addAction(self.out)
        menu.addAction(self.log)
        menu.exec(self.parent().mapToGlobal(self.pos()))

class HomeWindow(QWidget):
    pwdChanged = Signal(str,str)
    def __init__(self,authority,user_name,password,avatar="logo.png",file_path="test.db",parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.xt = XtContainer(authority, file_path,user_name)

        self.ui.avater.setPixmap(QPixmap(avatar).scaled(self.ui.avater.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        self.ui.userName.setDisabled(True)
        self.ui.logTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.logRemove.setIcon(FluentIcon.DELETE)

        self.query_menu = RoundMenu(parent=self)
        self.query_year_action = Action(text="年查询",triggered=lambda b=self.ui.query: b.setText("年查询"))
        self.query_month_action = Action(text="年月查询", triggered=lambda b=self.ui.query: b.setText("年月查询"))
        self.query_day_action = Action(text="年月日查询", triggered=lambda b=self.ui.query: b.setText("年月日查询"))
        self.query_hour_action = Action(text="y-m-d-h查询", triggered=lambda b=self.ui.query: b.setText("y-m-d-h查询"))
        self.query_minute_action = Action(text="y-m-d-h-m查询", triggered=lambda b=self.ui.query: b.setText("y-m-d-h-m查询"))
        self.query_second_action = Action(text="y-m-d-h-m-s查询", triggered=lambda b=self.ui.query: b.setText("y-m-d-h-m-s查询"))


        self.query_menu.addAction(self.query_year_action)
        self.query_menu.addAction(self.query_month_action)
        self.query_menu.addAction(self.query_day_action)
        self.query_menu.addAction(self.query_hour_action)
        self.query_menu.addAction(self.query_minute_action)
        self.query_menu.addAction(self.query_second_action)

        self.ui.query.setFlyout(self.query_menu)
        self.ui.time.setSecondVisible(True)

        self.user_name = user_name
        self.pwd = password

        self.bind()


    def bind(self):
        self.ui.passwordChange.clicked.connect(self.change_pwd)
        self.ui.query.clicked.connect(self.query_log)
        self.ui.logRemove.clicked.connect(self.delete_log)


    def show_user(self,user_name,pwd):
        self.ui.userName.setText(user_name)
        self.ui.password.setText(pwd)


    def change_pwd(self):
        try:
            user_name = self.ui.userName.text()
            pwd = self.ui.password.text()
            self.xt.change_pwd(user_name,pwd)
            self.set_user(user_name,pwd)
            self.show_user(user_name,pwd)
            InfoBar.success(
                title='密码修改',
                content="密码修改成功",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,  # won't disappear automatically
                parent=self
            )
        except Exception as e:
            InfoBar.error(
                title='密码修改',
                content="密码修改失败",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,  # won't disappear automatically
                parent=self
            )

    def set_user(self,user_name,pwd):
        self.user_name = user_name
        self.pwd = pwd
        self.pwdChanged.emit(user_name,pwd)

    def query_log(self):
        date = self.ui.date.getDate().getDate()
        time = self.ui.time.getTime()
        try:
            if self.ui.query.text() == "y-m-d-h-m-s查询":
                if date[0]==0 or time.second() == -1:
                    InfoBar.error(
                        title='日志查询失败',
                        content="日期或时间不能为空",
                        orient=Qt.Horizontal,
                        isClosable=False,
                        position=InfoBarPosition.BOTTOM,
                        duration=2000,  # won't disappear automatically
                        parent=self
                    )
                    return
                query = [date[0],date[1],date[2],time.hour(),time.minute(),time.second()]
                logs = self.xt.query_log(*query)
            elif self.ui.query.text() == "y-m-d-h-m查询":
                if date[0]==0 or time.second() == -1:
                    InfoBar.error(
                        title='日志查询失败',
                        content="日期或时间不能为空",
                        orient=Qt.Horizontal,
                        isClosable=False,
                        position=InfoBarPosition.BOTTOM,
                        duration=2000,  # won't disappear automatically
                        parent=self
                    )
                    return
                query = [date[0],date[1],date[2],time.hour(),time.minute()]
                logs = self.xt.query_log(*query)
            elif self.ui.query.text() == "y-m-d-h查询":
                if date[0]==0 or time.second() == -1:
                    InfoBar.error(
                        title='日志查询失败',
                        content="日期或时间不能为空",
                        orient=Qt.Horizontal,
                        isClosable=False,
                        position=InfoBarPosition.BOTTOM,
                        duration=2000,  # won't disappear automatically
                        parent=self
                    )
                    return
                query = [date[0],date[1],date[2],time.hour()]
                logs = self.xt.query_log(*query)
            elif self.ui.query.text() == "年月日查询":
                if date[0]==0:
                    InfoBar.error(
                        title='日志查询失败',
                        content="日期不能为空",
                        orient=Qt.Horizontal,
                        isClosable=False,
                        position=InfoBarPosition.BOTTOM,
                        duration=2000,  # won't disappear automatically
                        parent=self
                    )
                    return
                query = [date[0],date[1],date[2]]
                logs = self.xt.query_log(*query)
            elif self.ui.query.text() == "年月查询":
                if date[0]==0:
                    InfoBar.error(
                        title='日志查询失败',
                        content="日期不能为空",
                        orient=Qt.Horizontal,
                        isClosable=False,
                        position=InfoBarPosition.BOTTOM,
                        duration=2000,  # won't disappear automatically
                        parent=self
                    )
                    return
                query = [date[0],date[1]]
                logs = self.xt.query_log(*query)
            elif self.ui.query.text() == "年查询":
                if date[0]==0:
                    InfoBar.error(
                        title='日志查询失败',
                        content="日期不能为空",
                        orient=Qt.Horizontal,
                        isClosable=False,
                        position=InfoBarPosition.BOTTOM,
                        duration=2000,  # won't disappear automatically
                        parent=self
                    )
                    return
                query = [date[0]]
                logs = self.xt.query_log(*query)
            elif self.ui.query.text() == "查询":
                InfoBar.info(
                    title='日志查询失败',
                    content="请选择查询方式",
                    orient=Qt.Horizontal,
                    isClosable=False,
                    position=InfoBarPosition.BOTTOM,
                    duration=2000,  # won't disappear automatically
                    parent=self
                )
                return
            self.ui.logTable.clearContents()
            rows = len(logs)
            self.ui.logTable.setRowCount(rows)
            for i in range(rows):
                for j in range(len(logs[i])):
                    self.ui.logTable.setItem(i, j, QTableWidgetItem(logs[i][j]))
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()

    def delete_log(self):
        try:
            date = self.ui.logTable.item(self.ui.logTable.currentRow(),0).text()
            self.ui.logTable.removeRow(self.ui.logTable.currentRow())
            date = date.split("|")
            time = date[1]
            date = date[0]
            date = [int(each) for each in date.split("-")]
            time = [int(each) for each in time.split(":")]
            date = date+time
            self.xt.delete_log(*date)
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()


class XTMainWindow(FluentWindow):
    def __init__(self,authority,file_path,avatar,user_name,password,parent=None):
        super().__init__(parent=parent)

        self.resize(1000, 650)
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.xt = XtContainer(authority,file_path,user_name)

        self.setWindowIcon(QIcon(avatar))

        self.user_name = user_name
        self.pwd = password

        self.bomWind = BomWindow(authority,user_name,self,file_path)
        self.bomWind.setObjectName("bom_wind")

        self.adminWind = AdminWindow(authority,user_name,file_path)
        self.adminWind.setObjectName("admin_wind")

        self.logOut = LogOut(self)
        self.logOut.setObjectName("log_out")

        self.xtMain = NavigationTreeWidget(FluentIcon.VPN,"系统管理",isSelectable=False)
        self.xtMain.setObjectName("xt_main")

        self.home = HomeWindow(authority,user_name,password,avatar=avatar,file_path=file_path)
        self.home.setObjectName("home")

        self.addSubInterface(self.home, FluentIcon.HOME, "日志账户管理")



        self.navigationInterface.addWidget(
            routeKey="xt_main",
            widget=self.xtMain,
            onClick=lambda:self.stackedWidget.setCurrentWidget(self.bomWind),
            position=NavigationItemPosition.SCROLL,
        )


        self.addSubInterface(self.bomWind, FluentIcon.FOLDER, "工艺信息管理",parent=self.xtMain,position=NavigationItemPosition.SCROLL)
        self.addSubInterface(self.adminWind, FluentIcon.PEOPLE, "人员信息管理",parent=self.xtMain,position=NavigationItemPosition.SCROLL)


        self.navigationInterface.addWidget(
            routeKey="log_out",
            widget=self.logOut,
            onClick=self.logOut.show_info,
            position=NavigationItemPosition.BOTTOM,
        )

        self.bind()
        self.set_user(self.user_name,self.pwd)

        self.navigationInterface.setCurrentItem("home")
        # self.stackedWidget.setCurrentIndex(0)


    def bind(self):
        self.logOut.log.triggered.connect(self.export_log)
        self.home.pwdChanged.connect(self.change_user)

    def export_log(self):
        try:
            self.xt.export_log()
            InfoBar.success(
                title='日志消息',
                content="日志保存成功",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,  # won't disappear automatically
                parent=self
            )
        except AuthorityError as e:
            MessageBox("权限鉴定失败","无该操作权限，如有疑问请联系管理员",self).exec()
        except Exception as e:
            InfoBar.error(
                title='日志消息',
                content="日志保存失败",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,  # won't disappear automatically
                parent=self
            )

    def change_user(self, user_name, pwd):
        self.user_name = user_name
        self.pwd = pwd
        self.xt.user_name = user_name

    def set_user(self,user_name,pwd):
        self.user_name = user_name
        self.pwd = pwd
        self.home.user_name = user_name
        self.home.pwd = pwd
        self.xt.user_name = user_name

class XTLoginWindow(AcrylicWindow):

    def __init__(self,icon,background,file_path,title="login window"):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.background = background
        self.xt = XtContainer(4,file_path,"login manager")
        self.mainWindow = None
        self.user_name = None
        self.pwd = None
        self.file_path = file_path

        self.bind()


        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.ui.logo.setPixmap(QPixmap(icon).scaled(self.ui.logo.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        self.ui.imageLabel.setScaledContents(False)
        # self.ui.imageLabel.setMinimumSize(600,650)

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))

        self.resize(1000, 650)

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False)
        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: white
            }
        """)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(self.background).scaled(
            self.ui.imageLabel.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.ui.imageLabel.setPixmap(pixmap)

    def bind(self):
        self.ui.login.clicked.connect(self.check)

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
            self.mainWindow = XTMainWindow(authority, self.file_path)
            self.mainWindow.logOut.out.triggered.connect(self.back)
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

    def back(self):
        self.mainWindow.destroy()
        self.show()


if __name__ == "__main__":
    app = QApplication()
    # apply_stylesheet(app, theme='dark_teal.xml')
    # bw = BomWindow()
    # bw.show()
    # lw = LineWindow()
    # lw.show()
    # aw = AdminWindow()
    # aw.show()
    m = XTMainWindow(7,"test.db","logo.png","test","test")
    m.show()
    # l = XTLoginWindow("../../res/logo.png","../../res/background.jpg","test.db")
    # l.show()
    # h = HomeWindow(7,file_path="test.db")
    # h.show()
    app.exec()