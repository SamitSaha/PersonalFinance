import bcrypt

from src.auth import DatabaseConnection


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def save(self):
        db = DatabaseConnection()
        cursor = db.get_cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (self.name, self.email, self.password)
        )
        db.commit()

    @staticmethod
    def authenticate(email, password):
        db = DatabaseConnection()
        cursor = db.get_cursor()
        cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
            return True
        return False
