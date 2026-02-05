from datetime import datetime


class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date or datetime.today().strftime("%Y-%m-%d")

    def to_dict(self):
        return self.__dict__
