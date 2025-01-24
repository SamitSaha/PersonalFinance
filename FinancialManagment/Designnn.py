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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_FinancialManagment(object):
    def setupUi(self, FinancialManagment):
        if not FinancialManagment.objectName():
            FinancialManagment.setObjectName(u"FinancialManagment")
        FinancialManagment.resize(956, 520)
        self.centralwidget = QWidget(FinancialManagment)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(0, 0, 951, 31))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.SignUp = QPushButton(self.frame1)
        self.SignUp.setObjectName(u"SignUp")
        self.SignUp.setGeometry(QRect(680, 0, 93, 28))
        self.LogIN = QPushButton(self.frame1)
        self.LogIN.setObjectName(u"LogIN")
        self.LogIN.setGeometry(QRect(770, 0, 93, 28))
        self.LogOut = QPushButton(self.frame1)
        self.LogOut.setObjectName(u"LogOut")
        self.LogOut.setGeometry(QRect(860, 0, 93, 28))
        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(0, 30, 951, 91))
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 20, 181, 51))
        self.label.setMouseTracking(False)
        self.line = QFrame(self.frame2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(340, 50, 171, 31))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setGeometry(QRect(0, 120, 951, 651))
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(210, 10, 161, 41))
        self.pushButton_5 = QPushButton(self.frame3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(600, 10, 161, 41))
        self.pushButton_6 = QPushButton(self.frame3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(410, 10, 161, 41))
        self.pushButton_7 = QPushButton(self.frame3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(780, 10, 161, 41))
        self.pushButton_8 = QPushButton(self.frame3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 10, 161, 41))
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

# app = QApplication(sys.argv)
# window = Ui_FinancialManagment()
# window.show()
# app.exec()
