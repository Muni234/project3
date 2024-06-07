import json
import os
from datetime import datetime

class ExpenseTracker:
    def _init_(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, date, amount, category, description):
        expense = {
            'id': len(self.expenses) + 1,
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self, filter_by=None, filter_value=None):
        filtered_expenses = self.expenses
        if filter_by and filter_value:
            filtered_expenses = [expense for expense in self.expenses if expense[filter_by] == filter_value]
        
        for expense in filtered_expenses:
            print(f"ID: {expense['id']}, Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def delete_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense['id'] != expense_id]
        self.save_expenses()

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(date, amount, category, description)

        elif choice == '2':
            filter_option = input("Do you want to filter by date or category? (y/n): ").lower()
            if filter_option == 'y':
                filter_by = input("Filter by (date/category): ")
                filter_value = input(f"Enter {filter_by}: ")
                tracker.view_expenses(filter_by, filter_value)
            else:
                tracker.view_expenses()

        elif choice == '3':
            expense_id = int(input("Enter the ID of the expense to delete: "))
            tracker.delete_expense(expense_id)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == '_main_':
    main()
