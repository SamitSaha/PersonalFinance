import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="financemanagment"
        )
        self.cursor = self.conn.cursor()

    def insert_expense(self, date, expense_name, cost, user_id, category, total_expense):
        sql = """
        INSERT INTO expense_table (`Date`, `Expense Name`, `Cost`, `User ID`, `Category`, `Total Expense/Day`) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (date, expense_name, cost, user_id, category, total_expense)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def fetch_expenses(self):
        sql = "SELECT `id`, `Date`, `Expense Name`, `Cost`, `User ID`, `Category`, `Total Expense/Day` FROM expense_table"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def delete_expense(self, user_id):
        sql = "DELETE FROM expense_table WHERE `User ID` = %s"
        self.cursor.execute(sql, (user_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
