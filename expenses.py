

class Expenses:
    def __init__(self, db):
        self.db = db

    #adding expenses to the database, %s is used as placeholder in psycopg2
    def add_expense(self):
        amount = float(input("Enter expense amount: £"))
        description = input("Enter expense description:")
        category_id = int(input("Enter category ID:"))
        query = """
        INSERT INTO expenses (amount, description, category_id)
        VALUES(%s, %s, %s)"""
        self.db.execute(query, (amount, description, category_id))
        print("Expense added successfully!")

    #shows all expenses, using an inner join to combine expenses and categories table
    def view_expenses(self):
        query = """
        SELECT e.expense_id, e.amount, e.description, c.name, e.expense_date
        FROM expenses e
        JOIN categories c
        ON e.category_id = c.category_id
        ORDER BY e.expense_date DESC

        """

        all_expenses = self.db.fetch_all(query)

        print("--- ALL EXPENSES ---")

        for expense_id, amount, description, category, expense_date in all_expenses:
            print(
                f"ID: {expense_id}"
                f"\nAmount: £{amount}"
                f"\nDescription: {description}"
                f"\nCategory: {category}"
                f"\nDate: {expense_date}"
                "\n--------------------------")
                  
              

        
    
    def remove_expense(self, expense_id):
        query = """
        DELETE FROM expenses
            WHERE expense_id = %s
            """
        self.db.execute(query, (expense_id))

        print("Expense removed successfully")

    #shows the total of all the expenses, using COALESCE to prevent null values, if no expenses
    def total_expenses(self):
        query = """SELECT COALESCE(SUM(amount), 0)
        FROM expenses"""

        result = self.db.fetch_one(query)
        return result[0]
