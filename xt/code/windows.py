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
        self.head = ["ID","bom层级","零件名称","零件数量","零件描述","零件成本","零件生产周期","是否外购","注释"]

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
        self.container.add_group([self.ui.groupName.text(),self.ui.groupFather.currentText(),self.ui.groupDes.toPlainText()])
        self.close()

    def refresh_combo(self):
        groups = self.container.get_groups()
        fathers = ["root"]
        for group in groups:
            if group[1] not in fathers:
                print(group[1])
                fathers.append(group[1])
        self.ui.groupFather.addItems(fathers)




class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Admin()
        self.ui.setupUi(self)
        self.xt = XtContainer(7,"test.db")
        self.add_group = AddGroupWindow(self.xt)
        # self.refresh_group()
        self.bind()

    def bind(self):
        self.ui.groupNew.clicked.connect(self.open_group_window)

    """
    以下为组织关系树操作
    """
    def open_group_window(self):
        self.add_group.refresh_combo()
        self.add_group.show()

    def refresh_group(self):
        groups = self.xt.get_groups()
        root = ["root"]

        while root != []:
            finish = len(root)
            for group in groups:
                if group[1] == "root":
                    root.append(group[0])
                    self.ui.groupTree.addTopLevelItem(QTreeWidgetItem(group[0]))
                elif group[1] in root:
                    root.append(group[0])
                    father = self.ui.groupTree.findItems(group[1])
                    print(father)



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