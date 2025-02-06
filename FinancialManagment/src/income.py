class Income(Transaction):
    def __init__(self, user_id, source, amount, date):
        super().__init__(user_id, amount, date)
        self["source"] = source  # Dynamic attribute

    def save(self):
        db = DatabaseConnection()
        cursor = db.get_cursor()

        cursor.execute(
            "INSERT INTO income (user_id, source, amount, date) VALUES (%s, %s, %s, %s)",
            (self["user_id"], self["source"], self["amount"], self["date"])
        )

        db.commit()
        print(f"Income recorded: {self['source']} - {self['amount']} on {self['date']}")
