# from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


# class IncomeFeature(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Income Feature")
#         self.setGeometry(100, 100, 800, 400)
#         self.init_ui()

#     def init_ui(self):
#         # Table
#         self.table = QTableWidget(self)
#         self.table.setColumnCount(6)
#         self.table.setHorizontalHeaderLabels(["Date", "Income Value", "Source", "User ID", "Total Income/Day", "Actions"])
#         self.table.setRowCount(5)  # Example rows; can be dynamic

#         # Add/Edit/Delete buttons in each row
#         for row in range(5):
#             self.add_row(row)

#         # Layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.table)
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def add_row(self, row):
#         for col in range(5):
#             self.table.setItem(row, col, QTableWidgetItem(f"Data {row + 1}-{col + 1}"))

#         # Action buttons
#         add_button = QPushButton("Add")
#         edit_button = QPushButton("Edit")
#         delete_button = QPushButton("Delete")
#         actions_layout = QVBoxLayout()
#         actions_layout.addWidget(add_button)
#         actions_layout.addWidget(edit_button)
#         actions_layout.addWidget(delete_button)
#         actions_container = QWidget()
#         actions_container.setLayout(actions_layout)
#         self.table.setCellWidget(row, 5, actions_container)


from PySide6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, 
    QVBoxLayout, QWidget, QGridLayout
)
from PySide6.QtCore import QDate

class IncomeFeature(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Income Feature")
        self.setGeometry(100, 100, 900, 500)
        self.init_ui()

    def init_ui(self):
        # Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["Date", "Income Value", "Source", "User ID", "Category", "Total Day", "Actions"]
        )

        # Adjust column width for better visibility
        self.table.setColumnWidth(6, 250)  # Actions Column width increased

        # Start with 5 rows (but allow adding more dynamically)
        self.table.setRowCount(5)

        for row in range(5):
            self.add_row(row)

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
        self.table.setItem(row, 0, QTableWidgetItem(current_date))

        # Create empty fields for user input
        for col in range(1, 6):
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
        print(f"Adding data for row {row}")

    def handle_update(self, row):
        print(f"Updating data for row {row}")

    def handle_delete(self, row):
        """Deletes the selected row."""
        self.table.removeRow(row)
        print(f"Deleted row {row}")



