from abc import ABC,abstractmethod
import xt_module as md

def str_null(data,null):
    for i in range(len(data)):
        if null[i] == None and type(data[i]) == str:
            if data[i] == "":
                raise ValueError("NOT NULL ERROR")

class AuthorityError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class BaseContainer:
    def __init__(self,authority):
        self.authority = authority


    @abstractmethod
    def register(self,authority):
        """
        在此处对所有模块进行注册
        """
        pass

class XtContainer(BaseContainer):

    def __init__(self,authority,db:str):
        super().__init__(authority)
        self.log = md.XtLogModule(1,db)
        self.production = md.XtProductionModule(2,db)
        self.member = md.XtMemberModule(4,db)
        self.register(self.authority)

    def register(self,authority):
        self.log.authority_check(self.authority)
        self.production.authority_check(self.authority)
        self.member.authority_check(self.authority)

    def generate_log(self, user_name, operation):
        if not self.log.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.log.generate_log(user_name,operation)

    """
        以下为对BOM表的操作
    """
    def create_bom(self,name):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.create_bom("xt_bom_"+name)

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

    def delete_bom(self,name,id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.delete_bom("xt_bom_"+name,id)

    def get_in_bom(self,name):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        return self.production.get_in_bom("xt_bom_"+name)

    def update_bom(self,name,data):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        head = ["ID","LAYER","NAME","DESC","COST","CYCLE","BUY","ANNOTATION"]
        ids = self.get_ids(name)
        for i in range(len(ids)):
            ids[i] = ids[i][0]

        for i in range(len(data)):
            str_null(data[i],[None,None,None,None,None,None,None,""])
            if data[i][0] in ids:
                dicts={}

                for j in range(1,len(data[i])):
                    dicts[head[j]] = data[i][j]
                self.production.update_bom("xt_bom_"+name,dicts,data[i][0])
            else:
                self.production.add_bom("xt_bom_"+name,head,data[i])

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
        head = ["LINE_ID", "NAME","DESC", "WC"]
        ids = self.get_line_ids(bom_name,bom_id)
        for i in range(len(ids)):
            ids[i] = ids[i][0]

        for i in range(len(data)):
            str_null(data[i], [None, None, "", None])
            if data[i][0] in ids:
                dicts = {}

                for j in range(1, len(data[i])):
                    dicts[head[j]] = data[i][j]
                self.production.update_line(dicts, data[i][0])
            else:
                self.production.add_line("xt_bom_"+bom_name,bom_id, head, data[i])

        return True

    def del_line(self,id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.delete_line(id)

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
        head = ["WORK_ID", "DESC", "LINE_ID"]
        ids = self.get_work_ids(str(line_id))
        for i in range(len(ids)):
            ids[i] = ids[i][0]

        for i in range(len(data)):
            str_null(data[i], [None, "", None])
            if data[i][0] in ids:
                dicts = {}

                for j in range(1, len(data[i])):
                    dicts[head[j]] = data[i][j]
                self.production.update_work("work"+str(line_id), dicts, data[i][0])
            else:
                self.production.add_work("work"+str(line_id), head, data[i])

        return True
    def del_work(self,line_id,id):
        if not self.production.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.production.delete_work("work" + str(line_id),id)

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



    def del_group(self,name):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.delete_group(name)

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
        return self.member.add_character(["ID","CHARACTER"],data)


    def new_character(self,data):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        str_null(data,[None,None])
        self.member.new_character(["CHARACTER","AUTHORITY"],data)

    def rem_character(self,name):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.remove_character(name)

    def del_character(self,worker_id,character):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.delete_character(worker_id,character)

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

    def del_worker(self,worker_id):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.delete_worker(worker_id)

    def update_worker(self,worker_id,data):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        head = ["NAME","AGE","GENDER","PLACE","USER_NAME","PASSWORD","DES"]
        dicts = {}
        for i in range(len(data)):
            str_null(data, [None, None, None,None,None,None,""])
            dicts[head[i]] = data[i]
        self.member.update_worker(worker_id,dicts)
        return True

    def update_worker_root(self,worker_id):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.update_worker_root(worker_id)

    def update_worker_group(self,worker_id,group):
        if not self.member.is_activity():
            raise AuthorityError("受限制的访问权限")
        self.member.update_worker_root(worker_id,group)






if __name__ == "__main__":
    c = XtContainer(3,"test.db")
    print(c.generate_log("jdy","test the container"))
    # str_null(["a","","4"],[None,None,None])
