import sqlite3
conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS user (
    id TEXT PRIMARY KEY,
    web TEXT NOT NULL
)
''')

sql = "INSERT INTO user(id, web) VALUES (?, ?)"
cur.execute(sql, ("liuGrape", "github.com/liuGrape"))

conn.commit()

cur.execute("SELECT * FROM user")
all_rows = cur.fetchall()
print(all_rows)

cur.close()
conn.close()
