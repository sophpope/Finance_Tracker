from db_utils import Database
from expenses import Expenses
from income import Income
import time


def main():
    db = Database()

    expenses = Expenses(db)
    income = Income(db)

    while True:
        print("\n Finance Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Add Income")
        print("5. Remove Income")
        print("6. View Income")
        print("7. View Monthly Summary")
        print("8. View Spending by Category")
        print("9. Set Budget")
        print("10. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            expenses.add_expense()

        elif choice == '2':
            expenses.remove_expense()

        elif choice == '3':
            expenses.view_expenses()

        elif choice == '4':
            income.add_income()

        elif choice == '5':
            income.remove_income()

        elif choice == '6':
            income.view_income()

        elif choice == '7':
            pass
            #monthly summary

        elif choice == '8':
            pass
            #Spending by category

        elif choice == '9':
            pass # set budget

        elif choice == '10':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

        time.sleep(2)
        

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
