import sqlite3
print("add some data")

connection = sqlite3.connect('db.db')

with open('fill_db_sample_data.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()

print("done!")
