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