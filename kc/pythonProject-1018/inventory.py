import sqlite3

class InventoryManager:
    def __init__(self):
        # 创建或连接到库存数据库
        self.conn = sqlite3.connect('inventory.db')
        self.c = self.conn.cursor()

        # 创建商品表
        self.c.execute('''CREATE TABLE IF NOT EXISTS products
                     (product_id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER,  ID INTEGER)''')
        # self.c.execute('''DROP TABLE IF EXISTS products''')
    def add_product(self, name, quantity,  ID):
        """添加商品"""
        self.c.execute("INSERT INTO products (name, quantity,  ID) VALUES (?, ?,  ?)", (name, quantity,  ID))
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

# 示例用法
if __name__ == "__main__":
    manager = InventoryManager()

    # 添加商品
    manager.add_product("大众自动钳", 100, 1)
    manager.add_product("壳体2", 100, 2)
    manager.add_product("支架1", 100, 3)
    manager.add_product("配件", 100, 4)
    manager.add_product("左壳体1", 100,  5)
    manager.add_product("右壳体1", 100,  6)
    manager.add_product("密封圈2", 100, 7)
    manager.add_product("活塞1", 100, 8)
    manager.add_product("塑料套1", 100,  9)
    manager.add_product("橡胶套1", 100,  10)
    manager.add_product("放气螺栓1", 100, 11)
    manager.add_product("防尘帽1", 100, 12)
    manager.add_product("内六角螺栓1", 100, 13)
    manager.add_product("摩擦片2", 100,  14)
    manager.add_product("隔垫1", 100,  15)
    manager.add_product("开口导向套管2", 100, 16)

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