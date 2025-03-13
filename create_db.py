import sqlite3

conn = sqlite3.connect('user_db.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
               username TEXT PRIMARY KEY,
               password TEXT NOT NULL,
               name TEXT NOT NULL,
               age INTEGER NOT NULL,
               email TEXT NOT NULL
)""")

cursor.execute("""
INSERT INTO users (username, passowrd,  name, age, email) VALUES
('user1', 'pass123,'Mike Smith'), 30, 'mike@eample.com'),
('user2', 'pass123,'Bob  Woods'), 50, 'bob@eample.com'),
('user3', 'pass123,'Sara Winter'), 40, 'sara@eample.com'),
""")

conn.commit()
conn.close()