import sqlite3 

def show_color(username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT favorite_color FROM users WHERE Username='{username}' ORDER BY pk DESC;""".format(username = username))
    color = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    message = '{username}\'s favorite color is {color}.'.format(username=username, color=color)
    return color, message

