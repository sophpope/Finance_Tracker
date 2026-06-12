from finance_report import FinanceReport
from expenses import Expenses
from categories import Categories
import time

class Budget:
    def __init__(self,db):
        self.db = db
        self.finance_report = FinanceReport(db) 
        self.expenses = Expenses(db)
        self.categories = Categories(db)

    
    #set a budget for the month
    def add_budget(self):
        while True:
            try:
                print("Please view the categories for the budget")
                #re-using the function to view the expense categories
                self.expenses.view_expense_categories()

                budget_category = int(input("Please enter the category_id for the budget: "))
                if budget_category is None or budget_category > 16 or budget_category < 1:
                    print("Please enter a valid category_id")
                    time.sleep(2) 
                    continue
                
                amount = float(input("Please enter the monthly budget you would like to set: £"))
                if amount <= 0:
                    print("Budget amunt must be greater than 0")
                    time.sleep(2)
                    continue
                
                month = int(input("Enter the month number for the budget: "))
                if month < 1 or month > 12:
                    print("Month must be between 1 and 12")
                    time.sleep(2)
                    continue
                
                year = int(input("Enter the year for the budget: "))
        
                
                query = """INSERT INTO budgets (category_id, amount, month, year)
                VALUES(%s, %s, %s, %s)"""
            
                category_name =  self.categories.get_category_name(budget_category)


                self.db.execute(query, (budget_category, amount, month, year))

                print(f"{category_name} Budget added successfully!")
                break
            
            except ValueError:
                print("Please enter a valid number")

    def view_budgets(self):
        query = """SELECT b.budget_id, b.amount, c.name, b.month, b.year
        FROM budgets b
        JOIN categories c
        ON b.category_id = c.category_id
        """

        all_budgets = self.db.fetch_all(query)

        print("---- ALL BUDGETS ---")

        for budget_id, amount, name, month, year in all_budgets:
            print(
                f"ID: {budget_id}"
                f"\nAmount: £{amount}"
                f"\nCategory: {name}"
                f"\nDate {month}/{year}"
                "\n-------------------------"
            )

    def remove_budget(self):
        while True:
            try:
                self.view_budgets()
                budget_id = int(input("Please enter the Budget ID you would like to remove: "))

                query = """DELETE FROM budgets WHERE budget_id = %s"""

                result = self.db.execute(query, (budget_id,))

                if result is None:
                    print("ID does not exist")
                    time.sleep(2)
                    continue
                    

                print(f"Budget {budget_id} removed successfully")

            except ValueError:
                ("Please enter a valid Budget ID")

    def view_monthly_budget(self):
        try:
            while True:
                self.expenses.view_expense_categories()

                category_budget = """SELECT amount 
                FROM budgets
                WHERE category_id = %s
                AND month = %s
                AND year = %s"""

                category_spent = """SELECT COALESCE(SUM(amount), 0)
                FROM expenses
                WHERE category_id = %s
                AND EXTRACT(MONTH FROM expense_date) = %s
                AND EXTRACT(YEAR FROM expense_date) = %s"""

                budget_category_id = int(input("Please enter the category_id for the budget you want to view: "))
                #change this if any new categories are added 
                if budget_category_id is None or budget_category_id > 16 or budget_category_id < 1:
                    print('Please enter a valid category_id')
                    time.sleep(2)
                    continue 

                month = int(input("Enter the month: "))
                if month < 1 or month > 12:
                    print("Please enter a valid month number")
                    time.sleep(2)

                year = int(input("Enter the year: "))
            
                category_name =  self.categories.get_category_name(budget_category_id)

                budget_result = self.db.fetch_one(category_budget, (budget_category_id, month, year,))

                if budget_result is None:
                    print("No budget found.")
                    return
                
                budget_amount = budget_result[0]

                total_spent = self.db.fetch_one(category_spent, (budget_category_id, month, year,))[0]

                remaining_budget = budget_amount - total_spent

                print(f"\n---{category_name} Budget Overview ----")

                print(f"\nBudget: £{budget_amount}")
                print(f"\nSpent: £{total_spent}")
                print(f"\nRemaining: £{remaining_budget}")

                if remaining_budget < 0:
                    print(f"You are over budget by £{abs(remaining_budget)}")

                else:
                    print(f"You have £{remaining_budget} remaining in {category_name} budget")

        except ValueError:
            print("Please enter a valid value")

                       