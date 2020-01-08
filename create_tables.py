# import 5347
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
create_table_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL)"

cursor.execute(create_table_users)
cursor.execute(create_table_items)
cursor.execute("INSERT INTO items VALUES (NULL, 'cokes', 100)")

connection.commit()

connection.close()