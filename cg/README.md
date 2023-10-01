# 采购模块
这是ERP系统的采购模块，本模块的文件结构如下所示
``` Python
ERPProject #采购文件
├── cg_adesigned_ui # 储存PyQt design设计的所有采购模块.ui文件
|   ├── 
|   ├── 
|   └── ...
├── cg_db # 储存采购模块的数据库表，四个实体生成了四个数据库.db文件
|   ├── cg_list.bd
|   ├── cg_detail.bd
|   ├── cg_supplier.bd
|   ├── cg_receipt.bd
|   └── ...
├── cg_forms # 储存PyQt design生成的窗体.py文件
|   ├── __init__.py
|   ├── 
|   ├── 
|   └── ...
├── cg_function # 储存采购模块的功能函数.py文件
|   ├── __init__.py
|   ├── january.db
|   ├── february.db
|   └── ...
├── cg_database.py # 采购模块的数据库类
└── main.py # 采购模块运行的主函数
```