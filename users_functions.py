import sqlite3
from passlib.hash import pbkdf2_sha256

def register_user(email, first_name, last_name, password1, password2):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists users(email, first_name, last_name, hashed_psw)")
    another_user = find_user(email)
    if not another_user and '@' in email and password1 == password2:
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (email, first_name, last_name, pbkdf2_sha256.hash(password1)))
    else:
        return False
    con.commit()
    con.close()
    return True

def find_user(email):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    user = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    con.commit()
    con.close()
    return user

def login_user(email, password):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    user = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    con.commit()
    con.close()
    if not pbkdf2_sha256.verify(password, user[3]):
        return False
    return True

def print_all():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    user = cur.execute("SELECT * FROM users").fetchall()
    con.commit()
    con.close()
    for i in user:
        print(i)
