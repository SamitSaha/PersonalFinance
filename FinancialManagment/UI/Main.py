import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Designnn import Ui_FinancialManagment  # Replace with the correct module name if it's different

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()  # Create a QMainWindow instance
    ui = Ui_FinancialManagment()  # Create an instance of your UI class
    ui.setupUi(MainWindow)  # Set up the UI in the QMainWindow
    MainWindow.show()  # Show the main window
    sys.exit(app.exec())  # Start the application event loop

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_FinancialManagment()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
