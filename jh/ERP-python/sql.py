import sqlite3 as sql

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

    def MRP_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {}(
            product_id INTEGER PRIMARY KEY,
            planned_amount INTEGER NOT NULL,
            planned_deadline varchar(20)
        );
        '''.format(name))
        self.connection.commit()

    def worker_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
            worker_id INTEGER PRIMARY KEY,
            work_request varchar(30) NOT NULL
            work_time varchar(20)
        );
        """.format(name))
        self.connection.commit()

    def resource_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
            goods_id INTEGER PRIMARY KEY,
            goods_amount INTEGER NOT NULL 
            goods_time varchar(20) NOT NULL
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

    def sql_cmd(self,cmd):
        cursor = self.connection.cursor()
        cursor.execute(cmd)
        self.connection.commit()
        result = []
        for each in cursor:
            result.append(each)
            # print(each)
        return result

    def where(self,table_name,col,**dicts):
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

    def delete(self,table_name,**kwargs):
        cursor = self.connection.cursor()
        cmd = "DELETE FROM {} WHERE ".format(table_name)
        for k,v in kwargs.items():
            cmd += "{} = '{}' ".format(k,v)
        # print(cmd)
        cursor.execute(cmd[:-1])
        self.connection.commit()

    def update(self,table_name,dicts,**condition):
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


if __name__ == "__main__":
    db = DataBase("test.db")
    db.create_user_table("test")
    db.insert_table("test",["NAME","PASSWORD","KEY"],["112","asdasd","aaa"])
    # print(db.find_info("test",[]))
    print(db.sql_cmd("SELECT * FROM test"))
    # db.find_info("test",["PASSWORD"])
    # db.where("test",FORMAT="step")
    # db.where("test","FILE_PATH","NAME",FORMAT="step")
    # db.delete("test",FORMAT="step")
    # db.find_info("test")
