import psycopg2
from not_for_git import YOUR_PASSWORD


class Database:
    #database connection
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname = 'finance_tracker',
            user = 'postgres',
            password = YOUR_PASSWORD,
            host = 'localhost',
            port = '5432'
        )
        
        #returns a cursor object, you can use this to perform queries 
        self.cursor = self.conn.cursor()

    #executing queries 
    def execute(self, query, values = None):
        self.cursor.execute(query, values)
        self.conn.commit()

    #retrieving multiple records from the database
    def fetch_all(self, query, values = None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    #retrieving single values or a row from the database
    def fetch_one(self, query, values = None):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()
    
    #closing the database connection
    def close(self):
        self.cursor.close()
        self.conn.close()