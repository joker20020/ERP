import sqlite3

conn = sqlite3.connect('sales_management.db')
cursor = conn.cursor()

# 客户信息管理
cursor.execute(
'''CREATE TABLE  IF NOT EXISTS  tb_customers (
	cust_id      INT       NOT NULL,
	cust_name    VARCHAR(50)  NOT NULL,
	cust_address VARCHAR(50)  NULL,
	cust_zip     VARCHAR(10)  NULL,
	cust_contact VARCHAR(50)  NULL,
	cust_email   VARCHAR(255) NULL,
	PRIMARY KEY(cust_id)
)'''

)


# 销售产品管理
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL
)
''')

# 销售员管理
cursor.execute('''
CREATE TABLE IF NOT EXISTS salespersons (
    salesperson_id INTEGER PRIMARY KEY   NOT NULL,
    name TEXT,
    region TEXT,
    password INT
)
''')

# 销售业务管理
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales_activities (
    activity_id INTEGER PRIMARY KEY   NOT NULL,
    activity_date DATE,
    salesperson_id INTEGER,
    description TEXT,
    FOREIGN KEY(salesperson_id) REFERENCES salespersons(salesperson_id)
)
''')

# 销售订单管理
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales_orders (
    order_id INTEGER PRIMARY KEY    NOT NULL,
    order_date DATE,
    customer_id INTEGER,
    salesperson_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(salesperson_id) REFERENCES salespersons(salesperson_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
''')

# 查询特定客户的信息
def query_customer_info(customer_id):
    cursor.execute('SELECT * FROM tb_customers WHERE cust_id=?', (customer_id,))
    return cursor.fetchone()

# 查询特定销售员的销售业务
def query_salesperson_activities(salesperson_id):
    cursor.execute('SELECT * FROM sales_activities WHERE salesperson_id=?', (salesperson_id,))
    return cursor.fetchall()

# 查询特定产品的销售订单
def query_product_sales(product_id):
    cursor.execute('SELECT * FROM sales_orders WHERE product_id=?', (product_id,))
    return cursor.fetchall()

# 简化的销售预测功能 - 基于最近的销售订单
def sales_forecast(product_id, days=30):
    cursor.execute('''
        SELECT SUM(quantity) 
        FROM sales_orders 
        WHERE product_id=? AND julianday('now') - julianday(order_date) <= ? 
    ''', (product_id, days))
    total_sales_last_30_days = cursor.fetchone()[0] or 0
    return total_sales_last_30_days * (365 / days)  # 简化预测，基于过去的销售量

if __name__ == "__main__":
    print(query_customer_info(19))
    conn.close()
## See PyCharm help at https://www.jetbrains.com/help/pycharm/

