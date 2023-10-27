if __name__ == "__main__":
    from .xt_sql import Logger,XTDataBase
else:
    from xt_sql import Logger, XTDataBase


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
        bom_ids = self.get_ids(name)
        for bom_id in bom_ids:
            bom_id = bom_id[0]
            lines = self.get_line_ids("line"+"_"+name,bom_id)
            for line in lines:
                line = line[0]
                self.db.drop("work"+str(line))
                self.db.delete(line_name,LINE_ID=line)
        self.db.drop(name)
        self.db.drop(line_name + "_" + name)

    def delete_bom(self,name,id):
        lines = self.get_line_ids("line" + "_" + name, id)
        for line in lines:
            line = line[0]
            self.delete_line(line)
        self.db.delete(name,ID=id)

    def delete_line(self,id):
        self.db.delete("line",LINE_ID=id)
        self.db.drop("work"+str(id))

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

        if self.db.where("sysgroup",[],NAME="root") == []:
            self.db.insert_table("sysgroup",["NAME","FATHER","DES"],["root","HIDDEN CAN NOT BE USED",""])

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

    def add_worker(self,group,character,col,data,name="worker"):
        self.db.insert_table(name, col, data)
        worker_id = self.db.find_info(name,["ID"])[-1][0]
        self.bind_gw(worker_id,group)
        self.bind_wc(worker_id,character)

    def add_character(self,col,data,name="worker_character"):
        return self.db.insert_table(name,col,data)

    def new_character(self,col,data,name="character"):
        return self.db.insert_table(name,col,data)


    def delete_group(self,group_name,name="sysgroup"):
        self.db.delete(name,NAME=group_name)

    def remove_character(self,character,name="character"):
        self.db.delete(name,CHARACTER=character)

    def delete_character(self,worker_id,character,name="worker_character"):
        self.db.delete(name,ID=worker_id,CHARACTER=character)

    def delete_worker(self,worker_id,name="worker"):
        self.db.delete(name,ID=worker_id)

    def get_groups(self,name="sysgroup"):
        return self.db.find_info(name,[])

    def get_pwd(self,user_name,name="worker"):
        return self.db.where(name,["PASSWORD"],USER_NAME=user_name)

    def get_authority(self,user_name,name="character"):
        worker_id = self.db.where("worker",["ID"],USER_NAME=user_name)[0][0]
        return self.db.sql_cmd(f"SELECT AUTHORITY FROM {name} WHERE CHARACTER IN (SELECT CHARACTER FROM worker_character WHERE ID={worker_id})")

    def get_characters(self,user_id=None,name="character"):
        if user_id:
            return self.db.sql_cmd(f"SELECT CHARACTER FROM {name} WHERE CHARACTER IN (SELECT CHARACTER FROM worker_character WHERE ID={user_id})")
        else:
            return self.db.find_info(name,[])

    def get_worker_group(self,group_name):
        return self.db.sql_cmd(f"SELECT ID,NAME FROM worker WHERE ID IN (SELECT ID FROM worker_sysgroup WHERE ORG='{group_name}') ")

    def get_worker(self,worker_id,name="worker"):
        return self.db.where(name,[],ID=worker_id)

    def get_workers(self,name="worker"):
        return self.db.find_info(name,[])

    def update_worker(self,worker_id,dicts,name="worker"):
        return self.db.update(name,dicts,ID=worker_id)

    def update_worker_root(self,worker_id,group="root",name="worker_sysgroup"):
        return self.db.update(name,{"ORG":group},ID=worker_id)

    def change_pwd(self,user_name,pwd):
        self.db.update("worker", {"PASSWORD": pwd}, USER_NAME=user_name)
        return


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