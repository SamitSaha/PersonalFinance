from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class IncomeFeature(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Income Feature")
        self.setGeometry(100, 100, 800, 400)
        self.init_ui()

    def init_ui(self):
        # Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Date", "Income Value", "Source", "User ID", "Total Income/Day", "Actions"])
        self.table.setRowCount(5)  # Example rows; can be dynamic

        # Add/Edit/Delete buttons in each row
        for row in range(5):
            self.add_row(row)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_row(self, row):
        for col in range(5):
            self.table.setItem(row, col, QTableWidgetItem(f"Data {row + 1}-{col + 1}"))

        # Action buttons
        add_button = QPushButton("Add")
        edit_button = QPushButton("Edit")
        delete_button = QPushButton("Delete")
        actions_layout = QVBoxLayout()
        actions_layout.addWidget(add_button)
        actions_layout.addWidget(edit_button)
        actions_layout.addWidget(delete_button)
        actions_container = QWidget()
        actions_container.setLayout(actions_layout)
        self.table.setCellWidget(row, 5, actions_container)
