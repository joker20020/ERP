import sqlite3

class InventoryManager:
    def __init__(self,file_path):
        # 创建或连接到库存数据库

        self.file_path=file_path
        self.conn = sqlite3.connect(self.file_path)
        self.c = self.conn.cursor()

        # 创建商品表
        self.c.execute('''CREATE TABLE IF NOT EXISTS products
                     (product_id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER,  ID INTEGER, safe_inventory INTEGER)''')
        # self.c.execute('''DROP TABLE IF EXISTS products''')

        # 检查表是否为空
        self.c.execute("SELECT COUNT(*) FROM products")
        if self.c.fetchone()[0] == 0:
            self._initialize_products()

        # 创建入库表
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS ruku (
            id INTEGER PRIMARY KEY,
            entry_time TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            operator TEXT NOT NULL
        )
        ''')

        # 创建出库表
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS chuku (
            id INTEGER PRIMARY KEY,
            exit_time TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            operator TEXT NOT NULL
        )
        ''')
        self.conn.commit()

    def add_inventory(self, entry_time, product_id, quantity, operator):
        # 添加入库记录
        self.c.execute('''
        INSERT INTO ruku (entry_time, product_id, quantity, operator)
        VALUES (?, ?, ?, ?)
        ''', (entry_time, product_id, quantity, operator))

        # 更新库存表
        self.c.execute('''
        UPDATE products
        SET quantity = quantity + ?
        WHERE ID = ?
        ''', (quantity, product_id))

        self.conn.commit()

    def substact_inventory(self, exit_time, product_id, quantity, operator):
        # 添加出库记录
        self.c.execute('''
        INSERT INTO chuku (exit_time, product_id, quantity, operator)
        VALUES (?, ?, ?, ?)
        ''', (exit_time, product_id, quantity, operator))

        # 更新库存表
        self.c.execute('''
        UPDATE products
        SET quantity = quantity - ?
        WHERE ID = ?
        ''', (quantity, product_id))

        self.conn.commit()

    def _initialize_products(self):
        """初始化商品列表"""
        products = [
            ("大众自动钳", 30000, 1, 1000),
            ("壳体2", 3000, 2, 1000),
            ("支架1", 3000, 3, 1000),
            ("配件", 3000, 4, 1000),
            ("左壳体1", 3000, 5, 1000),
            ("右壳体1", 3000, 6, 1000),
            ("密封圈2", 3000, 7, 1000),
            ("活塞1", 3000, 8, 1000),
            ("塑料套1", 3000, 9, 1000),
            ("橡胶套1", 3000, 10, 1000),
            ("放气螺栓1", 3000, 11, 1000),
            ("防尘帽1", 3000, 12, 1000),
            ("内六角螺栓1", 3000, 13, 1000),
            ("摩擦片2", 3000, 14, 1000),
            ("隔垫1", 3000, 15, 1000),
            ("开口导向套管2", 3000, 16, 1000)
        ]
        self.c.executemany("INSERT INTO products (name, quantity, ID, safe_inventory) VALUES (?, ?, ?, ?)", products)
        self.conn.commit()

    def add_product(self, name, quantity, ID, safe_inventory):
        """添加商品"""
        self.c.execute("INSERT INTO products (name, quantity, ID, safe_inventory) VALUES (?, ?, ?, ?)", (name, quantity, ID, safe_inventory))
        self.conn.commit()

    def update_product(self, product_id, quantity):
        """更新商品数量"""
        self.c.execute("UPDATE products SET quantity = ? WHERE product_id = ?", (quantity, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        """删除商品"""
        self.c.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
        self.conn.commit()

    def list_products(self):
        """列出所有商品"""
        self.c.execute("SELECT * FROM products")
        return self.c.fetchall()

    def close(self):
        """关闭数据库连接"""
        self.conn.close()

    def query_by_id(self, search_id):
        # 使用参数化查询来提高安全性
        self.c.execute('SELECT quantity, safe_inventory FROM products WHERE ID=?', (search_id,))
        result = self.c.fetchone()
        if result:
            return result
        else:
            return "No product found with the given ID"

    def query_xiaoshou_by_id(self, search_id):
        # 使用参数化查询来提高安全性
        self.c.execute('SELECT name, quantity FROM products WHERE ID=?', (search_id,))
        result = self.c.fetchone()
        if result:
            return result
        else:
            return "No product found with the given ID"


# 示例用法
if __name__ == "__main__":
    manager = InventoryManager('inventory.db')
    manager.c.execute("DROP TABLE products")

    # 查询使用方法：
    db = InventoryManager('inventory.db')
    product_id = 8  # 可以替换为您要查询的ID
    print(db.query_by_id(product_id))

    # 销售查询使用方法：
    db = InventoryManager('inventory.db')
    product_id = 4  # 可以替换为您要查询的ID
    print(db.query_xiaoshou_by_id(product_id))

    # 列出所有商品
    print(manager.list_products())

    # # 更新商品
    # manager.update_product(1, 110)

    # # 列出所有商品
    # print(manager.list_products())

    # # 删除商品
    # manager.delete_product(2)

    # # 列出所有商品
    # print(manager.list_products())

    manager.close()

    # 添加商品
    # manager.add_product("大众自动钳", 101, 1, 41)
    # manager.add_product("壳体2", 102, 2, 42)
    # manager.add_product("支架1", 103, 3, 43)
    # manager.add_product("配件", 104, 4, 44)
    # manager.add_product("左壳体1", 105,  5, 45)
    # manager.add_product("右壳体1", 106,  6, 46)
    # manager.add_product("密封圈2", 107, 7, 47)
    # manager.add_product("活塞1", 108, 8, 48)
    # manager.add_product("塑料套1", 109,  9, 49)
    # manager.add_product("橡胶套1", 110,  10, 50)
    # manager.add_product("放气螺栓1", 111, 11, 51)
    # manager.add_product("防尘帽1", 112, 12, 52)
    # manager.add_product("内六角螺栓1", 113, 13, 53)
    # manager.add_product("摩擦片2", 114,  14, 54)
    # manager.add_product("隔垫1", 115,  15, 55)
    # manager.add_product("开口导向套管2", 116, 16, 56)