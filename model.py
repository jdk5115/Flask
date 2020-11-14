import sqlite3 

def my_name(username):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    message = '{username}\'s password is {password}.'.format(username=username, password=password)
    return password, message

def check_users():
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT username FROM users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    return users

def check_pw(username):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password

def signup(username, password, favorite_color):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users WHERE username='{username}';""".format(username=username))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute(""" INSERT INTO users(username, password, favorite_color) VALUES('{username}','{password}','{favorite_color}');""".format(username=username, password=password, favorite_color=favorite_color))
    else:
        return ('User already exists.')  
    
    return ('You have successfully signed up!')

    connection.commit()
    cursor.close()
    connection.close()
    return favorite_color

