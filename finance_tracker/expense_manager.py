from .expense import Expense
from .file_handler import load_data, save_data


class ExpenseManager:

    def __init__(self):
        self.expenses = load_data()

    def add(self, amount, category, desc):
        exp = Expense(amount, category, desc)
        self.expenses.append(exp.to_dict())
        save_data(self.expenses)

    def view(self):
        for e in self.expenses:
            print(e)
