"""
Database Viewer for Complaint Management System
Shows all tables and their contents
"""
import sqlite3
import os
from pathlib import Path

# Database path
db_path = Path('complaint_manager/backend/db.sqlite3')

if not db_path.exists():
    print(f"❌ Database not found at: {db_path}")
    print("The database will be created when you first run the backend server.")
    exit(1)

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=" * 80)
print("COMPLAINT MANAGEMENT SYSTEM - DATABASE CONTENTS")
print("=" * 80)

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = cursor.fetchall()

print(f"\n📊 Found {len(tables)} tables in database\n")

for table in tables:
    table_name = table[0]
    print("=" * 80)
    print(f"TABLE: {table_name}")
    print("=" * 80)
    
    # Get table schema
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    
    print("\nColumns:")
    for col in columns:
        col_id, col_name, col_type, not_null, default_val, pk = col
        pk_marker = " [PRIMARY KEY]" if pk else ""
        null_marker = " NOT NULL" if not_null else ""
        print(f"  - {col_name}: {col_type}{pk_marker}{null_marker}")
    
    # Get row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    
    print(f"\nTotal Records: {count}")
    
    # Show data if exists
    if count > 0:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        print("\nData:")
        col_names = [col[1] for col in columns]
        
        # Print header
        header = " | ".join(col_names)
        print(f"  {header}")
        print(f"  {'-' * len(header)}")
        
        # Print rows
        for row in rows:
            row_str = " | ".join(str(val) if val is not None else "NULL" for val in row)
            print(f"  {row_str}")
    
    print()

conn.close()

print("=" * 80)
print("✅ Database inspection complete!")
print("=" * 80)
