import json
import sqlite3
conn = sqlite3.Connection('rosterdb.sqlite')
curr = conn.cursor()
curr.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = open('roster_data.json')
data = fname.read()
jdata = json.loads(data)
for tim in jdata:
    name = tim[0]
    title = tim[1]
    role = tim[2]
    #print(role , title , name)
    curr.execute('INSERT OR IGNORE INTO User(name) VALUES(?)' ,(name, ))
    curr.execute('SELECT id FROM User WHERE name = ?' , (name , ))
    user_id = curr.fetchone()[0]
    curr.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)' , (title, ))
    curr.execute('SELECT id FROM Course WHERE title = ?' , (title, ))
    course_id = curr.fetchone()[0]
    curr.execute('INSERT OR IGNORE INTO Member(user_id , course_id , role) VALUES (?, ? , ?)',(user_id , course_id , role))
conn.commit()
curr.close()