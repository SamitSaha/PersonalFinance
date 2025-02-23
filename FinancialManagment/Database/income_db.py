import mysql.connector

class IncomeDB:
    def __init__(self):
        """Initialize database connection"""
        self.db = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="admin",
            database="financemanagment"
        )
        self.cursor = self.db.cursor()
    
    def fetch_all_income(self):
        """Fetech all the incomes from the database"""
        self.cursor.execute("SELECT * FROM income")
        return self.cursor.fetchall()
    
    def add_income(self, date, incomevalue, source, userid, category, totalincome):
        """Add a new expense to the database."""
        query = "INSERT INTO income (date, incomevalue, source, userid, category, totalincome) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (date, incomevalue, source, userid, category, totalincome))
        self.db.commit()
        
    def update_income(self, expense_id, date, incomevalue, source, userid, category, totalincome):
        """Update an existing income based on date."""
        query = """
        UPDATE income 
        SET date=%s, incomevalue=%s, source=%s, userid=%s, category=%s, totalincome=%s 
        WHERE id=%s
        """
        self.cursor.execute(query, (date, incomevalue, source, userid, category, totalincome, expense_id))
        self.db.commit()
    
    def delete_income(self, id):
        """Delete an income from the database based on id."""
        query = "DELETE FROM income WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.db.commit()    
        
        
        
        
        
        
        
        
        
        
        
        