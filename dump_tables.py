import sqlite3
try:
    conn = sqlite3.connect('complaint_manager/backend/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    with open('tables_output.txt', 'w') as f:
        f.write("Tables in database:\n")
        for t in tables:
            f.write(f"- {t[0]}\n")
    conn.close()
    print("Successfully wrote tables to tables_output.txt")
except Exception as e:
    with open('tables_output.txt', 'w') as f:
        f.write(f"Error: {e}")
