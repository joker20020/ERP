from xt_sql import Logger
from xt_sql import XTDataBase

class BaseModule:
    def __init__(self,operation_id):
        self.id = operation_id
        self.active = False

    ## 鉴权函数
    def authority_check(self,authority):
        if authority & self.id:
            self.active = True

    ## 模块是否启用判断
    def is_activity(self):
        return self.active

class XtLogModule(BaseModule):
    def __init__(self,operation_id,db):
        super().__init__(operation_id)
        self.logger = Logger(db)

    def search_by_date(self,*params):
        return self.logger.search_by_date(*params)

    def search_by_user(self,user):
        return self.logger.search_by_user(user)

    def generate_log(self, user_name, operation):
        return self.logger.generate(user_name,operation)

    def delete_by_date(self,*params):
        return self.logger.delete_by_date(*params)

    def delete_by_user(self, user):
        return self.logger.delete_by_user(user)

    def export_log(self):
        return self.logger.export_log()

class XtProductionModule(BaseModule):
    def __init__(self,operation_id,db):
        super().__init__(operation_id)
        self.db = XTDataBase(db)

    def create_bom(self,name):
        self.db.xt_bom_create_table(name)

    def create_line(self,name="line"):
        self.db.xt_line_create_table(name)

    def create_work(self,name,line_name):
        self.db.xt_work_create_table(name,line_name)

    def search_all(self,name):
        return self.db.find_info(name,[])

    def search_columns(self,name,col:list):
        return self.db.find_info(name, col)

    def add_bom(self,name,col,data):
        return self.db.insert_table(name,col,data)

    def add_line(self,bom_name,bom_id,col,data,name="line"):
        line_id = self.db.find_info(name,["LINE_ID"])[-1][0]
        self.db.insert_table(name, col, data)
        self.bind_bl(bom_name, name, bom_id,line_id)

    def add_work(self,name,col,data):
        return self.db.insert_table(name,col,data)

    def bind_bl(self,bom_name,bom_id,line_id,line_name="line"):
        name = bom_name+"_"+line_name
        self.db.xt_bl_create_table(name,bom_name,line_name)
        self.db.insert_table(name,["ID", "LINE_ID"],[bom_id,line_id])

class XtMemberModule(BaseModule):
    def __init__(self,operation_id,db):
        super().__init__(operation_id)
        self.db = XTDataBase(db)
        self.db.xt_character_create_table("character")
        self.create_group("group")
        self.create_woker("woker")

    def create_group(self,name):
        self.db.xt_group_create_table(name)

    def create_woker(self,name):
        self.db.xt_work_create_table(name,"character")

    def search_all(self,name):
        return self.db.find_info(name,[])

    def search_columns(self,name,col:list):
        return self.db.find_info(name, col)


    def add_group(self,col,data,name="group"):
        return self.db.insert_table(name,col,data)

    def add_woker(self,col,data,name="woker"):
        return self.db.insert_table(name,col,data)

    def add_character(self,col,data,name="character"):
        return self.db.insert_table(name,col,data)

    def bind_gw(self,woker_id,group,woker_name="woker",group_name="group"):
        name = woker_name +"-"+group_name
        self.db.xt_wg_create_table(name,group_name,group_name)
        self.db.insert_table(name,["ID", "ORG"],[woker_id,group])


if __name__ == "__main__":
    m = BaseModule(4)
    print(m.active)
    m.authority_check(6)
    print(m.active)
    # logm = XtLogModule(4,"test.db")
    # print(logm.search_by_date(2023,9,28,15))
    # print(logm.search_by_user("jdy"))
    pm = XtProductionModule(4,"test.db")
    pm.create_bom("test3")
    print(pm.search_all("test3"))