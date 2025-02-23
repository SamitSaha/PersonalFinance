import mysql.connector

class ExpenseDB:
    def __init__(self):
        """Initialize database connection."""
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",  # Change if necessary
            password="admin",  # Change this
            database="financemanagment"
        )
        self.cursor = self.db.cursor()

    def fetch_all_expenses(self):
        """Fetch all expenses from the database."""
        self.cursor.execute("SELECT * FROM expense")
        return self.cursor.fetchall()

    def add_expense(self, date, expensename, cost, userid, category, totalexpense):
        """Add a new expense to the database."""
        query = "INSERT INTO expense (date, expensename, cost, userid, category, totalexpense) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (date, expensename, cost, userid, category, totalexpense))
        self.db.commit()

    def update_expense(self, expense_id, date, expensename, cost, userid, category, totalexpense):
        """Update an existing expense based on a unique ID."""
        query = """
        UPDATE expense 
        SET date=%s, expensename=%s, cost=%s, userid=%s, category=%s, totalexpense=%s 
        WHERE id=%s
        """
        self.cursor.execute(query, (date, expensename, cost, userid, category, totalexpense, expense_id))
        self.db.commit()
    

    def delete_expense(self, id):
        """Delete an expense from the database based on id."""
        query = "DELETE FROM expense WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.db.commit()
