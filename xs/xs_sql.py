import sqlite3 as sql
import sys
import time
from PySide6.QtWidgets import QApplication, QWidget,QLineEdit,QVBoxLayout
# PySide6-uic demo.ui -o ui_demo.py
from xs2 import Ui_Form

class XSDataBase:
    def __init__(self, file_path):
        self.connection = sql.connect(file_path)
        self.sql_cmd("PRAGMA foreign_keys=ON")

    ## 数据库操作方法
    def insert_table(self, table_name, col_name: list, values: list):

        cursor = self.connection.cursor()
        cmd = f"INSERT INTO {table_name} (" + ",".join(col_name) + \
              f") VALUES ("
        for i in range(len(values)):
            cmd += f"'{values[i]}',"
        cmd = cmd[:-1] + ");"
        # print(cmd)
        cursor.execute(cmd)
        self.connection.commit()

    def find_info(self, table_name, args):
        cursor = self.connection.cursor()
        cmd = None
        # print(args)
        if not len(args):
            cmd = "SELECT * FROM {};".format(table_name)
            # print(cmd)
            cursor.execute(cmd)
            # print(" | ".join(self.params))
        else:
            cmd = "SELECT " + ", ".join(args) + " FROM {};".format(table_name)
            # print(cmd)
            cursor.execute(cmd)
            # print(" | ".join(args))
        result = []
        for each in cursor:
            result.append(each)
            # each = [str(i) for i in each ]
            # print(" | ".join(each))
        return result

    def sql_cmd(self, cmd):
        cursor = self.connection.cursor()
        cursor.execute(cmd)
        self.connection.commit()
        result = []
        for each in cursor:
            result.append(each)
            # print(each)
        return result

    def where(self, table_name, col, **dicts):
        cursor = self.connection.cursor()
        cmd = None
        # print(args)
        if not len(col):
            cmd = "SELECT * FROM {} WHERE ".format(table_name)
            for k, v in dicts.items():
                cmd += "{} = '{}' ".format(k, v)
            # print(cmd)
            cursor.execute(cmd)
            # print(" | ".join(self.params))
        else:
            cmd = "SELECT " + ", ".join(col) + " FROM {} WHERE ".format(table_name)
            for k, v in dicts.items():
                cmd += "{} = '{}' ".format(k, v)
            # print(cmd)
            cursor.execute(cmd)
            # print(" | ".join(col))
        result = []
        for each in cursor:
            result.append(each)
            # each = [str(i) for i in each]
            # print(" | ".join(each))
        return result

    def delete(self, table_name, **kwargs):
        cursor = self.connection.cursor()
        cmd = "DELETE FROM {} WHERE ".format(table_name)
        for k, v in kwargs.items():
            cmd += "{} = '{}' ".format(k, v)
        # print(cmd)
        cursor.execute(cmd[:-1])
        self.connection.commit()

    def update(self, table_name, dicts, **condition):
        cursor = self.connection.cursor()
        cmd = None
        # print(args)
        if len(condition):
            cmd = "UPDATE {} SET ".format(table_name)
            for k, v in dicts.items():
                if type(v) == str:
                    cmd += "{} = '{}',".format(k, v)
                else:
                    cmd += "{} = {},".format(k, v)
            cmd = cmd[:-1] + " WHERE "
            for k, v in condition.items():
                cmd += "{} = '{}'".format(k, v)
            # print(cmd)
            cursor.execute(cmd)
            # print(" | ".join(self.params))
        else:
            cmd = "UPDATE {} SET ".format(table_name)
            for k, v in dicts.items():
                cmd += "{} = '{}',".format(k, v)
            # print(cmd)
            cursor.execute(cmd[:-1])
            # print(" | ".join(col))

    def add_column(self, table_name, col_name, col_type):
        cursor = self.connection.cursor()
        cmd = "ALTER TABLE {} ADD COLUMN {} {};".format(table_name, col_name, col_type)
        # print(cmd)
        cursor.execute(cmd[:-1])
        self.connection.commit()

    def drop(self, table_name):
        cursor = self.connection.cursor()
        cmd = "DROP TABLE {} ;".format(table_name)
        # print(cmd)
        cursor.execute(cmd[:-1])
        self.connection.commit()

    """
    name:表名

    func:客户信息管理
    """

    def xs_customer_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
            cust_id      INT       NOT NULL,
	        cust_name    VARCHAR(50)  NOT NULL,
	        cust_address VARCHAR(50)  NULL,
	        cust_email   VARCHAR(255) NULL,
	        cust_points  VARCHAR(50)  NULL,
	        PRIMARY KEY(cust_id)
        );
        """.format(name))
        self.connection.commit()

    """
    
    name:表名
    销售产品管理
    """

    def xs_products_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                product_id TEXT PRIMARY KEY NOT NULL,
                product_name TEXT,
                price TEXT
                );
                """.format(name))
        self.connection.commit()

    """
    name:表名

    func:销售员管理
    """

    def xs_salespersons_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                salesperson_id INTEGER PRIMARY KEY   NOT NULL,
                name TEXT,
                region TEXT,
                password INT
                );
                """.format(name))
        self.connection.commit()

    """
    name:表名
    销售业务管理
    """
    def xs_sales_activities_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                activity_id INTEGER PRIMARY KEY   NOT NULL,
                activity_date DATE,
                salesperson_id INTEGER,
                description TEXT,
                FOREIGN KEY(salesperson_id) REFERENCES salespersons(salesperson_id)
                );
                """.format(name))
        self.connection.commit()
        """
           name:表名
           销售订单管理
           """
    def xs_sales_orders_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                order_id INTEGER PRIMARY KEY    NOT NULL,
                order_date DATE,
                customer_id INTEGER,
                salesperson_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY(salesperson_id) REFERENCES salespersons(salesperson_id),
                FOREIGN KEY(product_id) REFERENCES products(product_id)
                );
                """.format(name))
        self.connection.commit()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # UI类的实例化()
        self.ui.setupUi(self)
        self.db = XSDataBase("lk.db")
        self.bind()

    def bind(self):
        # self.ui.pushButton_3.clicked.connect(self.get_btn_text)
        self.ui.pushButton.clicked.connect(self.get_btn2_text)

    #按键获取客户
    # def get_btn_text(self):
    #     if self.ui.radioButton.isChecked():
    #         cid = self.ui.lineEdit.text()
    #         cname = self.ui.lineEdit_2.text()
    #         caddress = self.ui.lineEdit_3.text()
    #         cemail = self.ui.lineEdit_4.text()
    #         cpoints = self.ui.lineEdit_5.text()
    #         # self.db.insert_table('cust',['cust_id','cust_name','cust_address','cust_email','cust_points'],[cid,'cname','caddress','cemail''cpoints'])
    #     if self.ui.radioButton_2.isChecked():
    #         sid = self.ui.lineEdit_6.text()

    # 按键获取销售员
    def get_btn2_text(self):
        if self.ui.radioButton_5.isChecked():
            sid = self.ui.lineEdit_7.text()
            sname = self.ui.lineEdit_8.text()
            sregion= self.ui.lineEdit_9.text()
            password = self.ui.lineEdit_10.text()
            self.db.insert_table('sale',['salesperson_id','name','region','password'],[sid,sname,sregion,password])
            self.ui.lineEdit_10.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
        if self.ui.radioButton_6.isChecked():
            w_sid = self.ui.lineEdit_7.text()
            slist = self.db.where('sale',['salesperson_id','name','region','password'],salesperson_id=w_sid)
            print(slist)
            sstr = ' '.join(map(str,slist))
            self.ui.lineEdit_7.clear()
            if len(slist) == 0:
                self.ui.lineEdit_11.setText("查询失败")
            else:
                self.ui.lineEdit_11.setText(sstr)















if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MyWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出"""

    salespersons = XSDataBase('lk.db')
    salespersons.xs_salespersons_create_table('sale')
    # salespersons.insert_table('sale',['salesperson_id','name'],[20374105,'舒琛'])
    # salespersons.insert_table('sale', ['salesperson_id', 'name'], [20374103, '吴哥'])
    # print(salespersons.find_info('sale',[]))
    # salespersons.delete('sale',salesperson_id = 20374103)
    # print(salespersons.find_info('sale',[]))
    # customer = XSDataBase('lk.db')
    # customer.xs_customer_create_table('cust')
    # customer.insert_table('cust', ['cust_id', 'name'], [20374105, '舒琛'])
    # customer.insert_table('cust', ['cust_id', 'name'], [20374103, '吴哥'])
    # print(customer.find_info('cust', []))








