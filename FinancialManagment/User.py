import bcrypt
from Database.Signup_db import DatabaseConnection

class User:
    def _init_(self, first_name, last_name, email, phone, password, profile_pic=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.profile_pic = profile_pic  # Optional profile picture
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # Hash password

    def save(self):
        db = DatabaseConnection()
        cursor = db.get_cursor()

    
        cursor.execute("SELECT email FROM users WHERE email = %s", (self.email,))
        if cursor.fetchone():
            return False, "Email is already registered!"

        cursor.execute(
            "INSERT INTO users (first_name, last_name, email, phone, password_hash, profile_pic) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.first_name, self.last_name, self.email, self.phone, self.password_hash, self.profile_pic)
        )
        db.commit()
        return True, "User registered successfully!"