import mysql.connector

class SavingsDB:
    def __init__(self):
        """Initialize database connection"""
        self.db = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="admin",
            database="financemanagment"
        )
        self.cursor = self.db.cursor()
    
    def fetch_all_savings(self):
        """Fetech all the savings from the database"""
        self.cursor.execute("SELECT * FROM savings")
        return self.cursor.fetchall()
    
    def add_savings(self, date, goal, goalamount, userid, trackprogress, savinggoal):
        """Add a new savings to the database."""
        query = "INSERT INTO savings (date, goal, goalamount, userid, trackprogress, savinggoal) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (date, goal, goalamount, userid, trackprogress, savinggoal))
        self.db.commit()
        
    def update_savings(self, expense_id, date, goal, goalamount, userid, trackprogress, savinggoal):
        """Update an existing savings based on date."""
        query = """
        UPDATE savings 
        SET date=%s, goal=%s, goalamount=%s, userid=%s, trackprogress=%s, savinggoal=%s 
        WHERE id=%s
        """
        self.cursor.execute(query, (date, goal, goalamount, userid, trackprogress, savinggoal, expense_id))
        self.db.commit()
    
    def delete_savings(self, id):
        """Delete an savings from the database based on id."""
        query = "DELETE FROM savings WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.db.commit()    
        
        
        
        
        
        
        
        
        
        
        
        