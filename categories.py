import time

class Categories:
    
    def __init__(self, db):
        self.db = db

    def get_category_name(self, category_id):
        query = """SELECT name FROM categories WHERE category_id = %s"""

        result = self.db.fetch_one(query, (category_id,))

        if result is None:
            return None
        
        return result[0]
    
    def get_all_categories(self):
        category_query = """SELECT category_id, name 
        FROM categories
        ORDER BY category_id
        """

        categories = self.db.fetch_all(category_query)

        if not categories:
            print("No categories found")
            return

        print("\n--- All Categories ---")

        for category_id, name in categories:
            print(f"\n{category_id} | {name}")
        

    #View expense categories
    def view_expense_categories(self):
        expense_categories_query = """SELECT category_id, name
        FROM categories
        WHERE type = 'expense'"""

        expense_categories = self.db.fetch_all(expense_categories_query)
        print(f"\n--- EXPENSE CATEGORIES ---")
        for category_id, name in expense_categories:
            print(
                f"ID: {category_id}"
                f"\nCategory: {name}"
                "\n-----------------"
            )

    #view income categories
    def income_categories(self):
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

    def check_item_exists(self, table_name, id_column_name, item_id):
        query = f"""
        SELECT * 
        FROM {table_name} 
        WHERE {id_column_name} = %s """

        result = self.db.fetch_one(query, (item_id,))

        if result is None:
            return False
        
        return True
    
    def check_valid_date(self, table_name, date_column, month, year):
        #checking if any records exist for the date entered, so it doesn' return empty results - ONLY VIEWING ONE TO CHECK
        query = f"""SELECT 1 
        FROM {table_name} WHERE EXTRACT(MONTH FROM {date_column}) = %s
        AND EXTRACT(YEAR FROM {date_column}) = %s
        LIMIT 1"""

        result = self.db.fetch_one(query, (month, year,))

        if result is None:
            return False
    
        return True
    
    def check_category_records(self, table_name, category_id):
        query = f"""SELECT 1 FROM {table_name} WHERE category_id = %s"""

        result = self.db.fetch_one(query, (category_id, ))

        if result is None:
            return False
        
        return True