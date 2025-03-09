# # Add the imports required for showing a profile dashboard
# from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QDialog
# from PySide6.QtGui import QPixmap
# from PySide6.QtCore import Qt

# class Ui_ProfileDashboard(QDialog):
#     def __init__(self, user_info):
#         super().__init__()
#         self.user_info = user_info  # User information passed to the dashboard
#         self.setWindowTitle("Profile Dashboard")
#         self.setGeometry(100, 100, 400, 400)
#         self.setupUi()

#     def setupUi(self):
#         # Create a vertical layout for the dashboard
#         layout = QVBoxLayout()

#         # Profile picture
#         if self.user_info.get("profile_picture"):
#             pixmap = QPixmap(self.user_info["profile_picture"])
#         else:
#             pixmap = QPixmap(100, 100)  # Default blank profile picture
#             pixmap.fill(Qt.gray)

#         profile_pic_label = QLabel(self)
#         profile_pic_label.setPixmap(pixmap)
#         profile_pic_label.setFixedSize(150, 150)
#         profile_pic_label.setScaledContents(True)

#         # Name label
#         name_label = QLabel(f"Name: {self.user_info.get('name', 'N/A')}")
#         name_label.setStyleSheet("font-size: 14px; font-weight: bold;")

#         # Email label
#         email_label = QLabel(f"Email: {self.user_info.get('email', 'N/A')}")
#         email_label.setStyleSheet("font-size: 14px;")

#         # Phone number label
#         phone_label = QLabel(f"Phone: {self.user_info.get('phone', 'N/A')}")
#         phone_label.setStyleSheet("font-size: 14px;")

#         # Option label
#         option_label = QLabel(f"Option: {self.user_info.get('option', 'N/A')}")
#         option_label.setStyleSheet("font-size: 14px;")

#         # Back button
#         back_button = QPushButton("Back")
#         back_button.clicked.connect(self.close)

#         # Adding widgets to the layout
#         layout.addWidget(profile_pic_label, alignment=Qt.AlignCenter)
#         layout.addWidget(name_label)
#         layout.addWidget(email_label)
#         layout.addWidget(phone_label)
#         layout.addWidget(option_label)
#         layout.addWidget(back_button, alignment=Qt.AlignCenter)

#         self.setLayout(layout) 

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class Ui_ProfileDashboard(QDialog):
    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info  # User data from login
        self.setWindowTitle("Profile Dashboard")
        self.setGeometry(100, 100, 400, 400)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        # Profile picture
        profile_pic_label = QLabel(self)
        if self.user_info.get("profile_picture"):
            pixmap = QPixmap(self.user_info["profile_picture"])
        else:
            pixmap = QPixmap(100, 100)  # Default blank profile picture
            pixmap.fill(Qt.gray)
        
        profile_pic_label.setPixmap(pixmap)
        profile_pic_label.setFixedSize(150, 150)
        profile_pic_label.setScaledContents(True)
        layout.addWidget(profile_pic_label, alignment=Qt.AlignCenter)

        # Name
        name_label = QLabel(f"Name: {self.user_info.get('name', 'N/A')}")
        name_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(name_label)

        # Email
        email_label = QLabel(f"Email: {self.user_info.get('email', 'N/A')}")
        email_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(email_label)

        # Phone
        phone_label = QLabel(f"Phone: {self.user_info.get('phone', 'N/A')}")
        phone_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(phone_label)

        # Back Button
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)
