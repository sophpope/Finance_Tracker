import psycopg2
from not_for_git import YOUR_PASSWORD


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname = 'finance_tracker',
            user = 'postgres',
            password = YOUR_PASSWORD,
            host = 'localhost',
            port = '5432'
        )
        
        self.cursor = self.conn.cursor()


