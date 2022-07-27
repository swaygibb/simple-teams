import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO members (fullname, bio) VALUES (?, ?)", ('Steve Gibbs', 'My Name is steve gibbs and i\'m a software developer'))
cur.execute("INSERT INTO members (fullname, bio) VALUES (?, ?)", ('Jim Bob', 'Jim Bob is a developer at Jim Bob products'))

connection.commit()
connection.close()
