from db_utils import Database
from expenses import Expenses


def main():
    db = Database()

    expenses = Expenses(db)

    while True:
        print("\n Finance Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Add Income")
        print("5. View Monthly Summary")
        print("6. View Spending by Category")
        print("7. Set Budget")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            expenses.add_expense()

        elif choice == '2':
            expenses.remove_expense()

        elif choice == '3':
            expenses.view_expenses()

        elif choice == '4':
            pass
            #add when i've added function/query for adding income

        elif choice == '5':
            pass
            #add when i've got a function/query for monthly summary

        elif choice == '6':
            pass
            #add when i've got a function query for spending by category

        elif choice == '7':
            pass
            #add when budget option set

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

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
