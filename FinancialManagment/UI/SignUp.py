# # -*- coding: utf-8 -*-

# ################################################################################
# ## Form generated from reading UI file 'SignUp.ui'
# ##
# ## Created by: Qt User Interface Compiler version 6.8.1
# ##
# ## WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################

# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
#     QMainWindow, QMenuBar, QPushButton, QSizePolicy,
#     QStatusBar, QWidget)


# class Ui_SignUp(object):
#     def setupUi(self, SignUp):
#         if not SignUp.objectName():
#             SignUp.setObjectName(u"SignUp")
#         SignUp.resize(540, 600)  # Adjusted height to accommodate new elements
#         self.centralwidget = QWidget(SignUp)
#         self.centralwidget.setObjectName(u"centralwidget")
        
#         # Profile Picture
#         self.profilePicLabel = QLabel(self.centralwidget)
#         self.profilePicLabel.setObjectName(u"profilePicLabel")
#         self.profilePicLabel.setGeometry(QRect(220, 10, 100, 100))
#         self.profilePicLabel.setStyleSheet("border-radius: 50px; border: 2px solid gray;")
#         self.profilePicLabel.setPixmap(QPixmap("default_profile.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))  # Placeholder image
#         self.profilePicLabel.setAlignment(Qt.AlignCenter)
        
#         # Upload Button
#         self.uploadButton = QPushButton(self.centralwidget)
#         self.uploadButton.setObjectName(u"uploadButton")
#         self.uploadButton.setGeometry(QRect(220, 120, 100, 30))
#         self.uploadButton.setText("Upload")
#         self.uploadButton.clicked.connect(self.uploadProfilePicture)
        
#         # First Name        
#         self.lineEdit = QLineEdit(self.centralwidget)
#         self.lineEdit.setObjectName(u"lineEdit")
#         self.lineEdit.setGeometry(QRect(180, 50, 201, 31))
        
#         self.checkBox = QCheckBox(self.centralwidget)
#         self.checkBox.setObjectName(u"checkBox")
#         self.checkBox.setGeometry(QRect(180, 290, 81, 20))
        
#         self.lineEdit_7 = QLineEdit(self.centralwidget)
#         self.lineEdit_7.setObjectName(u"lineEdit_7")
#         self.lineEdit_7.setGeometry(QRect(180, 200, 201, 31))
        
#         self.lineEdit_8 = QLineEdit(self.centralwidget)
#         self.lineEdit_8.setObjectName(u"lineEdit_8")
#         self.lineEdit_8.setGeometry(QRect(180, 150, 201, 31))
        
#         self.lineEdit_9 = QLineEdit(self.centralwidget)
#         self.lineEdit_9.setObjectName(u"lineEdit_9")
#         self.lineEdit_9.setGeometry(QRect(180, 100, 201, 31))
        
#         self.lineEdit_2 = QLineEdit(self.centralwidget)
#         self.lineEdit_2.setObjectName(u"lineEdit_2")
#         self.lineEdit_2.setGeometry(QRect(180, 250, 201, 31))
#         self.label = QLabel(self.centralwidget)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(180, 30, 201, 20))
#         self.label_2 = QLabel(self.centralwidget)
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setGeometry(QRect(180, 80, 201, 20))
#         self.label_3 = QLabel(self.centralwidget)
#         self.label_3.setObjectName(u"label_3")
#         self.label_3.setGeometry(QRect(180, 130, 201, 20))
#         self.label_4 = QLabel(self.centralwidget)
#         self.label_4.setObjectName(u"label_4")
#         self.label_4.setGeometry(QRect(180, 180, 201, 20))
#         self.label_5 = QLabel(self.centralwidget)
#         self.label_5.setObjectName(u"label_5")
#         self.label_5.setGeometry(QRect(180, 230, 201, 20))
#         self.pushButton = QPushButton(self.centralwidget)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(230, 330, 93, 28))
#         SignUp.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(SignUp)
#         self.menubar.setObjectName(u"menubar")
#         self.menubar.setGeometry(QRect(0, 0, 540, 26))
#         SignUp.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(SignUp)
#         self.statusbar.setObjectName(u"statusbar")
#         SignUp.setStatusBar(self.statusbar)

#         self.retranslateUi(SignUp)

#         QMetaObject.connectSlotsByName(SignUp)
#     # setupUi

#     def retranslateUi(self, SignUp):
#         SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"SignUP", None))
#         self.checkBox.setText(QCoreApplication.translate("SignUp", u"  I read rules", None))
#         self.label.setText(QCoreApplication.translate("SignUp", u"First Name", None))
#         self.label_2.setText(QCoreApplication.translate("SignUp", u"Last Name", None))
#         self.label_3.setText(QCoreApplication.translate("SignUp", u"Email Address", None))
#         self.label_4.setText(QCoreApplication.translate("SignUp", u"New Password", None))
#         self.label_5.setText(QCoreApplication.translate("SignUp", u"Confirm Password", None))
#         self.pushButton.setText(QCoreApplication.translate("SignUp", u"SUbmit", None))
#     # retranslateUi

# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'SignUp.ui'
#
# Created by: Qt User Interface Compiler version 6.8.1
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QComboBox, QFileDialog)

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(540, 600)  # Adjusted height to accommodate new elements
        self.centralwidget = QWidget(SignUp)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Profile Picture
        self.profilePicLabel = QLabel(self.centralwidget)
        self.profilePicLabel.setObjectName(u"profilePicLabel")
        self.profilePicLabel.setGeometry(QRect(220, 10, 100, 100))
        self.profilePicLabel.setStyleSheet("border-radius: 50px; border: 2px solid gray;")
        self.profilePicLabel.setPixmap(QPixmap("default_profile.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))  # Placeholder image
        self.profilePicLabel.setAlignment(Qt.AlignCenter)

        # Upload Button
        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(220, 120, 100, 30))
        self.uploadButton.setText("Upload")
        self.uploadButton.clicked.connect(self.uploadProfilePicture)

        # First Name
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(180, 160, 201, 31))
        
        # Phone Number
        self.phoneLineEdit = QLineEdit(self.centralwidget)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setGeometry(QRect(180, 210, 201, 31))
        
        # Choice Option (ComboBox)
        self.choiceComboBox = QComboBox(self.centralwidget)
        self.choiceComboBox.setObjectName(u"choiceComboBox")
        self.choiceComboBox.setGeometry(QRect(180, 260, 201, 31))
        self.choiceComboBox.addItems(["Personal Finance", "Business Finance", "Overall"])

        # Other Fields
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(180, 310, 201, 31))
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(180, 360, 201, 31))
        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(180, 410, 201, 31))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 460, 201, 31))

        # Labels
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 140, 201, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 190, 201, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 240, 201, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 290, 201, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 340, 201, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 390, 201, 20))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 440, 201, 20))

        # Submit Button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 520, 93, 28))
        self.pushButton.setText("Submit")
        
        SignUp.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SignUp)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 26))
        SignUp.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SignUp)
        self.statusbar.setObjectName(u"statusbar")
        SignUp.setStatusBar(self.statusbar)

        self.retranslateUi(SignUp)
        QMetaObject.connectSlotsByName(SignUp)

    def uploadProfilePicture(self):
        filePath, _ = QFileDialog.getOpenFileName(None, "Choose Profile Picture", "", "Images (*.png *.xpm *.jpg *.jpeg)")
        if filePath:
            self.profilePicLabel.setPixmap(QPixmap(filePath).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.label.setText(QCoreApplication.translate("SignUp", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("SignUp", u"Phone Number", None))
        self.label_3.setText(QCoreApplication.translate("SignUp", u"Choose Option", None))
        self.label_4.setText(QCoreApplication.translate("SignUp", u"Email Address", None))
        self.label_5.setText(QCoreApplication.translate("SignUp", u"New Password", None))
        self.label_6.setText(QCoreApplication.translate("SignUp", u"Confirm Password", None))
        self.label_7.setText(QCoreApplication.translate("SignUp", u"Last name", None))
