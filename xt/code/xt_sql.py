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

    def find_info(self, table_name, args,**order):
        cursor = self.connection.cursor()
        cmd = None
        if not len(args):
            cmd = "SELECT * FROM {} ".format(table_name)
        else:
            cmd = "SELECT " + ", ".join(args) + " FROM {} ".format(table_name)
        if len(order):
            cmd += "ORDER BY "
            for key,value in order.items():
                cmd += f"{key} {value},"
            cmd = cmd[:-1]+";"

        cursor.execute(cmd)

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
            cmd += "{} = '{}' AND ".format(k, v)
        # print(cmd)
        cursor.execute(cmd[:-4])
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

    func:创建一张bom表
    """

    def xt_bom_create_table(self, name):
        cursor = self.connection.cursor()
        # AUTOINCREMENT
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
        ID INTEGER PRIMARY KEY ,
        LAYER INTEGER NOT NULL,
        NAME TEXT NOT NULL,
        PARENT INTEGER NOT NULL,
        COST REAL NOT NULL,
        CYCLE REAL NOT NULL,
        BUY INTEGER NOT NULL,
        ANNOTATION TEXT
        );
        """.format(name))
        self.connection.commit()

    """
    name:表名
    parent:外部键表名

    func:创建一张bom-line表
    """

    def xt_bl_create_table(self, name, bom, line):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                ID INTEGER NOT NULL,
                LINE_ID INTEGER NOT NULL,
                FOREIGN KEY (ID) REFERENCES {}(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (LINE_ID) REFERENCES {}(LINE_ID) ON DELETE CASCADE ON UPDATE CASCADE
                );
                """.format(name, bom, line))
        self.connection.commit()

    """
    name:表名

    func:创建一张工艺路线表
    """

    def xt_line_create_table(self, name):
        cursor = self.connection.cursor()
        # AUTOINCREMENT
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                LINE_ID INTEGER PRIMARY KEY ,
                NAME TEXT NOT NULL,
                CHEJIAN TEXT NOT NULL,
                DESC TEXT
                );
                """.format(name))
        self.connection.commit()

    """
    name:表名
    parent:外部键表名

    func:创建一张工序表
    """
    def xt_work_create_table(self, name, parent):
        cursor = self.connection.cursor()
        # AUTOINCREMENT
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                WORK_ID INTEGER PRIMARY KEY ,
                TIME INTEGER NOT NULL,
                WC TEXT NOT NULL,
                DESC TEXT, 
                LINE_ID INTEGER NOT NULL,
                FOREIGN KEY (LINE_ID) REFERENCES {}(LINE_ID) ON DELETE CASCADE ON UPDATE CASCADE
                );
                """.format(name, parent))
        self.connection.commit()

    """
    name:表名

    func:创建组织结构表
    """
    def xt_group_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                        NAME TEXT PRIMARY KEY ,
                        FATHER TEXT NOT NULL,
                        DES TEXT
                        );
                        """.format(name))
        self.connection.commit()

    """
    name:表名
    worker:外部键表名
    group:外部键表名

    func:创建人员组织表
    """
    def xt_wg_create_table(self, name, worker, group):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                ID INTEGER NOT NULL,
                ORG TEXT NOT NULL,
                FOREIGN KEY (ID) REFERENCES {}(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (ORG) REFERENCES {}(NAME) ON DELETE CASCADE ON UPDATE CASCADE
                );
                """.format(name, worker, group))
        self.connection.commit()

    """
    name:表名
    character:角色表

    func:创建人员信息表
    """
    def xt_worker_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT NOT NULL,
                        AGE INTEGER NOT NULL,
                        GENDER TEXT NOT NULL,
                        PLACE TEXT NOT NULL,
                        USER_NAME TEXT NOT NULL,
                        PASSWORD TEXT NOT NULL,
                        DES TEXT
                        );
                        """.format(name))
        self.connection.commit()

    """
        name:表名
        worker:外部键表名
        group:外部键表名

        func:创建人员角色表
        """

    def xt_wc_create_table(self, name, worker, character):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                    ID INTEGER NOT NULL,
                    CHARACTER TEXT NOT NULL,
                    FOREIGN KEY (ID) REFERENCES {}(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (CHARACTER) REFERENCES {}(CHARACTER) ON DELETE CASCADE ON UPDATE CASCADE
                    );
                    """.format(name, worker, character))
        self.connection.commit()

    """
    name:表名

    func:创建角色权限表
    """
    def xt_character_create_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                        CHARACTER TEXT PRIMARY KEY,
                        AUTHORITY INTEGER NOT NULL
                        );
                        """.format(name))
        self.connection.commit()




    def close(self):
        self.connection.commit()
        self.connection.close()

class Logger(XTDataBase):
    def __init__(self,file_path):
        import time
        super().__init__(file_path)
        self.xt_log_create_table()

    def xt_log_create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS LOG (
                            DATE TEXT NOT NULL,
                            USER TEXT NOT NULL,
                            OPERATION TEXT NOT NULL
                            );
                            """)
        self.connection.commit()


    ## 日志生成
    def generate(self,user_name,operation):
        operation_time = time.strftime("%Y-%m-%d|%H:%M:%S")
        self.insert_table("LOG",["DATE","USER","OPERATION"],[operation_time,user_name,operation])

    ## 通过日期查询
    def search_by_date(self,*params):
        if len(params)<=3:
            date = ""
            for each in params:
                date += "{:02}".format(each)
                date += "-"
            if len(params)==3:
                date = date[:-1]
            date += "*"
        else:
            date = "{}-{:02}-{}|".format(params[0],params[1],params[2])
            for i in range(3,len(params)):
                date += "{:02}".format(params[i])
                date += ":"
            if len(params)<6:
                date += "*"
            elif len(params)==6:
                date = date[:-1]
        cmd = "SELECT * FROM LOG WHERE DATE GLOB '{}' ;".format(date)
        return self.sql_cmd(cmd)

    ## 通过操作用户查询
    def search_by_user(self,user):
        cmd = "SELECT * FROM LOG WHERE USER='{}';".format(user)
        return self.sql_cmd(cmd)

    def delete_by_user(self,user):
        cmd = "DELETE FROM LOG WHERE USER='{}';".format(user)
        return self.sql_cmd(cmd)

    def delete_by_date(self,*params):

        if len(params)<=3:
            date = ""
            for each in params:
                date += "{:02}".format(each)
                date += "-"
            if len(params)==3:
                date = date[:-1]
            date += "*"
        else:
            date = "{}-{:02}-{}|".format(params[0],params[1],params[2])
            for i in range(3,len(params)):
                date += "{:02}".format(params[i])
                date += ":"
            if len(params)<6:
                date += "*"
            elif len(params)==6:
                date = date[:-1]
        cmd = "DELETE FROM LOG WHERE DATE GLOB '{}' ;".format(date)
        return self.sql_cmd(cmd)

    def export_log(self):
        log = self.sql_cmd("SELECT * FROM LOG")
        with open("log.txt","w+") as f:
            for each in log:
                f.write("   ".join(each))
                f.write("\n")




if __name__ == "__main__":
    db = XTDataBase("test.db")
    logger = Logger("test.db")
    logger.generate("jdy","test operation")
    # print(db.sql_cmd("SELECT name FROM sqlite_master"))
    # print(db.sql_cmd('PRAGMA table_info(bom1)'))
    # db.insert_table("xt_bom_1",["LAYER","NAME","NUM","DESC","COST","CYCLE","BUY"],[1,"BOM1_TEST",2,"This is a test!!!",4.5,3.4,True])
    # print(logger.search_by_date(2023,10,22,18,1,4))
    # print(logger.search_by_user("jdy"))
    # logger.export_log()
    # logger.delete_by_date(2023,9,28,13,55)
    # logger.delete_by_user("jdy")
    # print(logger.find_info("LOG",[]))


    # print(db.sql_cmd("SELECT name FROM sqlite_master WHERE type='table'"))
    # print(db.sql_cmd("SELECT * FROM sqlite_master WHERE name='line'"))
    # print(db.sql_cmd("PRAGMA table_info(sqlite_master)"))

    # db.xt_bom_create_table("bom1")
    # db.xt_bl_create_table("bl1","bom1","line1")
    # db.xt_line_create_table("line1")
    # db.xt_work_create_table("work1","line1")
    # db.xt_group_create_table("group1")
    # db.xt_character_create_table("character1")
    # db.xt_worker_create_table("worker1","character1")
    # db.xt_wg_create_table("wg1","worker1","group1")

    # db.insert_table("bom1",["LAYER","NAME","NUM","DESC","COST","CYCLE","BUY"],[1,"BOM1_TEST",2,"This is a test!!!",4.5,3.4,True])
    # db.insert_table("bom1", ["LAYER", "NAME", "NUM", "DESC", "COST", "CYCLE","BUY"],[1, "BOM1_TEST", 3, "This is a test!!!", 4.5, 3.4,False])
    # db.insert_table("line1", ["NAME","DESC", "WC"], ["test1","TEST", "WC TEST"])
    # db.insert_table("bl1", ["ID", "LINE_ID"],[1,1])
    # db.insert_table("bl1", ["ID", "LINE_ID"], [2, 1])
    # db.insert_table("work1", ["DESC", "LINE_ID"], ["TEST", 1])
    # db.insert_table("work1", ["DESC", "LINE_ID"], ["TEST", 1])
    # db.insert_table("work1", ["DESC", "LINE_ID"], ["TEST", 1])
    # db.insert_table("group1",["NAME","CHILD","DES"],["TEST","CTEST","111"])
    # db.insert_table("group1", ["NAME", "CHILD", "DES"], ["CTEST", "CCTEST", "222"])
    # db.insert_table("character1",["CHARACTER","AUTHORITY"],["admin",8])
    # db.insert_table("worker1",["ID","NAME","AGE","SEX","PLACE","USER_NAME","PASSWORD","CHARACTER","DES"],[1,"jdy",88,"男","asd","dddd","123456","admin","test"])
    # db.insert_table("worker1",["ID","NAME","AGE","SEX","PLACE","USER_NAME","PASSWORD","CHARACTER","DES"],[2,"jdy",88,"男","asd","dddd","123456","admin","test"])
    # db.insert_table("wg1",["ID","ORG"],[1,"TEST"])
    # db.insert_table("wg1", ["ID", "ORG"], [2, "CTEST"])

    # db.delete("bom1",ID=1)
    # db.delete("line",LINE_ID=1)
    # db.delete("character1",CHARACTER="admin")
    # db.delete("worker1",ID=1)
    # db.delete("group1",NAME="CTEST")
    # db.drop("line")
    # db.drop("work1")

    # print(db.find_info("bom1", []))
    # print(db.find_info("bl1", []))
    # print(db.find_info("line1", []))
    # print(db.find_info("work1", []))
    # print(db.find_info("group1", []))
    # print(db.find_info("character1", []))
    # print(db.find_info("worker1", []))
    # print(db.find_info("wg1", []))

    # db.find_info("test",["FILE_PATH"])
    # db.where("test",FORMAT="step")
    # db.where("test","FILE_PATH","NAME",FORMAT="step")
    # db.delete("test",FORMAT="step")
    # db.find_info("test")
