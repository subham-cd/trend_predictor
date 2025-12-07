import sqlite3
from datetime import datetime

DB_NAME = "trends.db"

def init_db():
    """Database aur Table banata hai agar nahi hai toh"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS trends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT,
            rank INTEGER,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def save_trends(trend_list):
    """Naye trends ko save karta hai"""
    init_db()  # Ensure table exists
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for i, topic in enumerate(trend_list, 1):
        c.execute("INSERT INTO trends (keyword, rank, timestamp) VALUES (?, ?, ?)", 
                  (topic, i, time_now))
    
    conn.commit()
    conn.close()

def get_history():
    """Last 10 records fetch karta hai"""
    # FIX: Pehle check karo ki table hai ya nahi
    init_db() 
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT keyword, rank, timestamp FROM trends ORDER BY id DESC LIMIT 10")
        data = c.fetchall()
    except sqlite3.OperationalError:
        # Agar table phir bhi nahi mili (rare case)
        data = []
    
    conn.close()
    return data

# Important: Jaise hi ye file load ho, table bana do
init_db()