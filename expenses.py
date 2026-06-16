
import time
from categories import Categories

class Expenses:
    def __init__(self, db):
        self.db = db
        self.categories = Categories(db)



    #adding expenses to the database, %s is used as placeholder in psycopg2
    def add_expense(self):
        try:
            while True:

                amount = float(input("Enter expense amount: £"))
                if amount <= 0:
                    print("Please enter a value higher than £")
                    time.sleep(2)
                    continue
            
                description = input("Enter expense description:")
                if description.strip() == "":
                    print("Please enter an expense description")
                    time.sleep(2)
                    continue

                self.categories.view_expense_categories()   
            
                category_id_input = int(input("Enter category ID:"))
                if category_id_input is None or category_id_input > 16 or category_id_input < 1:
                    print("Please enter a valid category_id")
                    time.sleep(2)
                    continue

                query = """
                INSERT INTO expenses (amount, description, category_id)
                VALUES(%s, %s, %s)"""

                category_name =  self.categories.get_category_name(category_id_input)

                self.db.execute(query, (amount, description, category_id_input))
                print(f"{category_name} Expense added successfully!")
                break
        
        except ValueError:
            ("Please enter a valid value")

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
                  
              

        
    
    def remove_expense(self):
        try:
            while True: 
                self.view_expenses()

                expense_id = int(input("Please enter the Expense ID you would like to remove: ")) 
                if not self.categories.check_item_exists("expenses", "expense_id", expense_id):
                    print("Expense ID does not exist")
                    time.sleep(2)
                    continue

                query = """
                DELETE FROM expenses
                    WHERE expense_id = %s
                    """
                self.db.execute(query, (expense_id,))

                print(f"Expense {expense_id} removed successfully")
                break

        except ValueError:
            print("Please enter a valid value")

    #shows the total of all the expenses, using COALESCE to prevent null values, if no expenses
    def total_expenses(self):
        query = """SELECT COALESCE(SUM(amount), 0)
        FROM expenses"""

        result = self.db.fetch_one(query)
        return result[0]
