import sqlite3 as sql
import sys
import time


class XTDataBase:
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

    def xs_customers_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
        cust_id      INT       NOT NULL,
	    cust_name    VARCHAR(50)  NOT NULL,
	    cust_address VARCHAR(50)  NULL,
	    cust_zip     VARCHAR(10)  NULL,
	    cust_contact VARCHAR(50)  NULL,
	    cust_email   VARCHAR(255) NULL,
	    PRIMARY KEY(cust_id)
        );
        """.format(name))
        self.connection.commit()

    """
    name:表名
    销售产品管理
    """

    def xc_products_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL
                );
                """.format(name))
        self.connection.commit()

    """
    name:表名

    func:销售员管理
    """

    def xc_salespersons_create_table(self, name):
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
    def xc_sales_activities_create_table(self, name):
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
    def xc_sales_orders_create_table(self, name):
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