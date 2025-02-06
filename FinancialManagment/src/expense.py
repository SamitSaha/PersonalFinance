from src.auth import DatabaseConnection
from src.transaction import Transaction


class Expense(Transaction):
    def __init__(self, user_id, category, amount, date):
        super().__init__(user_id, amount, date)
        self["category"] = category  # Dynamic attribute

    def save(self):
        db = DatabaseConnection()
        cursor = db.get_cursor()

        cursor.execute(
            "INSERT INTO expenses (user_id, category, amount, date) VALUES (%s, %s, %s, %s)",
            (self["user_id"], self["category"], self["amount"], self["date"])
        )

        db.commit()
        print(f"Expense recorded: {self['category']} - {self['amount']} on {self['date']}")
