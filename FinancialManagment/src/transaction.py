class Transaction:
    def __init__(self, user_id, amount, date):
        self.data = {
            "user_id": user_id,
            "amount": amount,
            "date": date
        }

    def __getitem__(self, key):
        return self.data.get(key, None)

    def __setitem__(self, key, value):
        self.data[key] = value

    def save(self):
        """This method must be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement the 'save' method")
