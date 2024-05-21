import sqlite3

conn = sqlite3.connect('userdata.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        mobile TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL,
        marital_status TEXT NOT NULL
    )
''')
conn.commit()
conn.close()
