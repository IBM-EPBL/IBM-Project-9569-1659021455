import sqlite3

conn = sqlite3.connect('account_database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE accounts (name TEXT, email TEXT, password TEXT)')
print("Table created successfully")
conn.close()