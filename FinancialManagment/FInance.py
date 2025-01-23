import sys 
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Personal Financial Manage')
        self.setWindowIcon(QIcon('maps.ico'))
        self.resize(1000, 1000) # Shape - width , height
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        #widgets
        self.inputField = QLineEdit()
        button = QPushButton('&here submit it', clicked=self.sayHello)
        button.clicked.connect(self.sayHello)
        self.output = QTextEdit()
        
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
        
    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))

# app = QApplication([])
app = QApplication(sys.argv)
app.setStyleSheet('''
                QWidget {
                    font-size: 25px;
                }  
                QPushButton {
                    font-size: 20px;
                }
                  ''')

window = MyApp()
window.show()
app.exec()