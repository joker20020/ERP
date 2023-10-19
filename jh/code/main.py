import sqlite3

# 计算物料需求量
# 毛需求 = 独立需求 + 相关需求
# 计划库存量 = 上期库存量 + 本期订单产出量 + 本期预计入库量 - 毛需求量
# 净需求量 = 本期毛需求量 - 上期库存量 - 本期预计入库量 + 安全库存量


# 初始化MRP数据库
conn = sqlite3.connect('mrp_example.db')
cursor = conn.cursor()


# 创建计划表
cursor.execute('''
CREATE TABLE IF NOT EXISTS MRP(
    product_id INTEGER PRIMARY KEY,
    planned_amount INTEGER
    planned_deadline varchar(20)
)
''')




# 创建所需的表
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales_forecast (
    product_id INTEGER PRIMARY KEY,
    forecast_amount INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bom (
    product_id INTEGER,
    material_id INTEGER,
    amount INTEGER,
    PRIMARY KEY (product_id, material_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    material_id INTEGER PRIMARY KEY,
    stock_amount INTEGER
)
''')

# 插入示例数据
cursor.executemany('INSERT OR REPLACE INTO sales_forecast VALUES (?, ?)', [
    (1, 100),  # 假设产品1预测销售量为100
])

cursor.executemany('INSERT OR REPLACE INTO bom VALUES (?, ?, ?)', [
    (1, 101, 2),  # 假设生产产品1需要原料101两份
    (1, 102, 3)   # 以及原料102三份
])

cursor.executemany('INSERT OR REPLACE INTO inventory VALUES (?, ?)', [
    (101, 150),  # 假设原料101库存为150份
    (102, 200)   # 原料102库存为200份
])

conn.commit()

# MRP计算
cursor.execute('''
SELECT
    b.material_id,
    sf.forecast_amount * b.amount AS required_amount,
    i.stock_amount,
    (sf.forecast_amount * b.amount) - i.stock_amount AS deficit
FROM
    sales_forecast sf
JOIN
    bom b ON sf.product_id = b.product_id
LEFT JOIN
    inventory i ON b.material_id = i.material_id
''')

material_plans = cursor.fetchall()

# 输出物料需求计划
for plan in material_plans:
    material_id, required_amount, stock_amount, deficit = plan
    print(f"Material {material_id}: Required = {required_amount}, Stock = {stock_amount}, Deficit = {deficit}")

# 查询相关数据


conn.close()
