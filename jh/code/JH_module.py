from JH_SQL import JHDataBase

class BaseModule:
    def __init__(self, operation_id):
        self.id = operation_id
        self.active = False

    ## 鉴权函数
    def authority_check(self, authority):
        if authority & self.id:
            self.active = True

    ## 模块是否启用判断
    def is_activity(self):
        return self.active
class JH_Module(BaseModule):
    def __init__(self):
        super().__init__()
        self.JH_db = JHDataBase()

    def create(self, table_name):
        self.JH_db.MPS_table(self, table_name)
        self.JH_db.MRP_table(self, table_name)
        self.JH_db.chejiancaigou_table(self, table_name)
        self.JH_db.chejianzuoye_table(self, table_name)
        self.JH_db.paigong_table(self, table_name)
        self.JH_db.lingliao_table(self, table_name)

    def insert(self, table_name):
        self.JH_db.insert_table(self, table_name, ["col_name: list, values: list"])

    def search(self, table_name):
        self.JH_db.find_info(self, table_name, [])