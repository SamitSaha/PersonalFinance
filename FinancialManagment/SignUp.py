

# from PySide6.QtCore import (QCoreApplication, QMetaObject,QRect, Qt)
# from PySide6.QtGui import (QPixmap)
# from PySide6.QtWidgets import (QLabel, QLineEdit, QMenuBar, QPushButton, QMessageBox, QStatusBar, QWidget, QComboBox, QFileDialog)
# from User import User
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
#         self.lineEdit.setGeometry(QRect(180, 160, 201, 31))
        
#         # Phone Number
#         self.phoneLineEdit = QLineEdit(self.centralwidget)
#         self.phoneLineEdit.setObjectName(u"phoneLineEdit")
#         self.phoneLineEdit.setGeometry(QRect(180, 210, 201, 31))
        
#         # Choice Option (ComboBox)
#         self.choiceComboBox = QComboBox(self.centralwidget)
#         self.choiceComboBox.setObjectName(u"choiceComboBox")
#         self.choiceComboBox.setGeometry(QRect(180, 260, 201, 31))
#         self.choiceComboBox.addItems(["Personal Finance", "Business Finance", "Overall"])

#         # Other Fields
#         self.lineEdit_7 = QLineEdit(self.centralwidget)
#         self.lineEdit_7.setObjectName(u"lineEdit_7")
#         self.lineEdit_7.setGeometry(QRect(180, 310, 201, 31))
#         self.lineEdit_8 = QLineEdit(self.centralwidget)
#         self.lineEdit_8.setObjectName(u"lineEdit_8")
#         self.lineEdit_8.setGeometry(QRect(180, 360, 201, 31))
#         self.lineEdit_9 = QLineEdit(self.centralwidget)
#         self.lineEdit_9.setObjectName(u"lineEdit_9")
#         self.lineEdit_9.setGeometry(QRect(180, 410, 201, 31))
#         self.lineEdit_2 = QLineEdit(self.centralwidget)
#         self.lineEdit_2.setObjectName(u"lineEdit_2")
#         self.lineEdit_2.setGeometry(QRect(180, 460, 201, 31))

#         # Labels
#         self.label = QLabel(self.centralwidget)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(180, 140, 201, 20))
#         self.label_2 = QLabel(self.centralwidget)
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setGeometry(QRect(180, 190, 201, 20))
#         self.label_3 = QLabel(self.centralwidget)
#         self.label_3.setObjectName(u"label_3")
#         self.label_3.setGeometry(QRect(180, 240, 201, 20))
#         self.label_4 = QLabel(self.centralwidget)
#         self.label_4.setObjectName(u"label_4")
#         self.label_4.setGeometry(QRect(180, 290, 201, 20))
#         self.label_5 = QLabel(self.centralwidget)
#         self.label_5.setObjectName(u"label_5")
#         self.label_5.setGeometry(QRect(180, 340, 201, 20))
#         self.label_6 = QLabel(self.centralwidget)
#         self.label_6.setObjectName(u"label_6")
#         self.label_6.setGeometry(QRect(180, 390, 201, 20))
#         self.label_7 = QLabel(self.centralwidget)
#         self.label_7.setObjectName(u"label_7")
#         self.label_7.setGeometry(QRect(180, 440, 201, 20))

#         # Submit Button
#         self.pushButton = QPushButton(self.centralwidget)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(230, 520, 93, 28))
#         self.pushButton.setText("Submit")
        
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

#     def uploadProfilePicture(self):
#         filePath, _ = QFileDialog.getOpenFileName(None, "Choose Profile Picture", "", "Images (*.png *.xpm *.jpg *.jpeg)")
#         if filePath:
#             self.profilePicLabel.setPixmap(QPixmap(filePath).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))

#     def retranslateUi(self, SignUp):
#         SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Sign Up", None))
#         self.label.setText(QCoreApplication.translate("SignUp", u"First Name", None))
#         self.label_2.setText(QCoreApplication.translate("SignUp", u"Phone Number", None))
#         self.label_3.setText(QCoreApplication.translate("SignUp", u"Choose Option", None))
#         self.label_4.setText(QCoreApplication.translate("SignUp", u"Email Address", None))
#         self.label_5.setText(QCoreApplication.translate("SignUp", u"New Password", None))
#         self.label_6.setText(QCoreApplication.translate("SignUp", u"Confirm Password", None))
#         self.label_7.setText(QCoreApplication.translate("SignUp", u"Last name", None))
        
#     def register_user(self):
       
#         first_name = self.lineEdit.text()
#         last_name = self.lineEdit_2.text()
#         email = self.lineEdit_8.text()
#         phone = self.phoneLineEdit.text()
#         password = self.lineEdit_7.text()
#         confirm_password = self.lineEdit_9.text()

#         if password != confirm_password:
#             QMessageBox.warning(None, "Error", "Passwords do not match!")
#             return

#         if not email or not password or not first_name or not last_name or not phone:
#             QMessageBox.warning(None, "Error", "All fields are required!")
#             return

#         # Get profile picture (if uploaded)
#         profile_pic = getattr(self, "profilePicPath", None)

#         # Create user object and save to DB
#         user = User(first_name, last_name, email, phone, password, profile_pic)
#         success, message = user.save()

#         if success:
#             QMessageBox.information(None, "Success", "Account created successfully!")
#         else:
#             QMessageBox.warning(None, "Error", message)


# from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
# from PySide6.QtGui import (QPixmap)
# from PySide6.QtWidgets import (QLabel, QLineEdit, QMenuBar, QPushButton, QMessageBox, QStatusBar, QWidget, QFileDialog)
# from User import User

# class Ui_SignUp(object):
#     def setupUi(self, SignUp):
#         if not SignUp.objectName():
#             SignUp.setObjectName(u"SignUp")
#         SignUp.resize(540, 600)
#         self.centralwidget = QWidget(SignUp)
#         self.centralwidget.setObjectName(u"centralwidget")
        
#         # Profile Picture
#         self.profilePicLabel = QLabel(self.centralwidget)
#         self.profilePicLabel.setObjectName(u"profilePicLabel")
#         self.profilePicLabel.setGeometry(QRect(220, 10, 100, 100))
#         self.profilePicLabel.setStyleSheet("border-radius: 50px; border: 2px solid gray;")
#         self.profilePicLabel.setPixmap(QPixmap("default_profile.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
#         self.profilePicLabel.setAlignment(Qt.AlignCenter)

#         # Upload Button
#         self.uploadButton = QPushButton(self.centralwidget)
#         self.uploadButton.setObjectName(u"uploadButton")
#         self.uploadButton.setGeometry(QRect(220, 120, 100, 30))
#         self.uploadButton.setText("Upload")
#         self.uploadButton.clicked.connect(self.uploadProfilePicture)

#         # First Name
#         self.firstNameLineEdit = QLineEdit(self.centralwidget)
#         self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
#         self.firstNameLineEdit.setGeometry(QRect(180, 160, 201, 31))
        
#         # Last Name
#         self.lastNameLineEdit = QLineEdit(self.centralwidget)
#         self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
#         self.lastNameLineEdit.setGeometry(QRect(180, 210, 201, 31))
        
#         # Phone Number
#         self.phoneLineEdit = QLineEdit(self.centralwidget)
#         self.phoneLineEdit.setObjectName(u"phoneLineEdit")
#         self.phoneLineEdit.setGeometry(QRect(180, 260, 201, 31))
        
#         # Email Address
#         self.emailLineEdit = QLineEdit(self.centralwidget)
#         self.emailLineEdit.setObjectName(u"emailLineEdit")
#         self.emailLineEdit.setGeometry(QRect(180, 310, 201, 31))
        
#         # New Password
#         self.newPasswordLineEdit = QLineEdit(self.centralwidget)
#         self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
#         self.newPasswordLineEdit.setGeometry(QRect(180, 360, 201, 31))
        
#         # Confirm Password
#         self.confirmPasswordLineEdit = QLineEdit(self.centralwidget)
#         self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
#         self.confirmPasswordLineEdit.setGeometry(QRect(180, 410, 201, 31))
        
#         # Submit Button
#         self.submitButton = QPushButton(self.centralwidget)
#         self.submitButton.setObjectName(u"submitButton")
#         self.submitButton.setGeometry(QRect(230, 470, 93, 28))
#         self.submitButton.setText("Submit")
        
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

#     def uploadProfilePicture(self):
#         filePath, _ = QFileDialog.getOpenFileName(None, "Choose Profile Picture", "", "Images (*.png *.xpm *.jpg *.jpeg)")
#         if filePath:
#             self.profilePicLabel.setPixmap(QPixmap(filePath).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))

#     def retranslateUi(self, SignUp):
#         SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Sign Up", None))
#         self.firstNameLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"First Name", None))
#         self.lastNameLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Last Name", None))
#         self.phoneLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Phone Number", None))
#         self.emailLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Email Address", None))
#         self.newPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"New Password", None))
#         self.confirmPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Confirm Password", None))

#     def register_user(self):
#         first_name = self.firstNameLineEdit.text()
#         last_name = self.lastNameLineEdit.text()
#         phone = self.phoneLineEdit.text()
#         email = self.emailLineEdit.text()
#         password = self.newPasswordLineEdit.text()
#         confirm_password = self.confirmPasswordLineEdit.text()

#         if password != confirm_password:
#             QMessageBox.warning(None, "Error", "Passwords do not match!")
#             return

#         if not first_name or not last_name or not phone or not email or not password:
#             QMessageBox.warning(None, "Error", "All fields are required!")
#             return

#         # Get profile picture (if uploaded)
#         profile_pic = getattr(self, "profilePicPath", None)

#         # Create user object and save to DB
#         user = User(first_name, last_name, email, phone, password, profile_pic)
#         success, message = user.save()

#         if success:
#             QMessageBox.information(None, "Success", "Account created successfully!")
#         else:
#             QMessageBox.warning(None, "Error", message)


from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QLabel, QLineEdit, QMenuBar, QPushButton, QMessageBox, QStatusBar, QWidget, QFileDialog)
from User import User
import bcrypt
from Database.Signup_db import DatabaseConnection

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(540, 600)
        self.centralwidget = QWidget(SignUp)
        self.centralwidget.setObjectName(u"centralwidget")

        # Profile Picture
        self.profilePicLabel = QLabel(self.centralwidget)
        self.profilePicLabel.setObjectName(u"profilePicLabel")
        self.profilePicLabel.setGeometry(QRect(220, 10, 100, 100))
        self.profilePicLabel.setStyleSheet("border-radius: 50px; border: 2px solid gray;")
        self.profilePicLabel.setPixmap(
            QPixmap("default_profile.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.profilePicLabel.setAlignment(Qt.AlignCenter)

        # Upload Button
        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(220, 120, 100, 30))
        self.uploadButton.setText("Upload")
        self.uploadButton.clicked.connect(self.uploadProfilePicture)

        # First Name
        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(180, 160, 201, 31))

        # Last Name
        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(180, 210, 201, 31))

        # Phone Number
        self.phoneLineEdit = QLineEdit(self.centralwidget)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setGeometry(QRect(180, 260, 201, 31))

        # Email Address
        self.emailLineEdit = QLineEdit(self.centralwidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(180, 310, 201, 31))

        # New Password
        self.newPasswordLineEdit = QLineEdit(self.centralwidget)
        self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
        self.newPasswordLineEdit.setGeometry(QRect(180, 360, 201, 31))

        # Confirm Password
        self.confirmPasswordLineEdit = QLineEdit(self.centralwidget)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
        self.confirmPasswordLineEdit.setGeometry(QRect(180, 410, 201, 31))

        # Submit Button
        self.submitButton = QPushButton(self.centralwidget)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(230, 470, 93, 28))
        self.submitButton.setText("Submit")
        self.submitButton.clicked.connect(self.register_user)

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
        """Handles profile picture selection."""
        filePath, _ = QFileDialog.getOpenFileName(None, "Choose Profile Picture", "", "Images (*.png *.jpg *.jpeg)")
        if filePath:
            self.profilePicLabel.setPixmap(QPixmap(filePath).scaled(100, 100))
            self.profilePicPath = filePath  # Store image path

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.firstNameLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"First Name", None))
        self.lastNameLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Last Name", None))
        self.phoneLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Phone Number", None))
        self.emailLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Email Address", None))
        self.newPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"New Password", None))
        self.confirmPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("SignUp", u"Confirm Password", None))

    def register_user(self):
        """Handles user registration and stores data in MySQL."""
        first_name = self.firstNameLineEdit.text().strip()
        last_name = self.lastNameLineEdit.text().strip()
        phone = self.phoneLineEdit.text().strip()
        email = self.emailLineEdit.text().strip()
        password = self.newPasswordLineEdit.text()
        confirm_password = self.confirmPasswordLineEdit.text()

        if password != confirm_password:
            QMessageBox.warning(None, "Error", "Passwords do not match!")
            return

        if not first_name or not last_name or not phone or not email or not password:
            QMessageBox.warning(None, "Error", "All fields are required!")
            return

        # Hash the password securely
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # Get profile picture path (if uploaded)
        profile_pic = getattr(self, "profilePicPath", None)

        try:
            db = DatabaseConnection()
            cursor = db.get_cursor()

            # Check if email already exists
            cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                QMessageBox.warning(None, "Error", "Email is already registered!")
                return

            # Insert user into the database
            cursor.execute(
                "INSERT INTO users (first_name, last_name, email, phone, password_hash, profile_pic) VALUES (%s, %s, %s, %s, %s, %s)",
                (first_name, last_name, email, phone, password_hash, profile_pic)
            )
            db.commit()

            QMessageBox.information(None, "Success", "Account created successfully!")

            # Clear input fields after success
            self.firstNameLineEdit.clear()
            self.lastNameLineEdit.clear()
            self.phoneLineEdit.clear()
            self.emailLineEdit.clear()
            self.newPasswordLineEdit.clear()
            self.confirmPasswordLineEdit.clear()

        except Exception as e:
            QMessageBox.warning(None, "Database Error", f"Failed to register user: {str(e)}")
        
    # def register_user(self, bcrypt=None):
    #     """Handles user registration and stores data in MySQL."""
    #     first_name = self.firstNameLineEdit.text()
    #     last_name = self.lastNameLineEdit.text()
    #     phone = self.phoneLineEdit.text()
    #     email = self.emailLineEdit.text()
    #     password = self.newPasswordLineEdit.text()
    #     confirm_password = self.confirmPasswordLineEdit.text()

    #     if password != confirm_password:
    #         QMessageBox.warning(None, "Error", "Passwords do not match!")
    #         return

    #     if not first_name or not last_name or not phone or not email or not password:
    #         QMessageBox.warning(None, "Error", "All fields are required!")
    #         return

    #     # Hash the password securely
    #     password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    #     # Get profile picture path (if uploaded)
    #     profile_pic = getattr(self, "profilePicPath", None)

    #     # Save to database
    #     try:
    #         db = DatabaseConnection()
    #         cursor = db.get_cursor()

    #         # Check if email already exists
    #         cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
    #         if cursor.fetchone():
    #             QMessageBox.warning(None, "Error", "Email is already registered!")
    #             return

    #         # Insert user into the database
    #         cursor.execute(
    #             "INSERT INTO users (first_name, last_name, email, phone, password_hash, profile_pic) VALUES (%s, %s, %s, %s, %s, %s)",
    #             (first_name, last_name, email, phone, password_hash, profile_pic)
    #         )
    #         db.commit()

    #         QMessageBox.information(None, "Success", "Account created successfully!")

    #     except Exception as e:
    #         QMessageBox.warning(None, "Database Error", f"Failed to register user: {str(e)}")