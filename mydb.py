# import sqlite3
# from flask import g
# import bcrypt

# class Database:
#     def __init__(self, db):
#         self.db = db

#     def get_db(self):
#         db = getattr(g, '_database', None)
#         if db is None:
#             db = g._database = sqlite3.connect(self.db)
#             # Create tables if they don't exist
#             self.create_tables()
#         return db

#     def close_connection(self, exception):
#         db = getattr(g, '_database', None)
#         if db is not None:
#             db.close()

#     def create_tables(self):
#         conn = self.get_db()
#         cur = conn.cursor()
#         # Create expense_record table
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS expense_record (
#                 rowid INTEGER PRIMARY KEY AUTOINCREMENT,
#                 item_name TEXT NOT NULL,
#                 item_price REAL NOT NULL,
#                 purchase_date DATE NOT NULL
#             )
#         """)
#         # Create budget_table if not exists
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS budget_table (
#                 budget REAL NOT NULL
#             )
#         """)
#         # Create user table if not exists
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS user (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT UNIQUE NOT NULL,
#                 email TEXT UNIQUE NOT NULL,
#                 password_hash TEXT NOT NULL
#             )
#         """)
#         # Commit changes and close cursor
#         conn.commit()
#         cur.close()

#     def fetchRecord(self, query):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute(query)
#         records = cur.fetchall()
#         cur.close()
#         return records

#     def fetchBudget(self):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("SELECT budget FROM budget_table")
#         result = cur.fetchone()
#         cur.close()
#         if result:
#             return result[0]
#         else:
#             return 0

#     def fetchTotalExpense(self):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("SELECT SUM(item_price) FROM expense_record")
#         total_expense_row = cur.fetchone()
#         total_expense = total_expense_row[0] if total_expense_row[0] is not None else 0
#         cur.close()
#         return total_expense

#     def get_budget(self):
#         return self.fetchBudget()

#     def insertRecord(self, item_name, item_price, purchase_date):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("INSERT INTO expense_record (item_name, item_price, purchase_date) VALUES (?, ?, ?)", (item_name, item_price, purchase_date))
#         conn.commit()
#         cur.close()

#     def updateRecord(self, item_name, item_price, purchase_date, rid):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ? WHERE rowid = ?", (item_name, item_price, purchase_date, rid))
#         conn.commit()
#         cur.close()

#     def removeRecord(self, rowid):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("DELETE FROM expense_record WHERE rowid = ?", (rowid,))
#         conn.commit()
#         cur.close()

#     def insertBudget(self, budget):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("INSERT INTO budget_table (budget) VALUES (?)", (budget,))
#         conn.commit()
#         cur.close()

#     def updateBudget(self, budget):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("UPDATE budget_table SET budget = ?", (budget,))
#         conn.commit()
#         cur.close()

#     def saveBudget(self, budget):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("SELECT budget FROM budget_table")
#         result = cur.fetchone()
#         if result:
#             cur.execute("UPDATE budget_table SET budget = ?", (budget,))
#         else:
#             cur.execute("INSERT INTO budget_table (budget) VALUES (?)", (budget,))
#         conn.commit()
#         cur.close()

#     def hash_password(self, password):
#         # Hash password using bcrypt
#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#         return hashed_password.decode('utf-8')

#     def verify_password(self, password, hashed_password):
#         # Verify password using bcrypt
#         return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

#     def authenticate_user(self, username, password):
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("SELECT password_hash FROM user WHERE username = ?", (username,))
#         result = cur.fetchone()
#         cur.close()
#         if result:
#             hashed_password = result[0]
#             return self.verify_password(password, hashed_password)
#         else:
#             return False

#     def add_user(self, username, email, password):
#         hashed_password = self.hash_password(password)
#         conn = self.get_db()
#         cur = conn.cursor()
#         cur.execute("INSERT INTO user (username, email, password_hash) VALUES (?, ?, ?)", (username, email, hashed_password))
#         conn.commit()
#         cur.close()

import sqlite3
from flask import g
import bcrypt

class Database:
    def __init__(self, db):
        self.db = db

    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.db)
            self.create_tables()
        return db

    def close_connection(self, exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    def create_tables(self):
        conn = self.get_db()
        cur = conn.cursor()
        # Create expense_record table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS expense_record (
                rowid INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                item_price REAL NOT NULL,
                purchase_date DATE NOT NULL
            )
        """)
        # Create budget_table if not exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS budget_table (
                budget REAL NOT NULL
            )
        """)
        # Create user table if not exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        conn.commit()
        cur.close()

    def fetchRecord(self, query):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()
        return records

    def fetchBudget(self):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("SELECT budget FROM budget_table")
        result = cur.fetchone()
        cur.close()
        return result[0] if result else 0

    def fetchTotalExpense(self):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("SELECT SUM(item_price) FROM expense_record")
        total_expense_row = cur.fetchone()
        cur.close()
        return total_expense_row[0] if total_expense_row[0] is not None else 0

    def get_budget(self):
        return self.fetchBudget()

    def insertRecord(self, item_name, item_price, purchase_date):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO expense_record (item_name, item_price, purchase_date) VALUES (?, ?, ?)", (item_name, item_price, purchase_date))
        conn.commit()
        cur.close()

    def updateRecord(self, item_name, item_price, purchase_date, rid):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ? WHERE rowid = ?", (item_name, item_price, purchase_date, rid))
        conn.commit()
        cur.close()

    def removeRecord(self, rowid):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM expense_record WHERE rowid = ?", (rowid,))
        conn.commit()
        cur.close()

    def saveBudget(self, budget):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("SELECT budget FROM budget_table")
        result = cur.fetchone()
        if result:
            cur.execute("UPDATE budget_table SET budget = ?", (budget,))
        else:
            cur.execute("INSERT INTO budget_table (budget) VALUES (?)", (budget,))
        conn.commit()
        cur.close()

    # def user_exists(self, username, email):
    #     conn = self.get_db()
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM user WHERE username = ? OR email = ?", (username, email))
    #     user = cur.fetchone()
    #     cur.close()
    #     return user is not None

    def user_exists(self, username, email):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE username = ? OR email = ?", (username, email))
        result = cur.fetchone()
        cur.close()
        return result is not None

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    # def authenticate_user(self, username, password):
    #     conn = self.get_db()
    #     cur = conn.cursor()
    #     cur.execute("SELECT password_hash FROM user WHERE username = ?", (username,))
    #     result = cur.fetchone()
    #     cur.close()
    #     if result:
    #         hashed_password = result[0]
    #         return self.verify_password(password, hashed_password)
    #     return False

    def authenticate_user(self, username, password):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password_hash FROM user WHERE username = ?", (username,))
        user = cur.fetchone()
        cur.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
            return {'id': user[0], 'username': user[1]}
        return None

    # def add_user(self, username, email, password):
    #     hashed_password = self.hash_password(password)
    #     conn = self.get_db()
    #     cur = conn.cursor()
    #     cur.execute("INSERT INTO user (username, email, password_hash) VALUES (?, ?, ?)", (username, email, hashed_password))
    #     conn.commit()
    #     cur.close()
    def add_user(self, username, email, password_hash):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO user (username, email, password_hash) VALUES (?, ?, ?)", (username, email, password_hash))
        conn.commit()
        cur.close()

    def get_user_by_username(self, username):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password_hash FROM user WHERE username = ?", (username,))
        user = cur.fetchone()
        cur.close()
        return user

    def get_user_by_id(self, user_id):
        conn = self.get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password_hash FROM user WHERE id = ?", (user_id,))
        user = cur.fetchone()
        cur.close()
        return user
