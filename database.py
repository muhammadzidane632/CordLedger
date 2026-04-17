import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS
                   transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id TEXT NOT NULL,
                   type TEXT NOT NULL,
                   amount REAL NOT NULL,
                   description TEXT,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                   )
''')
    
def add_transactions(user_id,trans_type, amount,description):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO transactions (user_id,type,amount,description)
    VALUES (?,?,?,?)
    ''',(str(user_id),trans_type,amount,description))
    conn.commit()
    conn.close()
    

