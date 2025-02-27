import mysql.connector

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="PersonalFinanceDB"
            )
        return cls._instance
    
    def get_cursor(self):
        return self.connection.cursor(dictionary=True)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
    