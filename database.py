import sqlite3
from hashlib import sha256

def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    
    # افزودن کاربر اولیه
    add_initial_user(c, 'admin', 'admin')
    
    conn.commit()
    conn.close()

def add_initial_user(cursor, username, password):
    hashed_password = sha256(password.encode()).hexdigest()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        print(f"User {username} added successfully.")
    except sqlite3.IntegrityError:
        print(f"User {username} already exists.")

if __name__ == "__main__":
    create_db()
