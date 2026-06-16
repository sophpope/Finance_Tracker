import time
from categories import Categories

class FinanceReport:
    def __init__(self, db):
        self.db = db
        self.categories = Categories(db)

    def monthly_summary(self):
        try:
            while True:
                print("Enter the month and year would like summarised")
                month = int(input("Enter month number: "))
                if month < 1 or month > 12:
                    print("Please enter a valid month number")
                    time.sleep(2)
                    continue 

                year = int(input("Enter year: "))
                
                income_exists = self.categories.check_valid_date("incomes", "income_date", month, year)
                expenses_exist = self.categories.check_valid_date("expenses", 'expense_date', month, year)

                if not income_exists and not expenses_exist:
                    print("No records found for that month and year")
                    time.sleep(2)
                    continue

                income_summary = """SELECT COALESCE(SUM(amount), 0)
                FROM incomes
                WHERE EXTRACT(MONTH FROM income_date) = %s
                AND EXTRACT(YEAR FROM income_date) = %s
                """

                expense_summary = """SELECT COALESCE(SUM(amount), 0)
                FROM expenses
                WHERE EXTRACT(MONTH FROM expense_date) = %s
                AND EXTRACT(YEAR FROM expense_date) = %s
                """

                total_income = self.db.fetch_one(income_summary, (month, year))[0]
                total_expenses = self.db.fetch_one(expense_summary, (month, year))[0]

                balance = total_income - total_expenses

                print(F"\n--- {month}/{year} SUMMARY ---")

                print(f"\nTotal Income: £{total_income}")
                print(f"\nTotal Expenses: £{total_expenses}")
                print(f"\nRemaining Balance: £{balance}")
                break

        except ValueError:
            print("Please enter a valid value")

    def category_spending(self):

        try:
            while True:

                #showing the exisiting expense/spending categories
                self.categories.view_expense_categories()

                
                selected_category_id = int(input("\nEnter the category_id you would like view: "))

                if selected_category_id is None or selected_category_id > 16 or selected_category_id < 1:
                    print("Please enter a valid category_id")
                    time.sleep(2)
                    continue

                category_summary = """SELECT e.expense_id, e.amount, e.description, c.name, e.expense_date
                FROM expenses e
                JOIN categories c
                ON e.category_id = c.category_id
                WHERE e.category_id = %s
                ORDER BY e.expense_date DESC
                """

                category_all = self.db.fetch_all(category_summary, (selected_category_id,))
                
                expense_records = self.categories.check_category_records("expenses", selected_category_id)
                income_records = self.categories.check_category_records("incomes", selected_category_id)
                
                category_name = self.categories.get_category_name(selected_category_id)


                if not expense_records and not income_records:
                    print(f"No {category_name} records found")
                    time.sleep(3)
                    continue



                print(f"--- {category_name} Category Overview ---")

                for expense_id, amount, description, category, expense_date in category_all:
                    print(
                        f"ID: {expense_id}"
                        f"\nAmount: £{amount}"
                        f"\nDescription: {description}"
                        f"\nCategory: {category}"
                        f"\nDate: {expense_date}"
                        "\n--------------------------")
                
                break
                    
        except ValueError:
            print("Please enter a valid value")


