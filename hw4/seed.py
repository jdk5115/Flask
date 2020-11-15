import sqlite3

connection = sqlite3.connect('todo.db')
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
        )VALUES(
        'Jon',
        'Kelly',
        'Green'
        );"""
)

cursor.execute(
    """INSERT INTO lists(
        listname
        )VALUES(
        'List1'
        );"""
)

cursor.execute(
    """INSERT INTO listitems(
        description,
        notes,
        checkbox
        )VALUES(
        'my first list',
        'cool list',
        '0'
        );"""
)

connection.commit()
cursor.close()
connection.close()