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
        username,
        listname
        )VALUES(
        'Jon',
        'List1'
        );"""
)

cursor.execute(
    """INSERT INTO listitems(
        username,
        description,
        notes,
        checkbox
        )VALUES(
        'Jon',
        'my first list',
        'cool list',
        '0'
        );"""
)

connection.commit()
cursor.close()
connection.close()