import sqlite3 as sql
import sys
import time
from PySide6.QtWidgets import QApplication, QWidget,QLineEdit,QVBoxLayout,QTableWidgetItem,QTextBrowser,QHeaderView
# PySide6-uic demo.ui -o ui_demo.py
from xs2 import Ui_Form

import os
sys.path.append(os.path.abspath("../kc"))
from inventory import InventoryManager
sys.path.append(os.path.abspath("../xt/code"))
from xt_container import OperationCode,XtContainer
'''
UPDATE：修改构造函数，将数据库文件作为参数传入，避免错误 line 229
'''

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
        self.connection.commit()

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
            cust_id         INT     PRIMARY KEY   NOT NULL,
            cust_name       TEXT    NULL,
            cust_address    TEXT    NULL,
            cust_email    TEXT    NULL,
            cust_points  INT  NULL
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
                product_id INT PRIMARY KEY NOT NULL,
                product_name TEXT,
                price TEXT,
                inventory TEXT
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
                salesperson_id INT PRIMARY KEY   NOT NULL,
                name TEXT,
                region TEXT,
                password TEXT
                );
                """.format(name))
        self.connection.commit()

    """
    name:表名
    销售业务管理
    """
    def xs_sale_performance_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                saleman_id INT PRIMARY KEY NOT NULL,
                saleman_name TEXT,
                completed_orders INT,
                value INT
                );
                """.format(name))
        self.connection.commit()
    def xs_sales_activities_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                activity_id INT PRIMARY KEY   NOT NULL,
                activity_date DATE,
                salesperson_id INT,
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
                order_id INT PRIMARY KEY    NOT NULL,
                order_date TEXT,
                O_product_name TEXT,
                O_customer_id INT,
                O_salesperson_id INT,
                O_product_id INT,
                O_number INT
                );
                """.format(name))
        self.connection.commit()

    def xs_sales_forcast_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                    f_id   INT   PRIMARY KEY    NOT NULL,
                    forcast INT   
                    );
                    """.format(name))
        self.connection.commit()


                # FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
                # FOREIGN KEY(salesperson_id) REFERENCES salespersons(salesperson_id),
                # FOREIGN KEY(product_id) REFERENCES products(product_id)
class MyWindow(QWidget):
    def __init__(self,user_name,kc_file,xt_log,file_path="lk.db"):
        super().__init__()
        self.ui = Ui_Form()  # UI类的实例化()
        self.ui.setupUi(self)
        self.kc_file=kc_file
        self.db = XSDataBase(file_path)
        self.bind()
        self.log=XtContainer(1,xt_log,user_name)
        header = self.ui.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)



    def bind(self):
        self.ui.pushButton_3.clicked.connect(self.get_btn_text)#客户信息管理
        self.ui.pushButton.clicked.connect(self.get_btn2_text)#销售员信息管理
        self.ui.pushButton_2.clicked.connect(self.get_btn3_text)
        self.ui.pushButton_4.clicked.connect(self.get_btn4_text)
        self.ui.pushButton_5.clicked.connect(self.get_btn5_text)#销售产品管理
        self.ui.pushButton_7.clicked.connect(self.get_btn6_text)#销售订单管理
        self.ui.pushButton_4.clicked.connect(self.get_btn7_text)
        self.ui.pushButton_9.clicked.connect(self.get_btn8_text)#销售员业务统计


    #按键获取客户
    def get_btn_text(self):
        if self.ui.radioButton.isChecked():
            cid = self.ui.lineEdit.text()
            cname = self.ui.lineEdit_2.text()
            caddress = self.ui.lineEdit_3.text()
            cemail = self.ui.lineEdit_4.text()
            cpoints = self.ui.lineEdit_5.text()
            self.db.insert_table('cust',['cust_id','cust_name','cust_address','cust_email','cust_points'],[cid,cname,caddress,cemail,cpoints])
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.textBrowser.setText("操作成功")
        if self.ui.radioButton_2.isChecked():
            self.ui.textBrowser.clear()
            w_cid = self.ui.lineEdit.text()
            clist = self.db.where('cust', ['cust_id','cust_name','cust_address','cust_email','cust_points'], cust_id=w_cid)
            # print(type(clist))
            # print(clist)
            # cstr = ' '.join(map(str, clist))
            # cstr = cstr.join('\n')
            self.ui.lineEdit.clear()
            if len(clist) == 0:
                self.ui.textBrowser.setText("此客户不存在")
            else:
                html_text = '客户ID：' + str(clist[0][0])
                self.ui.textBrowser.append(html_text)
                html_text = '客户姓名：' + str(clist[0][1])
                self.ui.textBrowser.append(html_text)
                html_text = '客户地址：' + str(clist[0][2])
                self.ui.textBrowser.append(html_text)
                html_text = '客户邮箱：' + str(clist[0][3])
                self.ui.textBrowser.append(html_text)
                html_text = '客户积分：' + str(clist[0][4])
                self.ui.textBrowser.append(html_text)
                # html_text = "<pre>{}</pre>".format(variable)  # 使用 <pre> 标签来保留文本的格式
                # html_text = "<h1>客户信息</h1><p>姓名：</p ><p>text1</p >"

                # 设置文本内容
                # self.ui.textBrowser.setHtml(html_text)
                # self.ui.textBrowser.setText(cstr)
        if self.ui.radioButton_4.isChecked():
            self.ui.textBrowser.clear()
            d_sid = self.ui.lineEdit.text()
            self.db.delete('cust', cust_id=d_sid)
            self.ui.lineEdit.clear()
            self.ui.textBrowser.setText("操作成功")
        if self.ui.radioButton_3.isChecked():
            self.ui.textBrowser.clear()
            u_cid = self.ui.lineEdit.text()
            u_cname = self.ui.lineEdit_2.text()
            u_caddress = self.ui.lineEdit_3.text()
            u_cemail = self.ui.lineEdit_4.text()
            u_cpoints = self.ui.lineEdit_5.text()
            # self.db.update('sale',{"salesperson_id":u_sid,"name":u_sname,"region":u_sregion:,"password": u_password})
            self.db.update('cust', {'cust_address': u_caddress}, cust_id=u_cid)
            self.db.update('cust', {"cust_email": u_cemail}, cust_id=u_cid)
            self.db.update('cust', {"cust_points": u_cpoints}, cust_id=u_cid)
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.textBrowser.setText("操作成功")
        self.log.generate_log(OperationCode.XS_CHANGE)

    def get_btn4_text(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.textBrowser.clear()

    # 按键获取销售员
    def get_btn2_text(self):
        if self.ui.radioButton_5.isChecked():
            self.ui.textBrowser_3.clear()
            sid = self.ui.lineEdit_7.text()
            sname = self.ui.lineEdit_8.text()
            sregion= self.ui.lineEdit_9.text()
            password = self.ui.lineEdit_10.text()
            self.db.insert_table('sale',['salesperson_id','name','region','password'],[sid,sname,sregion,password])
            self.db.insert_table('per',['saleman_id','saleman_name','completed_orders','value'],[sid,sname,0,0])
            self.ui.lineEdit_10.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
            self.ui.textBrowser_3.setText("操作成功")
        if self.ui.radioButton_6.isChecked():
            self.ui.textBrowser_3.clear()
            w_sid = self.ui.lineEdit_7.text()
            clist = self.db.where('sale',['salesperson_id','name','region','password'],salesperson_id=w_sid)
            # print(slist)
            # clist = ' '.join(map(str,slist))
            self.ui.lineEdit_7.clear()
            if len(clist) == 0:
                self.ui.textBrowser_3.setText("此销售员不存在")
            else:
                html_text = '销售员ID：' + str(clist[0][0])
                self.ui.textBrowser_3.append(html_text)
                html_text = '销售员姓名：' + str(clist[0][1])
                self.ui.textBrowser_3.append(html_text)
                html_text = '销售员职务：' + str(clist[0][2])
                self.ui.textBrowser_3.append(html_text)
                html_text = '销售员登录密码：' + str(clist[0][3])
                self.ui.textBrowser_3.append(html_text)
                # self.ui.textBrowser_3.setText(sstr)
            # w = self.db.find_info('sale',[])
            # print(w)
            # print(len(w))
            # print(w[1][2])
        if self.ui.radioButton_7.isChecked():
            self.ui.textBrowser_3.clear()
            d_sid = self.ui.lineEdit_7.text()
            self.db.delete('sale',salesperson_id=d_sid)
            self.db.delete('per', saleman_id=d_sid)
            self.ui.lineEdit_7.clear()
            self.ui.textBrowser_3.setText("操作成功")
        if self.ui.radioButton_8.isChecked():
            self.ui.textBrowser_3.clear()
            u_sid = self.ui.lineEdit_7.text()
            # u_sname = self.ui.lineEdit_8.text()
            u_sregion = self.ui.lineEdit_9.text()
            u_password = self.ui.lineEdit_10.text()
            # self.db.update('sale',{"salesperson_id":u_sid,"name":u_sname,"region":u_sregion:,"password": u_password})
            self.db.update('sale',{"region": u_sregion},salesperson_id=u_sid)
            self.db.update('sale', {"password": u_password}, salesperson_id=u_sid)
            self.ui.lineEdit_10.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
            self.ui.textBrowser_3.setText("操作成功")
        self.log.generate_log(OperationCode.XS_CHANGE)

    def get_btn3_text(self):
        self.ui.textBrowser_3.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()

   #销售产品管理
    def get_btn5_text(self):
        self.ui.lineEdit_13.clear()
        p_id = self.ui.lineEdit_12.text()
        p_sid = self.ui.lineEdit_14.text()
        p_cpassword = self.ui.lineEdit_15.text()
        p_test = self.db.where('sale',['password'],salesperson_id=p_sid)
        p_test = int(p_test[0][0])
        if int(p_cpassword) != p_test:
            self.ui.lineEdit_13.setText("用户名密码错误")
        else:
            kc = XSDataBase(self.kc_file)
            p_p=kc.where('products',['name'],product_id=p_id)
            p_p=len(p_p)
            if p_p == 0:
                self.ui.lineEdit_13.setText("此商品不存在")
            else:
                per = kc.find_info('products', [])
                # l_per = len(per)
                for i in range(3):
                    self.ui.tableWidget.setItem(0, i, QTableWidgetItem(str(per[0][i])))
                    self.ui.tableWidget.setItem(0,3,QTableWidgetItem(str(10)))
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_14.clear()
        self.ui.lineEdit_15.clear()


#销售订单管理
    def get_btn6_text(self):
        if self.ui.radioButton_9.isChecked():
            self.ui.textBrowser_2.clear()
            o_name = self.ui.lineEdit_11.text()
            o_id = self.ui.lineEdit_17.text()
            o_date = self.ui.lineEdit_18.text()
            o_pid = self.ui.lineEdit_19.text()
            o_number = self.ui.lineEdit_20.text()
            o_password = self.ui.lineEdit_26.text()
            o_cid = self.ui.lineEdit_21.text()
            o_sid = self.ui.lineEdit_6.text()
            # o_test = self.db.where('sale', ['password'], salesperson_id=o_sid)
            # print(o_test)
            #o_test2 = map(int, o_test)
            # o_test2 = int(o_test[0][0])
            # print(o_test2)
            # print(type(o_test2))
            inventory_manager = InventoryManager(self.kc_file)
            inventory_manager.substact_inventory(o_date,int(o_pid),int(o_number),o_sid)
            print(o_pid)
            print(type(o_sid))
            if len(self.db.where('cust',['cust_id'],cust_id=o_cid)) != 0:
                o_test = self.db.where('sale',['password'],salesperson_id=o_sid)
                o_test2 = int(o_test[0][0])
                # print(o_test2)
                if int(o_password) != o_test2:
                    self.ui.textBrowser_2.setText("用户名密码错误")
                else:
                    # order_id，order_date，product_name，customer_id，salesperson_id，product_id，number
                    self.db.insert_table('for',['f_id','forcast'],[o_id,0])
                    u_forcast=self.db.where('for',['forcast'],f_id=o_id)
                    u_forcast = int(u_forcast[0][0])+int(o_number)
                    self.db.update('for',{"forcast":u_forcast},f_id=o_id)
                    self.db.insert_table('ordr', ['order_id', 'order_date','O_product_name','O_customer_id','O_salesperson_id','O_product_id', 'O_number'],[o_id,o_date,o_name,o_cid,o_cid,o_pid,o_number])
                    # o_price = self.db.where('pod',['price'],product_id=o_pid)
                    # o_price2 = int(o_price[0][0])
                    o_price2 = 10
                    u_completed_orders = self.db.where('per',['completed_orders'],saleman_id=o_sid)
                    print(u_completed_orders)
                    u_completed_orders = int(u_completed_orders[0][0])
                    u_value = self.db.where('per',['value'],saleman_id=o_sid)
                    # print(u_value)
                    u_value = int(u_value[0][0])
                    u_points = self.db.where('cust', ['cust_points'], cust_id=o_cid)
                    u_points = int(u_points[0][0])
                    print(u_points+int(o_number) * int(o_price2))
                    self.db.update('cust', {"cust_points": u_points+int(o_number) * int(o_price2)}, cust_id=o_cid)
                    self.db.update('per', {"completed_orders": u_completed_orders+int(o_number)}, saleman_id=o_sid)
                    self.db.update('per', {"value": u_value+int(o_number)*int(o_price2)}, saleman_id=o_sid)
            else:
                self.ui.textBrowser_2.setText('该用户不存在')
            self.ui.textBrowser_2.setText("操作成功")
            self.ui.lineEdit_11.clear()
            self.ui.lineEdit_17.clear()
            self.ui.lineEdit_18.clear()
            self.ui.lineEdit_19.clear()
            self.ui.lineEdit_20.clear()
            self.ui.lineEdit_21.clear()
            self.ui.lineEdit_26.clear()
            self.ui.lineEdit_6.clear()
        if self.ui.radioButton_10.isChecked():
            self.ui.textBrowser_2.clear()
            o_id = self.ui.lineEdit_17.text()
            # order_id，order_date，product_name，customer_id，salesperson_id，product_id，number
            clist = self.db.where('ordr',['order_id', 'order_date','O_product_name','O_customer_id','O_salesperson_id','O_product_id', 'O_number'], order_id=o_id)
            # print(slist)
            # sstr = ' '.join(map(str,slist))
            # self.ui.textBrowser_2.setText(sstr)
            self.ui.lineEdit_17.clear()
            if len(clist) == 0:
                self.ui.textBrowser_2.setText("此订单不存在")
            else:
                html_text = '订单ID：' + str(clist[0][0])
                self.ui.textBrowser_2.append(html_text)
                html_text = '订单日期：' + str(clist[0][1])
                self.ui.textBrowser_2.append(html_text)
                html_text = '商品名称：' + str(clist[0][2])
                self.ui.textBrowser_2.append(html_text)
                html_text = '客户ID：' + str(clist[0][3])
                self.ui.textBrowser_2.append(html_text)
                html_text = '销售员ID：' + str(clist[0][4])
                self.ui.textBrowser_2.append(html_text)
                html_text = '商品ID：' + str(clist[0][5])
                self.ui.textBrowser_2.append(html_text)
                html_text = '商品数量：' + str(clist[0][6])
                self.ui.textBrowser_2.append(html_text)
                # self.ui.textBrowser_3.setText(sstr)
        if self.ui.radioButton_12.isChecked():
            kc = XSDataBase(self.kc_file)
            o_id = self.ui.lineEdit_17.text()
            p_p = kc.where('products', ['quantity'], product_id=o_id)
            print(p_p)
            number = self.db.where('ordr', ['o_number'], order_id=o_id)
            number = int(number[0][0])
            p_p = int(p_p[0][0])
            kc.update('products', {'quantity': p_p + number}, product_id=o_id)
            self.db.delete('ordr',order_id=o_id)
            self.db.delete('for',f_id=o_id)
            self.ui.lineEdit_7.clear()
            self.ui.textBrowser_2.setText("操作成功")
            self.ui.lineEdit_17.clear()
        if self.ui.radioButton_11.isChecked():
            self.ui.textBrowser_2.clear()
            o_name = self.ui.lineEdit_11.text()
            o_id = self.ui.lineEdit_17.text()
            o_date = self.ui.lineEdit_18.text()
            o_pid = self.ui.lineEdit_19.text()
            o_number = self.ui.lineEdit_20.text()
            o_password = self.ui.lineEdit_26.text()
            o_cid = self.ui.lineEdit_21.text()
            o_sid = self.ui.lineEdit_6.text()
            # order_id，order_date，product_name，customer_id，salesperson_id，product_id，number
            self.db.update('ordr', {"order_date": o_date},order_id=o_id)
            self.db.update('ordr', {"o_number": o_number}, order_id=o_id)
            # o_price = self.db.where('pod',['price'],product_id=o_pid)
            self.db.update('cust', {"cust_points": int(o_number) *int(10)}, cust_id=o_cid)
            self.db.update('per', {"completed_orders": o_number}, saleman_id=o_sid)
            self.db.update('per', {"value": int(o_number) * int(10)}, saleman_id=o_sid)
            self.ui.lineEdit_11.clear()
            self.ui.lineEdit_17.clear()
            self.ui.lineEdit_18.clear()
            self.ui.lineEdit_19.clear()
            self.ui.lineEdit_20.clear()
            self.ui.lineEdit_21.clear()
            self.ui.lineEdit_26.clear()
            self.ui.lineEdit_6.clear()
            self.ui.textBrowser_2.setText("操作成功")
        self.log.generate_log(OperationCode.XS_CHANGE)

    def get_btn7_text(self):
        self.ui.textBrowser_2.clear()
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_17.clear()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        self.ui.lineEdit_20.clear()
        self.ui.lineEdit_21.clear()
        self.ui.lineEdit_26.clear()
        self.ui.lineEdit_6.clear()

#业务员业绩分析
    # saleman_id,saleman_name,completed orders,value
    def get_btn8_text(self):
        per = self.db.find_info('per',[])
        l_per = len(per)
        for i in range(l_per):
            for j in range(4):
                # print(per[i][j])
                self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(per[i][j])))




















if __name__ == '__main__':
    # app = QApplication([])  # 启动一个应用
    # window = MyWindow('../kc/inventory.db','../test.db',"销售")  # 实例化主窗口
    # window.show()  # 展示主窗口
    # app.exec()  # 避免程序执行到这一行后直接退出"""

    kc = XSDataBase('../kc/inventory.db')

    # i=kc.find_info('products',[])
    # print(i)
    # kc.find_info('',[])
    salespersons = XSDataBase('lk.db')
    salespersons.xs_salespersons_create_table('sale')
    products = XSDataBase('lk.db')
    products.xs_products_create_table('pod')
    customer = XSDataBase('lk.db')
    customer.xs_customer_create_table('cust')
    order = XSDataBase('lk.db')
    order.xs_sales_orders_create_table('ordr')
    performance = XSDataBase('lk.db')
    performance.xs_sale_performance_create_table('per')
    forcast = XSDataBase('lk.db')
    forcast.xs_sales_forcast_create_table('for')
    # salespersons.insert_table('sale',['salesperson_id','name'],[20374105,'舒琛'])
    # salespersons.insert_table('sale', ['salesperson_id', 'name'], [20374103, '吴哥'])
    # print(salespersons.find_info('sale',[]))
    # salespersons.delete('sale',salesperson_id = 20374103)
    # print(salespersons.find_info('sale',[]))
    # customer.insert_table('cust', ['cust_id', 'name'], [20374105, '舒琛'])
    # customer.insert_table('cust', ['cust_id', 'name'], [20374103, '吴哥'])
    # print(customer.find_info('cust', []))








