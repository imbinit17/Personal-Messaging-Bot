import sqlite3

    
def getUser(chat_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    users = cursor.execute(''' SELECT * FROM users WHERE chat_id = ?''',(chat_id,)).fetchone()

    conn.close()
    if(users == None):
        return None
    else:
        return users[0]
    
def getThreadIDbyUser(chat_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    user = cursor.execute(''' SELECT * FROM users WHERE chat_id = ?''',(chat_id,)).fetchone()

    conn.close()
    return user[1]    
    
def getUserByThreadID(thread_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    users = cursor.execute(''' SELECT * FROM users WHERE thread_link_id = ?''',(thread_id,)).fetchone()

    conn.close()
    if(users == None):
        return None
    else:
        return users[0]


def addUser(chat_id,thread_link_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(''' INSERT OR IGNORE INTO users VALUES(?,?)''',(chat_id,thread_link_id))
    conn.commit()
    conn.close()