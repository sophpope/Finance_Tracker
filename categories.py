class Categories:
    def __init__(self, db):
        self.db = db

    def get_category_name(self, category_id):
        query = """SELECT name FROM categories WHERE category_id = %s"""

        result = self.db.fetch_one(query, (category_id,))

        if result is None:
            return None
        
        return result[0]