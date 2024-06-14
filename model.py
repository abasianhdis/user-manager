import logging
from hashlib import sha256
import sqlite3

# تنظیمات لاگ‌نویسی
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class UserModel:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def validate_user(self, username, password):
        hashed_password = sha256(password.encode()).hexdigest()
        c = self.conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
        user = c.fetchone()
        if user:
            logging.info(f"Login successful for user: {username}")
            return True
        logging.warning(f"Login failed for user: {username}")
        return False

    def add_user(self, username, password):
        hashed_password = sha256(password.encode()).hexdigest()
        try:
            c = self.conn.cursor()
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            self.conn.commit()
            logging.info(f"User added: {username}")
            return True
        except sqlite3.IntegrityError:
            logging.warning(f"Attempt to add existing user: {username}")
            return False

    def remove_user(self, username):
        c = self.conn.cursor()
        c.execute('DELETE FROM users WHERE username = ?', (username,))
        if c.rowcount > 0:
            self.conn.commit()
            logging.info(f"User removed: {username}")
            return True
        logging.warning(f"Attempt to remove non-existing user: {username}")
        return False

    def get_users(self):
        c = self.conn.cursor()
        c.execute('SELECT username FROM users')
        users = [row[0] for row in c.fetchall()]
        return users
