import sqlite3
conn = sqlite3.connect('namesdb.sqlite')
cur = conn.cursor()
cur.execute ('DROP TABLE IF EXISTS ages')
cur.execute('''CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)  ''')
cur.execute('DELETE FROM Ages')
cur.execute("INSERT INTO ages ( name , age) VALUES ('Mohammed', 39)")
cur.execute("INSERT INTO ages ( name ,  age) VALUES ('Sarra', 39)")
cur.execute("INSERT INTO ages ( name ,  age) VALUES ('Aneshia', 32)")
cur.execute("INSERT INTO ages ( name ,  age) VALUES ('Oonagh', 27)")
cur.execute("INSERT INTO ages ( name ,  age) VALUES ('Judith', 17)")
cur.execute("INSERT INTO ages ( name ,  age) VALUES ('Lilia', 33)")

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
    print(row)
conn.commit()
conn.close()