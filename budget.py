from finance_report import FinanceReport
from expenses import Expenses

class Budget:
    def __init__(self,db):
        self.db = db
        self.finance_report = FinanceReport(db) 
        self.expenses = Expenses(db)
    
    #set a budget for the month
    def add_budget(self):
        print("Please view the categories for the budget")
        #re-using the function to view the expense categories
        self.expenses.view_expense_categories()

        budget_category = int(input("Please enter the category_id for the budget: "))
        amount = float(input("Please enter the monthly budget you would like to set: £"))
        month = int(input("Enter the month number for the budget: "))
        year = int(input("Enter the year for the budget: "))

        query = """INSERT INTO budgets (category_id, amount, month, year)
        VALUES(%s, %s, %s, %s)"""

        self.db.execute(query, (budget_category, amount, month, year))
        print("Budget added successfully!")

        