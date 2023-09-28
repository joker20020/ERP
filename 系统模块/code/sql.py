import sqlite3 as sql

class XTDataBase:
    def __init__(self,file_path):
        self.connection = sql.connect(file_path)
        self.sql_cmd("PRAGMA foreign_keys=ON")

    ## 数据库操作方法
    def insert_table(self,table_name,col_name:list,values:list):

        cursor = self.connection.cursor()
        cmd = f"INSERT INTO {table_name} (" + ",".join(col_name) + \
              f") VALUES ("
        for i in range(len(values)):
            cmd += f"'{values[i]}',"
        cmd = cmd[:-1]+");"
        # print(cmd)
        cursor.execute(cmd)
        self.connection.commit()

    def find_info(self,table_name,args):
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

    """
    name:表名
    
    func:创建一张bom表
    """
    def xt_bom_create_table(self,name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        LAYER INTEGER NOT NULL,
        NAME TEXT NOT NULL,
        NUM INTEGER NOT NULL,
        DESC TEXT NOT NULL,
        COST REAL NOT NULL,
        CYCLE REAL NOT NULL,
        ANNOTATION TEXT
        );
        """.format(name))
        self.connection.commit()

    """
        name:表名
        parent:外部键表名

        func:创建一张bom-line表
    """
    def xt_bl_create_table(self,name,bom,line):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                ID INTEGER NOT NULL,
                LINE_ID INTEGER NOT NULL,
                FOREIGN KEY (ID) REFERENCES {}(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (LINE_ID) REFERENCES {}(LINE_ID) ON DELETE CASCADE ON UPDATE CASCADE
                );
                """.format(name,bom,line))
        self.connection.commit()

    """
        name:表名
        
        func:创建一张工艺路线表
    """
    def xt_line_create_table(self,name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                LINE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DESC TEXT,
                WC TEXT NOT NULL
                );
                """.format(name))
        self.connection.commit()

    """
        name:表名
        parent:外部键表名

        func:创建一张工序表
    """
    def xt_work_create_table(self,name,parent):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                WORK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DESC TEXT,
                LINE_ID INTEGER NOT NULL,
                FOREIGN KEY (LINE_ID) REFERENCES {}(LINE_ID) ON DELETE CASCADE ON UPDATE CASCADE
                );
                """.format(name,parent))
        self.connection.commit()





    def close(self):
        self.connection.commit()
        self.connection.close()


if __name__ == "__main__":
    db = XTDataBase("test.db")
    # db.xt_bom_create_table("bom1")
    # db.xt_bl_create_table("bl1","bom1","line1")
    # db.xt_line_create_table("line1")
    # db.xt_work_create_table("work1","line1")
    # db.insert_table("bom1",["LAYER","NAME","NUM","DESC","COST","CYCLE"],[1,"BOM1_TEST",2,"This is a test!!!",4.5,3.4])
    # db.insert_table("bom1", ["LAYER", "NAME", "NUM", "DESC", "COST", "CYCLE"],[1, "BOM1_TEST", 3, "This is a test!!!", 4.5, 3.4])
    # db.insert_table("line1", ["DESC", "WC"], ["TEST", "WC TEST"])
    # db.insert_table("bl1", ["ID", "LINE_ID"],[1,1])
    # db.insert_table("bl1", ["ID", "LINE_ID"], [2, 1])
    # db.insert_table("work1", ["DESC", "LINE_ID"], ["TEST", 1])
    # db.insert_table("work1", ["DESC", "LINE_ID"], ["TEST", 1])
    # db.insert_table("work1", ["DESC", "LINE_ID"], ["TEST", 1])
    # db.delete("bom1",ID=1)
    # db.delete("line1",LINE_ID=1)
    print(db.find_info("bom1",[]))
    print(db.find_info("bl1",[]))
    print(db.find_info("line1", []))
    print(db.find_info("work1", []))
    # db.find_info("test",["FILE_PATH"])
    # db.where("test",FORMAT="step")
    # db.where("test","FILE_PATH","NAME",FORMAT="step")
    # db.delete("test",FORMAT="step")
    # db.find_info("test")
