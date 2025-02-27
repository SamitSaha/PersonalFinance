from PySide6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, 
    QVBoxLayout, QWidget, QGridLayout, QMessageBox
)
from PySide6.QtCore import QDate
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Database.saving_db import SavingsDB

class SavingsFeature(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Savings Feature")
        self.setGeometry(100, 100, 900, 500)

        # Initialize database object
        self.db = SavingsDB()

        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["Date", "Goal", "Goal Amount", "User ID", "Track Progress", "Saving Goal", "Actions"]
        )
        self.table.setColumnWidth(6, 250)

        self.table.setRowCount(0)

        self.add_row_button = QPushButton("Add Row")
        self.add_row_button.clicked.connect(self.add_new_row)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_row_button)
        layout.addWidget(self.back_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_data(self):
        """Fetches data from the database and populates the table."""
        expenses = self.db.fetch_all_savings()
        
        self.table.setRowCount(0)  # Clear table before reloading
        for row_data in expenses:
            row_index = self.table.rowCount()
            self.table.insertRow(row_index)
            for col, data in enumerate(row_data):
                self.table.setItem(row_index, col, QTableWidgetItem(str(data)))
            self.add_action_buttons(row_index)

    def add_action_buttons(self, row):
        """Adds Add, Update, and Delete buttons to a row."""
        add_button = QPushButton("Add")
        update_button = QPushButton("Update")
        delete_button = QPushButton("Delete")

        add_button.clicked.connect(lambda: self.handle_add(row))
        update_button.clicked.connect(lambda: self.handle_update(row))
        delete_button.clicked.connect(lambda: self.handle_delete(row))

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
        current_date = QDate.currentDate().toString("yyyy-MM-dd")
        self.table.setItem(row_count, 0, QTableWidgetItem(current_date))
        for col in range(1, 6):
            self.table.setItem(row_count, col, QTableWidgetItem(""))
        self.add_action_buttons(row_count)

    def handle_add(self, row):
        """Adds new data to the database."""
        data = [self.table.item(row, col).text() if self.table.item(row, col) else "" for col in range(6)]
        if any(field == "" for field in data):
            QMessageBox.warning(self, "Error", "All fields must be filled before adding!")
            return

        self.db.add_savings(*data)
        QMessageBox.information(self, "Success", "Savings added successfully!")

    def handle_update(self, row):
        """Updates the existing data in the database."""
        expense_id = self.table.item(row, 6).text()
        print("the id is ",expense_id)
        # Get updated values from the table
        data = [self.table.item(row, col).text() if self.table.item(row, col) else "" for col in range(6)]

        # Ensure all fields are filled
        if any(field == "" for field in data):
            QMessageBox.warning(self, "Error", "All fields must be filled before updating!")
            return
        
        # Call the update function with the ID
        self.db.update_savings(expense_id, *data)
        QMessageBox.information(self, "Success", "Savings updated successfully!")

    def handle_delete(self, row):
        """Deletes a record from the database."""
        id = self.table.item(row, 6).text() if self.table.item(row, 6) else ""
        if not id:
            QMessageBox.warning(self, "Error", "Invalid date for deletion!")
            return

        self.db.delete_savings(id)
        self.table.removeRow(row)
        QMessageBox.information(self, "Success", "Savings deleted successfully!")

