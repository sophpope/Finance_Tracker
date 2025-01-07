class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount

        
    

class FinanceTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed")
        else:
            print("Invalid expense index")
            # add a for loop, to try again until valid index?

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Category: {expense.category}, Description: {expense.description}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: £{total:.2f}")

def main():
    tracker = FinanceTracker()

    categories = [
            "Groceries 🛒",
            "Eating Out 🍽️",
            "Takeaway 🥡",
            "Entertainment 🎭",
            "Activity 💃",
            "Exersize 🏋️‍♀️",
            "Clothes 👚",
            "Beauty 💄",
            "Electronic 📱",
            "Car Maintenance 🚗",
            "Utilities 💡",
            "Housing 🏡",
            "Medical 🏥",
            "Misc ❓"
        ]

    while True:
        print("\n Finance Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            for i, category_name in enumerate(categories):
                print(f"{i}. {category_name}")
            category = input("Enter the category index: ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount in £: "))
            expense = Expense(date, category, description, amount)
            tracker.add_expense(expense)

        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()




