from abc import ABC,abstractmethod
from enum import Enum

if __name__ == "__main__":
    from .xt_module import *
else:
    from xt_module import *

def str_null(data,null):
    for i in range(len(data)):
        if null[i] == None and type(data[i]) == str:
            if data[i] == "":
                raise ValueError("NOT NULL ERROR")

class AuthorityError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class OperationCode(Enum):
    XT_BOMS_CHANGE="修改了BOM表"
    XT_BOM_CHANGE="修改了BOM表的值"
    XT_LINE_CHANGE="修改了工艺路线"
    XT_WORK_CHANGE="修改了工序"
    XT_GROUP_CHANGE="修改了组织信息"
    XT_WORKER_CHANGE="修改了人员信息"
    XT_CHARACTER_CHANGE="修改了角色信息"
    XT_LOG_CHANGE="修改了日志信息"
    CG_CHANGE="修改了采购信息"
    JH_CHANGE="查询了计划信息"
    KC_CHANGE = "修改了库存信息"
    XS_CHANGE= "修改了销售信息"
class BaseContainer(ABC):
    def __init__(self,authority):
        self.authority = authority


    @abstractmethod
    def register(self,authority):
        """
        在此处对所有模块进行注册
        """
        pass

class XtContainer(BaseContainer):

    def __init__(self,authority,db:str,user_name):
        super().__init__(authority)
        self.log = XtLogModule(1,db)
        self.production = XtProductionModule(2,db)
        self.member = XtMemberModule(4,db)
        self.register(self.authority)
        self.user_name = user_name

    def register(self,authority):
        self.log.authority_check(self.authority)
        self.production.authority_check(self.authority)
        self.member.authority_check(self.authority)

    def generate_log(self,operation:OperationCode):
        self.log.generate_log(self.user_name,operation.value)

    def export_log(self):
        if not self.log.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.log.export_log()


    def query_log(self,*data,mode=1):
        if not self.log.is_activity():
            raise AuthorityError("受限制的访问权限")
        length = len(data)
        if mode == 0 and length==1:
            return self.log.search_by_user(data[0])
        elif mode ==1 and length >0 and length <= 6:
            return self.log.search_by_date(*data)
        raise ValueError("日志查询值不正确")

    def delete_log(self,*params):
        if not self.log.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.log.delete_by_date(*params)
        self.generate_log(OperationCode.XT_LOG_CHANGE)

    """
        以下为对BOM表的操作
    """
    def create_bom(self,name):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.create_bom("xt_bom_"+name)
        self.generate_log(OperationCode.XT_BOMS_CHANGE)

    def find_boms(self):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        result = self.production.db.sql_cmd('SELECT name FROM sqlite_master WHERE type="table" AND name LIKE "xt_bom_%"')
        return result

    def find_bom(self,text):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        result = self.production.db.sql_cmd(f'SELECT name FROM sqlite_master WHERE type="table" AND name LIKE "xt_bom_%{text}%"')
        return result

    def remove_boms(self,name):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.remove_boms("xt_bom_"+name)
        self.generate_log(OperationCode.XT_BOMS_CHANGE)

    def delete_bom(self,name,id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.delete_bom("xt_bom_"+name,id)
        ids = self.get_line_ids(name,id)
        for id in ids:
            self.del_line(id[0])
        self.generate_log(OperationCode.XT_BOM_CHANGE)

    def get_in_bom(self,name):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.production.get_in_bom("xt_bom_"+name)

    def update_bom(self,name,data):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        head = ["ID","LAYER","NAME","PARENT","NUM","COST","CYCLE","BUY","ANNOTATION"]
        ids = self.get_ids(name)
        for i in range(len(ids)):
            ids[i] = ids[i][0]

        for i in range(len(data)):
            str_null(data[i],[None,None,None,None,None,None,None,None,""])
            if data[i][0] in ids:
                dicts={}

                for j in range(1,len(data[i])):
                    dicts[head[j]] = data[i][j]
                self.production.update_bom("xt_bom_"+name,dicts,data[i][0])
            else:
                self.production.add_bom("xt_bom_"+name,head,data[i])

        self.generate_log(OperationCode.XT_BOM_CHANGE)
        return True

    def get_ids(self,name):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.production.get_ids("xt_bom_"+name)

    """
    以下为对工艺路线表操作
    """

    def update_line(self,bom_name,bom_id,data):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        head = ["LINE_ID", "NAME","CHEJIAN","DESC"]
        ids = self.get_line_ids(bom_name,bom_id)
        for i in range(len(ids)):
            ids[i] = ids[i][0]

        for i in range(len(data)):
            str_null(data[i], [None, None, None,""])
            if data[i][0] in ids:
                dicts = {}

                for j in range(1, len(data[i])):
                    dicts[head[j]] = data[i][j]
                self.production.update_line(dicts, data[i][0])
            else:
                self.production.add_line("xt_bom_"+bom_name,bom_id, head, data[i])
        self.generate_log(OperationCode.XT_LINE_CHANGE)
        return True

    def del_line(self,id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.delete_line(id)
        self.generate_log(OperationCode.XT_LINE_CHANGE)

    def get_lines(self,bom_name,bom_id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        bl_name = "line"+"_"+"xt_bom_"+bom_name
        lines = self.production.get_line(bl_name,bom_id)
        return lines

    def find_lines(self,bom_name,bom_id,text):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        bl_name = "line" + "_" + "xt_bom_" + bom_name
        lines = self.production.db.sql_cmd(f'SELECT * FROM line WHERE NAME LIKE "%{text}%" AND LINE_ID IN (SELECT LINE_ID FROM {bl_name} WHERE ID={bom_id})')
        return lines

    def get_line_ids(self,bom_name,bom_id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        bl_name = "line"+"_"+"xt_bom_"+bom_name
        ids = self.production.get_line_ids(bl_name,bom_id)
        return ids

    """
    以下为对工序操作
    """
    def update_work(self,line_id,data):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        head = ["WORK_ID","TIME","WC", "DESC", "LINE_ID"]
        ids = self.get_work_ids(str(line_id))
        for i in range(len(ids)):
            ids[i] = ids[i][0]

        for i in range(len(data)):
            str_null(data[i], [None, None,None,"", None])
            if data[i][0] in ids:
                dicts = {}

                for j in range(1, len(data[i])):
                    dicts[head[j]] = data[i][j]
                self.production.update_work("work"+str(line_id), dicts, data[i][0])
            else:
                self.production.add_work("work"+str(line_id), head, data[i])
        self.generate_log(OperationCode.XT_WORK_CHANGE)
        return True
    def del_work(self,line_id,id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.delete_work("work" + str(line_id),id)
        self.generate_log(OperationCode.XT_WORK_CHANGE)

    def get_works(self,line_id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        work_name = "work" + str(line_id)
        works = self.production.get_work(work_name)
        return works

    def get_work_ids(self,line_id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        work_name = "work"+str(line_id)
        ids = self.production.get_work_ids(work_name)
        return ids

    """
    以下为组织管理操作
    """
    def get_groups(self):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.member.get_groups()



    def add_group(self,data):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        str_null(data,[None,None,""])
        self.member.add_group(["NAME","FATHER","DES"],data)
        self.generate_log(OperationCode.XT_GROUP_CHANGE)



    def del_group(self,name):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.delete_group(name)
        self.generate_log(OperationCode.XT_GROUP_CHANGE)

    """
    以下为角色管理操作
    """
    def get_characters(self,user_id=None):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.member.get_characters(user_id)

    def add_character(self,data):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.add_character(["ID","CHARACTER"],data)
        self.generate_log(OperationCode.XT_CHARACTER_CHANGE)


    def new_character(self,data):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        str_null(data,[None,None])
        self.member.new_character(["CHARACTER","AUTHORITY"],data)
        self.generate_log(OperationCode.XT_CHARACTER_CHANGE)

    def rem_character(self,name):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.remove_character(name)
        self.generate_log(OperationCode.XT_CHARACTER_CHANGE)

    def del_character(self,worker_id,character):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.delete_character(worker_id,character)
        self.generate_log(OperationCode.XT_WORKER_CHANGE)

    """
    以下为用户管理操作
    """

    def get_worker_group(self,group_name):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.member.get_worker_group(group_name)

    def get_worker(self,worker_id):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.member.get_worker(worker_id)

    def get_workers(self):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.member.get_workers()

    def get_pwd(self,user_name):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.member.get_pwd(user_name)

    def get_authority(self,user_name):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.member.get_authority(user_name)


    def add_worker(self,group,character,data):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        str_null(data,[None,None,None,None,None,None])
        self.member.add_worker(group,character,["NAME","AGE","GENDER","PLACE","USER_NAME","PASSWORD"],data)
        self.generate_log(OperationCode.XT_WORKER_CHANGE)

    def del_worker(self,worker_id):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.delete_worker(worker_id)
        self.generate_log(OperationCode.XT_WORKER_CHANGE)

    def update_worker(self,worker_id,data):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        head = ["NAME","AGE","GENDER","PLACE","USER_NAME","PASSWORD","DES"]
        dicts = {}
        for i in range(len(data)):
            str_null(data, [None, None, None,None,None,None,""])
            dicts[head[i]] = data[i]
        self.member.update_worker(worker_id,dicts)
        self.generate_log(OperationCode.XT_WORKER_CHANGE)
        return True

    def update_worker_root(self,worker_id):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.update_worker_root(worker_id)
        self.generate_log(OperationCode.XT_WORKER_CHANGE)

    def update_worker_group(self,worker_id,group):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.update_worker_root(worker_id,group)
        self.generate_log(OperationCode.XT_WORKER_CHANGE)

    def change_pwd(self,user_name,pwd):
        self.member.change_pwd(user_name,pwd)
        self.generate_log(OperationCode.XT_WORKER_CHANGE)



if __name__ == "__main__":
    c = XtContainer(3,"test.db")
    print(c.generate_log("test the container"))
    # str_null(["a","","4"],[None,None,None])
