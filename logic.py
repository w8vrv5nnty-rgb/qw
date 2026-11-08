import sqlite3

def high_rating():
    con = sqlite3.connect("movie_database.db")
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM movies WHERE rating > 8.0 ORDER BY RANDOM() LIMIT 1"
        )
        row = cur.fetchone()         
        cur.close()
    return row                        

def random_movie():
    con = sqlite3.connect("movie_database.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM movies WHERE rating < 8.0 ORDER BY RANDOM() LIMIT 1")
        row = cur.fetchone()
        cur.close()
    return row 

def old_movie():
    con = sqlite3.connect("movie_database.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM movies WHERE year < 2001 ORDER BY RANDOM() LIMIT 1")
        row = cur.fetchone()
        cur.close()
    return row        

def new_movie():
    con = sqlite3.connect("movie_database.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM movies WHERE year > 2001 ORDER BY RANDOM() LIMIT 1")
        row = cur.fetchone()
        cur.close()
    return row  

def drama_movie():
    con = sqlite3.connect("movie_database.db")
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM movies WHERE LOWER(genre) LIKE ? ORDER BY RANDOM() LIMIT 1",
            ("%drama%",)
        )
        row = cur.fetchone()
        cur.close()
    return row  

def action_movie():
    con = sqlite3.connect("movie_database.db")
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM movies WHERE LOWER(genre) LIKE ? ORDER BY RANDOM() LIMIT 1",
            ("%action%",)
        )
        row = cur.fetchone()
        cur.close()
    return row  