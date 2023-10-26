import sqlite3
import os
import random

# 定义数据库文件夹名称为 cg_db
db_folder = 'D:/Python/ERPProject/cg_db'

# 父类 cg_database_entity
class cg_database_entity:

    # 先进行初始化设置
    def __init__(self, database_name, table_name, id_column):
        self.database_name = database_name
        self.table_name = table_name        
        self.id_column = id_column
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    # 基础操作 创建一个表
    def create_table(self, table_schema):
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            {table_schema}
        )
        ''')
        self.connection.commit()
        print(f"Created a new table '{self.table_name}'.")

    # 添加数据
    def add_item(self, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?'] * len(kwargs))
        values = tuple(kwargs.values())

        self.cursor.execute(f'''
            INSERT INTO {self.table_name} ({columns})
            VALUES ({placeholders})
        ''', values)
        self.connection.commit()

    # 删去数据
    def delete_item(self, item_id):
        self.cursor.execute(f'''
            DELETE FROM {self.table_name} WHERE {self.id_column} = ?
        ''', (item_id,))
        self.connection.commit()

    # 修改数据
    def update_item(self, item_id, **kwargs):
        set_values = ','.join([f"{key} = ?" for key in kwargs])
        values = tuple(kwargs.values())

        self.cursor.execute(f'''
            UPDATE {self.table_name}
            SET {set_values}
            WHERE {self.id_column} = ?
        ''', (*values, item_id))
        self.connection.commit()

    # 查询数据
    def query_item(self, item_id):
        self.cursor.execute(f'''
            SELECT * FROM {self.table_name} WHERE {self.id_column} = ?
        ''', (item_id,))
        return self.cursor.fetchone()

'''物理表结构
class cg_purchase_list # 采购清单实体
    ├── 'cg_purchase_list_id' 采购清单号，INTEGER，必填，主键
    │
    ├── 'jh_purchase_request_id' 采购请求号，INTEGER，必填，外键
    │
    ├── 'cg_remarks' 备注，TEXT，200
'''
class cg_purchase_list(cg_database_entity):
    table_schema = '''
        cg_purchase_list_id INT PRIMARY KEY NOT NULL,
        jh_purchase_request_id INT NOT NULL,
        cg_remarks CHAR(200)
    '''
    
    # jh_purchase_request_id INT FOREIGN PRIMARY KEY NOT NULL,

    def __init__(self, database_name):
        super().__init__(database_name, 'cg_purchase_list', 'cg_purchase_list_id')

'''物理表结构
class cg_purchase_detail # 采购订单明细
    ├── 'cg_purchase_detail_id' 采购明细号，INTEGER，必填，主键
    │
    ├── 'cg_purchase_list_id' 采购清单号，INTEGER，必填，来自cg_purchase_list的外键
    │
    ├── 'material_code' 物料编码，INTEGER，必填
    │
    ├── 'cg_order_lot' 订货批量，INTEGER，必填
    │
    ├── 'cg_total_price' 商品总价，REAL
    │
    ├── 'cg_receipt_id' 收货单号，INTEGER，16字节，来自cg_receipt_inspection的外键
    │
    ├── 'cg_remarks' 备注，TEXT，200字节
'''
class cg_purchase_detail(cg_database_entity):
    table_schema = '''
        cg_purchase_detail_id INT PRIMARY KEY NOT NULL,
        cg_purchase_list_id INT NOT NULL,
        material_code INT NOT NULL,
        cg_order_lot INT NOT NULL,
        cg_total_price REAL,
        cg_receipt_id INT,
        cg_remarks TEXT(200),
        FOREIGN KEY (cg_purchase_list_id) REFERENCES cg_purchase_list(cg_purchase_list_id)
        FOREIGN KEY (cg_receipt_id) REFERENCES cg_receipt_inspection(cg_receipt_id)
    '''
    
    def __inti__(self, database_name):
        super().__init__(database_name, 'cg_purchase_detail', 'cg_purchase_detail_id')

'''物理表结构
class cg_supplier_info # 供应商资料
    ├── 'cg_supplier_id' 供应商编号，INTEGER，必填，主键
    │
    ├── 'cg_supplier_name' 供应商名称，TEXT，50字节，必填
    │
    ├── 'cg_company_tel' 公司电话，TEXT，30字节
    │
    ├── 'cg_company_address' 公司地址，TEXT，50字节
    │
    ├── 'cg_remarks' 备注，TEXT，2000字节
'''
class cg_supplier_info(cg_database_entity):
    table_schema = '''
        cg_supplier_id INT PRIMARY KEY NOT NULL,
        cg_supplier_name TEXT(50) NOT NULL,
        cg_company_tel TEXT(30),
        cg_company_address TEXT(50),
        cg_remarks TEXT(2000)
    '''

    def __init__(self, database_name):
        super().__init__(database_name, 'cg_supplier_info', 'cg_supplier_id')

'''物理表结构
class cg_receipt_inspection # 收货与检验单
    ├── 'cg_receipt_id' 收货单号，INTEGER，必填，主键
    │
    ├── 'cg_arrival_time' 到货时间，DATETIME，16字节，必填
    │
    ├── 'cg_arrival_quantity' 到货量，INTEGER，必填
    │
    ├── 'cg_quelified_products' 合格品数，INTEGER
    │
    ├── 'cg_inbound_status' 入库状态，NUMERIC，必填
    │
    ├── 'cg_remarks' 备注，TEXT，200字节
'''
class cg_receipt_inspection(cg_database_entity):
    table_schema = '''
        cg_receipt_id INT PRIMARY KEY NOT NULL,
        cg_arrival_time DATETIME NOT NULL,
        cg_arrival_quantity INT NOT NULL,
        cg_quelified_products INT,
        cg_inbound_status NUMERIC NOT NULL,
        cg_remarks TEXT(200)
    '''

    def __init__(self, database_name):
        super().__init__(database_name, 'cg_receipt_inspection', 'cg_receipt_id')  

'''物理表结构
class cg_supplier_item # 供应商供货明细
    ├── 'cg_item_name' 物料名称，TEXT，20字节，必填
    │
    ├── 'material_code' 物料编码，INT，必填，主键
    │
    ├── 'cg_item_price' 物料价格，REAL，必填
    │
    ├── 'cg_remarks' 备注，TEXT，200字节
'''
class cg_supplier_item(cg_database_entity):
    table_schema = '''
        cg_item_name TEXT(20) NOT NULL,
        material_code INT NOT NULL,
        cg_item_price REAL NOT NULL,
        cg_remarks TEXT(200)
    '''

    def __init__(self, database_name):
        super().__init__(database_name, 'cg_supplier_item', 'cg_material_code')  

if __name__ == '__main__':

    # 访问路径及名称，此处访问 Detail of January.db
    database_name = os.path.join(db_folder, "40004005.db")
   
    # 判断是否有文件存在，如果有就读取进行操作，如果没有就新建一个表
    if os.path.exists(os.path.join(db_folder, database_name)):
        cg_sup_item = cg_supplier_item(database_name)
        # cg_sup_info = cg_supplier_info(database_name)
        # cg_rec_ins = cg_receipt_inspection(database_name)
        # cg_pur_det = cg_purchase_detail(database_name, 'cg_purchase_detail', 'cg_purchase_detail_id')
    else:
        cg_sup_item = cg_supplier_item(database_name)
        cg_sup_item.create_table(cg_supplier_item.table_schema)
        # cg_rec_ins = cg_receipt_inspection(database_name)
        # cg_rec_ins.create_table(cg_receipt_inspection.table_schema)
        # cg_pur_det = cg_purchase_detail(database_name, 'cg_purchase_detail', 'cg_purchase_detail_id')
        # cg_pur_det.create_table(cg_purchase_detail.table_schema)

    cg_sup_item.add_item(
        cg_item_name = '橡胶套',
        material_code = 10,
        cg_item_price = 15.52,
        cg_remarks = ''
    )

'''物理表结构
class cg_supplier_item # 供应商供货明细
    ├── 'cg_item_name' 物料名称，TEXT，20字节，必填
    │
    ├── 'material_code' 物料编码，INT，必填，主键
    │
    ├── 'cg_item_price' 物料价格，REAL，必填
    │
    ├── 'cg_remarks' 备注，TEXT，200字节
'''

'''
    # 案例输入
    # 增加三条记录
    cg_pur_lis.add_item(
        cg_purchase_list_id = 40001001,
        jh_purchase_request_id = 10004001,
        cg_remarks="don't have a clear clue"
    )

    cg_pur_lis.add_item(
        cg_purchase_list_id = 40001002,
        jh_purchase_request_id = 10004002,
        cg_remarks="but I'll fix it"        
    )

    cg_pur_lis.add_item(
        cg_purchase_list_id = 40001003,
        jh_purchase_request_id = 10004003,
        cg_remarks="try not to be mediocre"        
    )
    
    # 采购订单明细
    cg_pur_det.add_item(
        cg_purchase_detail_id = 40002001,
        cg_purchase_list_id = 40001001,
        material_code = 9001,
        cg_total_price = 500.56,
        cg_receipt_id = 40005001,
        cg_remarks = 'take advantages of sth'
    )

    # 删去一条记录
    cg_pur_lis.delete_item(40001001)

    # 更新一条记录
    cg_pur_lis.update_item(
        40001002,
        jh_purchase_request_id = 10004005,
        cg_remarks = "this is a update item"
    )

    # 在终端输出一条记录
    result = cg_pur_lis.query_item(40001002)
    print(result)

        for i in range(1, 17):
        pdid = 40002001 + i
        if (i > 10):
            crid = None
            remarks = '单号为' + str(pdid) + '的货物仍在途'
        else: 
            crid = pdid + i + 3000
            remarks = '单号为' + str(pdid) + '的货物已收货'
        orlo = random.randint(10, 300)
        tapr = orlo * 12.45
        
        cg_pur_det.add_item(
            cg_purchase_detail_id = pdid,
            cg_purchase_list_id = pdid - 1000,
            material_code = i,
            cg_order_lot = orlo,
            cg_total_price = tapr,
            cg_receipt_id = crid,
            cg_remarks = remarks            
        )
'''