# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Designnn.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys 
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar, QInputDialog,
    QWidget, QMessageBox)
from LogIn import Ui_MainWindow  # Import the login window class from LogIn.py
from SignUp import Ui_SignUp     # Import the SignUp Window class from SignUp.py
from Income import IncomeFeature 
from Expense import ExpenseFeature
from Savings import SavingsFeature
from Profile import Ui_ProfileDashboard

import bcrypt
from Database.Signup_db import DatabaseConnection

class IncomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Income")
        self.setGeometry(300, 300, 400, 300)
        self.label = QLabel("Income Management Window", self)
        self.label.setGeometry(50, 50, 300, 30)
        
class Ui_FinancialManagment(object):
    def setupUi(self, FinancialManagment):
        if not FinancialManagment.objectName():
            FinancialManagment.setObjectName(u"FinancialManagment")
        FinancialManagment.resize(956, 520)
        self.centralwidget = QWidget(FinancialManagment)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame1 = QFrame(self.centralwidget)
        
        # Frame 1
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(0, 0, 951, 31))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        
        # BUTTON
        self.SignUp = QPushButton(self.frame1)
        self.SignUp.setObjectName(u"SignUp")
        self.SignUp.setGeometry(QRect(680, 0, 93, 28))
        self.SignUp.clicked.connect(self.openSignUpWindow)  # Connect to new slot
        
        self.LogIN = QPushButton(self.frame1)
        self.LogIN.setObjectName(u"LogIN")
        self.LogIN.setGeometry(QRect(770, 0, 93, 28))
        self.LogIN.clicked.connect(self.openLoginWindow)  # Connect to new slot
        
        self.LogOut = QPushButton(self.frame1)
        self.LogOut.setObjectName(u"LogOut")
        self.LogOut.setGeometry(QRect(860, 0, 93, 28))
        self.LogOut.clicked.connect(self.openLoginWindow)  # Connect to new slot
        
        # Other UI components
        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(0, 30, 951, 91))
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        
        # FRAME 2
        self.label = QLabel(self.frame2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 20, 181, 51))
        self.label.setMouseTracking(False)
        
        self.line = QFrame(self.frame2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(340, 50, 171, 31))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        
        # FRAME 3
        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setGeometry(QRect(0, 120, 951, 651))
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)
        
        self.pushButton_4 = QPushButton(self.frame3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(210, 10, 161, 41))
        self.pushButton_4.clicked.connect(self.openIncomeWindow)  # Connect to new slot
        
        self.pushButton_5 = QPushButton(self.frame3)        
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(600, 10, 161, 41))
        self.pushButton_5.clicked.connect(self.openExpenseWindow)  # Connect to new slot

        
        self.pushButton_6 = QPushButton(self.frame3)        
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(410, 10, 161, 41))
        self.pushButton_6.clicked.connect(self.openSavingsWindow)  # Connect to new slot

        
        self.pushButton_7 = QPushButton(self.frame3)        
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(780, 10, 161, 41))
        
        self.pushButton_8 = QPushButton(self.frame3)        
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 10, 161, 41))
        self.pushButton_8.clicked.connect(self.openProfileDashboard)

        FinancialManagment.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FinancialManagment)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 956, 26))
        FinancialManagment.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FinancialManagment)
        self.statusbar.setObjectName(u"statusbar")
        FinancialManagment.setStatusBar(self.statusbar)

        self.retranslateUi(FinancialManagment)

        QMetaObject.connectSlotsByName(FinancialManagment)
    # setupUi

    def retranslateUi(self, FinancialManagment):
        FinancialManagment.setWindowTitle(QCoreApplication.translate("FinancialManagment", u"Financial Managment", None))
        self.SignUp.setText(QCoreApplication.translate("FinancialManagment", u"SignUp", None))
        self.LogIN.setText(QCoreApplication.translate("FinancialManagment", u"LogIn", None))
        self.LogOut.setText(QCoreApplication.translate("FinancialManagment", u"LogOut", None))
        self.label.setText(QCoreApplication.translate("FinancialManagment", u"Personal FInancial Managment", None))
        self.pushButton_4.setText(QCoreApplication.translate("FinancialManagment", u"Income", None))
        self.pushButton_5.setText(QCoreApplication.translate("FinancialManagment", u"Expense", None))
        self.pushButton_6.setText(QCoreApplication.translate("FinancialManagment", u"Savings", None))
        self.pushButton_7.setText(QCoreApplication.translate("FinancialManagment", u"Report", None))
        self.pushButton_8.setText(QCoreApplication.translate("FinancialManagment", u"Profile", None))
    # retranslateUi

    def clickHandler(self):
        dialog = QInputDialog()
        dialog = QInputDialog()
        dialog.setLabelText("Enter your name:")
        dialog.setLabelText("Enter your name2:")
        dialog.exec()
        dialog.exec()
        print(dialog.textValue())
        
        print(dialog.textValue())
    
    # Slot to open login window
    def openLoginWindow(self):
        from PySide6.QtWidgets import QMainWindow

        class LoginWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)

        self.loginWindow = LoginWindow()
        self.loginWindow.show()    
    
    # Slot to open SignUp window    
    def openSignUpWindow(self):
        from PySide6.QtWidgets import QMainWindow

        class SignUpWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                self.ui = Ui_SignUp()
                self.ui.setupUi(self)

        self.loginWindow = SignUpWindow()
        self.loginWindow.show()
    
    # Slot to open Income Winodw
    def openIncomeWindow(self):
        self.IncomeFeature = IncomeFeature()
        self.IncomeFeature.show()
        
    def openExpenseWindow(self):
        self.expensesWindow = ExpenseFeature()
        self.expensesWindow.show()
    
    def openSavingsWindow(self):
        self.savingsWindow = SavingsFeature()
        self.savingsWindow.show()
        
    def openProfileDashboard(self):
        # Mock user data for demonstration purposes
        user_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "profile_picture": "path_to_profile_pic.jpg",  # Use the actual file path
            "phone": "+1234567890",
            "option": "Premium User"
        }

        # Create and show the Profile Dashboard        
        self.profile_dashboard = Ui_ProfileDashboard(user_data)
        self.profile_dashboard.exec()
        
    def openReportWindow(self):
        self.report_dashboard = Ui_ProfileDashboard()
        self.report_dashboard.exec()