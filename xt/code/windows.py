import copy
import os
import sys

from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QMessageBox,QFileDialog,QTreeWidgetItem,QLineEdit,QListWidgetItem,QTableWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QUrl,Signal
from qt_material import apply_stylesheet

from ui.BomUI import Ui_Bom
from ui.LineUI import Ui_Line
from ui.AdminUI import Ui_Admin
from ui.MainUI import Ui_MainWindow
from ui.BomCreateUI import Ui_BomCreate
from ui.AddGroupUI import Ui_AddGroup
from ui.AddCharacterUI import Ui_AddCharacter
from ui.AddWorkerUI import Ui_AddWorker

from xt_container import XtContainer


class BomCreateWindow(QWidget):
    closed = Signal()
    def __init__(self,container):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_BomCreate()
        self.ui.setupUi(self)
        self.container = container
        self.name = ""
        self.bind()

    def bind(self):
        self.ui.bomCreate.clicked.connect(self.create_bom)


    def create_bom(self):
        self.name = self.ui.bomCreateName.text()
        if self.name != "":
            self.container.create_bom(self.name)
            self.closed.emit()
            self.ui.bomCreateName.setText("")
            self.close()
        else:
            self.close()

class BomWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Bom()
        self.ui.setupUi(self)
        self.xt = XtContainer(7,"test.db")
        self.bcw = BomCreateWindow(self.xt)
        self.lineWindow = LineWindow(self.xt)
        self.head = ["ID","bom层级","零件名称","零件描述","零件成本","零件生产周期","是否外购","注释"]

        self.data_type = [int,int,str,int,str,float,float,bool,str]
        # self.refresh_boms()
        self.bind()

    def bind(self):
        self.ui.bomNew.clicked.connect(self.create_bom)
        self.ui.bomRefresh.clicked.connect(self.refresh_boms)
        self.ui.bomRemove.clicked.connect(self.remove_bom)
        self.ui.partNew.triggered.connect(self.add_bom)
        self.ui.partRemove.triggered.connect(self.del_bom)
        self.ui.openLine.triggered.connect(self.open_line)
        self.ui.bomList.currentItemChanged.connect(self.show_bom)
        self.ui.bomUpdate.clicked.connect(self.sync_bom)
        # self.bomTable.addAction(self.partNew)
        # self.bomTable.addAction(self.partRemove)
        # self.bomTable.addAction(self.openLine)
        self.bcw.closed.connect(self.refresh_boms)


    """
    以下为对BOM表的操作
    """
    def create_bom(self):
        self.bcw.show()

    def remove_bom(self):
        name = self.ui.bomList.currentItem().text()
        self.xt.remove_boms(name)
        self.refresh_boms()

    def refresh_boms(self):
        boms = self.xt.find_boms()
        self.ui.bomList.clear()
        for bom in boms:
            bom = bom[0][7:]
            self.ui.bomList.addItem(bom)

    def add_bom(self):
        self.ui.bomTable.setRowCount(self.ui.bomTable.rowCount()+1)
        if self.ui.bomTable.rowCount() == 1:
            self.ui.bomTable.setItem(self.ui.bomTable.rowCount() - 1, 0, QTableWidgetItem("1"))
            return
        self.ui.bomTable.setItem(self.ui.bomTable.rowCount()-1, 0, QTableWidgetItem(str(
            int(self.ui.bomTable.item(self.ui.bomTable.rowCount()-2,0).text())+1
        )))

    def del_bom(self):
        id = int(self.ui.bomTable.item(self.ui.bomTable.currentRow(), 0).text())
        self.ui.bomTable.removeRow(self.ui.bomTable.currentRow())
        name = self.ui.bomList.currentItem().text()
        self.xt.delete_bom(name,id)

    def show_bom(self,current,previous):
        if not current:
            return
        name = self.ui.bomList.currentItem().text()
        parts = self.xt.get_in_bom(name)
        self.ui.bomTable.clearContents()
        rows = len(parts)
        self.ui.bomTable.setRowCount(rows)
        for i in range(rows):
            for j in range(len(parts[i])):
                if parts[i][j]:
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
        except Exception as e:
            QMessageBox.information(self,"数据错误","非空检验失败，请填写非空列后再同步")

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
        self.Wdata_type = [int,str,int]
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

    def add_line(self):
        self.ui.lineTable.setRowCount(self.ui.lineTable.rowCount() + 1)
        if self.ui.lineTable.rowCount() == 1:
            self.ui.lineTable.setItem(self.ui.lineTable.rowCount() - 1, 0, QTableWidgetItem("1"))
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
        except Exception as e:
            QMessageBox.information(self, "数据错误", "非空检验失败，请填写非空列后再同步")

    """
    以下为对工序操作
    """
    def refresh_work(self,item):
        if item == None or (item.row() == self.ui.lineTable.currentRow()and item.row()!=0) :
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
        if self.ui.workTable.rowCount() == 1:
            self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1, 0, QTableWidgetItem("1"))
            self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1, 2, QTableWidgetItem(
                self.ui.lineTable.item(self.ui.lineTable.currentRow(), 0).text()))
            return
        self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1, 0, QTableWidgetItem(str(
            int(self.ui.workTable.item(self.ui.workTable.rowCount() - 2, 0).text()) + 1
        )))
        self.ui.workTable.setItem(self.ui.workTable.rowCount() - 1,2,QTableWidgetItem(self.ui.lineTable.item(self.ui.lineTable.currentRow(),0).text()))

    def del_work(self):
        id = int(self.ui.workTable.item(self.ui.workTable.currentRow(), 0).text())
        self.ui.workTable.removeRow(self.ui.workTable.currentRow())
        self.container.del_work(self.ui.lineTable.item(self.ui.lineTable.currentRow(),0).text(),id)

    def sync_work(self):
        try:
            data = []
            for i in range(self.ui.workTable.rowCount()):
                if self.ui.workTable.item(i, 2).text() != self.ui.lineTable.item(self.ui.lineTable.currentRow(),0).text():
                    return
                data.append(
                    [self.Wdata_type[j](self.ui.workTable.item(i, j).text()) if self.ui.workTable.item(i, j).text() else "" for
                     j in range(self.ui.workTable.columnCount())])
            self.container.update_work(self.ui.lineTable.item(self.ui.lineTable.currentRow(), 0).text(),data)
        except Exception as e :
            QMessageBox.information(self, "数据错误", "非空检验失败，请填写非空列后再同步")


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
            QMessageBox.information(self, "数据错误", "非空检验失败，请填写非空列后再同步")

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
        self.bind()

    def bind(self):
        self.ui.ok.clicked.connect(self.add)

    def add(self):
        # print([self.ui.groupName.text(),self.ui.groupFather.currentText(),self.ui.groupDes.toPlainText()])
        try:
            self.container.add_character([self.ui.characterName.text(),int(self.ui.characterAuthority.text())])
            self.success.emit()
            self.clear_all()
            self.close()
        except ValueError as e:
            QMessageBox.information(self, "数据错误", "非空检验失败，请填写非空列后再同步")

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
            QMessageBox.information(self, "数据错误", "非空检验失败，请填写非空列后再同步")

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
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Admin()
        self.ui.setupUi(self)
        self.xt = XtContainer(7,"test.db")
        self.add_group = AddGroupWindow(self.xt)
        self.add_character = AddCharacterWindow(self.xt)
        self.add_worker = AddWorkerWindow(self.xt)
        self.refresh_group()
        self.refresh_character()
        self.bind()

    def bind(self):
        self.ui.groupNew.clicked.connect(self.open_group_window)
        self.ui.groupRemove.clicked.connect(self.del_group)
        self.ui.characterNew.clicked.connect(self.open_character_window)
        self.ui.characterRemove.clicked.connect(self.del_character)
        self.ui.workerNew.clicked.connect(self.open_worker_window)
        self.ui.groupTree.currentItemChanged.connect(self.show_worker)
        self.add_group.success.connect(self.refresh_group)
        self.add_character.success.connect(self.refresh_character)
        self.add_worker.success.connect(self.refresh_character)
        self.add_worker.success.connect(self.refresh_group)

    """
    以下为组织关系树操作
    """
    def open_group_window(self):
        self.add_group.refresh_combo()
        self.add_group.show()

    def open_character_window(self):
        self.add_character.show()

    def open_worker_window(self):
        self.add_worker.refresh_combo()
        self.add_worker.show()

    def show_worker(self):
        worker_id = int(self.ui.groupTree.currentItem().text(2))
        worker = self.xt.get_worker(worker_id)
        print(worker)

    def refresh_group(self):
        self.ui.groupTree.clear()
        groups = self.xt.get_groups()
        root = ["root"]
        temp = copy.deepcopy(groups)
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
            print(characters)
        for each in characters:
            self.ui.characterList.addItem(each[0])

    def del_group(self):
        name = self.ui.groupTree.currentItem().text(0)
        self.xt.del_group(name)
        self.refresh_group()

    def del_character(self):
        character = self.ui.characterList.currentItem().text()
        self.xt.del_character(character)
        self.refresh_character()

    def del_worker(self):
        worker_id = int(self.ui.workerID.text())
        self.xt.del_worker(worker_id)


    def __get_tree_item__(self,text:str,root:QTreeWidgetItem):
        if root.text(0) == text:
            return root
        for each in [root.child(i) for i in range(root.childCount())]:
            return self.__get_tree_item__(text,each)
        return None






class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bomWind = BomWindow()
        self.adminWind = AdminWindow()
        self.ui.bomLayout.addWidget(self.bomWind)
        self.ui.adminLayout.addWidget(self.adminWind)
        self.bind()

    def change_stack(self):
        id = self.ui.btn_group.checkedId()
        self.ui.stack.setCurrentIndex(id)

    def bind(self):
        # self.btn_group = QButtonGroup()
        # self.btn_group.addButton(self.cg, 0)
        # self.btn_group.addButton(self.jh, 1)
        # self.btn_group.addButton(self.kc, 2)
        # self.btn_group.addButton(self .xs, 3)
        # self.btn_group.addButton(self.xt, 4)
        # print(self.btn_group)
        ## 以上代码复制到UI文件中设置按钮组
        self.ui.btn_group.buttonToggled.connect(self.change_stack)

if __name__ == "__main__":
    app = QApplication()
    apply_stylesheet(app, theme='dark_teal.xml')
    # bw = BomWindow()
    # bw.show()
    # lw = LineWindow()
    # lw.show()
    # aw = AdminWindow()
    # aw.show()
    m = MainWindow()
    m.show()
    app.exec()