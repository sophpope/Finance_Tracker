class Income:
    def __init__(self, db):
        self.db = db

    #adding income to the database 
    def add_income(self):
        amount = float(input("Enter income amount: £"))
        description = input("Enter income description:")
        
        income_categories_query = """SELECT category_id, name 
        FROM categories
        WHERE type = 'income'
        """
        income_categories = self.db.fetch_all(income_categories_query)
        print(f"\n--- INCOME CATEGORIES ---")
        for category_id, name in income_categories:
            print(
                f"ID: {category_id}"
                f"\nCategory: {name}"
                "\n-----------------"
            )
        category_id_input = int(input("Enter category ID:"))

        query = """INSERT INTO incomes (amount, description, category_id)
        VALUES(%s, %s, %s)"""
        self.db.execute(query, (amount, description, category_id_input))
        print("Income added sucessfully!")

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
        income_id = int(input("Please enter the Income ID you would like to remove: "))

        query = """DELETE FROM incomes WHERE income_id = %s"""

        self.db.execute(query, (income_id,))

        print(f"Income {income_id} remove sucessfully")



    #calculates total income 
    def total_income(self):
        query = """SELECT COALESCE(SUM(amount), 0) FROM incomes"""

        result = self.db.fetch_one(query)
        return result[0]
    