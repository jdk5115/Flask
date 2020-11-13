import sqlite3

connection = sqlite3.connect('todo.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32),
        favorite_color VARCHAR(16)
    );"""
)
cursor.execute(
    """CREATE TABLE lists(
        listname VARCHAR(16)
    );"""
)
cursor.execute(
    """CREATE TABLE listitems(
        description VARCHAR(64),
        notes VARCHAR(32),
        checkbox BOOLEAN(1)
    );"""
)

connection.commit()
cursor.close()
connection.close()