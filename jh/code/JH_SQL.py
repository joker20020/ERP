import sys
import os
sys.path.append(os.path.abspath("../../xt/code"))
from xt_sql import XTDataBase
sys.path.append(os.path.abspath("../../xs"))
from xs_sql import XSDataBase
sys.path.append(os.path.abspath("../../kc"))
from inventory import InventoryManager
sys.path.append(os.path.abspath("../../cg"))
from cg_database import cg_database_entity

import sqlite3 as sql

from datetime import date, datetime, timedelta

# 计算物料需求量
# 毛需求 = 独立需求 + 相关需求
# 计划库存量 = 上期库存量 + 本期订单产出量 + 本期预计入库量 - 毛需求量
# 净需求量 = 本期毛需求量 - 上期库存量 - 本期预计入库量 + 安全库存量

class JHDataBase:
    def __init__(self, file_path):
        self.connection = sql.connect(file_path)
        # if len(params):
        #     self.params = params
        # else:
        #     self.params = ["FILE_PATH","NAME","DESCRIPTION","TIME_STAMP","AUTHOR","ORGANIZATION",
        #                "PREPROCESSOR","ORIGINATION_SYSTEM","AUTHORIZATION","FORMAT",
        #                "NUMBER","SYSTEM_ID","HEADER"]

    def MPS_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {}(
            product_id INTEGER PRIMARY KEY,
            planned_amount INTEGER NOT NULL,
            planned_deadline DATE
        );
        '''.format(name))
        self.connection.commit()

    def MRP_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {}(
            product_id INTEGER PRIMARY KEY,
            planned_amount INTEGER NOT NULL,
            planned_deadline TIME
        );
        '''.format(name))
        self.connection.commit()

    def chejiancaigou_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
            caigoupin_id INTEGER PRIMARY KEY,
            caigou_amount INTEGER NOT NULL,
            ddl_time INTEGER
        );
        """.format(name))
        self.connection.commit()

    def chejianzuoye_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
            chejian_id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL,
            product_amount INTEGER NOT NULL,
            ddl_time INTERGER
        );
        """.format(name))
        self.connection.commit()

    def paigong_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
            work_id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL,
            work_request varchar(30) NOT NULL,
            work_time INTEGER
        );
        """.format(name))
        self.connection.commit()

    def lingliao_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
            goods_id INTEGER PRIMARY KEY,
            goods_amount INTEGER NOT NULL,
            needed_time INTEGER NOT NULL
        );
        """.format(name))
        self.connection.commit()

    def insert_table(self, table_name, col_name: list, values: list):

        cursor = self.connection.cursor()
        cmd = f"INSERT INTO {table_name} (" + ",".join(col_name) + \
              f") VALUES ("
        for i in range(len(values)):
            cmd += f"'{values[i]}',"
        cmd = cmd[:-1]+");"
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
            for k,v in dicts.items():
                cmd += "{} = '{}' ".format(k,v)
            # print(cmd)
            cursor.execute(cmd)
            # print(" | ".join(self.params))
        else:
            cmd = "SELECT " + ", ".join(col) + " FROM {} WHERE ".format(table_name)
            for k,v in dicts.items():
                cmd += "{} = '{}' ".format(k,v)
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
        for k,v in kwargs.items():
            cmd += "{} = '{}' ".format(k,v)
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

    def close(self):
        self.connection.commit()
        self.connection.close()

    def MPS_insert(self):
        MPS = self.find_info("MPS_table", [])
        for i in range(len(MPS)):
            db.delete("MPS_table", product_id=i+1)
        db1 = XTDataBase("../../test.db")
        BOM1 = db1.where("xt_bom_bike", ["ID"], LAYER=1)
        for i in range(len(BOM1)):
            self.insert_table("MPS_table", ["product_id", "planned_amount", "planned_deadline"],[BOM1[i][0], 1000, date(2024,12,31)])

    def MRP_calculate(self):
        MPS = self.find_info("MPS_table", [])
        MRP = self.find_info("MRP_table", [])
        row = len(MPS)
        row2 = len(MRP)
        for i in range(row):
            MPS_amount = self.where("MPS_table", ["planned_amount"], product_id=i+1)
            if MPS_amount != []:
                MRP_amount = MPS_amount[0][0]
                MPS_planned_deadline = self.where("MPS_table", ["planned_deadline"], product_id=i+1)
                MRP_ddl = datetime.strptime(MPS_planned_deadline[0][0], "%Y-%m-%d")
                MRP_ddl_date = MRP_ddl.date() - timedelta(weeks=4)
                if i >= row2:
                    self.insert_table("MRP_table", ["product_id","planned_amount","planned_deadline"], [i+1, MRP_amount, MRP_ddl_date])
                else:
                    self.update("MRP_table", {"planned_amount": MRP_amount}, product_id=i+1)

        db1 = XTDataBase("../../test.db")
        db2 = XSDataBase("../../xs/xs_sql.db")
        BOM1 = db1.sql_cmd("SELECT ID FROM xt_bom_bike WHERE LAYER >= 2")



    def chejianzuoye_cal(self):
        db1 = XTDataBase("../../test.db")
        BOM_zuoye = db1.where("xt_bom_bike", ["ID"], BUY="否")

    def caigou_cal(self):
        db1 = XTDataBase("../../test.db")
        BOM_caigou = db1.where("xt_bom_bike", ["ID"], BUY="是")

    def paigong_cal(self):
        pass

    def lingliao_cal(self):
        pass




if __name__ == "__main__":
    db = JHDataBase("JHdatabase.db")

    db.MPS_table("MPS_table")
    db.MRP_table("MRP_table")
    db.chejiancaigou_table("caigou_table")
    db.chejianzuoye_table("zuoye_table")
    db.paigong_table("paigong_table")
    db.lingliao_table("lingliao_table")

    # db.insert_table("MPS_table",["product_id","planned_amount","planned_deadline"],[1, 100, date(2024,12,31)])

    db.MPS_insert()
    db.MRP_calculate()

    # for i in range (20):
    #     db.delete("MPS_table", product_id = i+1)
    #     db.delete("MRP_table", product_id = i+1)
