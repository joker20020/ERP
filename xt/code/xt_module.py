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
        self.create_line()

    def create_bom(self,name,line_name="line"):
        bl_name = line_name+"_"+name
        self.db.xt_bl_create_table(bl_name,name,line_name)
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
        self.db.insert_table(name, col, data)
        line_id = str(self.db.find_info(name,["LINE_ID"],LINE_ID="ASC")[-1][0])
        self.db.xt_work_create_table("work"+line_id,"line")
        self.bind_bl(bom_name, bom_id,line_id)

    def add_work(self,name,col,data):
        return self.db.insert_table(name,col,data)

    def remove_boms(self,name,line_name="line"):
        self.db.drop(name)
        self.db.drop(line_name+"_"+name)

    def delete_bom(self,name,id):
        self.db.delete(name,ID=id)

    def delete_line(self,id):
        self.db.delete("line",LINE_ID=id)

    def delete_work(self,name,id):
        self.db.delete(name, WORK_ID=id)


    def update_bom(self,name,dicts,id):
        self.db.update(name,dicts,ID=id)

    def update_line(self,dicts,id):
        self.db.update("line",dicts,LINE_ID=id)

    def update_work(self,name,dicts,id):
        self.db.update(name, dicts, WORK_ID=id)

    def get_in_bom(self,name):
        result = self.db.find_info(name,[],ID="ASC")
        return result

    def get_ids(self,name):
        return self.db.find_info(name,["ID"],ID="ASC")

    def get_line_ids(self,name,bom_id):
        return self.db.where(name,["LINE_ID"],ID=bom_id)

    def get_work_ids(self,name):
        return self.db.find_info(name, ["WORK_ID"], WORK_ID="ASC")

    def get_line(self,name,bom_id,line_name="line"):
        cmd = f"SELECT * FROM {line_name} WHERE LINE_ID IN (SELECT LINE_ID FROM {name} WHERE ID={bom_id})"
        return self.db.sql_cmd(cmd)

    def get_work(self,name):
        result = self.db.find_info(name, [], WORK_ID="ASC")
        return result



    def bind_bl(self,bom_name,bom_id,line_id,line_name="line"):
        name = line_name+"_"+bom_name
        self.db.xt_bl_create_table(name,bom_name,line_name)
        self.db.insert_table(name,["ID", "LINE_ID"],[bom_id,line_id])


class XtMemberModule(BaseModule):
    def __init__(self,operation_id,db):
        super().__init__(operation_id)
        self.db = XTDataBase(db)
        self.db.xt_character_create_table("character")
        self.create_group()
        self.create_worker()
        self.db.xt_wg_create_table("worker_sysgroup", "worker", "sysgroup")
        self.db.xt_wc_create_table("worker_character", "worker", "character")

    def create_group(self,name="sysgroup"):
        self.db.xt_group_create_table(name)

    def create_worker(self,name="worker"):
        self.db.xt_worker_create_table(name)

    def search_all(self,name):
        return self.db.find_info(name,[])

    def search_columns(self,name,col:list):
        return self.db.find_info(name, col)

    def add_group(self,col,data,name="sysgroup"):
        return self.db.insert_table(name,col,data)

    def add_worker(self,worker_id,group,character,col,data,name="worker"):
        self.bind_gw(worker_id,group)
        self.bind_wc(worker_id,character)
        return self.db.insert_table(name,col,data)

    def add_character(self,col,data,name="character"):
        return self.db.insert_table(name,col,data)

    def get_groups(self,name="sysgroup"):
        return self.db.find_info(name,[])

    def bind_gw(self,worker_id,group,worker_name="worker",group_name="sysgroup"):
        name = worker_name + "_" + group_name
        self.db.xt_wg_create_table(name,worker_name,group_name)
        self.db.insert_table(name,["ID", "ORG"],[worker_id,group])

    def bind_wc(self,worker_id,character,worker_name="worker",character_name="character"):
        name = worker_name + "_" + character_name
        self.db.xt_wc_create_table(name, worker_name, character_name)
        self.db.insert_table(name, ["ID", "CHARACTER"], [worker_id, character])


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