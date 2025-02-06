import matplotlib.pyplot as plt

from src.auth import DatabaseConnection


class Report:
    @staticmethod
    def generate_expense_report(user_id):
        db = DatabaseConnection()
        cursor = db.get_cursor()
        cursor.execute(
            "SELECT category, SUM(amount) FROM expenses WHERE user_id = %s GROUP BY category",
            (user_id,)
        )
        data = cursor.fetchall()

        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]

        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()
