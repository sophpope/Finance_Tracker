from db_utils import Database
from expenses import Expenses
from income import Income
import time
from finance_report import FinanceReport
from budget import Budget


def main():
    db = Database()

    expenses = Expenses(db)
    income = Income(db)
    finance_report = FinanceReport(db)
    budget = Budget(db)

    while True:
        try:
            print("\n Finance Tracker Menu:")
            print("1. Add Expense")
            print("2. Remove Expense")
            print("3. View Expenses")
            print("4. Add Income")
            print("5. Remove Income")
            print("6. View Income")
            print("7. View Monthly Summary")
            print("8. View Spending by Category")
            print("9. Add Budget")
            print("10. Remove Budget")
            print("11. Monthly Budget Overview")
            print("12. Exit")

            choice = int(input("Enter your choice (1-12): "))

            #change this is more options added to the list!
            if choice <= 1 or choice >= 12:
                print("Please enter a choice between 1 - 12")
                time.sleep(2)
                continue

            if choice == 1:
                expenses.add_expense()

            elif choice == 2:
                expenses.remove_expense()

            elif choice == 3:
                expenses.view_expenses()

            elif choice == 4:
                income.add_income()

            elif choice == 5:
                income.remove_income()

            elif choice == 6:
                income.view_income()

            elif choice == 7:
                finance_report.monthly_summary()

            elif choice == 8:
                finance_report.category_spending()

            elif choice == 9:
                budget.add_budget()

            elif choice == 10:
                budget.remove_budget()

            elif choice == 11:
                budget.view_monthly_budget()

            elif choice == 12:
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

            time.sleep(2)
        
        except ValueError:
            print("Please enter a number between 1-12")
        

if __name__ == "__main__":
    main()


# #add an expense
# expenses.add_expense(
#     24.95, #cost of expense
#     "Wing Stop", #description of expense
#     3 #category_id (takeaway)
# )

# #getting all expenses
# all_expenses = expenses.view_expenses()

# #looping through expenses and print to console
# for expense in all_expenses:
#     print(expense)

# #total of expenses 
# total = expenses.total_expenses()

# print(f"\nTotal Expenses: £{total}")

# db.close()
