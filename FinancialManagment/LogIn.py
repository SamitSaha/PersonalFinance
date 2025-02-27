# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QDialogButtonBox, QLabel, QLineEdit, QMenuBar, QPushButton, QWidget)

import bcrypt
from PySide6.QtWidgets import QMessageBox
from Database.Signup_db import DatabaseConnection


################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 259)
        # self.setWindowTitle("Income Feature")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(90, 30, 181, 16))
        self.label.setText("Enter Email Address")
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(90, 80, 91, 21))
        self.label_2.setText("Enter Password")
        
        self.emailInput = QLineEdit(self.centralwidget)
        self.emailInput.setObjectName("emailInput")
        self.emailInput.setGeometry(QRect(90, 50, 181, 31))
        
        self.passwordInput = QLineEdit(self.centralwidget)
        self.passwordInput.setObjectName("passwordInput")
        self.passwordInput.setGeometry(QRect(90, 100, 181, 31))
        self.passwordInput.setEchoMode(QLineEdit.Password)
        
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setGeometry(QRect(90, 150, 181, 31))
        self.loginButton.setText("Login")
        self.loginButton.clicked.connect(self.authenticate_user)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
    def authenticate_user(self):
        email = self.emailInput.text().strip()
        password = self.passwordInput.text()

        if not email or not password:
            QMessageBox.warning(None, "Error", "Email and Password cannot be empty!")
            return

        try:
            db = DatabaseConnection()
            cursor = db.get_cursor()
            cursor.execute("SELECT password_hash FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user and bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
                QMessageBox.information(None, "Success", "Login successful!")
                # Here, you can open the main dashboard
            else:
                QMessageBox.warning(None, "Error", "Invalid email or password!")
        
        except Exception as e:
            QMessageBox.warning(None, "Database Error", f"Login failed: {str(e)}")
            
# ////////////////////////////////////////////////////////////////////////////////////


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(423, 259)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
        
#         self.label = QLabel(self.centralwidget)
        
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(90, 30, 181, 16))
#         self.label_2 = QLabel(self.centralwidget)
        
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setGeometry(QRect(90, 80, 91, 21))
#         self.lineEdit = QLineEdit(self.centralwidget)
        
#         self.lineEdit.setObjectName(u"lineEdit")
#         self.lineEdit.setGeometry(QRect(90, 50, 181, 31))
#         self.lineEdit_2 = QLineEdit(self.centralwidget)
        
#         self.lineEdit_2.setObjectName(u"lineEdit_2")
#         self.lineEdit_2.setGeometry(QRect(90, 100, 181, 31))
#         self.buttonBox = QDialogButtonBox(self.centralwidget)
        
#         self.buttonBox.setObjectName(u"buttonBox")
#         self.buttonBox.setGeometry(QRect(80, 160, 193, 28))
#         self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
#         self.buttonBox.setCenterButtons(True)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(MainWindow)
        
#         self.menubar.setObjectName(u"menubar")
#         self.menubar.setGeometry(QRect(0, 0, 423, 26))
#         MainWindow.setMenuBar(self.menubar)
#         self.toolBar = QToolBar(MainWindow)
        
#         self.toolBar.setObjectName(u"toolBar")
#         MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
#         self.toolBar_2 = QToolBar(MainWindow)
        
#         self.toolBar_2.setObjectName(u"toolBar_2")
#         MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)

#         self.retranslateUi(MainWindow)

#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
#         self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Email Address", None))
#         self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
#         self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
#         self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

    # def login_user(self):
    #     email = self.lineEdit.text()
    #     password = self.lineEdit_2.text()
    #     user_id = User.authenticate(email, password)

    #     if user_id:
    #         QMessageBox.information(None, "Login Success", "Welcome back!")
    #         self.current_user_id = user_id  # Store logged-in user ID
    #         self.open_dashboard()
    #     else:
    #         QMessageBox.warning(None, "Login Failed", "Invalid credentials.")


# import sys
# import bcrypt
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PySide6.QtCore import Qt
# from Database.Signup_db import DatabaseConnection
# from PySide6.QtWidgets import QDialogButtonBox, QLabel, QLineEdit, QMenuBar, QToolBar, QWidget

# class Ui_MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()
    
#     def setupUi(self):
#         self.setObjectName("MainWindow")
#         self.resize(423, 259)
#         self.centralwidget = QWidget(self)
#         self.centralwidget.setObjectName("centralwidget")
        
#         self.label = QLabel("Enter Email Address", self.centralwidget)
#         self.label.setGeometry(90, 30, 181, 16)
        
#         self.label_2 = QLabel("Enter Password", self.centralwidget)
#         self.label_2.setGeometry(90, 80, 91, 21)
        
#         self.emailInput = QLineEdit(self.centralwidget)
#         self.emailInput.setGeometry(90, 50, 181, 31)
        
#         self.passwordInput = QLineEdit(self.centralwidget)
#         self.passwordInput.setGeometry(90, 100, 181, 31)
#         self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)  # Hide password
        
#         self.buttonBox = QDialogButtonBox(self.centralwidget)
#         self.buttonBox.setGeometry(80, 160, 193, 28)
#         self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
#         self.buttonBox.setCenterButtons(True)
        
#         self.setCentralWidget(self.centralwidget)
        
#         self.buttonBox.accepted.connect(self.login)
#         self.buttonBox.rejected.connect(self.close)
    
#     def login(self):
#         email = self.emailInput.text().strip()
#         password = self.passwordInput.text()
        
#         if not email or not password:
#             QMessageBox.warning(self, "Error", "All fields are required!")
#             return
        
#         try:
#             db = DatabaseConnection()
#             cursor = db.get_cursor()
            
#             cursor.execute("SELECT password_hash FROM users WHERE email = %s", (email,))
#             user = cursor.fetchone()
            
#             if user:
#                 stored_hashed_password = user[0]
#                 if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
#                     QMessageBox.information(self, "Success", "Login Successful!")
#                 else:
#                     QMessageBox.warning(self, "Error", "Incorrect password!")
#             else:
#                 QMessageBox.warning(self, "Error", "User not found!")
#         except Exception as e:
#             QMessageBox.warning(self, "Database Error", f"Failed to login: {str(e)}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_MainWindow()
#     window.show()
#     sys.exit(app.exec())
