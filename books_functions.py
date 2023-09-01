import sqlite3
import json

from datetime import datetime, timedelta

# this was only run once, not needed anymore
# from grab_books import *
# def add_books(books_data):
#     con = sqlite3.connect("books.db")
#     cur = con.cursor()
#     cur.execute("CREATE TABLE if not exists books(id, title, desc, on_loan, return_date, borrower)")
#     cur.executemany("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?)", books_data)
#     con.commit()
#     con.close()
# data = random_books()
# add_books(data)

def convert_to_datetime(string_date):
    return datetime(
        int(string_date[0:4]),
        int(string_date[5:7]),
        int(string_date[8:10]),
        int(string_date[11:13]),
        int(string_date[14:16])
        )

def has_passed(date):
    return convert_to_datetime(date) < datetime.now()

def is_same_date(date1, date2):
    #comparing datetime objects
    return str(date1)[0:10] == str(date2)[0:10]

def on_start_up():
    # This will update all books to make sure they
    # show as 'available' after the return date has passed
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    all_books = cur.execute("SELECT * FROM books")
    res = [[*book] for book in all_books]
    for book in res:
        if book[3] == "True" and has_passed(book[4]):
            cur.execute("UPDATE books SET borrower = ?, return_date = ?, on_loan = ? WHERE id = ?", ('', '', 'False', book[0]))
    con.commit()
    con.close()

def retrieve_all():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    all_books = cur.execute("SELECT * FROM books")
    # turning tuples to lists
    res = [[*book] for book in all_books]
    con.commit()
    con.close()
    return res

def available():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    books = cur.execute("SELECT * FROM books WHERE on_loan = ?", ("False",))
    res = [[*book] for book in books]
    con.commit()
    con.close()
    return res

def not_available():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    books = cur.execute("SELECT * FROM books WHERE on_loan = ?", ("True",))
    res = [[*book] for book in books]
    con.commit()
    con.close()
    return res

def returned_today():
    # This will only show books that are to be returned on today's date
    # (and not within 24 hours). For example if it's 11:53pm
    # and the book is meant to be returned at 00:05am the next day,
    # it will not appear in the search.
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    res = []
    books = cur.execute("SELECT * FROM books").fetchall()
    for book in books:
        if is_same_date(book[4], datetime.now()):
            res.append(book)
    con.commit()
    con.close()
    return res

def borrow_book(user_details, book_id, period=14):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    # user_details will be a dict with
    # "first_name", "last_name" and "email" as keys
    return_date = str(datetime.now() + timedelta(period))
    cur.execute("UPDATE books SET borrower = ?, return_date = ?, on_loan = ? WHERE id = ?", 
                (json.dumps(user_details), return_date, "True", book_id))
    con.commit()
    con.close()
    return return_date