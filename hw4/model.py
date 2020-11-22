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

def create_list(listname, username):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT listname FROM lists WHERE listname='{listname}';""".format(listname=listname))
    exist = cursor.fetchone()
    if exist is None:
       cursor.execute(""" INSERT INTO lists(username) VALUES('{username}');""".format(username=username))
       cursor.execute(""" INSERT INTO lists(listname) VALUES('{listname}');""".format(listname=listname))
    else:
        return ('List already exists.')  
    
    connection.commit()
    cursor.close()
    connection.close()
    message = 'Your list ' + listname + ' has successfully been created.'
    return message

def display_lists(username):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT listname FROM lists WHERE username='{username}' ORDER BY listname DESC;""")
    user_lists = cursor.fetchall()
  

    # for i in range(len(user_lists)):
    #     list_name = user_lists[i][0]
    #     lists.append(list_name)

    connection.commit()
    cursor.close()
    connection.close()
    return user_lists
