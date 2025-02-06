from PySide6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, 
    QVBoxLayout, QWidget, QGridLayout
)
from PySide6.QtCore import QDate
import sys
import datetime
from Database.database import Database

class ExpenseFeature(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Feature")
        self.setGeometry(100, 100, 900, 500)
        self.db = Database()  # Create database connection
        self.init_ui()

    def init_ui(self):
        # Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["Number", "Date", "Expense Name", "Cost", "Category", "Total Expense/Day", "Actions"]
        )

        # Adjust column width for better visibility
        self.table.setColumnWidth(6, 250)  # Actions Column width increased

        # Start with 5 rows (but allow adding more dynamically)
        self.table.setRowCount(5)

        # for row in range(5):
        #     self.add_row(row)
        
        expenses = self.db.fetch_expenses()
        self.table.setRowCount(len(expenses))

        for row, expense in enumerate(expenses):
            self.add_row(row)
            for col in range(6):
                self.table.setItem(row, col, QTableWidgetItem(str(expense[col])))  # Adjusting for ID column

        # "Add Row" Button
        self.add_row_button = QPushButton("Add Row")
        self.add_row_button.clicked.connect(self.add_new_row)
        
        # Back Button (Closes the Window)
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.close)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_row_button)
        layout.addWidget(self.back_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_row(self, row):
        # Auto-fill the date column with the current date
        current_date = QDate.currentDate().toString("yyyy-MM-dd")
        self.table.setItem(row, 1, QTableWidgetItem(current_date))

        # Create empty fields for user input
        for col in range(2, 6):
            self.table.setItem(row, col, QTableWidgetItem(""))

        # Action Buttons with better visibility
        add_button = QPushButton("Add")
        update_button = QPushButton("Update")
        delete_button = QPushButton("Delete")

        # Set minimum size for better visibility
        for button in [add_button, update_button, delete_button]:
            button.setMinimumWidth(75)  # Ensure they are large enough
            button.setMinimumHeight(25)

        add_button.clicked.connect(lambda: self.handle_add(row))
        update_button.clicked.connect(lambda: self.handle_update(row))
        delete_button.clicked.connect(lambda: self.handle_delete(row))

        # Use QGridLayout for better spacing
        actions_layout = QGridLayout()
        actions_layout.addWidget(add_button, 0, 0)
        actions_layout.addWidget(update_button, 0, 1)
        actions_layout.addWidget(delete_button, 0, 2)

        actions_container = QWidget()
        actions_container.setLayout(actions_layout)
        self.table.setCellWidget(row, 6, actions_container)

    def add_new_row(self):
        """Adds a new row dynamically when 'Add Row' is clicked."""
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.add_row(row_count)
        

    def handle_add(self, row):
        # print(f"Adding data for row {row}")
        # """Insert data from row into MySQL database."""
        # date = self.table.item(row, 0).text()
        # expense_name = self.table.item(row, 1).text()
        # cost = self.table.item(row, 2).text()
        # user_id = self.table.item(row, 3).text()
        # category = self.table.item(row, 4).text()
        # total_expense = self.table.item(row, 5).text()
        """Insert data from row into MySQL database."""
        def get_cell_text(row, col):
            item = self.table.item(row, col)
            return item.text().strip() if item else ""  # Return empty string if item is None
        
        date = get_cell_text(row, 1)
        expense_name = get_cell_text(row, 2)
        cost = get_cell_text(row, 3)
        user_id = get_cell_text(row, 4)
        category = get_cell_text(row, 5)
        total_expense = get_cell_text(row, 6)

        if expense_name and cost and user_id and category and total_expense:
            try:
                self.db.insert_expense(date, expense_name, cost, user_id, category, total_expense)
                print(f"Row {row} added successfully!")
            except Exception as e:
                print(f"Error adding row {row}: {e}")
        else:
            print("All fields must be filled!")

    def handle_update(self, row):
        print(f"Updating data for row {row}")
        """Update selected row's data in MySQL."""
        print(f"Updating row {row} (Feature to be implemented later).")

    def handle_delete(self, row):
        # """Deletes the selected row."""
        # # self.table.removeRow(row)
        # # print(f"Deleted row {row}")
        # """Deletes row from MySQL database."""
        # expense_id = row + 1  # Assuming row index matches expense_id (you may need to adjust this logic)

        # try:
        #     self.db.delete_expense(expense_id)
        #     self.table.removeRow(row)
        #     print(f"Deleted row {row} from database!")
        # except Exception as e:
        #     print(f"Error deleting row {row}: {e}")
        """Deletes the selected row."""
        expense_id_item = self.table.item(row, 0)  # Assuming column 0 is 'id'
        
        if expense_id_item is None:
            print("Error: No ID found for row deletion")
            return

        expense_id = expense_id_item.text()
        
        try:
            self.db.delete_expense(expense_id)
            self.table.removeRow(row)
            print(f"Deleted row {row} from database!")
        except Exception as e:
            print(f"Error deleting row {row}: {e}")
    
    def delete_expense(self, expense_id):
        sql = "DELETE FROM expense_table WHERE `id` = %s"  # Use primary key 'id'
        self.cursor.execute(sql, (expense_id,))
        self.conn.commit()

        
        



