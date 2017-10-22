import sqlite3


class Database:
    def __init__(self, filename="img.db"):
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        self.setup()
        self.empty()

    def setup(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS images (path, hash)''')
        self.conn.commit()

    def empty(self):
        self.cursor.execute('''DELETE FROM images''')

    def add_img(self, path, hash):
        v = (path, hash,)
        self.cursor.execute('''INSERT INTO images VALUES (?, ?)''', v)
        self.conn.commit()

    def get_duplicates(self):
        self.cursor.execute('''
            SELECT i1.path AS 'left', i2.path AS 'right' FROM images i1
            LEFT JOIN images i2 ON i1.hash = i2.hash AND i1.path != i2.path
            WHERE i2.path IS NOT NULL;
        ''')

        return self.cursor.fetchall()
