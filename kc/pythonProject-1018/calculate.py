import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory App")

        # 初始化组件
        self.combobox = QComboBox()
        self.pushbutton = QPushButton("Retrieve")
        self.line_edit = QLineEdit()

        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.combobox)
        layout.addWidget(self.pushbutton)
        layout.addWidget(self.line_edit)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 加载combobox选项
        self.load_combobox()

        # 连接信号和槽
        self.pushbutton.clicked.connect(self.retrieve_data)

    def load_combobox(self):
        # 在这里，我们可以从数据库中加载选择项，但为简化，我们直接添加几个选项
        self.combobox.addItems(["Option1", "Option2", "Option3"])

    def retrieve_data(self):
        # 获取选中的项
        selected_option = self.combobox.currentText()

        # 查询数据库
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        # 请根据您的数据库结构和需求更改此查询
        cursor.execute("SELECT value FROM your_table WHERE name=?", (selected_option,))
        result = cursor.fetchone()

        if result:
            self.line_edit.setText(str(result[0]))
        else:
            self.line_edit.setText("No data found")

        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


#     def load_product_details(self, product_name):
#         # Query the database to get product details
#         conn = sqlite3.connect("inventory.db")
#         cursor = conn.cursor()
#
#         cursor.execute("SELECT quantity FROM products WHERE product_name=?", (product_name,))
#         result = cursor.fetchone()
#
#         if result:
#             self.product_name_edit.setText(product_name)
#             self.product_quantity_edit.setText(str(result[0]))
#         else:
#             self.product_name_edit.clear()
#             self.product_quantity_edit.clear()
#
#         conn.close()
#
#
#     def add_product(self):
#         product_name = self.product_name_edit.text().strip()
#
#         if not product_name:
#             self.status_label.setText("Status: Please enter a product name!")
#             return
#
#         conn = sqlite3.connect("inventory.db")
#         cursor = conn.cursor()
#
#         try:
#             cursor.execute("INSERT INTO products (product_name, quantity) VALUES (?, 0)", (product_name,))
#             conn.commit()
#             self.status_label.setText(f"Status: Added product '{product_name}'!")
#             self.load_products()
#         except sqlite3.IntegrityError:
#             self.status_label.setText(f"Status: Product '{product_name}' already exists!")
#         finally:
#             conn.close()
#
#
#     def update_quantity(self):
#         product_name = self.product_name_edit.text().strip()
#         quantity = self.product_quantity_edit.text().strip()
#
#         if not product_name or not quantity:
#             self.status_label.setText("Status: Please enter product name and quantity!")
#             return
#
#         conn = sqlite3.connect("inventory.db")
#         cursor = conn.cursor()
#
#         cursor.execute("UPDATE products SET quantity=? WHERE product_name=?", (quantity, product_name))
#         conn.commit()
#         self.status_label.setText(f"Status: Updated quantity for '{product_name}'!")
#
#         conn.close()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = InventoryApp()
#     window.show()
#     sys.exit(app.exec())
