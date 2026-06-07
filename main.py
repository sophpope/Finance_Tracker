from db_utils import Database
from expenses import Expenses

db = Database()

expenses = Expenses(db)

#add an expense
expenses.add_expense(
    24.95, #cost of expense
    "Wing Stop", #description of expense
    3 #category_id (takeaway)
)

#getting all expenses
all_expenses = expenses.view_expenses()

#looping through expenses and print to console
for expense in all_expenses:
    print(expense)

#total of expenses 
total = expenses.total_expenses()

print(f"\nTotal Expenses: £{total}")

db.close()
