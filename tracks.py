import sqlite3
conn = sqlite3.connect('findtracksdb.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);''')
cur.execute('''CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);''')
cur.execute('''CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);''')
cur.execute('''CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')
fhand = open("tracks.csv")
for line in fhand:
    line = line.strip()
    pieces = line.split(',')

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    lenght = pieces[4]
    rating = pieces[5]
    genre = pieces[6]
    cur.execute(''' INSERT OR IGNORE INTO Artist(name) VALUES( ? )''' , (artist , ))
    cur.execute('''SELECT id FROM Artist WHERE name = ?''' , ( artist , ))
    artist_id = cur.fetchone()[0]
    #cur.execute('''INSERT OR IGNORE INTO Album( title , artist_id) VALUES (? , ?)''' , (album , artist_id))
    cur.execute('''INSERT OR IGNORE INTO Album( title , artist_id) VALUES(? , ?)''' , (album , artist_id))

    cur.execute('''SELECT id from album  WHERE title = ?''' , (album, ))
    album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Genre(name) VALUES (?)''' , (genre, ))
    #cur.execute('''SELECT id FROM Genre WHERE name = ?''' , (genre))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO  Track (title , album_id ,genre_id , len , rating , count  )
                   VALUES (? ,?, ? ,? ,?,?)''' , (name ,album_id , genre_id , lenght , rating , count))

conn.commit()
conn.close()