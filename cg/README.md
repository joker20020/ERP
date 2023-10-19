# 采购模块
这是ERP系统的采购模块，本模块的文件结构如下所示
``` Python
ERPProject #采购文件
├── cg_ui # 储存PyQt design设计的所有采购模块.ui文件
|   ├── u102.png # 窗体的icon
|   ├── version2.ui # 窗体的ui文件
|   └── ...
├── cg_db # 储存采购模块的数据库表，四个实体生成了四个数据库.db文件
|   ├── Purchase Detail.db
|   ├── Purchase List.db
|   ├── Purchase Receipt.db
|   ├── Purchase Supplier.db
|   └── ...
├── cg_database.py # 采购模块的数据库类
├── cg_widget.py # 采购模块的窗口与槽函数、子线程都放在这个文件中
└── ...
```