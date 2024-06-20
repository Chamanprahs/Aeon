import sqlite3

conn = sqlite3.connect('sessions.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user_sessions (user_id INTEGER PRIMARY KEY, string_session TEXT)''')
conn.commit()

def save_string_session(user_id, string_session):
    c.execute("INSERT OR REPLACE INTO user_sessions (user_id, string_session) VALUES (?, ?)", (user_id, string_session))
    conn.commit()

def get_string_session(user_id):
    c.execute("SELECT string_session FROM user_sessions WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    return result[0] if result else None

