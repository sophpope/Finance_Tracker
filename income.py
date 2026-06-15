from categories import Categories
import time

class Income:
    def __init__(self, db):
        self.db = db
        self.categories = Categories(db)


    #adding income to the database 
    def add_income(self):

        while True: 
            amount = float(input("Enter income amount: £"))
            if amount <= 0:
                print("Please enter an amount above £0")
                time.sleep(2)
                continue

            description = input("Enter income description:")
            if description.strip() == "":
                print("Please enter a income description")
                time.sleep(2)
                continue
        
            self.categories.income_categories()

            category_id_input = int(input("Enter category ID:"))

            #change this if more income categories are added to the database
            if category_id_input is None or category_id_input > 20 or category_id_input < 17:
                print("Please add a valid income category_id")
                time.sleep(2)
                continue

            query = """INSERT INTO incomes (amount, description, category_id)
            VALUES(%s, %s, %s)"""

            result = self.db.execute(query, (amount, description, category_id_input))
            
            print("Income added sucessfully!")
            break

    #shows all income added, using an inner join (like expenses)
    def view_income(self):
        query = """
        SELECT i.income_id, i.amount, i.description, c.name, i.income_date
        FROM incomes i
        JOIN categories c
        ON i.category_id = c.category_id
        ORDER BY i.income_date DESC
        """

        all_income = self.db.fetch_all(query)

        print("--- ALL INCOME ---")

        for income_id, amount, description, category, income_date in all_income:
            print(
                f"ID: {income_id}"
                f"\nAmount: £{amount}"
                f"\nDescription: {description}"
                f"\nCategory: {category}"
                f"\nDate: {income_date}"
                "\n--------------------------")
            
        
    #removing income
    def remove_income(self):
        try:
            while True:

                self.view_income()

                income_id = int(input("Please enter the Income ID you would like to remove: "))
                


                query = """DELETE FROM incomes WHERE income_id = %s"""

                result = self.db.execute(query, (income_id,))

                print(f"Income {income_id} remove sucessfully")
                break

        except ValueError:
            print("Please enter a valid value")



    #calculates total income 
    def total_income(self):
        query = """SELECT COALESCE(SUM(amount), 0) FROM incomes"""

        result = self.db.fetch_one(query)
        return result[0]
    