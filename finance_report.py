class FinanceReport:
    def __init__(self, db):
        self.db = db

    def monthly_summary(self):
        print("Enter the month and year would like summarised")
        month = int(input("Enter month number: "))
        year = int(input("Enter year: "))

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

    def category_spending(self):

        #showing the exisiting categories

        category_query = """SELECT category_id, name 
        FROM categories
        ORDER BY category_id
        """

        categories = self.db.fetch_all(category_query)

        if not categories:
            print("No categories found")
            return

        print("\n--- All Categories ---")

        for category_id, name in categories:
            print(f"\n{category_id} | {name}")

        
        selected_category_id = input("\nEnter the category_id you would like view: ")

        if selected_category_id.strip() == "":
            print("Category ID cannot be empty")
            return

        category_summary = """SELECT e.expense_id, e.amount, e.description, c.name, e.expense_date
        FROM expenses e
        JOIN categories c
        ON e.category_id = c.category_id
        WHERE e.category_id = %s
        ORDER BY e.expense_date DESC
        """

        category_all = self.db.fetch_all(category_summary, (selected_category_id))

        if not category_all:
            print("No expenses/income found")
            return


        print("--- Category Overview ---")

        for expense_id, amount, description, category, expense_date in category_all:
            print(
                f"ID: {expense_id}"
                f"\nAmount: £{amount}"
                f"\nDescription: {description}"
                f"\nCategory: {category}"
                f"\nDate: {expense_date}"
                "\n--------------------------")

